# 提取器清单（`handover/tools/extractors/`）

全部脚本由本机实测 + Ghidra 反编译对照得出，**非转录自其他实现**。运行需 Python 3.11+，仅用标准库、无第三方依赖。

| 脚本 | 作用 | 关键输入/输出 |
|---|---|---|
| `isaac-archive.py` | ARCH000 容器主解码器（三编码统一入口）| 某个 `.a` 归档 → 解码后的单文件 |
| `extract_all.py` | 批量提取某归档所有可解码条目（三编码）| 归档目录 → 解出的文件树 |
| `extract_assets.py` | 提取可直接解码的资源（mode0x00 XOR / mode0x02 stored 明文）| 归档目录 → 资源文件 |
| `isaac_lzw.py` | mode 0x01 LZW 解码器（本机 1.7.9B 实测修正版）| mode0x01 原始块 → 解压数据 |
| `isaac_lzw_exact.py` | mode 0x01 **精确移植 `FUN_009ae880`**（逐汇编对照最终版）| mode0x01 原始块 → 解压数据 |
| `isaac_mode02.py` | mode 0x02 解密，精确移植 `FUN_0099c270` 语义 | mode0x02 原始块 → 解压数据 |
| `isaac_mode02_stream.py` | mode 0x02 **流式 MiniZ** 解码（多块共享 inflate 流）| mode0x02 条目 → 解压数据 |
| `isaac_prng2.py` | mode 0x02 的 **PRNG 密钥流**（`FUN_009c2f10` 移植，非猜测）| seed → 密钥流 |
| `verify_index_semantics.py` | 验证索引语义：`size` = 解压后长度 | 归档索引 → 校验报告 |
| `build_index.py` | 解析 `ghidra_out/*.txt`，生成可导航索引 | 反编译 dump → `INDEX.md/json` |
| `diag_lzw.py` | 逐块诊断 mode0x01 LZW 失步点 | `config.a` → 诊断输出 |
| `lzw_search.py` | LZW 解码参数穷举 | 样本 → 参数组合 |
| `lzw_model_search.py` | LZW 精细模型搜索（目标是 24 个 XML 全解出）| 样本 → 参数组合 |
| `lzw_bruteforce.py` | LZW 剩余差异暴力搜索（以「XML 可解析」为判据）| 样本 → 参数组合 |
| `dl.py` | 多线程断点续传下载器（拉取外部依赖时用）| url → 本地文件 |

## 关键事实（已验证）
- ARCH000 索引：`0x08` 的 u32 = 索引偏移（同时是 mode0x02 的 ISAAC 密钥 seed）；`0x0C` u16 条目数；末尾 `count*20` 索引。条目 20 字节 LE：`hash_lo | special | offset | size | crc`。
- **`size` = 解压后长度**；压缩长度 = 下一条目 offset 之差。
- mode 0x00 = ASSET_SEED XOR；mode 0x01 = 变宽 LZW（`FUN_009ae880`）；mode 0x02 = MiniZ 多块流式 raw-deflate（`FUN_0099c270`）。
- mode 0x02 **XOR 子模式**（首块 `flag==0 && len==0x400`）走自定义 ISAAC 流密码，覆盖美术/音频原版资源——**按用户要求不做**（见 `SCOPE.md`）。

## 复现示例
```
python isaac_mode02_stream.py <archive.a> <out_dir>
```
