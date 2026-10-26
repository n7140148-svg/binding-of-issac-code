// DumpCore.java —— 导出指定地址的【汇编 + P-code】，用于精确还原算法
// 用法: analyzeHeadless <proj> <name> -process isaac-ng.exe -noanalysis \
//        -scriptPath <dir> -postScript DumpCore.java <outdir>

import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.address.Address;
import ghidra.program.model.pcode.*;
import java.io.*;
import java.util.*;

public class DumpCore extends GhidraScript {
    private DecompInterface decomp;
    private final Set<String> dumped = new HashSet<>();

    private static final long[] SEEDS = {
        0x0099bfa0L, 0x0099c170L, 0x0099c270L, 0x0099c690L,
        0x009c2f10L, 0x009c30b0L, 0x00963db0L, 0x0099c490L, 0x0099c590L
    };

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        String outDir = args.length > 0 ? args[0] : "C:/tmp/ghidra_out";
        new File(outDir).mkdirs();

        decomp = new DecompInterface();
        decomp.openProgram(currentProgram);

        for (long a : SEEDS) {
            Address addr = toAddr(a);
            Function f = getFunctionAt(addr);
            if (f == null) f = getFunctionContaining(addr);
            if (f == null) { println("NO FUNC at " + addr); continue; }
            println("SEED -> " + f.getName() + " @ " + f.getEntryPoint());
            dump(f, outDir, "seed");
            for (Function g : f.getCalledFunctions(monitor)) dump(g, outDir, "callee");
            for (Function g : f.getCallingFunctions(monitor)) dump(g, outDir, "caller");
        }

        // 全函数表扫描：0x00990000 - 0x009d0000
        FunctionIterator fit = currentProgram.getFunctionManager().getFunctions(true);
        int n = 0;
        while (fit.hasNext()) {
            Function f = fit.next();
            long v = f.getEntryPoint().getOffset();
            if (v >= 0x00990000L && v <= 0x009D0000L) {
                dump(f, outDir, "scan");
                n++;
            }
        }
        println("=== scanned " + n + " functions in 0x990000-0x9d0000");
        println("=== DONE");
    }

    private void dump(Function f, String outDir, String tag) {
        if (f == null) return;
        String key = f.getName() + "@" + f.getEntryPoint();
        if (!dumped.add(key)) return;
        try {
            File out = new File(outDir, f.getName() + "__" + f.getEntryPoint() + "__" + tag + ".txt");
            try (PrintWriter pw = new PrintWriter(new OutputStreamWriter(
                    new FileOutputStream(out), "UTF-8"))) {
                pw.write("========== FUNCTION " + key + "  tag=" + tag + " ==========\n\n");
                pw.write("---- ASSEMBLY ----\n");
                InstructionIterator ii = currentProgram.getListing().getInstructions(
                        f.getBody(), true);
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
            println("DUMPED " + key + " tag=" + tag);
        } catch (Exception e) {
            println("ERR " + key + ": " + e);
        }
    }
}
