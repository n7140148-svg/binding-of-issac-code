# 范围界定（用户 2026-10-26 口授）

## ✅ 已完成
1. ARCH000 三编码全部破解：
   - mode 0x00 —— ASSET_SEED XOR（graphics / music / sfx / videos）
   - mode 0x01 —— 变宽 LZW（精确移植 `FUN_009ae880`）
   - mode 0x02 —— MiniZ 多块流式 raw-deflate（精确移植 `FUN_0099c270`）
2. **6422 个文件提取**（含 2401 个 xml / anm2 机制数据表）
3. 资源/归档/加解密子系统 **1205 函数反编译 + 可导航索引**（`handover/INDEX.md/json` + `KEY-FUNCTIONS.md`）
4. 机制数据表映射到上游项目系统（`handover/DATA-MAP.md`）

## ❌ 明确不做（用户要求）
- mode 0x02 的 **XOR / ISAAC 美术资源子流**（repentance.a 约 2649 个 PNG/WAV/BIN 原版美术/音频）。
  - 提取器里 XOR 判定逻辑（`flag==0 && len==0x400`）在，但 ISAAC 密钥流（`FUN_009c2f10`/`FUN_009c30b0`/`FUN_009c2fd0`/`FUN_009b06f0`）未实现。
  - 原因：上游项目用占位图形，不需要原版贴图音频。
  - 如需补，证据链完整：见 `KEY-FUNCTIONS.md` 与 `ISAAC_REVERSE_REPORT.md` §3。

## ⏳ 本交接包的目标（待下一个 AI 推进）
- 游戏逻辑代码：道具池抽取、楼层/房间生成、敌人 AI/行为、弹幕/伤害/战斗、RNG/种子。
- 现状：第一茬候选函数由 `DumpGameLogic.java` 后台 dump（`handover/gamelogic_out/`），需二次精筛、重命名、按系统设计映射。

## 🚫 上游项目边界（重要，避免误解）
- 我们**自建**俯视肉鸽系统，**仅参考** Isaac 数据内容作为设计源；**不把 Isaac 代码拷进游戏**。
- 逆向产物是「设计参考 + 算法对照」，不是可链接的源码。
