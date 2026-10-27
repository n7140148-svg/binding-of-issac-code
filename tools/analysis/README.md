# Reproducing the continuation

The Node scripts use built-in modules only. Run from the repository root:

~~~powershell
node --test tools/analysis/audit_exports.test.mjs
node tools/analysis/audit_exports.mjs
node tools/analysis/read_pe_constants.mjs
node tools/analysis/index_focused.mjs
~~~

The audit regenerates reports/export-audit.json and an ignored C-only search
corpus under .analysis-cache/c. It handles the shipped legacy CSV format;
future quoted CSV from DumpGameLogic.java should use a standard CSV parser.
A pcode marker does not prove the section finished. The manifest command
validates target identities and regenerates export/script hashes.

## Focused Ghidra exports

Ghidra 12.1.4 and JDK 21 are already installed on this machine. Reuse its
analyzed database without running analysis or saving annotations:

~~~powershell
$env:JAVA_HOME = 'F:\zulu21.42.19-ca-jdk21.0.7-win_x64'
$taskRoot = (Get-Location).Path
$ghidra = 'E:\Tools\ghidra\ghidra_12.1.4_PUBLIC\support\analyzeHeadless.bat'
& $ghidra 'F:\ghidra_work\isaacng_game' isaacng_game -process isaac-ng.exe -readOnly -noanalysis -scriptPath "$taskRoot\tools\ghidra" -postScript DumpFocused.java "$taskRoot\evidence\focused" 00701230 00700c60
~~~

DumpStringReferences.java accepts an output CSV path followed by literal
substring keywords. It emits quoted CSV including multiline strings; use
a CSV parser rather than line-oriented splitting.

For recovered flow, use two postScript arguments in the same invocation:

~~~text
-postScript RepairLoggerFlow.java 00701230 00700c60
-postScript DumpFocused.java <absolute-output-directory> 00701230 00700c60
~~~

Use -readOnly -noanalysis. The repair clears the logger's no-return flag,
disassembles immediate call continuations and recomputes explicitly selected
function bodies in memory. It makes at most eight passes per target and does
not promise whole-program repair. Store recovered output in evidence/repaired
and preserve baseline exports. Review assembly and indirect calls before
treating recovered C as complete.

The evidence logs record the exact invocations from this pass. This workflow
does not execute the game or recover original source/type names.
# Reference Code Verification

Generate static arithmetic fixtures with node tools/analysis/reference_vectors.mjs.
Build and verify the C# runner using [reference/README.md](../../reference/README.md).
Package source, exports and framework-dependent runtime using
tools/analysis/package_reference.ps1 after validation. The package excludes the
original executable and historical bulk dump; the evidence manifest refers to
the original binary hash rather than redistributing that binary.

