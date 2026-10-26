# 重点逆向函数（已分析并用于破解归档格式）

这些函数是破解 ARCH000 三编码的直接证据来源。

| 地址 | 子系统 | 文件 | 反编译C |
|---|---|---|---|
| 0x00963db0 | archive-aux | `FUN_00963db0__00963db0__callee.txt` | ✅ |
| 0x0099bfa0 | archive-loader | `FUN_0099bfa0__0099bfa0__caller.txt` | — |
| 0x0099bfa0 | archive-loader | `FUN_0099bfa0__0099bfa0__seed.txt` | ✅ |
| 0x0099c170 | archive-init | `FUN_0099c170__0099c170__callee.txt` | ✅ |
| 0x0099c270 | mode0x02-readblock | `FUN_0099c270__0099c270__callee.txt` | — |
| 0x0099c270 | mode0x02-readblock | `FUN_0099c270__0099c270__seed.txt` | ✅ |
| 0x0099c690 | archive-io | `FUN_0099c690__0099c690__caller.txt` | ✅ |
| 0x009c2f10 | isaac-keygen | `FUN_009c2f10__009c2f10__callee.txt` | ✅ |
| 0x009c30b0 | isaac-randinit | `FUN_009c30b0__009c30b0__callee.txt` | ✅ |
| 0x009c30b0 | isaac-randinit | `FUN_009c30b0__009c30b0__caller.txt` | — |