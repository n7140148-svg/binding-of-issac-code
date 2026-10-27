# Entity damage entry point

Runnable queue core: [PendingDamage.cs](../reference/IsaacReference/Recovered/PendingDamage.cs).
HP application is an explicit original policy in [Combatant.cs](../reference/IsaacReference/Original/Combatant.cs).

2026-10-27. Partial static reconstruction of one non-player damage path.
Source: [0x00684bb0](../evidence/focused/00684bb0.txt), target SHA-256 in
[manifest.json](../evidence/manifest.json). Proposed name: Entity_TakeDamage.

The diagnostic "Entity TakeDamage should not be called for Entity Player!"
anchors this function's role and distinguishes it from player damage.
Its arguments appear to include an amount, two flag words, a source-like
argument and a cooldown value. Their full API types are unconfirmed.

The ordinary accepted path checks source/eligibility helpers and type-specific
exceptions, then implements two separate damage gates:

| Input Condition | Entity State |
| --- | --- |
| flags & 2, positive damage | Reject when +0x208 > 0; otherwise set +0x208 to 10 |
| flags & 0x40 | Reject when +0x20c > 0; otherwise set +0x20c to the cooldown argument |

There is multiplayer-dependent scaling, a doubling condition controlled by
an entity flag, and a helper at 0x00800e30 that can prevent acceptance.
On success it invokes 0x00680d60, 0x0068f0f0 and other helpers, ORs incoming
flags into pending fields and accumulates an amount at +0x14:

~~~c
param_1[6] = param_1[6] | param_3;
param_1[7] = param_1[7] | param_4;
param_1[5] = (int)(param_2 + (float)param_1[5]);
return 1;
~~~

The int casts above are decompiler storage artifacts: MOVSS/ADDSS-style
float operations must govern any reconstruction. This entry point does not
by itself establish when hit points are finally reduced. Naming +0x14 as
current HP would be unsupported. A special branch creates an effect and
returns zero rather than following the ordinary acceptance path.

For an independent design, keep eligibility, cooldown gates, scaling and
damage application as explicit stages. Still unresolved: player damage,
all flags and type IDs, callback cancellation rules, final HP/death handling,
projectile collision and runtime validation.

## Player wrapper

[00819e70](../evidence/repaired/00819e70.txt) registers the Lua method named
TakeDamage; [00846fb0](../evidence/repaired/00846fb0.txt) reads a number,
two integer arguments, a source-like userdata and an integer cooldown, then
calls the player object's native virtual dispatch and pushes its boolean result.
The reference facade is [PlayerCombat.cs](../reference/IsaacReference/Original/PlayerCombat.cs).
This establishes the wrapper contract, not the native player HP/death policy.

## Queue helpers and callback

[00680d60](../evidence/repaired/00680d60.txt) initializes an event record, and
[0068f0f0](../evidence/repaired/0068f0f0.txt) copies a 0x38-byte record to a
vector's end, falling back to capacity growth when full. The entity entry point
accumulates amount and flags after appending. Cooldown writes happen before
callback rejection and are retained even if acceptance fails.

[00800e30](../evidence/repaired/00800e30.txt) checks a callback-enabled bit,
invokes a Lua helper, and treats a non-nil result as a boolean acceptance value.
Absent an enabled callback or a non-nil result, it returns true. The damage
amount is passed in XMM2; the inferred C prototype omits that argument. The
managed core supplies an explicit acceptance delegate rather than recreating
the Lua environment. HP/death consumption and original cooldown-decrement
sites remain unresolved.
