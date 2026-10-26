# 当前逆向成果（截至 2026-10-26 23:06）

## 进度总览（逆向打包任务）

| # | 子任务 | 状态 | 实测数据 / 说明 |
|---|---|---|---|
| 1 | 二进制快照 `binary/isaac-ng.exe` | ✅ 完成 | 8.5MB，路径 `F:\庞渃瀿\The.Binding.of.Isaac\isaac-ng.exe` |
| 2 | 提取器全集 `tools/extractors/` | ✅ 完成 | 15 个 .py（ARCH000 三编码解码器 + 清单）|
| 3 | Ghidra 脚本 `tools/ghidra/` | ✅ 完成 | `DumpCore.java`（资源子系统）+ `DumpGameLogic.java`（跨全二进制按字符串挖掘，本轮已修编译错）|
| 4 | 报告 `reports/` | ✅ 完成 | `ISAAC_REVERSE_REPORT.md` + `TOPDOWN_PLAN_EVIDENCE.md`（最终版）|
| 5 | 资源子系统索引 `INDEX.md/json` | ✅ 完成 | 1205 函数（1134 含反编译 C）|
| 6 | 种子函数证据 `KEY-FUNCTIONS.md` | ✅ 完成 | 9 个破解归档格式的直接证据 |
| 7 | 数据表→项目映射 `DATA-MAP.md` | ✅ 完成 | 真实计数，已对接上游俯视化改造 |
| 8 | 接手文档（README / AI_HANDOVER / SCOPE / ENV / STATUS）| ✅ 完成 | 给接手 AI 的开箱指南 |
| 9 | **游戏逻辑第一茬 dump `gamelogic_out/`** | ✅ **本轮完成** | 扫描 14242 字符串 → 1488 种子 → 扩展 6623 候选 → **实 dump 1282 个函数（322MB）** |
| 10 | git 提交（scoped add）| ⏳ 待用户拍板 | 13 个 .cs 俯视化改动 + 本包，禁止 `git add .` |
| 11 | 游戏逻辑精筛 / 重命名 / 按系统映射 | ⏳ 接手 AI 的活 | 见 `AI_HANDOVER.md`，本包只给"第一茬素材" |

> 标注说明：`✅ 完成`= 本环境已落地、可复核；`⏳ 待拍板/接手 AI`= 本环境不做，按用户授权移交。

---

## 一、数据提取（已落地，上游项目直接参考）
从 DLC3（悔改）资源包提取的机制数据表（真实计数，非估算）：

| 数据表 | 规模 | 用途 |
|---|---|---|
| `itempools.xml` | **31 池 / 2058 条** | 道具池（treasure 407 / greedTreasure 348 / boss 59 / devil 94 / angel 66 …）|
| `items_metadata.xml` | **721 件**，quality 0–4 五级 | 51 / 197 / 249 / 184 / 40 |
| `items.xml` | **958 件** | passive 425 / familiar 126 / active 170 / trinket 188 / null 49 |
| `entities2.xml` | **1337 实体 / 197 Boss** | 敌人/实体定义 |
| `stages.xml` | **30 楼层** | 楼层定义 |
| `bosspools.xml` 等 | 其余表若干 | Boss 池等 |

总计 **6422 文件**（含 2401 个 xml / anm2）。

## 二、反编译
- **资源/归档子系统**：1205 函数（1134 含反编译 C），见 `handover/INDEX.md` / `INDEX.json`。
- **种子函数 9 个**（破解归档格式的直接证据）：见 `handover/KEY-FUNCTIONS.md`
  - `FUN_0099bfa0` / `FUN_0099c170`（状态初始化 + 种子）
  - `FUN_0099c270`（mode 0x02 读块）/ `FUN_0099c690`（mode 0x01 读块）
  - `FUN_009c2f10`（ISAAC 密钥流）/ `FUN_009c30b0`（ISAAC 初始化）/ `FUN_009c2fd0`（推进）
  - `FUN_009b06f0`（XOR 应用）/ `FUN_009ae880`（LZW 核心）
- **游戏逻辑第一茬 dump（本轮完成）**：`handover/gamelogic_out/`
  - 方法：`DumpGameLogic.java` 全二进制扫描字符串 → 取交叉引用种子函数 → 扩 1 层 caller/callee → 逐函数 dump 汇编+反编译C+pcode。
  - 规模：**1282 个候选函数成功落盘**（gamelogic/ 目录，322MB），INDEX.csv 1450 行（含少量 decompile 失败未落盘者）。
  - 种子 tags 分布（命中数）：player 63 / rng 30 / sound 28 / charge 16 / animation 14 / rotate 9 / lerp 9 / spawn 6 / entity 6 / bomb 6 / pickup 5 / boss 5 / teleport 4 / heart 4 / collectible 4 / anm2 4 / fly 3 / vec 2 / map 2 / enemy 2 …（其余 1 个的略）。
  - 最大几个函数（反编译体量）：`FUN_005b79c0`(rotate, 12.8MB) / `FUN_004ad2f0`(spawn, 10MB) / `FUN_0058cea0`(lerp, 9MB) / `FUN_0057f5f0`(sound, 5.8MB) / `FUN_00465940`(boss, 5.3MB)。
  - **性质**：粗筛候选，命名仍是 Ghidra 默认 `FUN_xxxx`，需接手 AI 二次精筛、按系统（道具抽取 / 楼层房间生成 / 敌人AI / 战斗 / RNG）归类重命名。

## 三、验证（可复核）
- 提取器产出与官方 filelist 命名一致；XML 可解析。
- mode 0x02 共享 `zlib.decompressobj(-15)` 流输出字节数 = 索引 `size` **精确匹配**（如 123288/123288）。
- LZW 精确移植 `FUN_009ae880`：config.a 24/24 解出（19/24 为 XML）。
- Ghidra 全量分析成功：isaac-ng.exe 已导入并分析到 `F:/ghidra_work/isaacng_game/isaacng_game.rep`，接手 AI 可直接打开复用，免重新分析。
- 俯视化改造（独立工作流）已通过 `Validator 29/0` + `QAProbeStage2 26/0` 验证（与本逆向包无关，仅说明上游在动）。

## 四、已知缺口（移交接手 AI）
- **游戏逻辑精筛/命名/按系统映射**：本包只给"第一茬素材"（1282 函数 + INDEX），接手 AI 据此深挖道具抽取 / 楼层房间生成 / 敌人 AI / 战斗逻辑，见 `AI_HANDOVER.md`。
- mode 0x02 XOR/ISAAC 美术子流（约 2649 个 PNG/WAV/BIN）：**用户明确不做**（见 `SCOPE.md`），提取器 XOR 判定逻辑在、密钥流不实现。
- 本包未做 git 提交（见进度总览 #10，待用户拍板）。
