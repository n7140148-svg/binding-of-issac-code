// Use only with analyzeHeadless -readOnly -noanalysis. Repairs are session-local.
import ghidra.app.script.GhidraScript;
import ghidra.app.cmd.function.CreateFunctionCmd;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.*;
import java.util.*;

public class RepairLoggerFlow extends GhidraScript {
    @Override
    public void run() throws Exception {
        Address loggerAddress = toAddr("0095e330");
        Function logger = getFunctionAt(loggerAddress);
        if (logger == null) throw new IllegalStateException("Logger not found");
        println("Logger previous no-return: " + logger.hasNoReturn());
        logger.setNoReturn(false);
        for (String entry : getScriptArgs()) {
            Function function = getFunctionAt(toAddr(entry));
            if (function == null) throw new IllegalArgumentException("No function at " + entry);
            long before = function.getBody().getNumAddresses();
            Set<Address> repaired = new HashSet<>();
            for (int pass = 0; pass < 8; pass++) {
                List<Address> continuations = new ArrayList<>();
                InstructionIterator instructions = currentProgram.getListing().getInstructions(function.getBody(), true);
                while (instructions.hasNext()) {
                    Instruction instruction = instructions.next();
                    if (!instruction.getFlowType().isCall()) continue;
                    for (Address target : instruction.getFlows()) {
                        if (target.equals(loggerAddress) && repaired.add(instruction.getAddress())) {
                            instruction.setFlowOverride(FlowOverride.NONE);
                            continuations.add(instruction.getAddress().add(instruction.getLength()));
                        }
                    }
                }
                if (continuations.isEmpty()) break;
                for (Address continuation : continuations) disassemble(continuation);
                CreateFunctionCmd.fixupFunctionBody(currentProgram, function, monitor);
            }
            println("REPAIRED " + entry + " body bytes " + before + " -> " + function.getBody().getNumAddresses());
        }
    }
}
