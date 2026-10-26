#!/usr/bin/env python3
"""LZW 剩余差异的暴力搜索 —— 以「XML 可解析」为唯一判据。

已确定（来自 isaac-ng.exe 汇编）：
  * 位流 MSB 优先，寄存器 + 剩余位数模型
  * 字典容量 0x1000，初始 size=0x100 width=8
  * 码宽切换判据：while ((1<<width) <= dictSize) width++
  * 首码立即输出
  * 块 = [u32 压缩长度][数据]，字典跨块保留

待定（本脚本搜索）：
  A) 块边界处位流是否重置
  B) 块边界处宽度是否重置为 8
  C) 块边界处字典 size 是否重置
  D) 每块首码之后的「prev」初值
  E) 块边界处 prev 是否保留

搜索空间：A×B×C×E = 2^4 = 16 组，另有 D 两种 → 32 组。
判据：config.a 24 个条目中能解析为 XML 的数量 + 可读率总和。
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

CFG = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed/config.a")
DICT_CAP = 0x1000
INIT_SIZE = 0x100


class BitStream:
    __slots__ = ("data", "pos", "reg", "bits")

    def __init__(self, data: bytes) -> None:
        self.data = data
        self.pos = 0
        self.reg = 0
        self.bits = 0

    def take(self, width: int) -> int:
        while self.bits < width:
            b = self.data[self.pos] if self.pos < len(self.data) else 0
            self.pos += 1
            self.reg = ((self.reg << 8) | b) & 0xFFFFFFFF
            self.bits += 8
        self.bits -= width
        return (self.reg >> self.bits) & ((1 << width) - 1)


class Dict:
    __slots__ = ("size", "width", "parent", "head")

    def __init__(self) -> None:
        self.size = INIT_SIZE
        self.width = 8
        self.parent = [-1] * DICT_CAP
        self.head = bytearray(DICT_CAP)
        for i in range(INIT_SIZE):
            self.head[i] = i

    def reset(self) -> None:
        self.size = INIT_SIZE
        self.width = 8
        for i in range(DICT_CAP):
            self.parent[i] = -1
        for i in range(INIT_SIZE):
            self.head[i] = i

    def adjust(self) -> None:
        w = self.width
        while (1 << (w & 0x1F)) <= self.size:
            w += 1
        self.width = w

    def insert(self, prev: int, ch: int) -> None:
        if self.size >= DICT_CAP:
            return
        i = self.size
        self.parent[i] = prev
        self.head[i] = ch & 0xFF
        self.size += 1

    def expand(self, code: int) -> bytes:
        st = bytearray()
        c = code
        g = 0
        while c != -1 and g < DICT_CAP:
            st.append(self.head[c])
            c = self.parent[c]
            g += 1
        st.reverse()
        return bytes(st)


def decode_entry(blob, offset, comp_size, out_len, opt):
    """opt: dict of flags"""
    d = Dict()
    cur = offset
    end = offset + comp_size
    pieces = []
    while cur + 4 <= end:
        clen = struct.unpack_from("<I", blob, cur)[0]
        cur += 4
        if clen == 0 or clen > 0x7FF or cur + clen > end:
            break
        pieces.append(blob[cur:cur + clen])
        cur += clen
    if not pieces:
        return b""

    out = bytearray()
    prev = -1
    last = 0
    bs = BitStream(b"")
    if opt["stream_cont"]:
        bs = BitStream(b"".join(pieces))
        chunks = [bs]
    else:
        chunks = [BitStream(c) for c in pieces]

    for bi, cb in enumerate(chunks):
        if bi > 0:
            if opt["reset_width"]:
                d.width = 8
            if opt["reset_size"]:
                d.reset()
            if opt["reset_prev"]:
                prev = -1
        if bi > 0 and not opt["stream_cont"]:
            cb = BitStream(chunks[bi].data)
        # 首码
        if prev == -1 and not opt["keep_prev"]:
            code = cb.take(d.width)
            s = d.expand(code)
            out += s
            last = s[0] if s else 0
            prev = code
        elif opt["keep_prev"] and bi > 0:
            pass
        # 主循环
        for _ in range(200000):
            if len(out) >= out_len + 8192:
                break
            if cb.pos > len(cb.data) and cb.bits <= 0:
                break
            if 0xFFF < d.size + 1:
                d.reset()
                code = cb.take(8)
                s = d.expand(code)
                out += s
                last = s[0] if s else 0
                prev = code
                continue
            d.adjust()
            code = cb.take(d.width)
            if code == d.size:
                if d.size >= DICT_CAP:
                    break
                if prev != -1:
                    d.insert(prev, last)
                s = d.expand(code)
                out += s
                last = s[0] if s else 0
                prev = code
                continue
            if code > d.size:
                break
            s = d.expand(code)
            out += s
            last = s[0] if s else 0
            if prev != -1 and d.size < DICT_CAP:
                d.insert(prev, last)
            prev = code
    return bytes(out[:out_len])


def main():
    blob = CFG.read_bytes()
    mode, entries = ia.read_archive(CFG)
    index_off = struct.unpack_from("<I", blob, 0x08)[0]
    fl = HERE.parent / "data" / "filelist.txt"
    names = {}
    for line in fl.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        h = 5381
        for ch in line.lower():
            h = ((h * 33) + ord(ch)) & 0xFFFFFFFF
        names.setdefault(h, line)

    results = []
    for sc, rw, rs, rp in itertools.product((True, False), repeat=4):
        opt = {"stream_cont": sc, "reset_width": rw, "reset_size": rs,
               "reset_prev": rp, "keep_prev": rp}
        ok = 0
        ratio_sum = 0.0
        for i, e in enumerate(entries):
            off, decl = e[2], e[3]
            comp = (entries[i + 1][2] - off) if i + 1 < len(entries) else (index_off - off)
            dec = decode_entry(blob, off, comp, decl, opt)
            pr = sum(1 for b in dec if 32 <= b < 127 or b in (9, 10, 13)) / max(1, len(dec))
            ratio_sum += pr
            try:
                ET.fromstring(dec)
                ok += 1
            except Exception:
                pass
        results.append((ok, ratio_sum, sc, rw, rs, rp))
        print(f"stream_cont={sc} reset_width={rw} reset_size={rs} reset_prev={rp} "
              f"-> XML={ok}/{len(entries)} ratio_sum={ratio_sum:.2f}")
    results.sort(reverse=True)
    print("\n=== TOP 3 ===")
    for r in results[:3]:
        print(" ", r)


if __name__ == "__main__":
    main()
