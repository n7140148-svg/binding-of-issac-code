#!/usr/bin/env python3
"""Build a navigable index of the Ghidra reverse-engineering dump for Isaac.

Scope (per user 2026-10-26): reverse to the level usable for OUR topdown
roguelike project. Audio/textures (the mode-0x02 XOR / ISAAC art-asset
sub-stream) are explicitly OUT OF SCOPE and not needed.

This script only parses the existing ghidra_out/*.txt dump; it does not
re-decompile anything.
"""
from __future__ import annotations
import json
import re
import os
from pathlib import Path

ROOT = Path(r"C:/Users/abc/WorkBuddy/2026-10-24-19-02-15/isaac_reverse")
OUT = ROOT / "handover"
OUT.mkdir(exist_ok=True)
GH = ROOT / "ghidra_out"

# Subsystem classification by function address band (from DumpCore.java scan
# range 0x00990000-0x009D0000) plus by name/keyword heuristics.
SEED_FUNCS = {
    "0x0099bfa0": "archive-loader",
    "0x0099c170": "archive-init",
    "0x0099c270": "mode0x02-readblock",
    "0x0099c690": "archive-io",
    "0x009c2f10": "isaac-keygen",
    "0x009c30b0": "isaac-randinit",
    "0x00963db0": "archive-aux",
    "0x0099c490": "archive-aux2",
    "0x0099c590": "archive-aux3",
}

KEYWORDS = {
    "lzw": "lzw",
    "deflate": "deflate",
    "miniz": "deflate",
    "isaac": "isaac",
    "xor": "crypto-xor",
    "archive": "archive",
    "seed": "archive",
    "crypt": "crypto-xor",
    "png": "art-asset",
    "wav": "art-asset",
    "xml": "data-parse",
    "room": "data-parse",
    "item": "data-parse",
    "entity": "data-parse",
    "stage": "data-parse",
}


def classify(name: str, addr: str) -> str:
    low = name.lower()
    for kw, tag in KEYWORDS.items():
        if kw in low:
            return tag
    if addr in SEED_FUNCS:
        return SEED_FUNCS[addr]
    return "other"


def parse_file(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    fn = path.name
    m = re.match(r"(FUN_[0-9a-fA-F]+)__([0-9a-fA-F]+)__(callee|caller|seed|scan)\.txt", fn)
    if not m:
        return None
    name, addr, tag = m.group(1), "0x" + m.group(2).lower(), m.group(3)
    # assembly line count
    asm = re.search(r"---- ASSEMBLY ----(.*?)---- DECOMPILED C ----", text, re.S)
    asm_lines = 0
    if asm:
        asm_lines = len([l for l in asm.group(1).splitlines() if l.strip()])
    # decompiled C block
    dec = re.search(r"---- DECOMPILED C ----\n(.*?)---- PCODE", text, re.S)
    dec_c = ""
    has_c = False
    if dec:
        dec_c = dec.group(1).strip()
        has_c = ("// decompile failed" not in dec_c) and len(dec_c) > 0
    # signature: first plausible function-decl line
    sig = ""
    if has_c:
        for line in dec_c.splitlines():
            s = line.strip()
            if s.startswith("//") or not s:
                continue
            if re.search(r"\w+\s+\*?\w+\s*\(", s) and ("(" in s) and (")" in s):
                sig = s[:160]
                break
    return {
        "name": name,
        "addr": addr,
        "tag": tag,
        "asm_lines": asm_lines,
        "has_c": has_c,
        "dec_len": len(dec_c),
        "sig": sig,
        "subsystem": classify(name, addr),
        "file": fn,
    }


def main():
    rows = []
    for p in sorted(GH.glob("FUN_*.txt")):
        r = parse_file(p)
        if r:
            rows.append(r)
    rows.sort(key=lambda r: (r["addr"], r["tag"]))

    # subsystem summary
    subs = {}
    for r in rows:
        s = r["subsystem"]
        subs.setdefault(s, {"total": 0, "with_c": 0, "asm": 0})
        subs[s]["total"] += 1
        if r["has_c"]:
            subs[s]["with_c"] += 1
        subs[s]["asm"] += r["asm_lines"]

    # write JSON
    (OUT / "INDEX.json").write_text(
        json.dumps({"count": len(rows), "subsystems": subs, "rows": rows},
                   ensure_ascii=False, indent=1), encoding="utf-8")

    # write Markdown index
    lines = []
    lines.append("# Isaac 逆向函数索引（Ghidra 反编译）\n")
    lines.append(f"> 自动生成 · 共 **{len(rows)}** 个函数文件 · 源目录 `isaac_reverse/ghidra_out/`\n")
    lines.append("> 范围：资源/归档/加解密子系统（地址段 0x00990000–0x009D0000）。\n")
    lines.append("> 音频/贴图（mode-0x02 XOR/ISAAC 美术资源子流）按用户要求不做。\n")
    lines.append("\n## 子系统统计\n")
    lines.append("| 子系统 | 函数数 | 含反编译C | 汇编行数 |")
    lines.append("|---|---|---|---|")
    for s in sorted(subs, key=lambda k: -subs[k]["total"]):
        v = subs[s]
        lines.append(f"| {s} | {v['total']} | {v['with_c']} | {v['asm']} |")
    lines.append("\n## 全量函数表\n")
    lines.append("| 地址 | 名 | tag | 子系统 | 反编译C | 汇编行 | 签名 |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in rows:
        c = "✅" if r["has_c"] else "—"
        sig = (r["sig"] or "").replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {r['addr']} | {r['name']} | {r['tag']} | {r['subsystem']} | {c} | {r['asm_lines']} | `{sig}` |")
    (OUT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    # also a focused KEY-FUNCTIONS doc for the ones we already analyzed
    key = [r for r in rows if r["addr"] in SEED_FUNCS]
    klines = ["# 重点逆向函数（已分析并用于破解归档格式）\n",
              "这些函数是破解 ARCH000 三编码的直接证据来源。\n",
              "| 地址 | 子系统 | 文件 | 反编译C |",
              "|---|---|---|---|"]
    for r in sorted(key, key=lambda x: x["addr"]):
        c = "✅" if r["has_c"] else "—"
        klines.append(f"| {r['addr']} | {r['subsystem']} | `{r['file']}` | {c} |")
    (OUT / "KEY-FUNCTIONS.md").write_text("\n".join(klines), encoding="utf-8")

    print(f"parsed {len(rows)} files")
    print("subsystems:")
    for s in sorted(subs, key=lambda k: -subs[k]["total"]):
        v = subs[s]
        print(f"  {s:14s} total={v['total']:4d} with_c={v['with_c']:4d} asm={v['asm']}")
    print(f"wrote {OUT/'INDEX.md'} ({OUT/'INDEX.json'}) ({OUT/'KEY-FUNCTIONS.md'})")


if __name__ == "__main__":
    main()
