# One enemy-wave spawning path

2026-10-27. Partial static analysis of
[0x0049e3b0](../gamelogic_out/gamelogic/FUN_0049e3b0__0049e3b0__gamelogic.txt).
The diagnostic "No enemy wave found for Gideon (difficulty: %d)" directly
identifies this as a Gideon wave helper. Proposed name: Gideon_SpawnWave.
The target binary identity is in [manifest.json](../evidence/manifest.json).

Observed on the branch where entity +0x314 is zero:

1. Select a difficulty from a small table indexed by a capped entity field.
2. Count room grid entries of a particular type; the loop bounds grid indices
   below 0x1c0. The exact grid type's name has not been validated.
3. Advance an entity RNG at +0x334 and use a derived stream with shifts
   (5,9,7), whose constants are recorded in pe-constants.json.
4. Request a candidate wave through 0x007e7770, process its cells and select
   entries through 0x007e7c20. A type-specific condition can reject the
   prepared wave; the visible outer retry counter is bounded at ten.
5. Convert accepted grid positions into world positions and call 0x00422e20
   with type/variant/subtype-like values and a per-spawn seed. Then invoke
   the created object's virtual slot +0x0c and update room bookkeeping.

The final spawn is visible in the decompiled C:

~~~c
piVar9 = (int *)FUN_00422e20(*(undefined4 *)((int)local_4c + -4),
    *(undefined2 *)local_4c, local_78, &DAT_00c02fec, local_60,
    *(undefined2 *)((int)local_4c + 2), uVar5);
~~~

The inferred argument meanings require inspection of the factory itself.
The zero-seed diagnostic paths in this older export also suffer from the
logger's no-return annotation; see the level report for the correction.

## Spawn Helpers

[007e7770](../evidence/repaired/007e7770.txt) queries 007e7180 with one type,
then queries again with an alternate type if the first result is null. The
inferred void return is misleading: callers use EAX as a selected room pointer.
[007e7c20](../evidence/repaired/007e7c20.txt) selects the first cumulative weight
strictly above sample * total and falls back to its first entry on exhaustion.
[00422e20](../evidence/repaired/00422e20.txt) forwards its seven arguments and
one final zero to factory 006d0ca0. Exact factory types remain open.

## One Animation-Driven Enemy Update

[0044e9a0](../evidence/repaired/0044e9a0.txt) is an anonymous enemy update,
not a confirmed generic fly AI. Entity identity is unresolved. Its state at
+0xab4 starts at zero, transitions to four and resets timer +0x360. The
ordinary branch applies damping bits 0x3f59999a (0.85f) at +0x2c4 and
decrements a local cooldown by the integer frame difference.

State four evaluates scream (16), directional attack (8), summon (13), and
airborne attack (6) branches in order. Decisions depend on flags, room state,
animation/target helpers and MT19937 draws; the reference model takes these
decisions as host inputs rather than claiming to reproduce their predicates.

State eight chooses Attack2Left/Up/Right/Down using the dominant target axis.
Equal absolute axes choose horizontal. Shoot triggers a projectile-like factory
call; animation completion returns to four. State 13 recognizes Skin Pull and
Shoot; it spawns four minus existing minions when the count is below four,
then returns to four on completion. State 16 plays Scream, and completion sets
two global fields and returns to four. State six includes movement while
airborne, a FlyDown phase after a timer test, and landing effects/damage calls.

[EnemyAnimationModel.cs](../reference/IsaacReference/Original/EnemyAnimationModel.cs)
is a host-driven subset with explicit event outputs. It omits the original
eligibility schedule, animation data, global side effects, velocities, room
changes and spawn/projectile internals. These are remaining reverse-engineering
targets. This pass explains one wave path and one update path; it does not
recover every enemy AI or the entire combat engine.
