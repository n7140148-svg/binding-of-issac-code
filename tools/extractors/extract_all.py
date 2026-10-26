#!/usr/bin/env python3
"""批量提取 Isaac ARCH000 归档中所有可解码条目。

三种编码（均由 isaac-ng.exe 反编译确认）：
  mode 0x00 —— ASSET_SEED XOR（graphics / music / sfx / videos）
  mode 0x01 —— LZW（config / fonts / rooms / animations）
  mode 0x02 —— MiniZ(zlib) + 可选 XOR 密钥流（repentance / afterbirthp / 本地化包）

用法: extract_all.py <packed_dir> <out_dir>
"""
from __future__ import annotations

import importlib.util
import os
import struct
import sys
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ia", HERE / "isaac-archive.py")
ia = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ia)

sys.path.insert(0, str(HERE))
from isaac_lzw_exact import decode_entry_mode01  # noqa: E402
from isaac_mode02_stream import decode_mode02_entry  # noqa: E402


def safe_name(p: str) -> str:
    return p.replace("\\", "/").lstrip("/").replace(":", "_")


def main() -> None:
    packed = Path(sys.argv[1])
    out_root = Path(sys.argv[2])
    total = 0
    summary = []
    for f in sorted(packed.glob("*.a")):
        try:
            mode, entries = ia.read_archive(f)
        except Exception as e:
            print(f"skip {f.name}: {e}")
            continue
        blob = f.read_bytes()
        index_off = struct.unpack_from("<I", blob, 0x08)[0]
        names = ia.load_name_table(os.environ.get("ISAEC_FILELIST"), f)
        n_ok = n_all = 0
        for i, e in enumerate(entries):
            h, sp, off, size, crc = e
            if i + 1 < len(entries):
                comp = entries[i + 1][2] - off
            else:
                comp = index_off - off
            data = None
            if mode == ia.MODE_ASSETS:
                span = ia.asset_span(entries, i, len(blob))
                data = ia.decode_assets(blob, off, size, sp, span)[:size]
            elif mode == ia.MODE_LZW:
                data = decode_entry_mode01(blob, off, comp, size)
            elif mode == ia.MODE_PRNG:
                data = decode_mode02_entry(blob, off, comp, size)
            n_all += 1
            if not data:
                continue
            res = names.get(h)
            if not res:
                res = f"{f.stem}/unnamed/{i:06d}.bin"
            dst = out_root / safe_name(res)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(data)
            n_ok += 1
        total += n_ok
        summary.append((f.name, mode, n_ok, n_all))
        print(f"{f.name:24s} mode={mode} extracted {n_ok}/{n_all}")
    print(f"\nTOTAL extracted: {total}")
    for s in summary:
        print("  ", s)


if __name__ == "__main__":
    main()
