import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve } from 'node:path';

const root = resolve(process.argv[2] ?? '.');
const binary = readFileSync(resolve(root, 'binary/isaac-ng.exe'));
const pe = binary.readUInt32LE(0x3c);
if (binary.readUInt16LE(0) !== 0x5a4d || binary.readUInt32LE(pe) !== 0x4550) throw Error('Not a PE');
const optional = pe + 24;
if (binary.readUInt16LE(optional) !== 0x10b) throw Error('Expected PE32');
const imageBase = binary.readUInt32LE(optional + 28);
const sections = [];
for (let i = 0; i < binary.readUInt16LE(pe + 6); i++) {
  const at = optional + binary.readUInt16LE(pe + 20) + i * 40;
  sections.push({ name: binary.toString('ascii', at, at + 8).replaceAll('\0', ''), rva: binary.readUInt32LE(at + 12), rawSize: binary.readUInt32LE(at + 16), rawOffset: binary.readUInt32LE(at + 20) });
}
const requests = [
  [0x00a08ba8, 12, 'GetCollectible local RNG shifts'],
  [0x00a08ad0, 12, 'GetCollectible retry RNG shifts'],
  [0x00a08ab8, 12, 'challenge RNG shifts'],
  [0x00a08c44, 12, 'wave RNG shifts'],
  [0x00a08be4, 12, 'start seed initialization RNG shifts'],
  [0x00b49b28, 8, 'MT twist table'],
  [0x00b6a198, 4, 'RandomFloat scale'],
  [0x00b6c940, 16, 'unsigned integer conversion offsets'],
  [0x00b6a880, 4, 'pool repick sample-equals-total divisor'],
  [0x00b5c940, 32, 'seed alphabet ASCII'],
  [0x00bea988, 32, 'layout cardinal direction int32 pairs'],
];
const constants = requests.map(([address, length, purpose]) => {
  const rva = address - imageBase;
  const section = sections.find(s => rva >= s.rva && rva + length <= s.rva + s.rawSize);
  if (!section) throw Error('Requested constant is not backed by file data: ' + address.toString(16));
  const offset = section.rawOffset + rva - section.rva;
  if (offset + length > binary.length) throw Error('Truncated PE section');
  const bytes = binary.subarray(offset, offset + length);
  return { address: '0x' + address.toString(16), purpose, section: section.name, fileOffset: offset, hex: bytes.toString('hex'), u32: Array.from({ length: length / 4 }, (_, i) => bytes.readUInt32LE(i * 4)), ...(length === 4 ? { f32: bytes.readFloatLE(0) } : {}), ...(length === 16 ? { f64: [bytes.readDoubleLE(0), bytes.readDoubleLE(8)] } : {}) };
});
const result = { binarySha256: createHash('sha256').update(binary).digest('hex'), imageBase, constants };
writeFileSync(resolve(root, 'evidence/pe-constants.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
