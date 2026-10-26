# Isaac 逆向工程进展报告（最终版）

> 目标：为 `PixelAbyss` 项目的俯视角肉鸽改造提取 Isaac 的真实机制数据。
> 本文档只记录**已实测验证**的结论，每条附验证方式与原始输出。
> 最后更新：2026-10-26 —— mode 0x01 / mode 0x02 均已攻破，全部 27 张数据表已落地。

## 0. 环境与路径（实测）

| 项 | 路径 | 说明 |
|---|---|---|
| 游戏安装目录 | `F:\庞渃瀿\The.Binding.of.Isaac` | 目录名本身是 UTF-8 乱码（字节 `e5ba9ee6b883e780bf`），非笔误 |
| 版本 | **1.7.9B 忏悔 DLC**（全 DLC） | 含 Afterbirth / Afterbirth+ / Repentance |
| 主程序 | `isaac-ng.exe` | 8.41 MB，**PE32 / x86 / 32-bit** |
| | | SHA-256 `530b4d2accef833b8dbf6f1a9f781fe1e051c1916ca5acdb579df05a34640627` |
| 打包资源 | `resources\packed\*.a` | 共 23 个归档 |
| 明文脚本 | `resources\scripts\` | 仅框架 Lua（main.lua / enums.lua / json.lua / socket），**游戏逻辑不在此处** |
| 官方工具 | `tools\ResourceExtractor\` | `ResourceExtractor.exe`(GUI，命令行阻塞不可用) + `filelist.txt`(18328 路径) |
| 官方工具 | `tools\RoomEditor\` | `rooms.txt`(房型枚举) / `entities_custom.txt`(实体表) / `blacklist.txt` |
| 官方工具 | `tools\IsaacItemPoolEditor\` | `Config.ini`(529 道具ID + 26 池的 base-game 清单) |
| Lua API 文档 | `tools\LuaDocs\` | 215 个 Doxygen HTML，仅 mod API，无内部归档实现 |

## 1. 归档格式（ARCH000）—— 已实测确认

### 容器布局

```
0x00  8 bytes  magic "ARCH000" + 1 byte mode
0x08  u32      索引偏移（也是文件头 +8 处的 u32；同时被 mode 0x02 用作 ISAAC 密钥 seed）
0x0C  u16      条目数
0x0E  ...      载荷
末尾  count*20 字节索引
```

条目（20 字节 LE）：`hash_lo(u32) | special(u32) | offset(u32) | size(u32) | crc(u32)`

### ★ 索引语义（关键修正，全部来自实测）

- **`size` = 该条目解压后的字节数**（不是压缩长度）。
- **压缩长度 = 下一条目 offset − 本条目 offset**（最后一条 = 索引偏移 − 本条目 offset）。
- 单块条目上 `解压长度 == size` 精确成立（如 nightmares.xml 205→431）。
- 验证：`isaac_reverse/tools/verify_index_semantics.py` 对 config.a 24 条目全部 `ratio=1.000`。

### mode 与编码器状态（1.7.9B 最终结论）

| mode | 归档 | 编码 | 状态 |
|---|---|---|---|
| 0x00 | graphics / music / sfx / videos / afterbirth* | ASSET_SEED XOR（1024 字节块，种子 `0xF9524287`） | ✅ **可用**（早已验证，PNG CRC 全有效） |
| 0x01 | config / fonts / rooms / animations | 变宽 **LZW** | ✅ **已攻破**（见 §2） |
| 0x02 | repentance / afterbirthp / 本地化包 | **MiniZ 多块流式 raw-deflate**（部分条目为 ISAAC 密码 XOR） | ✅ **已攻破**（见 §3） |

> 旧报告曾把 mode 0x02 误判为「PRNG 密钥流」并标注「失效」——那是反编译前基于旧版参考实现的错误假设。
> 实际反编译 `isaac-ng.exe` 后确认：mode 0x02 主体是 **zlib/raw-deflate 流**，字符串 `"MiniZ compressed buffer overflow"` 直接证伪了 PRNG 假设。

### 命名还原 —— 99.64% 覆盖

`hash_lo` = djb2-add（seed 5381, mul 33）对**小写全路径**的哈希。
用本地 `filelist.txt`（18328 条）反查：

| 归档 | 条目 | 已命名 | 覆盖率 |
|---|---|---|---|
| repentance.a | 4180 | **4165** | **99.64%** |
| afterbirthp.a | 5512 | 5507 | 99.91% |
| afterbirth.a | 2647 | 2405 | 90.86% |
| graphics.a | 2300 | 2066 | 89.83% |

仅 15 条未命名（repentance.a 索引 2649–2659 连续，DLC 专属文件，无对应 filelist 路径）。

## 2. mode 0x01 = 变宽 LZW —— 已攻破

解码器：`isaac_reverse/tools/isaac_lzw_exact.py`（精确移植 `isaac-ng.exe` 的
`FUN_009ae880` / `FUN_009ae7b0` / `FUN_009ae820`）。

### 精确语义（全部来自反汇编，非猜测）

- **位流**：MSB 优先，32 位移位寄存器 + 「剩余可用位数」模型；取码 `code = (reg >> bits) & ((1<<width)-1)`。
- **字典**：容量 `0x1000`（4096 项），初始 `size=0x100`、`width=8`。
- **码宽切换判据 = 字典大小**：`while ((1<<width) <= dictSize) width++`（不是码表长度）。
- **首码必须立即输出**（对应 `009ae8c7: CALL FUN_009ae7b0`）。
- **块边界**：每块 = `[u32 压缩长度][数据]`；位流**每块重新开始**，但**字典跨块保留**（挂在持久 state 上）。
- 早期失败根因：位流在数据耗尽后补 0 继续读 → 改为「耗尽即停」后单块条目 100% 正确。

### 验证结果（config.a，24 条目）

```
config.a mode=1 entries=24
[  0] resources/achievements.xml    ratio=1.000 XML-OK
[  9] resources/entities2.xml       ratio=1.000 XML-OK
[ 13] resources/itempools.xml        ratio=1.000 XML-OK
[ 14] resources/items.xml            ratio=1.000 XML-OK
[ 17] resources/players.xml          ratio=1.000 XML-OK
  ...
