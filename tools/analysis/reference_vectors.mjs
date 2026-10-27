// Independent BigInt/float32 oracle for the recovered algorithm descriptions.
// This produces static expected values, not gameplay or native execution traces.
import { writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(process.argv[2] ?? '.');
const mask32 = 0xffffffffn;
const bits = value => { const b = Buffer.alloc(4); b.writeFloatLE(value); return b.readUInt32LE(); };
const scaleBytes = Buffer.from('feff7f2f', 'hex');
const scale = scaleBytes.readFloatLE();
const configurations = [[3, 5, 20], [1, 11, 6], [1, 5, 19], [5, 9, 7], [3, 23, 25], [35, 37, 52]];
const xorshift = configurations.flatMap(shifts => [1, 0x12345678, 0x80000000, 0xffffffff].map(seed => {
  let state = BigInt(seed);
  const values = [], floats = [];
  for (let i = 0; i < 16; i++) {
    state ^= state >> BigInt(shifts[0] & 31);
    state = (state ^ (state << BigInt(shifts[1] & 31))) & mask32;
    state ^= state >> BigInt(shifts[2] & 31);
    values.push(Number(state));
    floats.push(bits(Math.fround(Math.fround(Number(state)) * scale)));
  }
  return { seed, shifts, values, floatBits: floats };
}));

const alphabet = 'ABCDEFGHJKLMNPQRSTWXYZ01234V6789';
const seeds = [0, 1, 2, 3, 31, 32, 5489, 0x12345678, 0x80000000, 0xffffffff].map(seed => {
  let checksum = 0;
  for (let n = BigInt(seed); n !== 0n; n >>= 5n) {
    const sum = (checksum + Number(n & 255n)) & 255;
    checksum = ((sum * 2) & 255) + (sum >= 128 ? 1 : 0);
  }
  const payload = ((BigInt(seed) ^ 0x0fef7ffdn) << 8n) | BigInt(checksum);
  let text = '';
  for (let shift = 35n; shift >= 0; shift -= 5n) text += alphabet[Number((payload >> shift) & 31n)];
  return { seed, text: text.slice(0, 4) + ' ' + text.slice(4) };
});
const result = {
  evidenceType: 'independent static arithmetic oracle; not observed game execution',
  xorshift, seeds,
  mtDefaultFirstTen: [3499211612, 581869302, 3890346734, 3586334585, 545404204, 4161255391, 3922919429, 949333985, 2715962298, 1323567403]
};
writeFileSync(resolve(root, 'evidence/reference-vectors.json'), JSON.stringify(result, null, 2) + '\n');
console.log('Generated ' + xorshift.length + ' xorshift vectors and ' + seeds.length + ' seed vectors.');
