import { readFileSync, readdirSync, writeFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve, join } from 'node:path';

const root = resolve(process.argv[2] ?? '.');
const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');
const targetSha256 = sha256(readFileSync(join(root, 'binary/isaac-ng.exe')));
const files = [];
for (const variant of ['focused', 'repaired']) {
  const directory = join(root, 'evidence', variant);
  if (!existsSync(directory)) continue;
  for (const name of readdirSync(directory).filter(n => n.endsWith('.txt')).sort()) {
    const bytes = readFileSync(join(directory, name)), text = bytes.toString('utf8');
    const identity = /^Executable SHA256: (.+)$/m.exec(text)?.[1].trim();
    if (identity !== targetSha256) throw Error('Target identity mismatch: ' + name);
    const header = /^Function: (.+)@([0-9a-f]+)$/m.exec(text);
    if (!header) throw Error('Missing function identity: ' + name);
    const c = text.slice(text.indexOf('---- DECOMPILED C ----'));
    if (!c.includes('---- DECOMPILED C ----') || c.includes('// decompile failed:')) throw Error('Export failed: ' + name);
    files.push({ address: '0x' + header[2], name: header[1], file: 'evidence/' + variant + '/' + name, variant, bytes: bytes.length, sha256: sha256(bytes), diagnosticNoReturnWarnings: [...c.matchAll(/Subroutine does not return/g)].length });
  }
}
const scripts = ['DumpFocused.java', 'DumpStringReferences.java', 'RepairLoggerFlow.java'].map(name => ({ file: 'tools/ghidra/' + name, sha256: sha256(readFileSync(join(root, 'tools/ghidra', name))) }));
const result = { targetSha256, tool: 'Ghidra 12.1.4, JDK 21', database: 'F:/ghidra_work/isaacng_game/isaacng_game.gpr', mode: '-process isaac-ng.exe -readOnly -noanalysis', evidenceType: 'ordinary Ghidra exports; not REA Evidence records', limitations: ['Static analysis; no gameplay execution.', 'focused preserves the database annotations; repaired applies RepairLoggerFlow in memory before exporting.', 'Repaired bodies and decompiler types still require assembly review.'], scripts, files };
writeFileSync(join(root, 'evidence/manifest.json'), JSON.stringify(result, null, 2) + '\n');
console.log('Validated ' + files.length + ' exports against ' + targetSha256);
