#!/usr/bin/env python3
"""mode 0x02 条目解码 —— 严格按 isaac-ng.exe 的 FUN_0099c270 语义实现。

反汇编证据（isaac-ng.exe, Ghidra 12.1.4）：

  FUN_0099c270 是"取下一块"的函数。mode==2 分支（0x0099c32a 起）：

    1) 读 4 字节 -> local_8c
         uVar9    = local_8c & 0x7fffffff   ; 低 31 位 = 本块压缩长度
         local_98 = local_8c >> 31         ; 高  1 位 = flag
       (0x0099c342 / 0x0099c348)

    2) 读 uVar9 字节到 param_1+0x1c
       (0x0099c374 ~ 0x0099c380)

    3) 关键：状态对象 param_1+0x14，其 +0x10 字节是**粘性标志**
       (0x0099c39e  MOV AL,byte ptr [EDX + 0x10])
       (0x0099c3b1  TEST AL,AL / JNZ -> XOR 分支)

       * 若标志已为 1            -> 本块走 XOR 明文分支
       * 若标志为 0 且 flag==0 且 len==0x400
                                  -> 标志置 1，本块走 XOR 明文分支
         (0x0099c3b5 TEST CL,CL / 0x0099c3b9 CMP ESI,0x400
          / 0x0099c3c1 MOV AL,0x1 / 0x0099c3c7 写回标志)
       * 否则                    -> 走 MiniZ inflate 分支

    4) MiniZ 分支 (0x0099c3ce):
         flags = (flag ^ 1) * 2            ; 0x0099c3da / 0x0099c3dd
         解压状态 = *(param_1+0x14+0xc)   ; 0x0099c3e6  <-- 跨块保留！
         out_size 初值 = 0x400 (1024)      ; 0x0099c3a7
       调用 FUN_009aeb00 = miniz 的 tinfl 解压。
       flags 的 bit0 是 TINFL_FLAG_PARSE_ZLIB_HEADER，
       而 (flag^1)*2 永远为 0 或 2，bit0 恒为 0
         => **永远是 raw deflate，永远不解析 zlib 头**。
       flags bit1 = TINFL_FLAG_HAS_MORE_INPUT
         => flag==0 时置位 = 本块只是流的中间段，后面还有块。

    5) XOR 分支 (0x0099c40c):
         memcpy(dest, src, len) -> FUN_009b06f0(dest, len) 逐字节异或

  结论：mode 0x02 条目 = 多个 [u32 hdr][payload] 块串成**同一条 raw deflate 流**，
        必须用同一个 decompressobj 逐块喂入；不能用每块独立解压。
"""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

U32 = 0xFFFFFFFF


def iter_blocks(blob: bytes, off: int, comp: int):
    """按 FUN_0099c270 的读块方式遍历一个条目的所有块。

    产出 (flag, payload, block_total_len)。
    """
    cur = off
    end = off + comp
    while cur + 4 <= end:
        hdr = struct.unpack_from("<I", blob, cur)[0]
        ln = hdr & 0x7FFFFFFF
        flag = hdr >> 31
        if cur + 4 + ln > end:
            break
        yield flag, blob[cur + 4:cur + 4 + ln], 4 + ln
        cur += 4 + ln


def decode_mode02_entry(blob: bytes, off: int, comp: int, size: int,
                         seed: int | None = None,
                         xor_key: bytes | None = None) -> bytes | None:
    """解一个 mode 0x02 条目。返回解压后数据（长度应等于 size）或 None。"""
    out = bytearray()
    do = zlib.decompressobj(-15)   # raw deflate，跨块共享状态
    xor_mode = False
    first = True

    for flag, payload, _blen in iter_blocks(blob, off, comp):
        # --- 粘性标志判定（严格照 0x0099c39e ~ 0x0099c3cc） ---
        # 该标志是**每条目独立**的（FUN_00999c170 每次初始化时清零），
        # 且只在本条目的**首块**上做判定：
        #   flag == 0 且 len == 0x400  ->  本条目整体走 XOR 明文
        #   否则                        ->  本条目整体走 MiniZ inflate
        if first:
            first = False
            xor_mode = (flag == 0 and len(payload) == 0x400)
            if xor_mode and xor_key is None:
                return None      # XOR 模式：需要 ISAAC 密钥流，暂不处理

        if xor_mode:
            out += bytes(b ^ k for b, k in zip(payload, xor_key))
            continue

        # --- MiniZ / tinfl 分支 ---
        try:
            out += do.decompress(payload)
        except zlib.error:
            return None

    if xor_mode:
        return bytes(out[:size]) if size else bytes(out)

    try:
        out += do.flush()
    except zlib.error:
        pass
    if len(out) != size:
        # 容错：有些条目 size 字段可能不等于实际输出
        return bytes(out) if out else None
    return bytes(out)


def main():
    import sys
    packed = Path(sys.argv[1])
    for arch in sorted(packed.glob("*.a")):
        blob = arch.read_bytes()
        mode = blob[7]
        if mode != 2:
            continue
        ioff = struct.unpack_from("<I", blob, 0x08)[0]
        cnt = struct.unpack_from("<H", blob, 0x0C)[0]
        ents = [struct.unpack_from("<5I", blob, ioff + i * 20) for i in range(cnt)]
        ok = bad = 0
        crc_ok = crc_bad = 0
        for i, (h, sp, off, size, crc) in enumerate(ents):
            comp = (ents[i + 1][2] - off) if i + 1 < cnt else (ioff - off)
            d = decode_mode02_entry(blob, off, comp, size)
            if d is None:
                bad += 1
                continue
            ok += 1
            if zlib.crc32(d) & U32 == crc:
                crc_ok += 1
            else:
                crc_bad += 1
        print(f"{arch.name:22s} mode=2 entries={cnt:5d} decode_ok={ok:5d} "
              f"fail={bad:4d}  crc32_match={crc_ok:5d} crc32_mismatch={crc_bad:4d}")


if __name__ == "__main__":
    main()
