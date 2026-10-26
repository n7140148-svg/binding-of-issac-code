#!/usr/bin/env python3
"""Isaac ARCH000 mode 0x01（LZW）归档解码器 —— 本机 1.7.9B 实测修正版。

与上游参考实现（caos-obliquo/tboi-recomp）的差异，均由本机实测确定：

1. **每块独立解码**：条目由多个「4 字节长度头 + LZW 数据」块组成，
   每块的字典必须重置。上游把所有块连续喂给同一个解码器 → 字典污染 → 失步。
2. **起始码宽 8 位**：上游用 8 位起始但对「无 256/257 复位码」的处理不同；
   实测本机数据无 clear/end 码，起始宽度即 8。
3. **码宽切换条件**：当 `len(table)+1 >= (1<<width)` 时增宽（延迟切换）。
   上游用 `len(table).bit_length() > width`（提前切换）→ 与游戏编码器不同步。

实测依据：`config.a` 的 `itempools.xml` 条目，本解码器输出完整可读 XML，
逐字符与结构均正确（`<ItemPools>` 开头、`<Pool Name="treasure">` 池、
`<Item Id="1" Weight="1" .../>` 条目）。
"""

from __future__ import annotations

import struct
from typing import Iterator

U32 = 0xFFFFFFFF


def _read_code(data: bytes, bitpos: int, width: int) -> int:
    """从 MSB 优先的位流读一个 width 位的码。"""
    byte = bitpos >> 3
    off = bitpos & 7
    chunk = int.from_bytes(data[byte:byte + 3].ljust(3, b"\x00"), "big")
    return (chunk >> (24 - off - width)) & ((1 << width) - 1)


def decode_lzw_block(data: bytes, width0: int = 8, max_width: int = 16) -> bytes:
    """解码一个 LZW 块。无 clear/end 码，字典从 256 个单字节字面量开始。"""
    out = bytearray()
    bit = 0
    nbits = len(data) * 8
    width = width0
    table: list[bytes] = [bytes([i]) for i in range(256)]
    prev: bytes | None = None
    while bit + width <= nbits:
        code = _read_code(data, bit, width)
        bit += width
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
        # 延迟切换：字典达到当前码宽上限才增宽
        if len(table) + 1 >= (1 << width) and width < max_width:
            width += 1
    return bytes(out)


def iter_lzw_blocks(blob: bytes, offset: int, size: int) -> Iterator[bytes]:
    """按「4 字节长度头 + 数据」逐块产出 LZW 载荷。"""
    cursor = offset
    end = offset + size
    while cursor + 4 <= end:
        length = struct.unpack_from("<i", blob, cursor)[0]
        cursor += 4
        if length <= 0 or cursor + length > end:
            break
        yield blob[cursor:cursor + length]
        cursor += length


def decode_lzw(blob: bytes, offset: int, size: int) -> bytes:
    """解码一个 mode 0x01 条目：逐块独立解码后拼接。"""
    out = bytearray()
    for block in iter_lzw_blocks(blob, offset, size):
        out += decode_lzw_block(block)
    return bytes(out)
