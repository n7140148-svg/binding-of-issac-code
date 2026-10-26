# Ghidra 反编译脚本（`handover/tools/ghidra/`）

## DumpCore.java（资源子系统，已完成）
扫描 `0x00990000`–`0x009D0000` 全部函数，dump **汇编 + 反编译 C + pcode**；并以 9 个种子函数为中心导出 callee/caller。
产出：`isaac_reverse/ghidra_out/FUN_*.txt`（1205 个，1134 含 C）。

运行（需先 import + 全量 analyze）：
```
analyzeHeadless <projDir> <projName> -import <isaac-ng.exe> \
  -scriptPath <dir> -postScript DumpCore.java <outDir>
```

## DumpGameLogic.java（游戏逻辑，本交接包目标）
跨全二进制，按**字符串交叉引用**发现游戏逻辑函数：
1. 扫描所有已定义字符串，命中关键词（itempool / tear / room / entity / rng …）的，取其代码 XREF → 种子函数；
2. 种子函数向外扩 1 层 callers + callees → 候选集；
3. 每个候选 dump 汇编 + C + pcode，并写 `gamelogic_INDEX.csv`。

⚠️ 这是**粗筛**，命中常有噪声（通用字符串工具/日志），需接手 AI 二次精筛、重命名、按系统设计映射。

运行（注意：项目库 + 缓存必须放 F:，C: 盘空间不足，见 `ENV.md`）：
```
export JAVA_HOME="/f/zulu21.42.19-ca-jdk21.0.7-win_x64"
export PATH="$JAVA_HOME/bin:$PATH"
export _JAVA_OPTIONS="-Dghidra.framework.db.packed.cache.dir=F:/ghidra_work/cache"
analyzeHeadless F:/ghidra_work/isaacng_game isaacng_game \
  -import "/f/庞渃瀿/The.Binding.of.Isaac/isaac-ng.exe" \
  -scriptPath isaac_reverse/ghidra_scripts \
  -postScript DumpGameLogic.java <outDir> \
  -analysisTimeout 1200
```
产出（本包已为其预留 `handover/gamelogic_out/`）：
- `gamelogic/*.txt` —— 每个候选函数的 汇编 + 反编译 C + pcode
- `gamelogic_INDEX.csv` —— `addr,name,size,tag,matched`

## 环境
- Ghidra 12.1.4：`E:\Tools\ghidra\ghidra_12.1.4_PUBLIC\`
- JDK 21：`F:\zulu21.42.19-ca-jdk21.0.7-win_x64`（运行前 set `JAVA_HOME` + `PATH`）
