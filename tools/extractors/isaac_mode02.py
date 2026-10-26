#!/usr/bin/env python3
"""mode 0x02 解密 —— 精确移植 isaac-ng.exe 的反汇编（无猜测）。

证据链（isaac-ng.exe, Ghidra 12.1.4 反编译 + 汇编）：

  FUN_0099c270 (refill_buffer) 的 mode==2 分支：
      read 4 bytes -> local_8c
      uVar9    = local_8c & 0x7fffffff      ; 低 31 位 = 压缩长度
      local_98 = local_8c >> 31            ; 高 1 位 = 标志
      read uVar9 bytes into (param_1 + 0x1c)
      if (first block) {
          if (flag==0 && len==0x400) { reuse previous dictionary; memcpy }
          else { FUN_009aeb00(...)  -> MiniZ inflate }
      }
      else {
          memcpy(_Dst, src, len);
          FUN_009b06f0(_Dst, len);           <-- XOR 解密
          ... inflate
      }

  FUN_009b06f0 (XOR 解密)：
      for (i = 0; i < len; i++) {
          if ((i & 3) == 0) {
              puVar1 = (uint *)*param_1;          // 密钥流对象
              uVar3   = puVar1[*puVar1 + 1];      // 取下一个 32 位密钥字
              *puVar1 = *puVar1 + 1;               // 索引++
              if (0xff < *puVar1) FUN_009c2fd0(); // 索引 > 255 时重新生成
          } else {
              uVar3 = uVar3 >> 8;                  // 右移 8 -> 小端取字节
          }
          buf[i] ^= (byte)uVar3;
      }

  FUN_009c2f10 (密钥流生成，256 个 32 位字):
      汇编逐条对应：
        MOV EAX,ESI ; SHL EAX,0xf ; MOV EDX,ESI ; XOR EAX,ESI ; SHR EDX,0x9
        SHL EAX,0x8 ; XOR EAX,EDX ; XOR EAX,ESI
          => EAX = ((seed<<15 ^ seed) << 8) ^ (seed>>9) ^ seed
        随后每轮：
          PUSH 0x5851f42d ; PUSH 0x4c957f2d ; PUSH ECX ; PUSH EAX
          CALL __allmul       ; EDX:EAX = EAX:ECX * 0x4c957f2d5851f42d
          ADD EAX,0x7f ; ADC EDX,0x0
          SHR EDI,0x1b ; SHRD EBX,ECX,0x1b ; SHR ESI,0xd
          MOV ECX,EDI ; NEG ECX ; AND ECX,0x1f
          XOR EBX,ESI
          MOV EDX,EBX ; SHL EDX,CL ; MOV ECX,EDI ; SHR EBX,CL ; OR EDX,EBX
          MOV [ECX],EDX          ; 存 32 位密钥字
          ; 下一轮 EAX=EDX(高32), ECX=EAX(低32)

      关键：**乘法是 64x64 -> 128**，乘数常量 0x4c957f2d5851f42d 拆成
      高/低两半分别 PUSH（cdecl 参数：低32先PUSH=0x4c957f2d，再高32=0x5851f42d）。
"""
from __future__ import annotations

import struct
from pathlib import Path

U32 = 0xFFFFFFFF
U64 = 0xFFFFFFFFFFFFFFFF

MULT = 0x4C957F2D5851F42D


