#!/usr/bin/env python3
"""LZW 解码参数穷举 —— 找出能让多块条目全部解出可读 XML 的参数组合。

观察到的事实（config.a / resources/ambush.xml，27 块）：
  * 第 0 块能解出 `<ambushRoom>...`（可读 XML 开头）
  * 第 8、22、25 块也能解出 `<babies ...>` / `<backdrops ...>` / `<bosscolors ...>`
    —— 说明「某些块」单独解是可读的，而夹在中间的大多数块不可读。

这个分布说明：**块边界不是按「4 字节长度头」整齐切分的**，
或者 **长度头的含义不是压缩后长度**，或者 **块的起始位点不在字节边界**。

本脚本对每种假设穷举解码，用「可打印字符占比」当评分，自动报告最优方案。
"""
from __future__ import annotations

import importlib.util
import itertools
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ia", HERE / "isaac-archive.py")
ia = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ia)

ISAAC = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed/config.a")


class BitReader:
    def __init__(self, data: bytes) -> None:
        self.data = data
        self.bit = 0

    def read(self, width: int) -> int | None:
        if self.bit + width > len(self.data) * 8:
            return None
        value = 0
        for _ in range(width):
            byte = self.bit >> 3
            value = (value << 1) | ((self.data[byte] >> (7 - (self.bit & 7))) & 1)
            self.bit += 1
        return value

    def tell(self) -> int:
        return self.bit

    def seek(self, bit: int) -> None:
        self.bit = bit


def decode_lzw_stream(data: bytes, width0: int, grow_rule: str,
                      max_width: int = 16) -> bytes:
    """可变宽 LZW 解码。

    grow_rule:
      'bitlen'  —— len(table).bit_length() > width  (上游/提前切换)
      'delay1'  —— len(table) + 1 >= (1 << width)   (延迟切换)
      'delay2'  —— len(table) >= (1 << width)
      'strict'  —— len(table) > (1 << width)
    """
    out = bytearray()
    reader = BitReader(data)
    width = width0
    table = [bytes([i]) for i in range(256)]
    previous: bytes | None = None
    while True:
        code = reader.read(width)
        if code is None:
            break
        if previous is None:
            if code >= len(table):
                break
            entry = table[code]
        elif code < len(table):
            entry = table[code]
            table.append(previous + entry[:1])
        else:
            entry = previous + previous[:1]
            table.append(entry)
        out += entry
        previous = entry
        if grow_rule == "bitlen":
            grow = len(table).bit_length() > width
        elif grow_rule == "delay1":
            grow = len(table) + 1 >= (1 << width)
        elif grow_rule == "delay2":
            grow = len(table) >= (1 << width)
        else:
            grow = len(table) > (1 << width)
        if grow and width < max_width:
            width += 1
    return bytes(out)


def score(data: bytes) -> float:
    if not data:
        return 0.0
    printable = sum(1 for b in data if 32 <= b < 127 or b in (9, 10, 13))
    return printable / len(data)


def split_len_prefixed(blob, offset, size, header=4, signed=True):
    fmt = "<i" if signed else "<I"
    out = []
    cursor = offset
    end = offset + size
    while cursor + header <= end:
        length = struct.unpack_from(fmt, blob, cursor)[0]
        cursor += header
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
    names = {}
    for nm in ("resources/ambush.xml", "resources/itempools.xml",
               "resources/items.xml", "resources/entities2.xml"):
        names[djb2(nm)] = nm

    for e in entries:
        if e[0] not in names:
            continue
        nm = names[e[0]]
        off, size = e[2], e[3]
        print(f"\n=== {nm}  offset={off} size={size} ===")

        # ---- 假设 A: 4 字节长度头 + 独立 LZW 流（当前模型）----
        blocks, consumed = split_len_prefixed(blob, off, size)
        print(f"[A] 4字节头切分: {len(blocks)} 块, 消费 {consumed}/{size}")
        for width0 in (8, 9):
            for rule in ("bitlen", "delay1", "delay2", "strict"):
                tot = 0.0
                good = 0
                for _, _, payload in blocks:
                    dec = decode_lzw_stream(payload, width0, rule)
                    s = score(dec)
                    tot += s
                    if s > 0.95:
                        good += 1
                print(f"    w0={width0} rule={rule:8s} 平均可读率={tot/len(blocks):.3f} "
                      f"全可读块={good}/{len(blocks)}")

        # ---- 假设 B: 整个条目是一条连续 LZW 流，块头只是分帧 ----
        print(f"[B] 整条目单流:")
        for width0 in (8, 9):
            for rule in ("bitlen", "delay1", "delay2", "strict"):
                # 把所有块数据首尾相接后连续解
                joined = b"".join(b for _, _, b in blocks)
                dec = decode_lzw_stream(joined, width0, rule)
                print(f"    w0={width0} rule={rule:8s} -> {len(dec):6d} 字节, "
                      f"可读率={score(dec):.3f} | {dec[:70]!r}")

        # ---- 假设 C: 长度头是「解压后长度」，块数据是原始明文 ----
        print(f"[C] 长度头=解压长度, 数据明文:")
        for _, _, payload in blocks[:6]:
            head = payload[:40]
            print(f"    {head!r}")

        break  # 只看第一个命中的


if __name__ == "__main__":
    main()
