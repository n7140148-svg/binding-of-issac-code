#!/usr/bin/env python3
"""mode 0x02 的 PRNG 密钥流 —— 直接从 Ghidra 反编译移植，非猜测。

来源证据（isaac-ng.exe, Ghidra 12.1.4 反编译）：

  FUN_009c2f10(uint *state_out, uint seed):
      local_1c = 0x100;
      uVar3 = (seed << 15 ^ seed) << 8 ^ seed >> 9 ^ seed;
      do {
          lVar4 = __allmul(uVar3, seed, 0x4c957f2d, 0x5851f42d);
          uVar2 = (uint)((ulonglong)(lVar4 + 0x7f) >> 0x20);
          bVar1 = (byte)(seed >> 0x18);
          uVar3 = (uVar3 >> 0x1b | seed << 5) ^ seed >> 0xd;
          *local_20 = uVar3 << (-(bVar1 >> 3) & 0x1f) | uVar3 >> (bVar1 >> 3);
          local_1c--;
          uVar3 = (uint)(lVar4 + 0x7f);
          seed = uVar2;
      } while (local_1c != 0);
      *state_out = 0;   // 计数器归零

  语义解读（x86 __allmul 语义）：
      lVar4 = uVar3 * seed            (64 位乘积)
      uVar2 = (uint)((lVar4 + 0x7f) >> 32)   ← 高 32 位 + 进位，即 (prod + 0x7f) 的高 32
      uVar3_new = ((uVar3 >> 27) | (seed << 5)) ^ (seed >> 13)     ← xorshift 结构
      *local_20 = rotl32(uVar3_new, seed >> 27)                  ← 旋转量 = seed 的高 5 位
      seed = uVar2  （下一轮 seed = 乘积高 32 + 0x7f）

  等价于：state = (state * seed + 0x7F) 的 64 位乘法，但 state 只有 32 位，
  高位由 uVar3>>27 | seed<<5 拼回 —— 这是一个 32x32→64 的 LCG + xorshift 混合。

本脚本实现上述算法，用已知明文（XML 头 <?xml）验证。
"""
from __future__ import annotations

import struct
import sys
from pathlib import Path

U32 = 0xFFFFFFFF


def _seed_expand(seed: int) -> int:
    """uVar3 = (seed << 15 ^ seed) << 8 ^ seed >> 9 ^ seed"""
    s = seed & U32
    t = ((s << 15) & U32) ^ s
    t = ((t << 8) & U32) ^ (s >> 9) ^ s
    return t & U32


def _rotl32(v: int, n: int) -> int:
    n &= 31
    return ((v << n) | (v >> (32 - n))) & U32 if n else v


class PrngStream2:
    """FUN_009c2f10 的逐字移植。"""

    def __init__(self, seed: int) -> None:
        self.seed = seed & U32
        self.u = _seed_expand(self.seed)
        self.counter = 0
        self.buf: list[int] = []
        self._generate()

    def _generate(self) -> None:
        seed = self.seed
        u = self.u
        out: list[int] = []
        for _ in range(0x100):
            # lVar4 = uVar3 * seed  (64 位)
            prod = (u * seed) & 0xFFFFFFFFFFFFFFFF
            hi = ((prod + 0x7F) >> 32) & U32
            b = (seed >> 24) & 0xFF
            rot = (b >> 3) & 0x1F
            u_new = (((u >> 27) | ((seed << 5) & U32)) & U32) ^ ((seed >> 13) & U32)
            u_new &= U32
            word = _rotl32(u_new, rot)
            out.append(word)
            u = (prod + 0x7F) & U32
            seed = hi
        self.buf = out
        self.seed = seed
        self.u = u
        self.counter = 0

    def next_byte(self) -> int:
        if self.counter >= len(self.buf):
            self._generate()
        w = self.buf[self.counter]
        self.counter += 1
        return (w >> 24) & 0xFF


def decode_prng_entry(blob: bytes, offset: int, size: int, special: int) -> bytes:
    """mode 0x02 条目解码：9 字节记录头 + 密钥流 XOR。"""
    stream = PrngStream2(special)
    data = blob[offset:offset + size]
    out = bytearray(len(data))
    for i, b in enumerate(data):
        out[i] = b ^ stream.next_byte()
    return bytes(out)


def main():
    packed = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed")
    target = packed / "repentance.a"
    blob = target.read_bytes()
    assert blob[:7] == b"ARCH000"
    mode = blob[7]
    index_off = struct.unpack_from("<I", blob, 0x08)[0]
    count = struct.unpack_from("<H", blob, 0x0C)[0]
    print(f"repentance.a mode={mode} entries={count}")

    # filelist 反查
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

    PT = b"<?xml"
    hits = 0
    tried = 0
    for i in range(count):
        h, sp, off, size, crc = struct.unpack_from("<5I", blob, index_off + i * 20)
        nm = names.get(h, "")
        if not nm.endswith(".xml"):
            continue
        tried += 1
        rec = blob[off:off + 9]
        if len(rec) < 9:
            continue
        stored = rec[3] == 0x80
        if stored:
            continue
        dec = decode_prng_entry(blob, off + 9, size, sp)
        ok = dec[:5] == PT
        if ok:
            hits += 1
        if tried <= 12:
            print(f"[{i:4d}] {nm:44s} sp={sp:08x} {'MATCH' if ok else 'no   '} "
                  f"| {dec[:48]!r}")
    print(f"\nPRNG 解密命中 <?xml : {hits}/{tried} 个 xml 条目")


if __name__ == "__main__":
    main()
