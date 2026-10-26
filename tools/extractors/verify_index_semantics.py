#!/usr/bin/env python3
"""验证 ARCH000 索引语义修正：size = 解压后长度，载荷长度由下一条目 offset 决定。

依据（config.a 索引表）：
    entry0 offset=0x000E(14)    size=25894
    entry1 offset=0x2274(8820)  size=7390
若 size 是压缩长度，则 entry0 覆盖 [14, 25908) 会与 entry1 的 8820 重叠 —— 不可能。
若 size 是**解压后长度**，则 entry0 压缩载荷 = [14, 8820) = 8806 字节 → 25894 字节，
压缩比 2.94，对 XML 完全合理。

本脚本对全部条目验证：修正后的载荷能否解出**完整可解析 XML**。
"""
from __future__ import annotations

import importlib.util
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ia", HERE / "isaac-archive.py")
ia = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ia)

sys.path.insert(0, str(HERE))
from isaac_lzw import decode_lzw_block  # noqa: E402

ISAAC = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed/config.a")


def load_names():
    fl = HERE.parent / "data" / "filelist.txt"
    names = {}
    if fl.exists():
        for line in fl.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            h = 5381
            for ch in line.lower():
                h = ((h * 33) + ord(ch)) & 0xFFFFFFFF
            names.setdefault(h, line)
    return names


def split_blocks(blob, offset, comp_size):
    out = []
    cursor = offset
    end = offset + comp_size
    while cursor + 4 <= end:
        length = struct.unpack_from("<i", blob, cursor)[0]
        cursor += 4
        if length <= 0 or cursor + length > end:
            break
        out.append((cursor, length, blob[cursor:cursor + length]))
        cursor += length
    return out, cursor - offset


def main():
    mode, entries = ia.read_archive(ISAAC)
    blob = ISAAC.read_bytes()
    names = load_names()
    print(f"config.a mode={mode} entries={len(entries)}\n")

    print(f"{'idx':>3} {'hash':>10} {'off':>7} {'comp':>7} {'decl':>7} "
          f"{'blocks':>6} {'dec':>7} {'ratio':>5} {'xml?':>5}  name")
    total_ok = 0
    for i, e in enumerate(entries):
        off, size = e[2], e[3]
        if i + 1 < len(entries):
            comp = entries[i + 1][2] - off
        else:
            comp = struct.unpack_from("<I", blob, 0x08)[0] - off
        blocks, consumed = split_blocks(blob, off, comp)
        dec = bytearray()
        for _, _, payload in blocks:
            dec += decode_lzw_block(payload)
        dec = bytes(dec)
        printable = sum(1 for b in dec if 32 <= b < 127 or b in (9, 10, 13))
        ratio = printable / max(1, len(dec))
        try:
            ET.fromstring(dec)
            xml_ok = "OK"
            total_ok += 1
        except Exception:
            xml_ok = "-"
        nm = names.get(e[0], "?")
        print(f"{i:3d} {e[0]:10x} {off:7d} {comp:7d} {size:7d} "
              f"{len(blocks):6d} {len(dec):7d} {ratio:5.2f} {xml_ok:>5}  {nm}")

    print(f"\n可解析 XML: {total_ok}/{len(entries)}")


if __name__ == "__main__":
    main()
