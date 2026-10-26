# Isaac 逆向阶段性成果 · 交接包（Handover Package）

> 打包日期：2026-10-26
> 目标（用户口授）：**逆向到「能用于我们项目」的程度，音频与贴图不需要**。
> 本包用途：**交给另一个 AI 直接接着干，继续把游戏逻辑代码（道具抽取 / 楼层房间生成 / 敌人 AI / 战斗 / RNG）逆出来**。
> 上游项目：PixelAbyss（俯视角肉鸽，参考 Isaac 数据做自己的系统，不拷 Isaac 代码）。

---

## 0. 这份包里有什么（目录地图）

| 内容 | 位置 | 说明 |
|---|---|---|
| **顶层接手指南** | `handover/AI_HANDOVER.md` | ⭐ 下一个 AI 必读：如何接着挖游戏逻辑 |
| **范围界定** | `handover/SCOPE.md` | 什么做 / 什么不做 / 项目边界 |
| **环境事实** | `handover/ENV.md` | Ghidra / JDK / 二进制 / 项目路径 |
| **当前成果状态** | `handover/STATUS.md` | 已提取数据 + 反编译进度 |
| **资源子系统索引** | `handover/INDEX.md` / `INDEX.json` | 1205 函数，1134 含反编译 C |
| **种子函数清单** | `handover/KEY-FUNCTIONS.md` | 破解归档格式直接依赖的 9 个函数 |
| **数据表→系统映射** | `handover/DATA-MAP.md` | Isaac 数据表 → 上游系统 |
| **游戏逻辑第一茬** | `handover/gamelogic_out/` | DumpGameLogic 后台 dump（待精筛） |
| **游戏二进制** | `handover/binary/isaac-ng.exe` | 8.5MB PE32 快照，可离线用 |
| **提取器** | `handover/tools/extractors/` | 15 个 .py，ARCH000 三编码解码 + 索引 |
| **Ghidra 脚本** | `handover/tools/ghidra/` | `DumpCore.java`（资源）/ `DumpGameLogic.java`（游戏逻辑） |
| **逆向报告** | `handover/reports/` | `ISAAC_REVERSE_REPORT.md`、`TOPDOWN_PLAN_EVIDENCE.md` |

---

## 1. 一句话结论
- **资源/归档子系统（加载贴图音频的机制）已 100% 逆完**：三编码全破、6422 文件提取、1205 函数反编译并索引。
- **游戏逻辑（玩法系统本身）是本次交接要补的口子**：已给出现成发现脚本 `DumpGameLogic.java` 与第一茬候选 dump，下一个 AI 据此精筛、命名、按系统设计映射即可。

## 2. 怎么用
另一个 AI 从 `AI_HANDOVER.md` 第 1 步开始即可。环境准备、复现命令、定位具体系统的方法、精筛与交付标准都在里面。

## 3. 红线（别碰）
- mode 0x02 的 XOR/ISAAC 美术子流（音频/贴图）——用户明确不要。
- 不要把 Isaac 代码直接拷进上游游戏（见 `SCOPE.md`）。
- 每个结论附 Ghidra 函数地址 + 反编译片段，绝不臆造。

---

## 4. 本机发布到 GitHub（已打包为本地 git 仓库）

本目录 `handover/` 已被初始化为独立 git 仓库，全部成果（含 322MB 游戏逻辑 dump）已 `commit`。
你只需要在**自己本机**（已装 `gh` 并 `gh auth login`，或已配 SSH/GitHub Desktop）执行下面几步即可上 GitHub：

```bash
# 1) 在 GitHub 建空仓库（公开/私有自选）
gh repo create isaac-reverse-handover --private     # 改成 --public 即公开

# 2) 关联远程并推送（把 <你的用户名> 换成实际账号）
git remote add origin https://github.com/<你的用户名>/isaac-reverse-handover.git
git branch -M main
git push -u origin main
```

> 若用 SSH：`git remote add origin git@github.com:<你的用户名>/isaac-reverse-handover.git`
> 若不用 gh：先在 GitHub 网页建空仓库，拿到 URL 再执行第 2 步。
> 仓库约 331MB（含 `gamelogic_out/` 的 1282 个反编译函数），首次 clone 较慢属正常。
