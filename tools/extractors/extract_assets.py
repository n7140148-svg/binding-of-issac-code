#!/usr/bin/env python3
"""批量提取 Isaac ARCH000 归档中可直接解码的资源。

支持两类：
  mode 0x00 —— 已验证的 ASSET_SEED XOR 密码（graphics/music/sfx/videos）
  mode 0x02 —— 记录头声明 stored 的条目（明文，9 字节头之后即载荷）

用法: extract_assets.py <packed_dir> <out_dir> [archive.a ...]
"""
import importlib.util, os, sys, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ia", HERE / "isaac-archive.py")
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)

REC = ia.RECORD_HEADER_SIZE

def safe_name(p):
    return p.replace("\\", "/").lstrip("/").replace(":", "_")

def main():
    packed = Path(sys.argv[1]); out_root = Path(sys.argv[2])
    targets = sys.argv[3:] or [f.name for f in sorted(packed.glob("*.a"))]
    total = collections.Counter()
    for name in targets:
        f = packed / name
        if not f.is_file():
            print(f"skip {name}: missing"); continue
        try:
            mode, entries = ia.read_archive(f)
        except Exception as e:
            print(f"skip {name}: {e}"); continue
        blob = f.read_bytes()
        names = ia.load_name_table(os.environ.get("ISAEC_FILELIST"), f)
        n_out = 0
        for i, e in enumerate(entries):
            off, size, special = e[2], e[3], e[1]
            data = None
            if mode == ia.MODE_ASSETS:
                span = ia.asset_span(entries, i, len(blob))
                data = ia.decode_assets(blob, off, size, special, span)[:size]
            elif mode == ia.MODE_PRNG and ia.is_stored(blob, e):
                data = blob[off + REC: off + REC + size]
            if not data:
                continue
            res = names.get(e[0])
            if not res:
                res = f"{name[:-2]}/unnamed/{i:06d}.bin"
            dst = out_root / safe_name(res)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(data)
            n_out += 1
        total[name] = n_out
        print(f"{name}: extracted {n_out}/{len(entries)}")
    print("TOTAL:", sum(total.values()), dict(total))

if __name__ == "__main__":
    main()
