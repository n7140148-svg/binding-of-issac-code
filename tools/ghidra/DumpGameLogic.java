// DumpGameLogic.java —— 跨全二进制，按【字符串交叉引用】发现"游戏逻辑"函数
// 用法（analyzeHeadless 会自动先 import + 全量 analyze，再跑此 postScript）:
//   analyzeHeadless <projDir> <projName> -import <isaac-ng.exe>
//        -postScript DumpGameLogic.java <outDir> [keywordsFile]
//
// 策略:
//   1) 全程序扫描已定义字符串，凡是内容命中"游戏逻辑关键词"的，取其代码交叉引用 -> 种子函数
//   2) 种子函数向外扩 1 层 callers + callees -> 候选集（真正的逻辑常在被调用方/调用方）
//   3) 对每个候选函数 dump: 汇编 + 反编译 C + pcode，并写 INDEX.csv
//
// 关键词只做"粗筛"，产出是第一茬候选，接手 AI 需二次精筛/重命名。

import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.listing.*;
import ghidra.program.model.address.Address;
import ghidra.program.model.data.DataType;
import ghidra.program.model.symbol.Reference;
import java.io.*;
import java.util.*;

public class DumpGameLogic extends GhidraScript {
    private DecompInterface decomp;
    private final Set<String> dumped = new HashSet<>();
    private final Map<String,String> matchInfo = new HashMap<>(); // key -> matched keywords / "expanded"

    // 游戏逻辑粗筛关键词（小写匹配）。覆盖：道具池/抽取、楼层/房间、实体/敌人AI、
    // 弹幕/伤害、拾取物、RNG/种子、动画、音效、Lua、mod 等。
    private static final String[] KEYWORDS = {
        "itempool","treasure","boss","stage","room","entity","rng","seed","tear","bomb",
        "teleport","curse","shop","devil","angel","secret","library","arcade","sacrifice",
        "ultra","charge","familiar","trinket","collectible","active","passive","heart",
        "coin","key","pickup","enemy","npc","projectile","damage","knockback","wave","spawn",
        "grid","door","animation","anm2","sound","sfx","music","lua","mod","chest","lock",
        "champion","variant","subtype","color","pedestal","map","minimap","save","runstate",
        "player","flag","achievement","challenge","daily","greed","bossrush","library","void",
        "downpour","mines","maw","gehenna","depth","albumen","delirium","mother","father",
        "isaac","magdalene","cain","judas","blue baby","eve","samson","azazel","lazarus",
        "eden","the lost","lilith","keeper","apollyon","the forgotten","bethany","jacob",
        "troll","bomb bag","compass","map piece","dingle","guppy","bee","fly","spider",
        "boil","sack","globin","host","clotty","grunt","horf","leaper","pooter","psy","tumor",
        "sprite","frame","easing","lerp","vec","vector","transform","rotate","collide","aabb"
    };

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        String outDir = args.length > 0 ? args[0] : "C:/tmp/ghidra_gl";
        new File(outDir).mkdirs();
        File glDir = new File(outDir, "gamelogic");
        glDir.mkdirs();

        decomp = new DecompInterface();
        decomp.openProgram(currentProgram);

        Set<Function> seeds = new HashSet<>();
        StringBuilder seedLog = new StringBuilder();

        // Pass 1: 字符串 -> 种子函数
        Listing listing = currentProgram.getListing();
        DataIterator dit = listing.getDefinedData(true);
        int strScanned = 0;
        while (dit.hasNext()) {
            Data d = dit.next();
            DataType dt = d.getDataType();
            if (dt == null) continue;
            String dtName = dt.getName().toLowerCase();
            if (!dtName.contains("string")) continue;
            strScanned++;
            String content = d.getDefaultValueRepresentation();
            if (content == null) continue;
            String low = content.toLowerCase();
            // 去掉包裹引号
            String core = low.replaceAll("^\"|\"$", "");
            List<String> hits = new ArrayList<>();
            for (String kw : KEYWORDS) {
                if (core.contains(kw)) { hits.add(kw); }
            }
            if (hits.isEmpty()) continue;
            Reference[] refs = currentProgram.getReferenceManager().getReferencesTo(d.getAddress());
            for (Reference r : refs) {
                Address from = r.getFromAddress();
                Function f = getFunctionContaining(from);
                if (f != null) {
                    seeds.add(f);
                    String k = f.getName() + "@" + f.getEntryPoint();
                    matchInfo.putIfAbsent(k, "seed:" + String.join(",", hits));
                }
            }
        }
        println("=== scanned " + strScanned + " strings, found " + seeds.size() + " seed functions ===");
        seedLog.append("seed_count=").append(seeds.size()).append("\n");

