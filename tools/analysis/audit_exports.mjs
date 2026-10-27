import { readFileSync, readdirSync, mkdirSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve, relative, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

// Recover unquoted C++ names by anchoring on the numeric size and known tag.
export function parseLegacyIndex(text) {
  const rows = [], rejected = [];
  for (const [i, line] of text.split(/\r?\n/).entries()) {
    if (!line.trim() || line.startsWith('addr,')) continue;
    const m = /^(0x[0-9a-f]+),(.*),(\d+),(expanded_callee|expanded_caller|seed:[^,]+),(.*)$/i.exec(line);
    if (!m) { rejected.push({ line: i + 1, text: line }); continue; }
    rows.push({ address: m[1].toLowerCase(), name: m[2], size: Number(m[3]), tag: m[4], matched: m[5] });
  }
  return { rows, rejected };
}

export function inspectExport(text) {
  const header = /^========== FUNCTION (.+)@([0-9a-f]+) ==========/im.exec(text);
  if (!header) return null;
  const marker = '---- DECOMPILED C ----';
  const start = text.indexOf(marker), end = text.indexOf('---- PCODE', start);
  const c = start < 0 ? '' : text.slice(start + marker.length, end < 0 ? undefined : end).trim();
  return {
    address: '0x' + header[2].toLowerCase().padStart(8, '0'), name: header[1],
    hasC: c.length > 0 && !c.startsWith('// decompile failed'),
    hasPcodeMarker: end >= 0, c,
    calls: [...new Set([...text.slice(0, start < 0 ? undefined : start).matchAll(/\bCALL 0x([0-9a-f]+)/gi)].map(m => '0x' + m[1].toLowerCase().padStart(8, '0')))].sort(),
  };
}

export function audit(root) {
  const source = join(root, 'gamelogic_out', 'gamelogic');
  const index = parseLegacyIndex(readFileSync(join(root, 'gamelogic_out', 'gamelogic_INDEX.csv'), 'utf8'));
  const functions = [], unrecognized = [];
  const cache = join(root, '.analysis-cache', 'c');
  mkdirSync(cache, { recursive: true });
  for (const name of readdirSync(source).sort()) {
    const path = join(source, name), bytes = readFileSync(path);
    const item = inspectExport(bytes.toString('utf8'));
    if (!item) { unrecognized.push({ file: name, bytes: bytes.length }); continue; }
    if (item.hasC) writeFileSync(join(cache, item.address.slice(2) + '.c'), item.c + '\n');
    const { c, ...metadata } = item;
    functions.push({ ...metadata, file: relative(root, path).replaceAll('\\', '/'), bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') });
  }
  const exported = new Set(functions.map(f => f.address));
  const indexed = new Set(index.rows.filter(r => r.size > 0).map(r => r.address));
  const result = {
    sourceCommit: execFileSync('git', ['rev-parse', 'HEAD'], { cwd: root, encoding: 'utf8' }).trim(),
    binarySha256: createHash('sha256').update(readFileSync(join(root, 'binary', 'isaac-ng.exe'))).digest('hex'),
    limitations: ['Static exports only; no gameplay execution.', 'Legacy tag/matched fields preserved without inferring lost keyword boundaries.', 'A PCODE marker does not prove the pcode section finished.', 'Direct calls only; indirect callees remain unknown.'],
    summary: { indexedRows: index.rows.length, exportedFunctions: functions.length, withC: functions.filter(f => f.hasC).length, withoutPcodeMarker: functions.filter(f => !f.hasPcodeMarker).length, unrecognizedFiles: unrecognized.length, rejectedRows: index.rejected.length, firstAddress: functions.map(f => f.address).sort()[0], lastAddress: functions.map(f => f.address).sort().at(-1) },
    rejectedRows: index.rejected, unrecognizedFiles: unrecognized,
    indexedWithoutExport: [...indexed].filter(a => !exported.has(a)).sort(),
    exportedWithoutIndex: [...exported].filter(a => !indexed.has(a)).sort(), functions,
  };
  mkdirSync(join(root, 'reports'), { recursive: true });
  writeFileSync(join(root, 'reports', 'export-audit.json'), JSON.stringify(result, null, 2) + '\n');
  return result;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  console.log(JSON.stringify(audit(resolve(process.argv[2] ?? '.')).summary, null, 2));
}
