# 环境事实（实测，2026-10-26）

| 资产 | 路径 |
|---|---|
| 游戏本体 | `F:\庞渃瀿\The.Binding.of.Isaac\isaac-ng.exe`（8.5MB PE32）|
| 二进制快照 | `handover/binary/isaac-ng.exe`（同包可离线使用）|
| Ghidra | `E:\Tools\ghidra\ghidra_12.1.4_PUBLIC\`（`analyzeHeadless` 在 `support/`）|
| JDK | `F:\zulu21.42.19-ca-jdk21.0.7-win_x64`（Zulu JDK 21，Ghidra 12.1.4 要求 21）|
| 既有 Ghidra 项目（资源子系统）| `isaac_reverse/ghidra_proj/isaacng` |
| 全量分析项目（本包新跑）| `F:\ghidra_work\isaacng_game`（**放 F: 盘**）|
| 反编译 dump（资源）| `isaac_reverse/ghidra_out/` |
| 游戏逻辑 dump（本包新跑）| `handover/gamelogic_out/`（后台产出）|
| 提取数据表 | `isaac_reverse/extracted2/resources-dlc3/` |
| 报告 | `isaac_reverse/notes/` |

## 跑 Ghidra 前必做
C: 盘仅剩 ~2.3GB，**不足以放下全量分析的程序库**，必须把项目库 + packed-db 缓存迁到 F:：
```
export JAVA_HOME="/f/zulu21.42.19-ca-jdk21.0.7-win_x64"
export PATH="$JAVA_HOME/bin:$PATH"
export _JAVA_OPTIONS="-Dghidra.framework.db.packed.cache.dir=F:/ghidra_work/cache"
java -version   # 应显示 Zulu 21
```
`analyzeHeadless` 的项目目录也请用 F: 路径（如 `F:/ghidra_work/isaacng_game`），否则导入阶段会因 C: 空间不足失败（报错 `磁盘空间不足`）。

## 已确认的关键地址段
- 资源/归档/加解密子系统：`0x00990000`–`0x009D0000`（已完整反编译，1205 函数）
- 游戏逻辑（道具抽取 / 楼层房间生成 / 敌人 AI / 战斗 / RNG）：位于其他地址段；本包用 `DumpGameLogic.java` 按字符串跨全二进制自动发现，不依赖固定地址段。