        // Pass 2: 扩 1 层 callers + callees
        Set<Function> candidates = new HashSet<>(seeds);
        for (Function f : new ArrayList<>(seeds)) {
            try {
                for (Function g : f.getCalledFunctions(monitor)) {
                    candidates.add(g);
                    String k = g.getName() + "@" + g.getEntryPoint();
                    matchInfo.putIfAbsent(k, "expanded_callee");
                }
            } catch (Exception e) {}
            try {
                for (Function g : f.getCallingFunctions(monitor)) {
                    candidates.add(g);
                    String k = g.getName() + "@" + g.getEntryPoint();
                    matchInfo.putIfAbsent(k, "expanded_caller");
                }
            } catch (Exception e) {}
        }
        println("=== total candidate functions: " + candidates.size() + " ===");

        // Dump 全部候选
        int n = 0;
        try (PrintWriter csv = new PrintWriter(new OutputStreamWriter(
                new FileOutputStream(new File(outDir, "gamelogic_INDEX.csv")), "UTF-8"))) {
            csv.write("addr,name,size,tag,matched\n");
            List<Function> sorted = new ArrayList<>(candidates);
            sorted.sort(Comparator.comparingLong(f -> f.getEntryPoint().getOffset()));
            for (Function f : sorted) {
                long v = f.getEntryPoint().getOffset();
                String key = f.getName() + "@" + f.getEntryPoint();
                long sz = f.getBody() != null ? f.getBody().getNumAddresses() : 0;
                String tag = matchInfo.getOrDefault(key, "?");
                String matched = tag.startsWith("seed:") ? tag.substring(5) : "";
                csv.write(String.format("0x%08x,%s,%d,%s,%s\n", v, f.getName(), sz, tag, matched));
                dump(f, glDir);
                n++;
            }
        }
        println("=== DUMPED " + n + " game-logic candidate functions ===");
        println("=== DONE ===");
    }

    private void dump(Function f, File outDir) {
        if (f == null) return;
        String key = f.getName() + "@" + f.getEntryPoint();
        if (!dumped.add(key)) return;
        try {
            File out = new File(outDir, f.getName() + "__" + f.getEntryPoint() + "__gamelogic.txt");
            try (PrintWriter pw = new PrintWriter(new OutputStreamWriter(
                    new FileOutputStream(out), "UTF-8"))) {
                pw.write("========== FUNCTION " + key + " ==========\n\n");
                pw.write("---- ASSEMBLY ----\n");
                InstructionIterator ii = currentProgram.getListing().getInstructions(f.getBody(), true);
                while (ii.hasNext()) {
                    Instruction ins = ii.next();
                    pw.write(ins.getAddress() + "  " + ins.toString() + "\n");
                }
                pw.write("\n---- DECOMPILED C ----\n");
                DecompileResults res = decomp.decompileFunction(f, 180, monitor);
                if (res != null && res.decompileCompleted()) {
                    pw.write(res.getDecompiledFunction().getC());
                } else {
                    pw.write("// decompile failed\n");
                }
                pw.write("\n---- PCODE (high-level ops) ----\n");
                try {
                    HighFunction hf = res.getHighFunction();
                    if (hf != null) {
                        Iterator<PcodeOpAST> ops = hf.getPcodeOps();
                        while (ops.hasNext()) {
                            PcodeOpAST op = ops.next();
                            if (op.getOpcode() == PcodeOp.UNIMPLEMENTED) continue;
                            pw.write(op.toString() + "\n");
                        }
                    }
                } catch (Exception e) {
                    pw.write("// pcode dump failed: " + e + "\n");
                }
            }
            println("DUMPED " + key);
        } catch (Exception e) {
            println("ERR " + key + ": " + e);
        }
    }
}
