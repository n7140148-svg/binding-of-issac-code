# Gameplay function map

Updated 2026-10-27. Semantic names are analyst proposals; database symbols
have not been renamed. Target identity: [manifest.json](evidence/manifest.json).

| Address | Proposed Name | Evidence | Boundary |
| --- | --- | --- | --- |
| 0x00701230 | ItemPool_GetCollectible | [recovered](evidence/repaired/00701230.txt) | Diagnostic identifies role; special cases partial |
| 0x00700c60 | ItemPool_SelectWeightedEntry | [recovered](evidence/repaired/00700c60.txt) | Weights, depletion and fallback traced |
| 0x007034d0 | ItemPool_ParseXml | [recovered](evidence/repaired/007034d0.txt) | Attributes parsed; mod merging partial |
| 0x00702950 | ItemPool_Initialize | [baseline](evidence/focused/00702950.txt) | Calls parser; full initialization open |
| 0x00704ad0 | ItemPool_SelectAlternatePool | [baseline](evidence/focused/00704ad0.txt) | Provisional; calling effect unidentified |
| 0x005b3c80 | Player_RerollInventory | [baseline](evidence/focused/005b3c80.txt) | Replacement caller chain traced |
| 0x007a7d50 | RNG_RandomInt | [recovered](evidence/repaired/007a7d50.txt) | Xorshift and modulo confirmed |
| 0x007a7db0 | RNG_RandomFloat | [recovered](evidence/repaired/007a7db0.txt) | Exact float conversion confirmed |
| 0x007a7e20 | RNG_AdvanceState | [baseline](evidence/focused/007a7e20.txt) | Transition confirmed; return contract open |
| 0x006c3d50 | GlobalMT_Seed | [baseline](evidence/focused/006c3d50.txt) | MT19937 initialization identified |
| 0x006c3d90 | GlobalMT_Next | [baseline](evidence/focused/006c3d90.txt) | MT19937 twist and temper identified |
| 0x005b6370 | ShuffleU32_Fastcall | [baseline](evidence/focused/005b6370.txt) | Fisher-Yates structure confirmed |
| 0x005b6400 | ShuffleU32_Thiscall | [baseline](evidence/focused/005b6400.txt) | Same structure, different convention |
| 0x00711e60 | Level_Init | [recovered](evidence/repaired/00711e60.txt) | Generation dispatch traced |
| 0x0070e330 | Level_GenerateOrdinary | [recovered](evidence/repaired/0070e330.txt) | Acceptance and placement orchestration traced |
| 0x007103c0 | Level_GenerateBackwards | [recovered](evidence/repaired/007103c0.txt) | Diagnostic identifies path; algorithm partial |
| 0x00684bb0 | Entity_TakeDamage | [baseline](evidence/focused/00684bb0.txt) | Non-player damage acceptance traced |
| 0x0049e3b0 | Gideon_SpawnWave | [legacy](gamelogic_out/gamelogic/FUN_0049e3b0__0049e3b0__gamelogic.txt) | Spawning path partial; full AI open |
| 0x0095e330 | Log_Print | [baseline](evidence/focused/0095e330.txt) | Returning logger; no-return annotation incorrect |

## Additional Exports and Code

| Address | Proposed Name | Boundary |
| --- | --- | --- |
| 0x0093df80 | Seed_EncodeString | Alphabet, XOR and checksum traced |
| 0x0093e080 | Seed_ParseString | Strict format/checksum validation |
| 0x0093e220 | Seeds_InitializeStart | Fourteen stage slots and extra seed |
| 0x00705f30 | Seeds_GetStageSeed | Identified by Lua registration |
| 0x006c4560 | Seeds_GetNextSeed | Advances stream, result in EAX |
| 0x0090e760 | Layout_Generate | Grid reset, dead-end retries/sorting |
| 0x00911060 | Layout_GrowFrontier | Deque and expansion budgets traced |
| 0x00911690 | Layout_GetNeighborCandidates | Shape/door-dependent; partial |
| 0x00910fd0 | Layout_CountRelevantNeighbors | Shape-sensitive neighbor exclusions |
| 0x009106c0 | Layout_MarkDeadEnds | Marking and parent clearing |
| 0x00910820 | Layout_CollectDeadEnds | Collects room marker +0x3c |
| 0x0090fd90 | Layout_TryAddDeadEnd | First acceptable extension |
| 0x00706f00 | Level_PlaceRooms | Exported; template rules partial |
| 0x00680d60 | DamageEvent_Initialize | Record initialization |
| 0x0068f0f0 | DamageEvent_Append | Vector append, stride 0x38 |
| 0x00800e30 | DamageCallback_Accept | Lua boolean with default true |
| 0x007e7770 | RoomConfig_QueryWithFallback | Alternate type retry |
| 0x007e7c20 | Spawn_PickWeightedEntry | Cumulative weights and first fallback |
| 0x00422e20 | EntityFactory_Forward | Forwards seven arguments and zero |
| 0x0044e9a0 | Enemy_UpdateAnimationStates | Anonymous identity; selected paths traced |

These functions are in evidence/repaired/ADDRESS.txt; file hashes and additional
registration/helper exports are in [manifest.json](evidence/manifest.json).
Runnable code and evidence boundaries: [reference](reference/README.md) and
[delivery report](reports/FINAL_CODE_2026-10-27.md).

Read [the continuation report](reports/CONTINUATION_2026-10-27.md) for
coverage, caveats, validation and next targets. The full legacy-export audit
and direct-call lists are in [export-audit.json](reports/export-audit.json).
