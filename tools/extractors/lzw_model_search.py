#!/usr/bin/env python3
"""LZW 解码器精细模型搜索 —— 目标是让 24 个 XML 条目**全部**解出可解析 XML。

已确认的事实：
  * ARCH000 索引的 size 字段 = **解压后字节数**（单块条目 dec == size 精确成立）
  * 载荷 = 若干「4 字节长度头 + 数据」块
  * 字典**跨块共享**（players.xml 共享解可读率 0.926 vs 独立 0.49）
  * 上游 grow 规则 `len(table).bit_length() > width` 优于延迟切换

待定：块长度头的确切语义，以及块边界的码宽处理。
本脚本穷举「块头语义 × 码宽规则 × 是否每块重置码宽」，
用「24 条目中可解析 XML 的数量」+「dec 是否精确等于 decl」当评分。
"""
from __future__ import annotations

import importlib.util
import itertools
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ia", HERE / "isaac-archive.py")
ia = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ia)

ISAAC = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed/config.a")


class BitReader:
    __slots__ = ("d", "b")

    def __init__(self, d: bytes) -> None:
        self.d = d
        self.b = 0

    def read(self, w: int) -> int | None:
        if self.b + w > len(self.d) * 8:
            return None
        v = 0
        for _ in range(w):
            v = (v << 1) | ((self.d[self.b >> 3] >> (7 - (self.b & 7))) & 1)
            self.b += 1
        return v


def decode_blocks(blocks, w0=8, rule="bitlen", reset_width_per_block=False,
                  skip_first_code=False):
    """blocks: list[bytes]，返回解码文本。字典跨块共享。"""
    out = bytearray()
    width = w0
    table = [bytes([i]) for i in range(256)]
    prev = None
    first = True
    for payload in blocks:
        r = BitReader(payload)
        if reset_width_per_block:
            width = w0
        prev = None if reset_width_per_block else prev
        first = True
        while True:
            code = r.read(width)
            if code is None:
                break
            if skip_first_code and first:
                first = False
                prev = table[code] if code < len(table) else None
                if prev is None:
                    break
                continue
            first = False
            if prev is None:
                if code >= len(table):
                    break
                entry = table[code]
            elif code < len(table):
                entry = table[code]
                table.append(prev + entry[:1])
            else:
                entry = prev + prev[:1]
                table.append(entry)
            out += entry
            prev = entry
            if rule == "bitlen":
                grow = len(table).bit_length() > width
            elif rule == "delay1":
                grow = len(table) + 1 >= (1 << width)
            elif rule == "delay2":
                grow = len(table) >= (1 << width)
            else:
                grow = len(table) > (1 << width)
            if grow and width < 16:
                width += 1
    return bytes(out)


def split_blocks(blob, offset, comp, header_semantics):
    """header_semantics: 'comp' | 'decomp' | 'u32be' | 'u16'"""
    out = []
    cursor = offset
    end = offset + comp
    while cursor + 4 <= end:
        if header_semantics == "u16":
            if cursor + 2 > end:
                break
            length = struct.unpack_from("<H", blob, cursor)[0]
            cursor += 2
        elif header_semantics == "u32be":
            length = struct.unpack_from(">I", blob, cursor)[0]
            cursor += 4
        else:
            length = struct.unpack_from("<i", blob, cursor)[0]
            cursor += 4
        if length <= 0 or cursor + length > end:
            break
        out.append(blob[cursor:cursor + length])
        cursor += length
    return out


def main():
    mode, entries = ia.read_archive(ISAAC)
    blob = ISAAC.read_bytes()

    best = []
    for hs in ("comp",):
        for w0 in (8,):
            for rule in ("bitlen", "delay1", "delay2", "strict"):
                for rw in (False, True):
                    for sk in (False, True):
                        ok = 0
                        exact = 0
                        for i, e in enumerate(entries):
                            off = e[2]
                            comp = (entries[i + 1][2] - off) if i + 1 < len(entries) \
                                else (struct.unpack_from("<I", blob, 0x08)[0] - off)
                            bs = split_blocks(blob, off, comp, hs)
                            dec = decode_blocks(bs, w0, rule, rw, sk)
                            if len(dec) == e[3]:
                                exact += 1
                            try:
                                ET.fromstring(dec)
                                ok += 1
                            except Exception:
                                pass
                        best.append((ok, exact, hs, w0, rule, rw, sk))
                        print(f"hs={hs} w0={w0} rule={rule:7s} resetW={rw} skip1={sk} "
                              f"-> XML ok={ok}/{len(entries)} exact={exact}/{len(entries)}")

    best.sort(reverse=True)
    print("\n=== TOP 5 ===")
    for b in best[:5]:
        print(" ", b)


if __name__ == "__main__":
    main()
