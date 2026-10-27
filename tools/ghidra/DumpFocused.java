// Export selected functions without changing the analyzed program.
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.listing.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class DumpFocused extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) throw new IllegalArgumentException("Usage: DumpFocused.java <outDir> <entry> [entry...]");
        File output = new File(args[0]);
        if (!output.isDirectory() && !output.mkdirs()) throw new IOException("Cannot create " + output);
        DecompInterface decompiler = new DecompInterface();
        try {
            if (!decompiler.openProgram(currentProgram)) throw new IOException(decompiler.getLastMessage());
            for (int i = 1; i < args.length; i++) {
                monitor.checkCancelled();
                Function function = getFunctionAt(toAddr(args[i]));
                if (function == null) throw new IllegalArgumentException("No function at " + args[i]);
                File destination = new File(output, function.getEntryPoint() + ".txt");
                try (PrintWriter writer = new PrintWriter(destination, StandardCharsets.UTF_8)) {
                    writer.println("Program: " + currentProgram.getName());
                    writer.println("Executable SHA256: " + currentProgram.getExecutableSHA256());
                    writer.println("Language: " + currentProgram.getLanguageID());
                    writer.println("Function: " + function.getName() + "@" + function.getEntryPoint());
                    writer.println("---- CALLEES ----");
                    List<Function> callees = new ArrayList<>(function.getCalledFunctions(monitor));
                    callees.sort(Comparator.comparing(Function::getEntryPoint));
                    for (Function callee : callees) writer.println(callee.getEntryPoint() + " " + callee.getName());
                    writer.println("---- ASSEMBLY ----");
                    InstructionIterator instructions = currentProgram.getListing().getInstructions(function.getBody(), true);
                    while (instructions.hasNext()) {
                        Instruction instruction = instructions.next();
                        writer.println(instruction.getAddress() + "  " + instruction);
                    }
                    writer.println("---- DECOMPILED C ----");
                    DecompileResults result = decompiler.decompileFunction(function, 120, monitor);
                    if (!result.decompileCompleted() || result.getDecompiledFunction() == null) writer.println("// decompile failed: " + result.getErrorMessage());
                    else writer.print(result.getDecompiledFunction().getC());
                }
                println("EXPORTED " + destination);
            }
        } finally {
            decompiler.dispose();
        }
    }
}
