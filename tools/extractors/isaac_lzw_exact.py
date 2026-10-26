#!/usr/bin/env python3
"""mode 0x01 (LZW) 解码器 —— 精确移植 isaac-ng.exe FUN_009ae880 / FUN_009ae7b0 / FUN_009ae820。

本版是**逐条汇编对照**后的最终版，修正了此前所有版本的三处根本错误：

错误 1）**第一个码必须立即输出**
    汇编 009ae8b4: CALL FUN_009ae820        ; 读第一个码
         009ae8c7: CALL FUN_009ae7b0        ; ★ 立刻输出它（此前版本漏了）
    没有这一步，所有后续字符都会错位。

错误 2）**码宽切换判据是「字典大小」，不是「码表长度」**
    汇编 009ae979: MOV EDX,[EDX+0x4]        ; width
         009ae98d: JC  0x009ae9a9           ; if (1<<width) > dictSize -> 不调整
         009ae992: INC EDX                  ; while ((1<<width) <= dictSize) width++
         009ae9a6: MOV [EAX+0x4],EDX        ; state[4] = width

错误 3）**块边界语义**
    汇编 009ae8a2-009ae8b0: 位寄存器 ESI / 位计数 BL 是 FUN_009ae880 的**局部变量**
        → 每个压缩块的位流**从头开始**（不跨块延续）
    而字典 size / width / base 挂在 this 上 → **跨块保留**

位流模型（FUN_009ae820 汇编）：
    base@+0x00, pos@+0x08, reg@+0x0c, bits(byte)@+0x10
    补字节:  while (bits < width) { bits += 8; reg = (reg<<8) | *base++; }
    取码:    bits -= width;  code = (reg >> bits) & ((1<<width)-1)     ← MSB 优先

字典项（16 字节）：[+0]=parent, [+4]=link, [+8]=link_copy, [+12]=head(首字符)
    插入: new.parent = prev; new.head = 首字符; prev.link = new_index
    输出(FUN_009ae7b0): 沿 parent 链逆序压栈，再正序输出
"""
from __future__ import annotations

import struct
from pathlib import Path

DICT_CAP = 0x1000
INIT_SIZE = 0x100


class BitStream:
    """MSB 优先；寄存器 + 剩余可用位数（对应汇编 ESI / BL）。

    **数据耗尽时 take() 返回 None**（对应汇编的「输入读满即停」语义）。
    早期版本在耗尽后补 0 继续读，导致每块解压出远超实际的内容。
    """

    __slots__ = ("data", "pos", "reg", "bits")

    def __init__(self, data: bytes) -> None:
        self.data = data
        self.pos = 0
        self.reg = 0
        self.bits = 0

    def take(self, width: int) -> int | None:
        while self.bits < width:
            if self.pos >= len(self.data):
                return None          # 输入耗尽 —— 与汇编「读满即停」一致
            b = self.data[self.pos]
            self.pos += 1
            self.reg = ((self.reg << 8) | b) & 0xFFFFFFFF
            self.bits += 8
        self.bits -= width
        return (self.reg >> self.bits) & ((1 << width) - 1)


class LzwDict:
    """对应 FUN_009ae880 使用的 state（this+0 size / this+4 width / this+8 base）。"""

    __slots__ = ("size", "width", "parent", "link", "head")

    def __init__(self) -> None:
        self.size = INIT_SIZE
        self.width = 8
        self.parent = [-1] * DICT_CAP
        self.link = [-1] * DICT_CAP
        self.head = bytearray(DICT_CAP)
        for i in range(INIT_SIZE):
            self.head[i] = i

    def reset_dict(self) -> None:
        """汇编 009ae900: 只清 link，size=0x100，width=8。"""
        self.size = INIT_SIZE
        self.width = 8
        for i in range(DICT_CAP):
            self.link[i] = -1
        # 0..255 的 parent/head 从未被改写，保持原样即可

    def adjust_width(self) -> None:
        w = self.width
        if (1 << (w & 0x1F)) <= self.size:
            while (1 << (w & 0x1F)) <= self.size:
                w += 1
            self.width = w

    def insert(self, prev: int, ch: int) -> int:
        i = self.size
        if i >= DICT_CAP:
            return -1
        self.parent[i] = prev
        self.link[i] = -1
        self.head[i] = ch & 0xFF
        if 0 <= prev < DICT_CAP:
            self.link[prev] = i
        self.size += 1
        return i

    def expand(self, code: int) -> bytes:
        """FUN_009ae7b0：沿 parent 链收集 head，再正序输出。"""
        stack = bytearray()
        c = code
        guard = 0
        while c != -1 and guard < DICT_CAP:
            stack.append(self.head[c])
            c = self.parent[c]
            guard += 1
        stack.reverse()
        return bytes(stack)


