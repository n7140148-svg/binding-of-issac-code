# Code Delivery and Investigation Boundary

Date: 2026-10-27. Target: binary/isaac-ng.exe, SHA-256
530b4d2accef833b8dbf6f1a9f781fe1e051c1916ca5acdb579df05a34640627.

Runnable C# code is in [reference](../reference/README.md). The deliverable is
an independently written algorithm reference and original gameplay models.
Whole-game reverse engineering remains incomplete. No gameplay execution or
comparison against a running Isaac instance was performed. Compilation and
reference tests cannot establish original-game parity.

## Findings Added in This Pass

1. Seed encoding/parsing is traced from Lua registration helpers 0082efa0 and
   0082ef40 to [0093df80](../evidence/repaired/0093df80.txt) and
   [0093e080](../evidence/repaired/0093e080.txt). These use eight alphabet symbols
   with one separating space, XOR mask 0x0fef7ffd, and an eight-bit checksum.
   Each checksum iteration adds the low byte of the current seed, rotates the
   byte left once, then advances the seed by five bits. Alphabet bytes at
   00b5c940 are ABCDEFGHJKLMNPQRSTWXYZ01234V6789. Parsing requires exact case,
   nine characters and the space at offset four. Invalid input returns zero.
   The managed API also distinguishes encoded zero from a parse failure.
2. The selector's sample-equals-total remap uses the float bits 0x4057e204 at
   00b6a880: 3.3731698989868164. This is read from the PE, not guessed from a
   reciprocal. The ordinary repick budget permits 10 or 20 remaps followed by
   an exhaustion scan. The initial entry and the final failed entry may differ;
   the exhaustion scan excludes the final failed entry.
3. [00911060](../evidence/repaired/00911060.txt) grows layout candidates with a
   deque. For small requested counts the start expansion budget is two or
   three; other expansions draw four random low bits and sum them. Candidate
   acceptance precedes the post-insertion budget check: zero budget does not
   mean that no candidate can be inserted. Enqueue choice is one-third back,
   otherwise front. Room insertion still depends on shape and occupancy helpers.
4. [00911690](../evidence/repaired/00911690.txt) creates shape-aware neighbors,
   tests eight possible door slots, uses a 13-entry shape/probability table,
   and sets child depth from parent record +0x40 plus one. This is substantially
   more complex than a one-cell grid tree. [0090e760](../evidence/repaired/0090e760.txt)
   attempts at most five dead-end additions before sorting by descending depth.
5. [00706f00](../evidence/repaired/00706f00.txt) is now exported. It requests boss
   and special-room templates via room configuration helpers, advances the
   level RNG, and can report failure to the outer generation retry. It is not
   a complete decoded map-placement specification.
6. [0068f0f0](../evidence/repaired/0068f0f0.txt) appends a 0x38-byte record, using
   a capacity-growth helper when needed. [00680d60](../evidence/repaired/00680d60.txt)
   initializes that record. [00684bb0](../evidence/repaired/00684bb0.txt) sets
   cooldowns before its acceptance callback; cancellation retains those writes.
   The reference implementation preserves that ordering and separates pending
   amounts from HP application.
7. [007e7c20](../evidence/repaired/007e7c20.txt) selects the first cumulative
   interval strictly above sample * total, otherwise warning and first entry.
   [007e7770](../evidence/repaired/007e7770.txt) retries room selection with its
   alternate type argument if its first room query fails. Its return value
   is used by callers despite Ghidra's inferred void prototype.
8. [00422e20](../evidence/repaired/00422e20.txt) forwards seven arguments and
   a final zero to entity factory 006d0ca0. Entity type meaning is not inferred
   from this wrapper alone.
9. [0044e9a0](../evidence/repaired/0044e9a0.txt) contains an animation-driven
   enemy update path. State zero initializes state four. State four can select
   16, 8, 13 or 6 in priority order. State eight chooses Attack2Left/Up/Right/Down
   and spawns on Shoot; state 13 uses Skin Pull and Shoot events, spawning up
   to four minus existing minions; state 16 plays Scream and returns to four.
   State six contains airborne/landing behavior. Calling it generic fly AI
   is unsupported. Identity and helper-controlled predicates remain unresolved.

