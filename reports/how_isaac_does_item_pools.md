# Collectible selection and inventory reroll

Runnable weighted core: [ItemPool.cs](../reference/IsaacReference/Recovered/ItemPool.cs).
Its API policies and omitted wrapper behavior are described in [reference](../reference/README.md).

2026-10-27, static Ghidra analysis of the SHA-256 recorded in
[the RNG report](how_isaac_does_rng.md). No gameplay execution.
Semantic names below are report annotations, not recovered symbols.

## Entry point and evidence

[0x00701230](../evidence/repaired/00701230.txt) contains the diagnostic
"ItemPool::GetCollectible Seed is 0" and is confidently named
ItemPool_GetCollectible. It dispatches special cases, invokes the weighted
selector [0x00700c60](../evidence/repaired/00700c60.txt), applies fallback
and substitutions, then offers a final result override.

The inferred signature is GetCollectible(this, pool, seed, flags, defaultId).
The assembly must accompany the C: several member calls omit their implicit
ECX object in Ghidra's rendered arguments, and the selector receives its
floating-point sample through XMM1 rather than an ordinary C parameter.

## Observed main path

1. Log an error for seed zero; return zero for pool -1. The logger itself
   returns, so its call alone does not prove a fatal exit.
2. Apply run/ownership checks and special selection paths. Helpers at
   0x008028d0 and 0x00802a20 provide early and final overrides; their exact
   callback contracts have not been traced in this pass.
3. Optionally replace the effective pool through 0x00704ad0. Its pool ranges
   depend on a run field; naming an item effect needs further evidence.
4. Address a pool record with this + 4 + poolIndex * 0x34. Generate a float
   with 0x007a7db0 and multiply by the pool's total base weight.
5. Pass the scaled sample in XMM1 to 0x00700c60. Assembly at 0x007015fa
   through 0x0070160f proves the random draw, multiplication and register
   argument that are misleading in the decompiled C.
6. Inspect the returned entry's byte at +0x14. If the outer acceptance
   condition fails, advance a separate local retry state and draw again.
   The retry logic uses a counter initialized to 20. Do not merge this with
   the selector's separate repick budget.
7. If no candidate survives, use defaultId when nonzero. Otherwise pool zero
   falls back to ID 0x19; another pool recurses to pool zero. Several later
   substitutions and the final override can still change the result.

Challenge-specific IDs and ownership checks exist in the wrapper. Numeric
IDs are retained rather than assigning names from an unverified build.

## Weighted selector: observations

0x00700c60 walks six-word (0x18-byte) entries between pool offsets +4 and
+8. Its layout supports these provisional field names:

| Entry Offset | Meaning Supported by Use |
| --- | --- |
| +0x00 | Collectible ID |
| +0x04 | Base interval weight, accumulated during selection |
| +0x08 | Remaining acceptance weight, reduced after a selection |
| +0x0c | Amount subtracted from remaining weight |
| +0x10 | Removal threshold |
| +0x14 | Byte consulted by outer acceptance; exact meaning open |

The selector accumulates base weights until cumulativeWeight > sample.
Within that interval it derives a residual fraction and checks it against
remainingWeight / baseWeight. Two bitsets at object offsets +0x67c and
+0x68c, an eligibility helper at 0x006fe950, and flags filtering an item
type can reject an entry as well.

On rejection it maps the residual fraction back across the full pool and
restarts the scan. This inner repick does not call an RNG. It starts with
a budget of 10, or 20 when flags bit 1 is set. Exhaustion logs a warning,
then scans forward with wraparound for an eligible entry with positive
remaining weight, excluding the final failed entry. It returns no entry
if that scan cannot find one. This fallback was absent from the original
decompilation because the logger had a mistaken no-return annotation.
Both this remapping and the outer RNG retry loop matter for exact behavior.

When flags bit 0 is clear and remainingWeight is positive, the chosen
entry's remainingWeight is reduced by the decrement. Falling below the
threshold zeros it and may set an exclusion bit, subject to run-specific
conditions. Selection is stateful; a fixed weighted list alone does not
capture this path.

## Inventory reroll caller

[0x005b3c80](../evidence/focused/005b3c80.txt) removes eligible existing
collectibles, then requests replacements from 0x00701230. At 0x005b424f
and 0x005b42b2, ECX is game + 0x1a5cc, locating the pool manager instance.
Each attempt advances an RNG object at a player-associated object +0x11c0.
It passes flags 0x0c or 6, tries at most ten times to fill an empty slot,
and falls back to ID 0x19 if it still has zero. A run-specific rejection
of ID 0x26b is visible; its named meaning remains unconfirmed.

## Application and open questions

PixelAbyss can independently design base weight, depletion, exclusion,
eligibility and fallback as distinct policies. These are design references,
not source to link or transplant into the upstream game.

[0x007034d0](../evidence/repaired/007034d0.txt) independently confirms the
layout from XML attribute parsing: Weight initializes both +4 and +8,
DecreaseBy initializes +0x0c, and RemoveOn initializes +0x10. The C stores:

~~~c
puVar12[1] = (uint)fStack_100e4;
puVar12[2] = (uint)fStack_100e0;
puVar12[3] = (uint)fStack_100dc;
~~~

Here the decompiler's uint casts represent float bit storage, as the
assembly's moves and subsequent float operations show. Do not translate
them into numeric float-to-integer conversions.

Open: complete XML/mod merge policy, full flag enum, all callbacks and
special cases, eligibility/unlock rules, final override semantics, and runtime
parity. The ordinary selection chain is located and decompiled; full
GetCollectible behavior is only partially explained.

The remap is totalWeight * residualFromRight. If it equals totalWeight exactly,
the code divides by the float at 00b6a880, bits 0x4057e204 (3.3731698989868164).
The exhaustion scan excludes the final rejected entry, which need not be the
first rejected entry. These details are implemented in the reference core.
