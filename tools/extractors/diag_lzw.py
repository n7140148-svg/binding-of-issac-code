#!/usr/bin/env python3
"""逐块诊断 mode 0x01 条目的 LZW 解码失步点。

对 `config.a` 里的 `resources/itempools.xml`：
  1. 切出全部 LZW 块（4 字节长度头 + 数据）
  2. 每块单独解码，输出长度与前后若干字符
  3. 找出第一个「不像 XML 文本」的块 → 定位失步根因
"""
from __future__ import annotations

import importlib.util
import os
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ia", HERE / "isaac-archive.py")
ia = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ia)

sys.path.insert(0, str(HERE))
from isaac_lzw import decode_lzw_block  # noqa: E402

ISAAC = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed/config.a")


def split_blocks(blob, offset, size):
    """返回 [(块起始绝对偏移, 块长度, 载荷 bytes)]"""
    out = []
    cursor = offset
    end = offset + size
    while cursor + 4 <= end:
        length = struct.unpack_from("<i", blob, cursor)[0]
        cursor += 4
        if length <= 0 or cursor + length > end:
            break
        out.append((cursor, length, blob[cursor:cursor + length]))
        cursor += length
    return out, cursor - offset


def djb2(name: str) -> int:
    h = 5381
    for ch in name.lower():
        h = ((h * 33) + ord(ch)) & 0xFFFFFFFF
    return h


def main():
    mode, entries = ia.read_archive(ISAAC)
    blob = ISAAC.read_bytes()
    print(f"config.a mode={mode} entries={len(entries)}")

    # 按 hash 反查资源名
    want = {}
    for name in ("resources/itempools.xml", "resources/items.xml",
                 "resources/entities2.xml", "resources/ambush.xml",
                 "resources/bosses.xml", "resources/challenges.xml"):
        want[djb2(name)] = name

    target = None
    for e in entries:
        if e[0] in want:
            target = (e, want[e[0]])
            break

    if not target:
        print("未匹配；全部 hash：")
        for e in entries:
            print(" ", hex(e[0]), e[1], e[2], e[3])
        return

    e, name = target
    print(f"命中 {name}: hash={hex(e[0])} offset={e[2]} size={e[3]}")

    blocks, consumed = split_blocks(blob, e[2], e[3])
    print(f"切出 {len(blocks)} 块，消费 {consumed}/{e[3]} 字节，尾差 = {e[3] - consumed}")

    ok = 0
    bad = []
    for idx, (off, ln, data) in enumerate(blocks):
        dec = decode_lzw_block(data)
        printable = sum(1 for b in dec if 32 <= b < 127 or b in (9, 10, 13))
        ratio = printable / max(1, len(dec))
        flag = "OK " if ratio > 0.95 else "BAD"
        if ratio > 0.95:
            ok += 1
        else:
            bad.append(idx)
        if idx < 10 or ratio <= 0.95 or idx >= len(blocks) - 3:
            print(f"[{idx:3d}] {flag} off={off} len={ln} -> dec={len(dec):5d} "
                  f"ratio={ratio:.2f} | {dec[:56]!r}")

    print(f"\n可读块 {ok}/{len(blocks)}，坏块 {len(bad)} 个")
    if bad:
        print("首个坏块 index =", bad[0], " 坏块 =", bad[:24])


if __name__ == "__main__":
    main()
