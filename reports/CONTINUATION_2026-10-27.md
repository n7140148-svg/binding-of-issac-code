# Reverse engineering continuation, 2026-10-27

## Results and evidence boundary

Repository baseline: ecffed287126fef89a5f2b66bbc2bccb81298869.
Binary SHA-256: 530b4d2accef833b8dbf6f1a9f781fe1e051c1916ca5acdb579df05a34640627.
This pass reviews the handoff, audits its exports, and continues gameplay
analysis using the existing Ghidra 12.1.4 database on this machine.
The game was not executed. These are ordinary Ghidra/static-file findings,
not REA Evidence records. The REA diagnostic found missing Codex registration;
no client configuration or analysis engine installation was performed.

26 new export records cover 18 unique functions: 18 baseline exports and
8 exports after a temporary logger-flow correction. Each records its
executable hash; [manifest.json](../evidence/manifest.json) adds export and
script hashes. The source database's annotations were not saved: all runs
used -readOnly -noanalysis, and the repair log confirms changes were discarded.

| Handoff Question | Result | Explanation |
| --- | --- | --- |
| Item selection | Main chain located; special cases partial | [item pools](how_isaac_does_item_pools.md) |
| Level/room generation | Retry and placement orchestration recovered; graph algorithm open | [level generation](how_isaac_does_level_generation.md) |
| Enemy AI | One wave spawning path traced; state machines open | [enemy waves](how_isaac_does_enemy_waves.md) |
| Combat | Non-player damage acceptance traced; final HP/death processing open | [combat](how_isaac_does_combat.md) |
| RNG/seeds | Xorshift, MT19937, float conversion and shuffling explained; seed lifecycle open | [RNG](how_isaac_does_rng.md) |
| Semantic index | Added without modifying raw legacy index | [gl_INDEX.md](../gl_INDEX.md) |

This is a continuation, not completion of every handoff criterion.
The archive art/audio stream and independent PixelAbyss code are outside
this pass, following SCOPE.md.

## Review findings

1. Incorrect no-return metadata on logger 0x0095e330 removed reachable code
   from analyzed bodies and C output. Temporary correction recovered level
   generation after progress messages and the pool selector's sequential
   fallback after repick exhaustion. Preserve baseline/repaired distinctions;
   a C export alone is not proof of coverage.
2. The shipped discovery script does not compile against installed Ghidra:
   pcode classes lack imports, and ReferenceManager.getReferencesTo returns
   an iterator, not Reference[]. Both are fixed and javac-checked.
3. Its CSV writer does not quote commas in C++ names or keyword fields.
   A normal CSV parser silently shifts columns. Future writes are quoted
   and flushed per record. The legacy parser anchors on numeric size and tag,
   preserving ambiguous keyword payload rather than inventing boundaries.
4. The legacy CSV ends with an incomplete line containing only "0" and stops
   before the full candidate set described in the handoff. Its 1451 valid
   rows accompany 1282 function exports from 0x00401f50 to 0x005eff40.
   1279 contain C; 157 additional files are empty. Seven indexed nonzero-size
   entries lack matching exports, two exports have no valid index row, and
   the final export lacks its pcode marker and usable C. Exact lists and
   hashes are in [export-audit.json](export-audit.json).
5. Gameplay RNG cannot be established by the archive PRNG script mentioned
   in AI_HANDOVER.md. The binary has distinct xorshift and MT19937 code.
   RandomFloat's multiplier is slightly below 2^-32. Register arguments and
   float stores also require more care than the decompiled C suggests.

## Validation

- Three Node regression tests pass for malformed names, truncated rows,
  ambiguous keywords, missing sections and direct-call extraction.
- All four Ghidra scripts compile against installed Ghidra/JDK jars.
- Focused exports, string discovery and temporary flow repair executed
  successfully against the existing analyzed program.
- All 26 exported records match the binary SHA-256 and have C output.
- PE constants were read through section-backed VA-to-file mappings; raw
  bytes, offsets and decoded values are retained in pe-constants.json.
- No gameplay runtime parity tests have been performed.

## Next bounded investigations

1. Trace 0x0090e760 and 0x00706f00 for graph growth, room choice, shapes and
   doors. Apply the logger correction where appropriate.
2. Trace 0x008028d0, 0x00802a20 and 0x006fe950 for pool callbacks, final
   overrides and eligibility. Complete flags and special cases.
3. Trace 0x00680d60, 0x0068f0f0 and the consumer of entity +0x14 for damage
   application/death, then locate the separate player damage path.
4. Trace 0x007e7770, 0x007e7c20 and 0x00422e20 for waves and spawn arguments,
   then identify at least one full enemy update state machine.
5. Recover start-seed conversion, per-system initialization and save/load
   rules before claiming replay compatibility.

Reproduction: [tools/analysis/README.md](../tools/analysis/README.md).
