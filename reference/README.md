# Runnable C# Reference Code

This is a dependency-free .NET 10 library and console runner built from the
gameplay investigation. It is usable reference code, not recovered original
game source, a complete Isaac implementation, or a seed-compatible replacement.
It is kept separate from upstream PixelAbyss, following SCOPE.md.

## Build and Run

From the repository root, with .NET SDK 10 installed:

~~~powershell
dotnet build reference/IsaacReference.Runner/IsaacReference.Runner.csproj -c Release
dotnet run --project reference/IsaacReference.Runner -c Release --no-build -- verify
dotnet run --project reference/IsaacReference.Runner -c Release --no-build -- demo 5489
dotnet run --project reference/IsaacReference.Runner -c Release --no-build -- seed "B910 ZDCA"
dotnet run --project reference/IsaacReference.Runner -c Release --no-build -- pool path/to/itempools.xml treasure 5489 20
~~~

The runner exits nonzero on verification or input failure. There are no NuGet
dependencies; NuGet.Config clears external sources. The pool command requires
an existing extracted XML file. It samples the core pool; it does not execute
the original GetCollectible wrapper's game-specific rules.

The packaged build is ../artifacts/IsaacReference-2026-10-27.zip. After extraction,
run dotnet runtime/IsaacReference.Runner.dll verify or replace verify with demo.
The runtime needs .NET 10; rebuilding source needs the .NET 10 SDK.

## Code and Evidence

| Library File | Implementation Boundary | Evidence Addresses |
| --- | --- | --- |
| Recovered/XorShift32.cs | uint32 transitions, modulo, float bits, shuffle | 007a7d50, 007a7db0, 005b6370 |
| Recovered/Mt19937.cs | MT19937 initialization, twist and temper | 006c3d50, 006c3d90 |
| Recovered/SeedCodec.cs | Seed string encoding and checksum parsing | 0093df80, 0093e080 |
| Recovered/StartSeedState.cs | Initial 14 stage slots, extra seed, next-seed stream | 0093e220, 00705f30, 006c4560 |
| Recovered/ItemPool.cs | Ordinary weighted selector, residual repicks, depletion | 00700c60, 007034d0 |
| Recovered/WeightedSpawn.cs | Cumulative weight selection and first-entry fallback | 007e7c20 |
| Recovered/PendingDamage.cs | Selected cooldown and pending-event behavior | 00684bb0, 00680d60, 0068f0f0 |
| Recovered/RoomRestrictions.cs | Shape bounds, occupancy and connection gate core | 00910d10, 00910dd0, 00910ec0, 009101d0 |
| Original/FloorGenerator.cs | Original single-cell tree layout and special rooms | Architecture informed by 0090e760 / 00911060 |
| Original/EnemyAnimationModel.cs | Host-driven subset of one anonymous AI path | Selected branches at 0044e9a0 |
| Original/PlayerCombat.cs | Player TakeDamage dispatch facade and queued result | 00819e70, 00846fb0 |
| Original/Combatant.cs | Original HP application and death policy | No original HP/death compatibility claim |

Every address refers to the SHA-256 in ../evidence/manifest.json. Those exports
contain assembly and C pseudocode. Recovered APIs use managed validation and
exceptions instead of native memory errors, logging and traps. Snapshot formats,
XML input validation and host tick/drain APIs are new interface choices.

Item eligibility, temporary exclusions and unlock rules are caller policies.
ItemType must be supplied when type filters matter; itempools.xml alone does not
provide it. The default removal policy excludes nonnegative IDs; the original
has challenge-specific exceptions and a special item side effect. Passing
excludeOnRemoval=false disables this reference policy.

The floor model uses its own single-cell candidates, retry cap and room
assignments. It does not implement large room shapes, the door candidate table,
original room templates, stage special cases or the original stream schedule.
AI inputs supply eligibility decisions and animation events; they are pulses
from the host, not a full animation or collision engine. Damage cooldowns are
set before callback rejection, as observed; advancing them and draining events
are explicit host actions. The reference combatant commits queued damage on
demand. PlayerCombat models the Lua wrapper argument and boolean boundary,
while the native player HP/death consumer remains unresolved.

## Verification

The console verifier checks independent arithmetic vectors, MT19937's default
sequence, seed checksum failures and 10,000 seed round trips, pool selection and
depletion edges, cooldown mutation order, animation state transitions, and
connectivity/tree/dead-end invariants over 200 generated floors. JSON snapshots
verify deterministic continuation of the reference models.

../tools/analysis/reference_vectors.mjs regenerates the checked-in fixture using
JavaScript BigInt and explicit float32 rounding. These are static algorithm
oracles, not traces captured from the game. The verifier does not establish
native gameplay parity, distribution parity, or recovery of all game systems.

See ../reports/FINAL_CODE_2026-10-27.md for results and remaining reverse
engineering work.