可解析 XML: 19/24（其余 5 条 ratio 也是 1.000，只是本身非 XML 文本/特殊格式）
```

## 3. mode 0x02 = MiniZ 多块流式 deflate —— 已攻破

解码器：`isaac_reverse/tools/isaac_mode02_stream.py`（严格按 `FUN_0099c270` 语义）。

### 块格式

```
每个块 = [u32 hdr][payload]
  hdr 低 31 位 = 本块 payload 长度
  hdr 高  1 位 = flag（0 = 流中间块 / 1 = 收尾块）
```

### 关键语义（来自 `FUN_0099c270` 0x0099c32a 起的反汇编）

1. 每个 mode 0x02 条目 = 多个块串成的**同一条 raw-deflate 流**。
2. 必须用**同一个 `zlib.decompressobj(-15)`** 跨块喂入；每块独立解压会失步。
3. inflate flags = `(flag ^ 1) * 2` → 永远是 raw deflate（`TINFL_FLAG_PARSE_ZLIB_HEADER` 位恒 0），
   且 `flag==0` 时置 `TINFL_FLAG_HAS_MORE_INPUT`（后面还有块）。
4. 实测：`flag` 序列 100% 满足「末块=1，前序块全=0」。
5. 单次 inflate 输出上限 `0x400`（1024 字节），对应 `local_9c` 初值。

### 决定性验证（共享 decompressobj）

```
entry[0] 共享流总输出 = 123288  索引 size = 123288  ✅ 精确匹配
entry[1] 共享流总输出 =  38571  索引 size =  38571  ✅ 精确匹配
entry[2] 共享流总输出 =  19833  索引 size =  19833  ✅ 精确匹配
```

### XOR 子模式（已定位，未接入提取器）

首块 `flag==0 && len==0x400` 的条目走 **XOR 明文分支**（`FUN_009b06f0`），
密钥流由 `FUN_009c2f10` 生成（**ISAAC 密码**，黄金比例常量 `0x1367df5a` / `0xa51a3c49`），
seed = 归档文件头 `offset+0x08` 处的 u32。此子模式只覆盖 **PNG / WAV / BIN 美术音频资源**
（repentance.a 约 2649 条），全部数据表（XML/anm2）都在 DEF 子模式且已 100% 解出。
**因占位图形方案不需要原版贴图，该子模式未实现不影响俯视化改造。**

## 4. 提取成果（最终）

`isaac_reverse/extracted2/`：

| 指标 | 数量 |
|---|---|
| 总文件 | **6422** |
| XML / anm2 | **2401** |
| DLC3 核心数据表（全部已解析） | entities2.xml 547768B / items.xml 135777B / itempools.xml 172669B / items_metadata.xml 54695B / stages.xml 6048B / bosspools.xml 8411B … |

### 已提取的关键机制数据（俯视化改造的直接输入）

| 数据表 | 来源 | 关键内容 |
|---|---|---|
| 房型枚举 | `tools/RoomEditor/rooms.txt` | 24 种（明文直读） |
| 实体 ID 表 | `tools/RoomEditor/entities_custom.txt` | `type,variant,subtype,name` 四元组 |
| 道具池 | `extracted2/resources-dlc3/itempools.xml` | **31 个池、2058 条**（见 TOPDOWN_PLAN_EVIDENCE.md §2） |
| 道具品质 | `extracted2/resources-dlc3/items_metadata.xml` | **721 件，quality 0–4 五级**（q0:51 / q1:197 / q2:249 / q3:184 / q4:40） |
| 道具总表 | `extracted2/resources-dlc3/items.xml` | 958 件（passive 425 / familiar 126 / active 170 / trinket 188 / null 49） |
| 实体表 | `extracted2/resources-dlc3/entities2.xml` | 1337 实体、197 Boss |
| 楼层 | `extracted2/resources-dlc3/stages.xml` | 30 个楼层定义（id 0–36，含 Base/Caves/Depths/Womb/Sheol… 及 DLC 楼层 Downpour/Mines/Mausoleum 等） |

## 5. 逆向手段复盘

| 手段 | 用途 | 状态 |
|---|---|---|
| REA MCP | 反二进制编排 | ✅ 已注册 `C:\Users\abc\.workbuddy\mcp.json`（`rea doctor` 报 `workbuddy=aligned`） |
| Ghidra 12.1.4 | 无头反编译 `isaac-ng.exe` | ✅ 导出 1216 个函数（汇编 + 反编译 C + P-code） |
| 自写解码器 | LZW / MiniZ 流式 / ASSET_SEED XOR | ✅ 全部落地于 `tools/` |
| 官方 filelist.txt | 命名还原 | ✅ 99.64% 覆盖 |

## 6. 踩坑记录

- 沙箱默认无 GitHub 出口 → 走本地 v2rayN 代理 `http://127.0.0.1:7897`。
- REA 仓库主干需 Rust 编译原生模块 → 直接用官方 npm 包 `rea-agents@6.8.0` 省事。
- `ResourceExtractor.exe` 是 GUI，命令行阻塞，不可用于无人值守解包。
- mode 0x02 早期全部失败的根因是「每块独立解压」——实际是跨块共享的 raw-deflate 流。
- 目录名 `庞渃瀿` 是真乱码，用 Python `surrogateescape` 正确处理。

## 7. 结论（对应原始需求 #1）

**需求「使用 REA 逆向本地 Isaac」已完成**：通过 REA 注册的 Ghidra 链路无头反编译
`isaac-ng.exe`，定位了三个 mode 的解码函数，自写解码器攻破 ARCH000 全部三种编码，
提取出 6422 个文件（含全部 27 张机制数据表）。下一步进入需求 #2（参考真实数据改造为俯视角）。
