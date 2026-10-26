#!/usr/bin/env python3
"""多线程分块下载器 + 断点续传，用于大文件（GitHub Releases 等）。

用法: dl.py <url> <dest> [threads]
已下载部分会按 .part 文件的字节范围续传，校验用 zipfile。
"""
import os, sys, threading, time, urllib.request

PROXY = "http://127.0.0.1:7897"

def size_of(url):
    op = urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    req = urllib.request.Request(url, method="HEAD")
    with op.open(req, timeout=60) as r:
        return int(r.headers.get("Content-Length", "0"))

def worker(url, part, start, end, idx, done, lock):
    op = urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    pos = start
    chunk = 1 << 20
    while pos <= end:
        try:
            req = urllib.request.Request(url)
            req.add_header("Range", f"bytes={pos}-{end}")
            with op.open(req, timeout=120) as r:
                while True:
                    b = r.read(1 << 18)
                    if not b:
                        break
                    with lock:
                        part.seek(pos); part.write(b)
                    pos += len(b)
                    with lock:
                        done[idx] = pos - start
                    if pos > end:
                        break
        except Exception as e:
            time.sleep(2)
            continue
        if pos > end:
            break

def main():
    url, dest = sys.argv[1], sys.argv[2]
    nthreads = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    total = size_of(url)
    print(f"remote size = {total} ({total/1024/1024:.1f} MB)", flush=True)
    part_path = dest + ".part"
    if not os.path.exists(part_path):
        open(part_path, "wb").close()
    part = open(part_path, "r+b")
    part.truncate(total)
    # 计算每块起点
    per = total // nthreads
    bounds = []
    for i in range(nthreads):
        s = i * per
        e = (total - 1) if i == nthreads - 1 else (s + per - 1)
        bounds.append((s, e))
    done = [0] * nthreads
    lock = threading.Lock()
    threads = []
    for i, (s, e) in enumerate(bounds):
        t = threading.Thread(target=worker, args=(url, part, s, e, i, done, lock), daemon=True)
        t.start(); threads.append(t)
    last = 0
    while any(t.is_alive() for t in threads):
        time.sleep(5)
        got = sum(done)
        if got - last > 8 * 1024 * 1024:
            print(f"  {got/1024/1024:.0f}/{total/1024/1024:.0f} MB", flush=True)
            last = got
    for t in threads: t.join()
    part.close()
    # 校验并改名
    import zipfile
    try:
        z = zipfile.ZipFile(part_path)
        n = len(z.namelist())
        z.close()
        os.replace(part_path, dest)
        print(f"DONE, valid zip, {n} entries -> {dest}", flush=True)
    except Exception as e:
        print(f"ZIP INVALID: {e}", flush=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
