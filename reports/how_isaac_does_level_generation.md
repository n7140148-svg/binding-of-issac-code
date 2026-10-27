# Level generation: recovered orchestration

Additional layout helpers and the original single-cell reference model are
available in [the code delivery](FINAL_CODE_2026-10-27.md).

2026-10-27. Partial static reconstruction, not runtime validation.
Target identity is recorded in [manifest.json](../evidence/manifest.json).

## Evidence correction

The original Ghidra database marks 0x0095e330 as no-return, although its
[export](../evidence/focused/0095e330.txt) has a returning logging path.
This cut 0x00711e60 off at its ordinary "Level::Init" message and cut
0x0070e330 off at "generate...". The baseline exports are retained under
evidence/focused. RepairLoggerFlow.java clears the annotation in memory,
disassembles the continuations, and recomputes selected function bodies.
The Ghidra run used -readOnly; its log confirms database changes were discarded.

| Function | Baseline Body Bytes | Recovered Body Bytes |
| --- | --- | --- |
| 0x00711e60 | 740 | 3963 |
| 0x0070e330 | 2395 | 3628 |
| 0x007103c0 | 937 | 1571 |

These are analyzed address counts, not proof of a complete original function.
Read the recovered assembly alongside C; inferred types remain imperfect.

## Confirmed main chain

[0x00711e60](../evidence/repaired/00711e60.txt), provisionally Level_Init,
contains "Level::Init m_Stage %d, m_StageType %d Seed %u". It initializes
state, advances an RNG at level +0x18164, then dispatches generation based
on stage and run flags. Its default path calls
[0x0070e330](../evidence/repaired/0070e330.txt). A path guarded by stage < 7
and a run flag calls [0x007103c0](../evidence/repaired/007103c0.txt), whose
"Invalid backwards path stage ID" diagnostic identifies a distinct backwards
generation path. Other branches call 0x00710a20, 0x0071aa70, 0x0071d540 or
0x00717520; their complete algorithms are not explained here.

The ordinary orchestrator 0x0070e330:

1. Computes generation parameters with stage/run-dependent adjustments.
2. Clears prior generation state and invokes 0x0090e760, a candidate layout
   generator, at assembly address 0x0070eec9.
3. Rejects a result when its usability flag is false, logging
   "generated level is not usable".
4. Checks a dead-end count against a target, logging
   "not enough dead ends (%d/%d)" on failure. After more than ten attempts,
   every fifth failed attempt can increase the size parameter while below 64.
5. Logs "placing rooms...", clears a room lookup region to -1, and calls
   0x00706f00. A false result clears state and repeats generation.
6. Applies stage-specific follow-up operations and logs the number of loops.

Recovered C shows the placement retry directly:

~~~c
cVar3 = FUN_00706f00(local_408,local_40c,local_420);
if (cVar3 == '\0') {
  FUN_007062e0();
  puVar17 = puVar18;
  goto LAB_0070ec90;
}
~~~

A counter logs severity 3 after more than 100 attempts; the logger returns,
so this is not evidence of a hard retry cap or process termination.

## Design reference and open work

The observed architecture separates a candidate layout, structural acceptance
checks and room placement, with retries around the whole process. PixelAbyss
can independently adopt that separation and bounded failure handling.
Its implementation should choose its own actual retry cap.

## Room restrictions

The focused exports isolate the placement predicates. 00910d10 validates each
shape offset against the 13x13 bounds, rejects occupied cells and skips a
candidate when it matches the current room. 00910dd0 tests door slots, maps the
candidate through 009101d0, and rejects missing, incompatible or already-used
connections. 00910ec0 allocates a room record, stores its generation index,
and writes every shape cell into the room lookup table. The reference core is
RoomRestrictions.cs; the native shape table and full template catalog remain
unresolved.

## Layout Helpers Recovered

[0090e760](../evidence/repaired/0090e760.txt) clears 169 grid slots, calls initial
growth 00911060 and dead-end classification 00910820, then tries up to five
0090fd90 additions when there are too few dead ends. It sorts the final list
by descending room-record +0x40, a generation depth established by child
construction in 00911690.

[00911060](../evidence/repaired/00911060.txt) processes a deque of room indices.
Small layouts give the start room a two-or-three expansion budget; non-start
rooms sum four RNG low bits. Placement checks occur before the budget is tested
after an insertion. Accepted rooms go to the deque's back when RNG % 3 == 0,
otherwise its front. Candidate count and neighbor constraints can stop growth.
Some configurations permit an extra connection with probability 1/10.

[00911690](../evidence/repaired/00911690.txt) enumerates eight door slots and a
13-entry shape/probability table, checks shape occupancy, and initializes child
depth to parent depth plus one. [009106c0](../evidence/repaired/009106c0.txt)
marks non-start records with fewer than two relevant neighbors, then clears the
mark on their connecting parents. [00910820](../evidence/repaired/00910820.txt)
collects those marks. This is shape-aware bookkeeping, not simply counting
four neighboring single-cell rooms.

[00706f00](../evidence/repaired/00706f00.txt) is exported and calls configuration
queries, shape/door helpers, and special-room placement. It includes explicit
boss-room lookup failures and returns failure to its outer retry loop.

Unresolved: complete candidate occupancy/connection rules, the shape table's
full semantics, template data and selection, all special generation branches,
later seed scheduling, and runtime parity. The original model in
[FloorGenerator.cs](../reference/IsaacReference/Original/FloorGenerator.cs)
implements a deterministic single-cell tree with its own bounded retries and
room assignments. Its tests establish its own invariants only.
