# 提取数据表 → 我们项目系统的映射（DATA-MAP）

> 说明：PixelAbyss 是**自建**的俯视角肉鸽，运行时**不直接读取** Isaac 的 XML。
> Isaac 数据表的作用是「设计参考源」——用真实规模/结构校准我们自己的系统
> （道具池数量、品质分层、楼层数、实体类型等），而非搬运内容。
> 原始需求「参考 Isaac 源码把项目改为俯视」即指此。

源目录：`isaac_reverse/extracted2/resources-dlc3/`

| Isaac 数据表 | 规模（实测） | 我们项目对应系统 | 用途性质 |
|---|---|---|---|
| `itempools.xml` | **31 池 / 2058 条** | `Run.cs` 道具投放 / 强化池 | 设计参考：池种类与条数规模 |
| `items_metadata.xml` | **721 件，quality 0–4 五级**（q0:51/q1:197/q2:249/q3:184/q4:40） | 道具品质分层 | 设计参考：品质分布比例 |
| `items.xml` | 958 件（passive425/familiar126/active170/trinket188/null49） | 道具分类框架 | 设计参考：道具大类划分 |
| `entities2.xml` | 1337 实体 / 197 Boss | `Enemy.cs` / `Boss.cs` 敌人原型 | 设计参考：敌人/Boss 类型数 |
| `stages.xml` | **30 楼层**（含 DLC Downpour/Mines/Mausoleum 等） | `Run.cs` 楼层脊柱 / `TerrainGen.cs` | 设计参考：楼层结构与递进 |
| `bosspools.xml` | Boss 投放池 | `Boss.cs` Boss 选择 | 设计参考：Boss 分层 |
| `players.xml` | 多角色 | （不适用） | ⚠️ 伊布是原创宝可梦角色，**不取自 Isaac** |
| `pocketitems.xml` | 口袋道具 | 主动道具框架 | 设计参考 |

## 我们项目自建数据落点（不等同于 Isaac 表）

- 道具池与品质：在 `Defs.cs` / `Run.cs` 中以「 curated 子集」实现，规模对齐 Isaac 真实值（31 池 / 5 级品质）。
- 楼层脊柱：当前 `Validator` 验证的是 4 层链式（L1→L4 超梦）可玩脊柱，结构参考 `stages.xml` 的递进模式。
- 敌人原型：当前实现 3 原型（蠕虫巡逻 / 蝙蝠游荡俯冲 / 射手瞄准），类型数量参考 `entities2.xml` 总量。
- 形态系统：`Forms.cs` 伊布 9 态 + 卡拉卡拉 + 胖丁 = 11 形态（原创设计，仅方法论受 roguelike 启发）。

## 如何「继续用」这些数据

1. 要扩道具池/楼层/Boss 种类时，先回 `extracted2/resources-dlc3/` 对应表取真实规模与命名，再在我们 `Core/` 里加 curated 条目。
2. 要核对 Isaac 原版某机制时，用 `isaac_reverse/ghidra_out/` 查对应函数（先见 `handover/INDEX.md`）。
3. 命名还原对照：官方 `tools/ResourceExtractor/filelist.txt`（18328 路径）可作反查。
