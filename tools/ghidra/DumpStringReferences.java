// Find entry points by diagnostic strings, without changing the program.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Locale;

public class DumpStringReferences extends GhidraScript {
    private String csv(String text) { return "\"" + text.replace("\"", "\"\"") + "\""; }
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) throw new IllegalArgumentException("Usage: <csvPath> <keyword> [keyword...]");
        try (PrintWriter writer = new PrintWriter(new File(args[0]), StandardCharsets.UTF_8)) {
            writer.println("string_address,reference_address,function_address,function_name,text");
            DataIterator data = currentProgram.getListing().getDefinedData(true);
            while (data.hasNext()) {
                monitor.checkCancelled();
                Data item = data.next();
                if (!(item.getValue() instanceof String)) continue;
                String text = (String)item.getValue();
                boolean hit = false;
                for (int i = 1; i < args.length; i++) {
                    if (text.toLowerCase(Locale.ROOT).contains(args[i].toLowerCase(Locale.ROOT))) hit = true;
                }
                if (!hit) continue;
                ReferenceIterator refs = currentProgram.getReferenceManager().getReferencesTo(item.getAddress());
                while (refs.hasNext()) {
                    Reference ref = refs.next();
                    Function function = getFunctionContaining(ref.getFromAddress());
                    writer.println(csv(item.getAddress().toString()) + "," + csv(ref.getFromAddress().toString()) + "," + csv(function == null ? "" : function.getEntryPoint().toString()) + "," + csv(function == null ? "" : function.getName()) + "," + csv(text));
                }
            }
        }
    }
}