def decode_chunk(src: bytes, d: LzwDict, out_len_guard: int = 1 << 30) -> bytes:
    """解一个压缩块（位流重置，字典沿用）。

    安全阀：
      * 输入耗尽（pos > len）时停止
      * 输出超过 out_len_guard + 4096 时停止
      * 迭代次数硬上限，防止任何状态不自洽导致的死循环
    """
    bs = BitStream(src)
    out = bytearray()

    # ---- 第一个码：读 + 立即输出 ----
    code = bs.take(d.width)
    if code is None:
        return b""
    s = d.expand(code)
    out += s
    last_char = s[0] if s else 0
    prev = code

    max_iter = (len(src) * 8) // 4 + 4096
    for _ in range(max_iter):
        if len(out) > out_len_guard + 4096:
            break

        # ---- 字典溢出重置（009ae8f0）----
        if 0xFFF < d.size + 1:
            d.reset_dict()
            code = bs.take(8)
            if code is None:
                break
            s = d.expand(code)
            out += s
            last_char = s[0] if s else 0
            prev = code
            continue

        # ---- 码宽调整 ----
        d.adjust_width()

        code = bs.take(d.width)
        if code is None:
            break

        if code == d.size:
            # ---- KwKwK：code == 下一个待分配码 ----
            if d.size >= DICT_CAP:
                break
            if prev != -1:
                d.insert(prev, last_char)
            s = d.expand(code)
            out += s
            last_char = s[0] if s else 0
            prev = code
            continue

        if code > d.size:
            # 非法码（游戏会 abort）——停止
            break

        # ---- 正常路径 ----
        s = d.expand(code)
        out += s
        last_char = s[0] if s else 0
        if prev != -1 and d.size < DICT_CAP:
            d.insert(prev, last_char)
        prev = code

    return bytes(out)


def decode_entry_mode01(blob: bytes, offset: int, comp_size: int,
                         out_len: int) -> bytes:
    """mode 0x01 条目解码。

    块结构：条目载荷 = 若干「4 字节压缩长度头 + 该长度数据」分片。

    **关键语义（由 isaac-ng.exe 汇编 + 实测双重确定）**：
      * 每块由游戏侧 refill_buffer 单独喂给 LZW 解码器，
        因此**每块的位流重新开始**（位寄存器/位计数是 FUN_009ae880 的局部量）
      * 但**字典（size / width / 表）挂在持久 state 上，跨块保留**
        （state 由 FUN_0099c170 初始化，FUN_009ae880 通过 this 访问）
      * 每块的首码宽度取自 state 里保存的当前宽度（汇编 009ae899:
        MOVZX EAX, byte ptr [EBX + 0x4]）
    """
    d = LzwDict()
    cur = offset
    end = offset + comp_size
    out = bytearray()
    while cur + 4 <= end and len(out) < out_len:
        clen = struct.unpack_from("<I", blob, cur)[0]
        cur += 4
        if clen == 0 or clen > 0x7FF or cur + clen > end:
            break
        out += decode_chunk(blob[cur:cur + clen], d, out_len - len(out))
        cur += clen
    return bytes(out[:out_len])


def main() -> None:
    import importlib.util
    import xml.etree.ElementTree as ET
    HERE = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location("ia", HERE / "isaac-archive.py")
    ia = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ia)

    cfg = Path("F:/庞渃瀿/The.Binding.of.Isaac/resources/packed/config.a")
    blob = cfg.read_bytes()
    mode, entries = ia.read_archive(cfg)
    index_off = struct.unpack_from("<I", blob, 0x08)[0]

    fl = HERE.parent / "data" / "filelist.txt"
    names: dict[int, str] = {}
    for line in fl.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        h = 5381
        for ch in line.lower():
            h = ((h * 33) + ord(ch)) & 0xFFFFFFFF
        names.setdefault(h, line)

    print(f"config.a mode={mode} entries={len(entries)}\n")
    ok = 0
    total = 0
    for i, e in enumerate(entries):
        off, decl = e[2], e[3]
        comp = (entries[i + 1][2] - off) if i + 1 < len(entries) else (index_off - off)
        dec = decode_entry_mode01(blob, off, comp, decl)
        nm = names.get(e[0], "?")
        printable = sum(1 for b in dec if 32 <= b < 127 or b in (9, 10, 13))
        ratio = printable / max(1, len(dec))
        try:
            ET.fromstring(dec)
            status = "XML-OK"
            ok += 1
        except Exception:
            status = "xml-fail"
        total += 1
        print(f"[{i:3d}] {nm:36s} comp={comp:6d} decl={decl:6d} "
              f"ratio={ratio:.3f} {status}")
    print(f"\n可解析 XML: {ok}/{total}")


if __name__ == "__main__":
    main()
