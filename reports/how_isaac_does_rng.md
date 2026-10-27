# Gameplay RNG and shuffling

Latest code and additional seed findings: [delivery report](FINAL_CODE_2026-10-27.md)
and [reference library](../reference/README.md). The open seed-encoding item in
the earlier notes below is resolved by 0093df80 / 0093e080.

Investigation date: 2026-10-27. Static evidence only; the game was not run.
Target SHA-256: 530b4d2accef833b8dbf6f1a9f781fe1e051c1916ca5acdb579df05a34640627.
Addresses below refer to this PE32 snapshot, image base 0x00400000.

## Confirmed: configurable xorshift streams

[0x007a7d50](../evidence/repaired/007a7d50.txt) advances a four-word object:
state at +0, shift counts at +4, +8, +12. The assembly uses SHR, SHL, SHR
with x86's low-five-bit shift-count masking, storing results as uint32.

~~~c
x ^= x >> (a & 31);
x ^= x << (b & 31);
x ^= x >> (c & 31);
~~~

A zero input state logs "RNG Seed is zero!", reloads the state, and hits an
INT3 breakpoint if it is still zero. The repaired export exposes this path;
the original database incorrectly treated the logger as non-returning.
RandomInt(bound), the proposed semantic name for 0x007a7d50, consumes one
state transition even for bound zero, then returns zero or x % bound.
There is no rejection sampling in this function. Modulo reduction can
therefore introduce bias; it is part of this observed behavior.

[0x007a7e20](../evidence/focused/007a7e20.txt) performs the same transition.
Ghidra declares its return void; do not infer a public return contract from
that declaration alone. Several callers inline the transition instead.

## Confirmed: float conversion is not an exact division by 2^32

[0x007a7db0](../evidence/repaired/007a7db0.txt) advances the state, converts
the unsigned result to single precision, multiplies in single precision,
and returns through x87. The correction table at 0x00b6c940 contains double
values 0 and 4294967296 for converting signed to unsigned values.
The multiplier at 0x00b6a198 has bits 0x2f7ffffe, or
2.3283061589829401e-10. This is slightly below 2^-32; substituting that
mathematical reciprocal would lose exact float behavior.

Raw bytes and file offsets are in [pe-constants.json](../evidence/pe-constants.json),
reproducible with: node tools/analysis/read_pe_constants.mjs.

The local ItemPool::GetCollectible RNG uses shifts (3,5,20), its retry
stream uses (1,11,6), and the inspected wave helper uses (5,9,7).
These are observed instances, not a complete enumeration of RNG streams.

## Confirmed: a separate MT19937 global generator

[0x006c3d50](../evidence/focused/006c3d50.txt) initializes 624 words using
1812433253 * (previous ^ (previous >> 30)) + index, modulo 2^32.
[0x006c3d90](../evidence/focused/006c3d90.txt) twists with lag 397 and
matrix constant 0x9908b0df, then tempers using shifts 11, 7, 15, 18.
The pre-shift masks in assembly are equivalent to the usual post-shift
masks 0x9d2c5680 and 0xefc60000. An uninitialized index of 625 invokes
initialization with 5489 (MOV ECX,0x1571 at 0x006c3da7).
Together these identify the MT19937 algorithm from this binary.
Seed lifecycle and the generator's complete gameplay role remain open.

## Confirmed: descending Fisher-Yates structure

[0x005b6370](../evidence/focused/005b6370.txt) and
[0x005b6400](../evidence/focused/005b6400.txt) accept a range of four-byte
entries, loop from n-1 down through 1, advance the supplied xorshift
object once per iteration, and swap entry i with entry random % (i+1).
For n <= 1 they consume no random values. Their calling conventions differ.

## Design reference and remaining work

For PixelAbyss, separate named RNG streams make random-call dependencies
explicit. Treat that as a design choice; this pass has not reconstructed
the complete Isaac stream ownership or seed schedule.

The archive generator described by tools/extractors/isaac_prng2.py is not
the gameplay RNG above. Comparing only that file cannot establish gameplay
seed parity. Archive art/audio streams remain outside scope.
## Seed codec and initial stage slots

[0093df80](../evidence/repaired/0093df80.txt) formats eight symbols separated
after four characters. It XORs the input with 0x0fef7ffd, attaches an eight-bit
checksum, and indexes the alphabet at 00b5c940. Checksum accumulation adds the
current seed's low byte modulo 256, rotates left once, then shifts the seed
right by five bits. [0093e080](../evidence/repaired/0093e080.txt) validates exact
length, case, alphabet and checksum; it returns zero on invalid input.

[0093e220](../evidence/repaired/0093e220.txt) initializes the start seed object.
Input zero consumes one MT19937 result and uses max(result, 1). It initializes
a xorshift stream with shifts (3,23,25) from 00a08be4, writes fourteen advances
to offsets +0x18 through +0x4c, then stores the fifteenth at +0x50. The Lua
GetStageSeed registration at 0082ee90 points to
[00705f30](../evidence/repaired/00705f30.txt), which reads +0x18 + index*4.
GetNextSeed at 0082ee30 points to [006c4560](../evidence/repaired/006c4560.txt);
its assembly advances the stream at +8 and leaves the new state in EAX, despite
Ghidra's inferred void prototype. The C# StartSeedState implements this path.

Still unresolved: complete shift-table selection, later changes to stage slots,
special seed effects, persistence and ownership of every stream, and native
runtime replay. Managed snapshot replay tests cover the reference APIs only.
