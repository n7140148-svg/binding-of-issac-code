import test from 'node:test';
import assert from 'node:assert/strict';
import { parseLegacyIndex, inspectExport } from './audit_exports.mjs';

test('recovers template names and rejects a truncated row', () => {
  const result = parseLegacyIndex('addr,name,size,tag,matched\n0x00400000,Thing<int,char>,59,expanded_callee,\n0');
  assert.equal(result.rows[0].name, 'Thing<int,char>');
  assert.equal(result.rows[0].size, 59);
  assert.deepEqual(result.rejected, [{ line: 3, text: '0' }]);
});

test('preserves ambiguous keyword payload', () => {
  const result = parseLegacyIndex('0x00400000,FUN_00400000,59,seed:rng,seed,room');
  assert.equal(result.rows[0].matched, 'seed,room');
});

test('distinguishes failed decompilation, truncated sections, and empty files', () => {
  const prefix = '========== FUNCTION FUN_00400000@00400000 ==========\n';
  assert.equal(inspectExport(prefix + '---- DECOMPILED C ----\n// decompile failed\n---- PCODE').hasC, false);
  const result = inspectExport(prefix + '00400000  CALL 0x00701230\n---- DECOMPILED C ----\nvoid f() {}');
  assert.equal(result.hasC, true);
  assert.equal(result.hasPcodeMarker, false);
  assert.deepEqual(result.calls, ['0x00701230']);
  assert.equal(inspectExport(''), null);
});