10. [0093e220](../evidence/repaired/0093e220.txt) initializes a (3,23,25)
    xorshift stream, fourteen stage seeds and one additional seed. Seed zero
    consumes one global MT19937 result, clamped to at least one. Lua bindings
    identify stage getter 00705f30 and next-seed generator 006c4560. Their
    ordinary initialization/read/advance behavior is implemented in StartSeedState.
    Later stage reseeding and every global stream consumer remain open.
11. [009106c0](../evidence/repaired/009106c0.txt) marks non-start rooms with
    fewer than two relevant neighbors and then clears connecting-parent marks.
    [00800e30](../evidence/repaired/00800e30.txt) establishes the damage
    acceptance helper's Lua boolean/default-true behavior. These refine the
    earlier layout and damage notes without recovering all consumers.

12. [00819e70](../evidence/repaired/00819e70.txt) registers the player Lua
    TakeDamage method, and [00846fb0](../evidence/repaired/00846fb0.txt)
    forwards amount, flags, source and cooldown to native player dispatch and
    returns its boolean. The reference PlayerCombat facade records this
    boundary without claiming native HP/death recovery.
13. [00910d10](../evidence/repaired/00910d10.txt), [00910dd0](../evidence/repaired/00910dd0.txt)
    and [00910ec0](../evidence/repaired/00910ec0.txt) establish shape bounds,
    occupancy and door connection restrictions. RoomRestrictions exposes this
    predicate core while leaving the native shape/template tables open.

## Coverage Checklist

| Investigation Area | Current Result | Still Required for Exact Compatibility |
| --- | --- | --- |
| RNG and seeds | Main generators, shuffle and seed string codec implemented | Complete seed/stream ownership, all initialization and save paths, runtime replay |
| Item pools | Ordinary selection chain decoded; weighted core implemented | All wrapper special cases, unlocks, callbacks, merge policy and substitutions |
| Levels | Init, ordinary retries, layout growth and placement helpers exported | Full shape/door/template constraints and special generation branches |
| Enemy AI/waves | One update path and one wave-spawning chain explained | All predicate helpers, actor identity, animation data, physics and other enemies |
| Combat | Non-player queue path plus player Lua/native dispatch boundary implemented | Collision, HP/death consumer, all flag and effect semantics |

The handover's main-path discovery and reference-code work have advanced across
all five areas. These are partial compatibility results, not a claim that every
gameplay function has been reverse engineered. Archive art/audio work remains
excluded. Existing source files and historical exports are preserved.

## Validation

The Release build passed with zero warnings and zero errors. The runner passed
60 verification groups, including 200 floor seeds and 10,000 codec round trips.
The Node export-audit suite passed all three tests. All 73 focused/repaired
exports were hashed and checked against the target. Output is recorded in
[reference-validation.txt](reference-validation.txt). Reproduce the evidence
check with tools/analysis/index_focused.mjs.

The local source/evidence/runtime package is
artifacts/IsaacReference-2026-10-27.zip. Generate it with
tools/analysis/package_reference.ps1. Its runtime requires .NET 10 and can be
run after extraction with dotnet runtime/IsaacReference.Runner.dll verify.
The original executable and historical bulk dump are excluded from this package.

Fixtures are generated by a separate BigInt/float32 oracle. They establish that
the managed code matches the documented arithmetic, not that a live game was
observed. The floor/AI/combat models are verified against their own explicit
contracts. No upstream game source, graphics or audio is packaged into the
reference runner.

## Remaining Targets

Follow the native shape table and room templates behind 009101d0/007e7180, the
consumers of damage queue offsets +8/+0xc and pending amount +0x14, native
player HP/death handling, and AI predicates 00695680 / 00695a30 / 006d0380.
These are concrete unresolved targets, not completed work. Keep the temporary
logger-flow correction enabled for exports; the saved database remains unchanged.
