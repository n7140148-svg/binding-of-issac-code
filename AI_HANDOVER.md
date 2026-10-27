# 给下一个 AI 的接手指南（游戏逻辑逆向）

> 2026-10-27 code delivery: start with [reference/README.md](reference/README.md)
> and [the delivery report](reports/FINAL_CODE_2026-10-27.md). The runnable code
> separates recovered algorithms from original gameplay policies. Compatibility
> gaps and concrete remaining targets are listed there; do not restart analysis.
>
> Earlier continuation: read [the report](reports/CONTINUATION_2026-10-27.md)
> and [gl_INDEX.md](gl_INDEX.md) first. The old dump is partial, its CSV is
> malformed, and logger 0x0095e330 has a wrong no-return annotation in the
> database. Fresh exports and temporary correction tools are included.
> Gameplay RNG is distinct from the archive generator referenced below.
> Continue from the report's next function addresses and preserve unknowns.

你是接手《以撒的结合：悔改》(Binding of Isaac: Repentance) 逆向的 AI。
本包已经把"资源/归档子系统"逆完，并准备好了"游戏逻辑发现脚本"。你的任务：

> **把游戏逻辑代码（道具池抽取 / 楼层房间生成 / 敌人 AI / 战斗 / RNG）逆出来，
> 整理成「Isaac 怎么做 X」的可读说明，供上游俯视肉鸽项目（PixelAbyss）参考。**

---

## 0. 先读这俩，别急着写代码
- `SCOPE.md` —— 范围、什么做/什么不做、项目边界（务必先看，避免越界）
- `DATA-MAP.md` —— Isaac 数据表 → 上游系统映射（你逆出的逻辑要给这些数据「供血」）

## 1. 环境准备（一次性）
Ghidra 12.1.4 需要 JDK 21，本机已具备：
```
export JAVA_HOME="/f/zulu21.42.19-ca-jdk21.0.7-win_x64"
export PATH="$JAVA_HOME/bin:$PATH"
java -version          # 期望 Zulu 21
"/e/Tools/ghidra/ghidra_12.1.4_PUBLIC/support/analyzeHeadless" --help   # 不应再报 java 缺失
```

## 2. 复现「资源子系统」反编译（可选，产物已在 `isaac_reverse/ghidra_out/`）
```
analyzeHeadless isaac_reverse/ghidra_proj/isaacng isaacng \
  -process isaac-ng.exe -scriptPath isaac_reverse/ghidra_scripts \
  -postScript DumpCore.java isaac_reverse/ghidra_out
```

## 3. 拿游戏逻辑第一茬（已为你跑过，在 `handover/gamelogic_out/`；重跑命令）
```
analyzeHeadless isaac_reverse/ghidra_proj_game isaacng_game \
  -import "/f/庞渃瀿/The.Binding.of.Isaac/isaac-ng.exe" \
  -scriptPath isaac_reverse/ghidra_scripts \
  -postScript DumpGameLogic.java isaac_reverse/handover/gamelogic_out \
  -analysisTimeout 1200
```
产出：
- `gamelogic_out/gamelogic/*.txt` —— 每个候选函数的 汇编 + 反编译 C + pcode
- `gamelogic_out/gamelogic_INDEX.csv` —— `addr,name,size,tag,matched`

`DumpGameLogic.java` 的逻辑：扫描全程序字符串 → 命中关键词（itempool/tear/room/entity/rng…）的取其代码 XREF 作种子 → 种子向外扩 1 层 callers+callees → dump 全部候选。**这是粗筛**，需你二次精筛。

## 4. 如何定位「具体某个系统」
Isaac 无符号，函数名都是 `FUN_xxxxxx`。靠**字符串交叉引用**定位（DumpGameLogic 已自动做了一层）：

| 想找的系统 | 搜这些字符串 / 关键词 |
|---|---|
| 道具池抽取 | "itempool"、"treasure"、"boss"、"devil"、"angel"、"shop"、"secret"、"library"；看谁读 `itempools.xml` |
| 楼层/房间生成 | "Stage"、"Room"、"grid"、"door"、"curse"、"minimap"、"map"；看谁读 `stages.xml` / rooms |
| 实体/敌人 AI | "Entity"、"NPC"、"variant"、"subtype"、"champion"、"state"、"wave"、"spawn" |
| 弹幕/伤害/战斗 | "TEAR"、"BOMB"、"projectile"、"damage"、"knockback"、"familiar"、"charge" |
| RNG/种子 | "Seed"、"RNG"、"random"、"rand"；对照 `tools/extractors/isaac_prng2.py` 的 `FUN_009c2f10` |
| 动画/音效 | "anm2"、"sfx"、"music"、"sound"、"frame"、"easing"、"lerp" |

Ghidra 内操作：`Search > For Strings` → 命中字符串 `References > Show References to Address` → 顺引用找函数 → `Function > Call Tree` 向外扩。

## 5. 精筛与整理（关键交付）
1. **去噪**：很多命中是通用字符串工具/日志，按函数体是否真操作 itempool/room/entity 判定。
2. **重命名**：`FUN_xxxxxx` → 语义名（如 `ItemPool_Roll`、`Stage_GenRoom`），记录进索引。
3. **按系统设计映射**：对照 `DATA-MAP.md` 的每个上游系统，写「Isaac 对应实现 = 哪个函数 + 核心算法」。
4. **产出可读说明**：每个系统一份 `how_isaac_does_X.md`，含反编译 C 关键片段 + 算法解读 + 对上游项目的可借鉴点。

## 6. 红线（别碰）
- mode 0x02 的 XOR/ISAAC 美术子流（音频/贴图）——用户明确不要。
- 不要把 Isaac 代码直接拷进上游游戏（见 `SCOPE.md` 边界）。
- 每个结论附 Ghidra 函数地址 + 反编译片段；无法确定的标「未确认」，不臆造。

## 7. 验收标准（判断你做完了）
- [ ] 道具池抽取主链路函数已定位 + 反编译 + 命名
- [ ] 楼层/房间生成主链路函数已定位 + 反编译 + 命名
- [ ] 敌人 AI / 战斗至少各 1 条主干已梳理
- [ ] RNG/种子机制对照 `isaac_prng2.py` 闭合
- [ ] 每个上游系统有一份 `how_isaac_does_X.md`
- [ ] 更新 `gamelogic_INDEX.csv` / 生成 `gl_INDEX.md` 并入本包