class KeyStream:
    """FUN_009c2f10 + FUN_009b06f0 的精确合并实现。"""

    def __init__(self, seed: int) -> None:
        self.seed = seed & U32
        self.words: list[int] = []
        self.index = 0
        self._generate()

    def _generate(self) -> None:
        seed = self.seed
        # EAX = ((seed<<15 ^ seed) << 8) ^ (seed>>9) ^ seed
        eax = (((seed << 15) & U32) ^ seed)
        eax = ((eax << 8) & U32) ^ ((seed >> 9) & U32) ^ seed
        eax &= U32
        ecx = 0
        out: list[int] = []
        for _ in range(0x100):
            # __allmul: EDX:EAX = (EAX:ECX as 64-bit) * MULT
            acc = ((ecx << 32) | eax) & U64
            prod = (acc * MULT) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
            edx = (prod >> 32) & U32
            eax_new = prod & U32
            # ADD EAX,0x7f ; ADC EDX,0
            eax_new = (eax_new + 0x7F) & U32
            if eax_new < 0x7F:
                edx = (edx + 1) & U32
            edx &= U32
            # SHRD EBX,ECX,0x1b  -> EBX = (ECX:EAX >> 27) 低32
            ebx = (acc >> 27) & U32
            # SHR EDI,0x1b  (EDI 原为 ECX)
            edi = (ecx >> 27) & U32
            # SHR ESI,0xd  (ESI 原为 ECX)
            esi = (ecx >> 13) & U32
            ecx_new = edi
            neg = (-ecx_new) & U32
            cl = neg & 0x1F
            ebx ^= esi
            # SHL EDX,CL ; SHR EBX,CL ; OR
            val = ((ebx << cl) | (ebx >> (32 - cl) if cl else 0)) & U32
            out.append(val)
            # 下一轮: EAX = edx, ECX = eax_new
            eax = edx
            ecx = eax_new
        self.words = out
        self.index = 0

    def next_word(self) -> int:
        if self.index > 0xFF:
            # FUN_009c2fd0: 重新生成（种子来自末尾状态）
            self.seed = self.words[-1]
            self._generate()
        w = self.words[self.index]
        self.index += 1
        return w


def decrypt_mode02(data: bytes, seed: int) -> bytes:
    """FUN_009b06f0 的逐字节 XOR。"""
    ks = KeyStream(seed)
    out = bytearray(len(data))
    cur = 0
    for i in range(len(data)):
        if (i & 3) == 0:
            cur = ks.next_word()
        else:
            cur = (cur >> 8) & U32
        out[i] = data[i] ^ (cur & 0xFF)
    return bytes(out)


def main():
    packed = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed")
    fl = Path(__file__).resolve().parent.parent / "data" / "filelist.txt"
    names: dict[int, str] = {}
    for line in fl.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        h = 5381
        for ch in line.lower():
            h = ((h * 33) + ord(ch)) & 0xFFFFFFFF
        names.setdefault(h, line)

    for arch in ("repentance.a", "afterbirthp.a", "afterbirth.a"):
        f = packed / arch
        if not f.exists():
            continue
        blob = f.read_bytes()
        mode = blob[7]
        index_off = struct.unpack_from("<I", blob, 0x08)[0]
        count = struct.unpack_from("<H", blob, 0x0C)[0]
        print(f"\n===== {arch} mode={mode} entries={count} =====")

        tried = hit = 0
        for i in range(count):
            h, sp, off, size, crc = struct.unpack_from("<5I", blob, index_off + i * 20)
            nm = names.get(h, "")
            if not nm.endswith(".xml"):
                continue
            tried += 1
            data = blob[off:off + size]
            # 4 字节头：低31位=长度, 高1位=标志
            if len(data) < 4:
                continue
            hdr = struct.unpack_from("<I", data, 0)[0]
            clen = hdr & 0x7FFFFFFF
            flag = hdr >> 31
            payload = data[4:4 + clen]
            dec = decrypt_mode02(payload, sp)
            for label, raw in (("decrypt+miniz", dec), ("raw", payload)):
                try:
                    import zlib
                    out = zlib.decompress(raw, -15)
                except Exception:
                    continue
                if out[:5] == b"<?xml" or out[:1] == b"<":
                    print(f"  [{i:4d}] {nm:42s} hdr={hdr:08x} flag={flag} "
                          f"len={clen} {label} -> {len(out)}B  {out[:56]!r}")
                    hit += 1
                    break
            if tried <= 4 and hit == 0:
                print(f"  [{i:4d}] {nm:42s} hdr={hdr:08x} sp={sp:08x} "
                      f"前16字节 {data[:16].hex(' ')}")
        print(f"  --> 命中 {hit}/{tried}")


if __name__ == "__main__":
    main()
