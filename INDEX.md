# Isaac 逆向函数索引（Ghidra 反编译）

> 自动生成 · 共 **1205** 个函数文件 · 源目录 `isaac_reverse/ghidra_out/`

> 范围：资源/归档/加解密子系统（地址段 0x00990000–0x009D0000）。

> 音频/贴图（mode-0x02 XOR/ISAAC 美术资源子流）按用户要求不做。


## 子系统统计

| 子系统 | 函数数 | 含反编译C | 汇编行数 |
|---|---|---|---|
| other | 1195 | 1134 | 121990 |
| archive-loader | 2 | 1 | 132 |
| mode0x02-readblock | 2 | 1 | 564 |
| isaac-randinit | 2 | 1 | 396 |
| archive-aux | 1 | 1 | 65 |
| archive-init | 1 | 1 | 76 |
| archive-io | 1 | 1 | 65 |
| isaac-keygen | 1 | 1 | 69 |

## 全量函数表

| 地址 | 名 | tag | 子系统 | 反编译C | 汇编行 | 签名 |
|---|---|---|---|---|---|---|
| 0x00409b40 | FUN_00409b40 | caller | other | — | 5515 | `` |
| 0x0041b9c0 | FUN_0041b9c0 | caller | other | — | 528 | `` |
| 0x0041ca20 | FUN_0041ca20 | caller | other | — | 635 | `` |
| 0x0066da20 | FUN_0066da20 | caller | other | — | 4486 | `` |
| 0x00671820 | FUN_00671820 | caller | other | — | 772 | `` |
| 0x006722b0 | FUN_006722b0 | caller | other | — | 2405 | `` |
| 0x00674810 | FUN_00674810 | caller | other | — | 520 | `` |
| 0x00674f20 | FUN_00674f20 | caller | other | — | 1007 | `` |
| 0x006f3cd0 | FUN_006f3cd0 | caller | other | — | 2816 | `` |
| 0x006f6080 | FUN_006f6080 | caller | other | — | 1548 | `` |
| 0x006f74d0 | FUN_006f74d0 | caller | other | — | 387 | `` |
| 0x006f8de0 | FUN_006f8de0 | caller | other | — | 823 | `` |
| 0x006fa550 | FUN_006fa550 | caller | other | — | 839 | `` |
| 0x006fb340 | FUN_006fb340 | caller | other | — | 376 | `` |
| 0x006fb850 | FUN_006fb850 | caller | other | — | 1879 | `` |
| 0x006fd040 | FUN_006fd040 | caller | other | — | 503 | `` |
| 0x006fd720 | FUN_006fd720 | caller | other | — | 1066 | `` |
| 0x007034d0 | FUN_007034d0 | caller | other | — | 803 | `` |
| 0x0079fe00 | FUN_0079fe00 | caller | other | — | 1880 | `` |
| 0x007e4070 | FUN_007e4070 | caller | other | — | 137 | `` |
| 0x007e5c20 | FUN_007e5c20 | caller | other | — | 787 | `` |
| 0x007e6880 | FUN_007e6880 | caller | other | — | 309 | `` |
| 0x007e6cb0 | FUN_007e6cb0 | caller | other | — | 218 | `` |
| 0x007ee6a0 | FUN_007ee6a0 | caller | other | — | 436 | `` |
| 0x0086c570 | FUN_0086c570 | caller | other | — | 955 | `` |
| 0x0086f2b0 | FUN_0086f2b0 | caller | other | — | 1124 | `` |
| 0x00875810 | FUN_00875810 | caller | other | — | 1406 | `` |
| 0x0087c340 | FUN_0087c340 | caller | other | — | 444 | `` |
| 0x0087fbe0 | FUN_0087fbe0 | caller | other | — | 192 | `` |
| 0x00888220 | FUN_00888220 | caller | other | — | 750 | `` |
| 0x0088c100 | FUN_0088c100 | caller | other | — | 385 | `` |
| 0x0088d3f0 | FUN_0088d3f0 | caller | other | — | 2100 | `` |
| 0x008b1560 | FUN_008b1560 | caller | other | — | 2131 | `` |
| 0x008b64d0 | FUN_008b64d0 | caller | other | — | 1462 | `` |
| 0x008b7d10 | FUN_008b7d10 | caller | other | — | 308 | `` |
| 0x008e8330 | FUN_008e8330 | caller | other | — | 3192 | `` |
| 0x0090c930 | FUN_0090c930 | caller | other | — | 902 | `` |
| 0x0091f0a0 | FUN_0091f0a0 | caller | other | — | 311 | `` |
| 0x00940030 | FUN_00940030 | caller | other | — | 461 | `` |
| 0x0095e330 | FUN_0095e330 | callee | other | — | 155 | `` |
| 0x00963120 | FUN_00963120 | callee | other | — | 98 | `` |
| 0x00963880 | FUN_00963880 | caller | other | ✅ | 337 | `void FUN_00963880(undefined4 param_1,int param_2,ushort param_3)` |
| 0x00963db0 | FUN_00963db0 | callee | archive-aux | ✅ | 65 | `` |
| 0x00963e70 | FUN_00963e70 | callee | other | — | 83 | `` |
| 0x00963e70 | FUN_00963e70 | caller | other | ✅ | 83 | `undefined4 __thiscall FUN_00963e70(int param_1,int param_2,undefined4 *param_3)` |
| 0x00964750 | FUN_00964750 | caller | other | — | 279 | `` |
| 0x00965cc0 | FUN_00965cc0 | caller | other | — | 411 | `` |
| 0x0096bb90 | FUN_0096bb90 | caller | other | — | 568 | `` |
| 0x00990000 | FUN_00990000 | scan | other | ✅ | 8 | `void FUN_00990000(void)` |
| 0x00990020 | FUN_00990020 | scan | other | ✅ | 8 | `void FUN_00990020(void)` |
| 0x00990040 | FUN_00990040 | scan | other | ✅ | 8 | `void FUN_00990040(void)` |
| 0x00990060 | FUN_00990060 | scan | other | ✅ | 18 | `void FUN_00990060(undefined8 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x009900b0 | FUN_009900b0 | scan | other | ✅ | 8 | `void FUN_009900b0(void)` |
| 0x009900d0 | FUN_009900d0 | scan | other | ✅ | 16 | `void FUN_009900d0(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x00990110 | FUN_00990110 | scan | other | ✅ | 8 | `void FUN_00990110(void)` |
| 0x00990130 | FUN_00990130 | scan | other | ✅ | 8 | `void FUN_00990130(void)` |
| 0x00990150 | FUN_00990150 | scan | other | ✅ | 8 | `void FUN_00990150(void)` |
| 0x00990170 | FUN_00990170 | scan | other | ✅ | 8 | `void FUN_00990170(void)` |
| 0x00990190 | FUN_00990190 | scan | other | ✅ | 8 | `void FUN_00990190(void)` |
| 0x009901b0 | FUN_009901b0 | scan | other | ✅ | 8 | `void FUN_009901b0(void)` |
| 0x009901d0 | FUN_009901d0 | scan | other | ✅ | 8 | `void FUN_009901d0(void)` |
| 0x009901f0 | FUN_009901f0 | scan | other | ✅ | 8 | `void FUN_009901f0(void)` |
| 0x00990210 | FUN_00990210 | scan | other | ✅ | 8 | `void FUN_00990210(void)` |
| 0x00990230 | FUN_00990230 | scan | other | ✅ | 8 | `void FUN_00990230(void)` |
| 0x00990250 | FUN_00990250 | scan | other | ✅ | 8 | `void FUN_00990250(void)` |
| 0x00990270 | FUN_00990270 | scan | other | ✅ | 20 | `void FUN_00990270(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x009902c0 | FUN_009902c0 | scan | other | ✅ | 8 | `void FUN_009902c0(void)` |
| 0x009902e0 | FUN_009902e0 | scan | other | ✅ | 18 | `void FUN_009902e0(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x00990330 | FUN_00990330 | scan | other | ✅ | 8 | `void FUN_00990330(void)` |
| 0x00990350 | FUN_00990350 | scan | other | ✅ | 8 | `void FUN_00990350(void)` |
| 0x00990370 | FUN_00990370 | scan | other | ✅ | 8 | `void FUN_00990370(void)` |
| 0x00990390 | FUN_00990390 | scan | other | ✅ | 8 | `void FUN_00990390(void)` |
| 0x009903b0 | FUN_009903b0 | scan | other | ✅ | 8 | `void FUN_009903b0(void)` |
| 0x009903d0 | FUN_009903d0 | scan | other | ✅ | 8 | `void FUN_009903d0(void)` |
| 0x009903f0 | FUN_009903f0 | scan | other | ✅ | 8 | `void FUN_009903f0(void)` |
| 0x00990410 | FUN_00990410 | scan | other | ✅ | 8 | `void FUN_00990410(void)` |
| 0x00990430 | FUN_00990430 | scan | other | ✅ | 8 | `void FUN_00990430(void)` |
| 0x00990450 | FUN_00990450 | scan | other | ✅ | 10 | `void FUN_00990450(void)` |
| 0x00990480 | FUN_00990480 | scan | other | ✅ | 10 | `void FUN_00990480(void)` |
| 0x009904b0 | FUN_009904b0 | scan | other | ✅ | 10 | `void FUN_009904b0(void)` |
| 0x009904e0 | FUN_009904e0 | scan | other | ✅ | 10 | `void FUN_009904e0(void)` |
| 0x00990510 | FUN_00990510 | scan | other | ✅ | 8 | `void FUN_00990510(void)` |
| 0x00990530 | FUN_00990530 | scan | other | ✅ | 10 | `void FUN_00990530(void)` |
| 0x00990560 | FUN_00990560 | scan | other | ✅ | 8 | `void FUN_00990560(void)` |
| 0x00990580 | FUN_00990580 | scan | other | ✅ | 8 | `void FUN_00990580(void)` |
| 0x009905a0 | FUN_009905a0 | scan | other | ✅ | 10 | `void FUN_009905a0(void)` |
| 0x009905d0 | FUN_009905d0 | scan | other | ✅ | 8 | `void FUN_009905d0(void)` |
| 0x009905f0 | FUN_009905f0 | scan | other | ✅ | 8 | `void FUN_009905f0(void)` |
| 0x00990610 | FUN_00990610 | scan | other | ✅ | 8 | `void FUN_00990610(void)` |
| 0x00990630 | FUN_00990630 | scan | other | ✅ | 8 | `void FUN_00990630(void)` |
| 0x00990650 | FUN_00990650 | scan | other | ✅ | 8 | `void FUN_00990650(void)` |
| 0x00990670 | FUN_00990670 | scan | other | ✅ | 8 | `void FUN_00990670(void)` |
| 0x00990690 | FUN_00990690 | scan | other | ✅ | 8 | `void FUN_00990690(void)` |
| 0x009906b0 | FUN_009906b0 | scan | other | ✅ | 8 | `void FUN_009906b0(void)` |
| 0x009906d0 | FUN_009906d0 | scan | other | ✅ | 8 | `void FUN_009906d0(void)` |
| 0x009906f0 | FUN_009906f0 | scan | other | ✅ | 8 | `void FUN_009906f0(void)` |
| 0x00990710 | FUN_00990710 | scan | other | ✅ | 8 | `void FUN_00990710(void)` |
| 0x00990730 | FUN_00990730 | scan | other | ✅ | 8 | `void FUN_00990730(void)` |
| 0x00990750 | FUN_00990750 | scan | other | ✅ | 8 | `void FUN_00990750(void)` |
| 0x00990770 | FUN_00990770 | scan | other | ✅ | 8 | `void FUN_00990770(void)` |
| 0x00990790 | FUN_00990790 | scan | other | ✅ | 8 | `void FUN_00990790(void)` |
| 0x009907b0 | FUN_009907b0 | scan | other | ✅ | 8 | `void FUN_009907b0(void)` |
| 0x009907d0 | FUN_009907d0 | scan | other | ✅ | 8 | `void FUN_009907d0(void)` |
| 0x009907f0 | FUN_009907f0 | scan | other | ✅ | 8 | `void FUN_009907f0(void)` |
| 0x00990810 | FUN_00990810 | scan | other | ✅ | 10 | `void FUN_00990810(void)` |
| 0x00990840 | FUN_00990840 | scan | other | ✅ | 10 | `void FUN_00990840(void)` |
| 0x00990870 | FUN_00990870 | scan | other | ✅ | 8 | `void FUN_00990870(void)` |
| 0x00990890 | FUN_00990890 | scan | other | ✅ | 16 | `void FUN_00990890(undefined4 param_1,undefined8 param_2)` |
| 0x009908d0 | FUN_009908d0 | scan | other | ✅ | 16 | `void FUN_009908d0(undefined4 param_1,undefined8 param_2)` |
| 0x00990910 | FUN_00990910 | scan | other | ✅ | 16 | `void FUN_00990910(undefined4 param_1,undefined8 param_2)` |
| 0x00990950 | FUN_00990950 | scan | other | ✅ | 10 | `void FUN_00990950(void)` |
| 0x00990980 | FUN_00990980 | scan | other | ✅ | 10 | `void FUN_00990980(void)` |
| 0x009909b0 | FUN_009909b0 | scan | other | ✅ | 10 | `void FUN_009909b0(void)` |
| 0x009909e0 | FUN_009909e0 | scan | other | ✅ | 13 | `void FUN_009909e0(undefined4 param_1,undefined4 param_2)` |
| 0x00990a10 | FUN_00990a10 | scan | other | ✅ | 13 | `void FUN_00990a10(undefined4 param_1,undefined4 param_2)` |
| 0x00990a40 | FUN_00990a40 | scan | other | ✅ | 13 | `void FUN_00990a40(undefined4 param_1,undefined4 param_2)` |
| 0x00990a70 | FUN_00990a70 | scan | other | ✅ | 10 | `void FUN_00990a70(void)` |
| 0x00990aa0 | FUN_00990aa0 | scan | other | ✅ | 10 | `void FUN_00990aa0(void)` |
| 0x00990ad0 | FUN_00990ad0 | scan | other | ✅ | 10 | `void FUN_00990ad0(void)` |
| 0x00990b00 | FUN_00990b00 | scan | other | ✅ | 8 | `void FUN_00990b00(void)` |
| 0x00990b20 | FUN_00990b20 | scan | other | ✅ | 8 | `void FUN_00990b20(void)` |
| 0x00990b40 | FUN_00990b40 | scan | other | ✅ | 10 | `void FUN_00990b40(void)` |
| 0x00990b70 | FUN_00990b70 | scan | other | ✅ | 10 | `void FUN_00990b70(void)` |
| 0x00990ba0 | FUN_00990ba0 | scan | other | ✅ | 10 | `void FUN_00990ba0(void)` |
| 0x00990bd0 | FUN_00990bd0 | scan | other | ✅ | 10 | `void FUN_00990bd0(void)` |
| 0x00990c00 | FUN_00990c00 | scan | other | ✅ | 10 | `void FUN_00990c00(void)` |
| 0x00990c30 | FUN_00990c30 | scan | other | ✅ | 10 | `void FUN_00990c30(void)` |
| 0x00990c60 | FUN_00990c60 | scan | other | ✅ | 18 | `void FUN_00990c60(undefined4 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00990cb0 | FUN_00990cb0 | scan | other | ✅ | 18 | `void FUN_00990cb0(undefined4 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00990d00 | FUN_00990d00 | scan | other | ✅ | 18 | `void FUN_00990d00(undefined4 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00990d50 | FUN_00990d50 | scan | other | ✅ | 10 | `void FUN_00990d50(void)` |
| 0x00990d80 | FUN_00990d80 | scan | other | ✅ | 10 | `void FUN_00990d80(void)` |
| 0x00990db0 | FUN_00990db0 | scan | other | ✅ | 10 | `void FUN_00990db0(void)` |
| 0x00990de0 | FUN_00990de0 | scan | other | ✅ | 16 | `void FUN_00990de0(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x00990e20 | FUN_00990e20 | scan | other | ✅ | 16 | `void FUN_00990e20(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x00990e60 | FUN_00990e60 | scan | other | ✅ | 16 | `void FUN_00990e60(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x00990ea0 | FUN_00990ea0 | scan | other | ✅ | 10 | `void FUN_00990ea0(void)` |
| 0x00990ed0 | FUN_00990ed0 | scan | other | ✅ | 10 | `void FUN_00990ed0(void)` |
| 0x00990f00 | FUN_00990f00 | scan | other | ✅ | 10 | `void FUN_00990f00(void)` |
| 0x00990f30 | FUN_00990f30 | scan | other | ✅ | 8 | `void FUN_00990f30(void)` |
| 0x00990f50 | FUN_00990f50 | scan | other | ✅ | 8 | `void FUN_00990f50(void)` |
| 0x00990f70 | FUN_00990f70 | scan | other | ✅ | 10 | `void FUN_00990f70(void)` |
| 0x00990fa0 | FUN_00990fa0 | scan | other | ✅ | 10 | `void FUN_00990fa0(void)` |
| 0x00990fd0 | FUN_00990fd0 | scan | other | ✅ | 10 | `void FUN_00990fd0(void)` |
| 0x00991000 | FUN_00991000 | scan | other | ✅ | 10 | `void FUN_00991000(void)` |
| 0x00991030 | FUN_00991030 | scan | other | ✅ | 10 | `void FUN_00991030(void)` |
| 0x00991060 | FUN_00991060 | scan | other | ✅ | 10 | `void FUN_00991060(void)` |
| 0x00991090 | FUN_00991090 | scan | other | ✅ | 20 | `void FUN_00991090(undefined4 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x009910e0 | FUN_009910e0 | scan | other | ✅ | 20 | `void FUN_009910e0(undefined4 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x00991130 | FUN_00991130 | scan | other | ✅ | 20 | `void FUN_00991130(undefined4 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x00991180 | FUN_00991180 | scan | other | ✅ | 10 | `void FUN_00991180(void)` |
| 0x009911b0 | FUN_009911b0 | scan | other | ✅ | 10 | `void FUN_009911b0(void)` |
| 0x009911e0 | FUN_009911e0 | scan | other | ✅ | 10 | `void FUN_009911e0(void)` |
| 0x00991210 | FUN_00991210 | scan | other | ✅ | 18 | `void FUN_00991210(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x00991260 | FUN_00991260 | scan | other | ✅ | 18 | `void FUN_00991260(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x009912b0 | FUN_009912b0 | scan | other | ✅ | 18 | `void FUN_009912b0(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x00991300 | FUN_00991300 | scan | other | ✅ | 10 | `void FUN_00991300(void)` |
| 0x00991330 | FUN_00991330 | scan | other | ✅ | 10 | `void FUN_00991330(void)` |
| 0x00991360 | FUN_00991360 | scan | other | ✅ | 10 | `void FUN_00991360(void)` |
| 0x00991390 | FUN_00991390 | scan | other | ✅ | 8 | `void FUN_00991390(void)` |
| 0x009913b0 | FUN_009913b0 | scan | other | ✅ | 8 | `void FUN_009913b0(void)` |
| 0x009913d0 | FUN_009913d0 | scan | other | ✅ | 10 | `void FUN_009913d0(void)` |
| 0x00991400 | FUN_00991400 | scan | other | ✅ | 10 | `void FUN_00991400(void)` |
| 0x00991430 | FUN_00991430 | scan | other | ✅ | 10 | `void FUN_00991430(void)` |
| 0x00991460 | FUN_00991460 | scan | other | ✅ | 10 | `void FUN_00991460(void)` |
| 0x00991490 | FUN_00991490 | scan | other | ✅ | 10 | `void FUN_00991490(void)` |
| 0x009914c0 | FUN_009914c0 | scan | other | ✅ | 10 | `void FUN_009914c0(void)` |
| 0x009914f0 | FUN_009914f0 | scan | other | ✅ | 10 | `void FUN_009914f0(void)` |
| 0x00991520 | FUN_00991520 | scan | other | ✅ | 10 | `void FUN_00991520(void)` |
| 0x00991550 | FUN_00991550 | scan | other | ✅ | 10 | `void FUN_00991550(void)` |
| 0x00991580 | FUN_00991580 | scan | other | ✅ | 10 | `void FUN_00991580(void)` |
| 0x009915b0 | FUN_009915b0 | scan | other | ✅ | 10 | `void FUN_009915b0(void)` |
| 0x009915e0 | FUN_009915e0 | scan | other | ✅ | 10 | `void FUN_009915e0(void)` |
| 0x00991610 | FUN_00991610 | scan | other | ✅ | 10 | `void FUN_00991610(void)` |
| 0x00991640 | FUN_00991640 | scan | other | ✅ | 10 | `void FUN_00991640(void)` |
| 0x00991670 | FUN_00991670 | scan | other | ✅ | 10 | `void FUN_00991670(void)` |
| 0x009916a0 | FUN_009916a0 | scan | other | ✅ | 10 | `void FUN_009916a0(void)` |
| 0x009916d0 | FUN_009916d0 | scan | other | ✅ | 10 | `void FUN_009916d0(void)` |
| 0x00991700 | FUN_00991700 | scan | other | ✅ | 10 | `void FUN_00991700(void)` |
| 0x00991730 | FUN_00991730 | scan | other | ✅ | 10 | `void FUN_00991730(void)` |
| 0x00991760 | FUN_00991760 | scan | other | ✅ | 10 | `void FUN_00991760(void)` |
| 0x00991790 | FUN_00991790 | scan | other | ✅ | 10 | `void FUN_00991790(void)` |
| 0x009917c0 | FUN_009917c0 | scan | other | ✅ | 10 | `void FUN_009917c0(void)` |
| 0x009917f0 | FUN_009917f0 | scan | other | ✅ | 22 | `` |
| 0x00991850 | FUN_00991850 | scan | other | ✅ | 22 | `` |
| 0x009918b0 | FUN_009918b0 | scan | other | ✅ | 22 | `` |
| 0x00991910 | FUN_00991910 | scan | other | ✅ | 10 | `void FUN_00991910(void)` |
| 0x00991940 | FUN_00991940 | scan | other | ✅ | 10 | `void FUN_00991940(void)` |
| 0x00991970 | FUN_00991970 | scan | other | ✅ | 10 | `void FUN_00991970(void)` |
| 0x009919a0 | FUN_009919a0 | scan | other | ✅ | 20 | `` |
| 0x00991a00 | FUN_00991a00 | scan | other | ✅ | 20 | `` |
| 0x00991a60 | FUN_00991a60 | scan | other | ✅ | 20 | `` |
| 0x00991ac0 | FUN_00991ac0 | scan | other | ✅ | 10 | `void FUN_00991ac0(void)` |
| 0x00991af0 | FUN_00991af0 | scan | other | ✅ | 10 | `void FUN_00991af0(void)` |
| 0x00991b20 | FUN_00991b20 | scan | other | ✅ | 10 | `void FUN_00991b20(void)` |
| 0x00991b50 | FUN_00991b50 | scan | other | ✅ | 8 | `void FUN_00991b50(void)` |
| 0x00991b70 | FUN_00991b70 | scan | other | ✅ | 8 | `void FUN_00991b70(void)` |
| 0x00991b90 | FUN_00991b90 | scan | other | ✅ | 10 | `void FUN_00991b90(void)` |
| 0x00991bc0 | FUN_00991bc0 | scan | other | ✅ | 10 | `void FUN_00991bc0(void)` |
| 0x00991bf0 | FUN_00991bf0 | scan | other | ✅ | 10 | `void FUN_00991bf0(void)` |
| 0x00991c20 | FUN_00991c20 | scan | other | ✅ | 10 | `void FUN_00991c20(void)` |
| 0x00991c50 | FUN_00991c50 | scan | other | ✅ | 10 | `void FUN_00991c50(void)` |
| 0x00991c80 | FUN_00991c80 | scan | other | ✅ | 10 | `void FUN_00991c80(void)` |
| 0x00991cb0 | FUN_00991cb0 | scan | other | ✅ | 10 | `void FUN_00991cb0(void)` |
| 0x00991ce0 | FUN_00991ce0 | scan | other | ✅ | 10 | `void FUN_00991ce0(void)` |
| 0x00991d10 | FUN_00991d10 | scan | other | ✅ | 10 | `void FUN_00991d10(void)` |
| 0x00991d40 | FUN_00991d40 | scan | other | ✅ | 10 | `void FUN_00991d40(void)` |
| 0x00991d70 | FUN_00991d70 | scan | other | ✅ | 10 | `void FUN_00991d70(void)` |
| 0x00991da0 | FUN_00991da0 | scan | other | ✅ | 10 | `void FUN_00991da0(void)` |
| 0x00991dd0 | FUN_00991dd0 | scan | other | ✅ | 10 | `void FUN_00991dd0(void)` |
| 0x00991e00 | FUN_00991e00 | scan | other | ✅ | 10 | `void FUN_00991e00(void)` |
| 0x00991e30 | FUN_00991e30 | scan | other | ✅ | 10 | `void FUN_00991e30(void)` |
| 0x00991e60 | FUN_00991e60 | scan | other | ✅ | 10 | `void FUN_00991e60(void)` |
| 0x00991e90 | FUN_00991e90 | scan | other | ✅ | 8 | `void FUN_00991e90(void)` |
| 0x00991eb0 | FUN_00991eb0 | scan | other | ✅ | 10 | `void FUN_00991eb0(void)` |
| 0x00991ee0 | FUN_00991ee0 | scan | other | ✅ | 10 | `void FUN_00991ee0(void)` |
| 0x00991f10 | FUN_00991f10 | scan | other | ✅ | 10 | `void FUN_00991f10(void)` |
| 0x00991f40 | FUN_00991f40 | scan | other | ✅ | 10 | `void FUN_00991f40(void)` |
| 0x00991f70 | FUN_00991f70 | scan | other | ✅ | 10 | `void FUN_00991f70(void)` |
| 0x00991fa0 | FUN_00991fa0 | scan | other | ✅ | 10 | `void FUN_00991fa0(void)` |
| 0x00991fd0 | FUN_00991fd0 | scan | other | ✅ | 10 | `void FUN_00991fd0(void)` |
| 0x00992000 | FUN_00992000 | scan | other | ✅ | 8 | `void FUN_00992000(void)` |
| 0x00992020 | FUN_00992020 | scan | other | ✅ | 10 | `void FUN_00992020(void)` |
| 0x00992050 | FUN_00992050 | scan | other | ✅ | 10 | `void FUN_00992050(void)` |
| 0x00992080 | FUN_00992080 | scan | other | ✅ | 10 | `void FUN_00992080(void)` |
| 0x009920b0 | FUN_009920b0 | scan | other | ✅ | 10 | `void FUN_009920b0(void)` |
| 0x009920e0 | FUN_009920e0 | scan | other | ✅ | 10 | `void FUN_009920e0(void)` |
| 0x00992110 | FUN_00992110 | scan | other | ✅ | 10 | `void FUN_00992110(void)` |
| 0x00992140 | FUN_00992140 | scan | other | ✅ | 10 | `void FUN_00992140(void)` |
| 0x00992170 | FUN_00992170 | scan | other | ✅ | 10 | `void FUN_00992170(void)` |
| 0x009921a0 | FUN_009921a0 | scan | other | ✅ | 10 | `void FUN_009921a0(void)` |
| 0x009921d0 | FUN_009921d0 | scan | other | ✅ | 10 | `void FUN_009921d0(void)` |
| 0x00992200 | FUN_00992200 | scan | other | ✅ | 10 | `void FUN_00992200(void)` |
| 0x00992230 | FUN_00992230 | scan | other | ✅ | 10 | `void FUN_00992230(void)` |
| 0x00992260 | FUN_00992260 | scan | other | ✅ | 10 | `void FUN_00992260(void)` |
| 0x00992290 | FUN_00992290 | scan | other | ✅ | 10 | `void FUN_00992290(void)` |
| 0x009922c0 | FUN_009922c0 | scan | other | ✅ | 10 | `void FUN_009922c0(void)` |
| 0x009922f0 | FUN_009922f0 | scan | other | ✅ | 10 | `void FUN_009922f0(void)` |
| 0x00992320 | FUN_00992320 | scan | other | ✅ | 10 | `void FUN_00992320(void)` |
| 0x00992350 | FUN_00992350 | scan | other | ✅ | 10 | `void FUN_00992350(void)` |
| 0x00992380 | FUN_00992380 | scan | other | ✅ | 10 | `void FUN_00992380(void)` |
| 0x009923b0 | FUN_009923b0 | scan | other | ✅ | 10 | `void FUN_009923b0(void)` |
| 0x009923e0 | FUN_009923e0 | scan | other | ✅ | 10 | `void FUN_009923e0(void)` |
| 0x00992410 | FUN_00992410 | scan | other | ✅ | 10 | `void FUN_00992410(void)` |
| 0x00992440 | FUN_00992440 | scan | other | ✅ | 10 | `void FUN_00992440(void)` |
| 0x00992470 | FUN_00992470 | scan | other | ✅ | 10 | `void FUN_00992470(void)` |
| 0x009924a0 | FUN_009924a0 | scan | other | ✅ | 10 | `void FUN_009924a0(void)` |
| 0x009924d0 | FUN_009924d0 | scan | other | ✅ | 10 | `void FUN_009924d0(void)` |
| 0x00992500 | FUN_00992500 | scan | other | ✅ | 10 | `void FUN_00992500(void)` |
| 0x00992530 | FUN_00992530 | scan | other | ✅ | 10 | `void FUN_00992530(void)` |
| 0x00992560 | FUN_00992560 | scan | other | ✅ | 10 | `void FUN_00992560(void)` |
| 0x00992590 | FUN_00992590 | scan | other | ✅ | 10 | `void FUN_00992590(void)` |
| 0x009925c0 | FUN_009925c0 | scan | other | ✅ | 10 | `void FUN_009925c0(void)` |
| 0x009925f0 | FUN_009925f0 | scan | other | ✅ | 10 | `void FUN_009925f0(void)` |
| 0x00992620 | FUN_00992620 | scan | other | ✅ | 10 | `void FUN_00992620(void)` |
| 0x00992650 | FUN_00992650 | scan | other | ✅ | 10 | `void FUN_00992650(void)` |
| 0x00992680 | FUN_00992680 | scan | other | ✅ | 10 | `void FUN_00992680(void)` |
| 0x009926b0 | FUN_009926b0 | scan | other | ✅ | 10 | `void FUN_009926b0(void)` |
| 0x009926e0 | FUN_009926e0 | scan | other | ✅ | 10 | `void FUN_009926e0(void)` |
| 0x00992710 | FUN_00992710 | scan | other | ✅ | 10 | `void FUN_00992710(void)` |
| 0x00992740 | FUN_00992740 | scan | other | ✅ | 10 | `void FUN_00992740(void)` |
| 0x00992770 | FUN_00992770 | scan | other | ✅ | 10 | `void FUN_00992770(void)` |
| 0x009927a0 | FUN_009927a0 | scan | other | ✅ | 10 | `void FUN_009927a0(void)` |
| 0x009927d0 | FUN_009927d0 | scan | other | ✅ | 8 | `void FUN_009927d0(void)` |
| 0x009927f0 | FUN_009927f0 | scan | other | ✅ | 10 | `void FUN_009927f0(void)` |
| 0x00992820 | FUN_00992820 | scan | other | ✅ | 10 | `void FUN_00992820(void)` |
| 0x00992850 | FUN_00992850 | scan | other | ✅ | 16 | `void FUN_00992850(undefined4 param_1,undefined8 param_2)` |
| 0x00992890 | FUN_00992890 | scan | other | ✅ | 16 | `void FUN_00992890(undefined4 param_1,undefined8 param_2)` |
| 0x009928d0 | FUN_009928d0 | scan | other | ✅ | 10 | `void FUN_009928d0(void)` |
| 0x00992900 | FUN_00992900 | scan | other | ✅ | 10 | `void FUN_00992900(void)` |
| 0x00992930 | FUN_00992930 | scan | other | ✅ | 14 | `void FUN_00992930(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x00992960 | FUN_00992960 | scan | other | ✅ | 8 | `void FUN_00992960(void)` |
| 0x00992980 | FUN_00992980 | scan | other | ✅ | 14 | `void FUN_00992980(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009929b0 | FUN_009929b0 | scan | other | ✅ | 14 | `void FUN_009929b0(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009929e0 | FUN_009929e0 | scan | other | ✅ | 8 | `void FUN_009929e0(void)` |
| 0x00992a00 | FUN_00992a00 | scan | other | ✅ | 8 | `void FUN_00992a00(void)` |
| 0x00992a20 | FUN_00992a20 | scan | other | ✅ | 18 | `void FUN_00992a20(undefined4 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00992a70 | FUN_00992a70 | scan | other | ✅ | 18 | `void FUN_00992a70(undefined4 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00992ac0 | FUN_00992ac0 | scan | other | ✅ | 10 | `void FUN_00992ac0(void)` |
| 0x00992af0 | FUN_00992af0 | scan | other | ✅ | 10 | `void FUN_00992af0(void)` |
| 0x00992b20 | FUN_00992b20 | scan | other | ✅ | 16 | `` |
| 0x00992b60 | FUN_00992b60 | scan | other | ✅ | 8 | `void FUN_00992b60(void)` |
| 0x00992b80 | FUN_00992b80 | scan | other | ✅ | 16 | `` |
| 0x00992bc0 | FUN_00992bc0 | scan | other | ✅ | 8 | `void FUN_00992bc0(void)` |
| 0x00992be0 | FUN_00992be0 | scan | other | ✅ | 20 | `void FUN_00992be0(undefined4 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x00992c30 | FUN_00992c30 | scan | other | ✅ | 20 | `void FUN_00992c30(undefined4 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x00992c80 | FUN_00992c80 | scan | other | ✅ | 10 | `void FUN_00992c80(void)` |
| 0x00992cb0 | FUN_00992cb0 | scan | other | ✅ | 10 | `void FUN_00992cb0(void)` |
| 0x00992ce0 | FUN_00992ce0 | scan | other | ✅ | 18 | `` |
| 0x00992d20 | FUN_00992d20 | scan | other | ✅ | 8 | `void FUN_00992d20(void)` |
| 0x00992d40 | FUN_00992d40 | scan | other | ✅ | 18 | `` |
| 0x00992d80 | FUN_00992d80 | scan | other | ✅ | 8 | `void FUN_00992d80(void)` |
| 0x00992da0 | FUN_00992da0 | scan | other | ✅ | 22 | `` |
| 0x00992e00 | FUN_00992e00 | scan | other | ✅ | 22 | `` |
| 0x00992e60 | FUN_00992e60 | scan | other | ✅ | 10 | `void FUN_00992e60(void)` |
| 0x00992e90 | FUN_00992e90 | scan | other | ✅ | 10 | `void FUN_00992e90(void)` |
| 0x00992ec0 | FUN_00992ec0 | scan | other | ✅ | 20 | `` |
| 0x00992f00 | FUN_00992f00 | scan | other | ✅ | 8 | `void FUN_00992f00(void)` |
| 0x00992f20 | FUN_00992f20 | scan | other | ✅ | 20 | `` |
| 0x00992f60 | FUN_00992f60 | scan | other | ✅ | 8 | `void FUN_00992f60(void)` |
| 0x00992f80 | FUN_00992f80 | scan | other | ✅ | 10 | `void FUN_00992f80(void)` |
| 0x00992fb0 | FUN_00992fb0 | scan | other | ✅ | 8 | `void FUN_00992fb0(void)` |
| 0x00992fd0 | FUN_00992fd0 | scan | other | ✅ | 10 | `void FUN_00992fd0(void)` |
| 0x00993000 | FUN_00993000 | scan | other | ✅ | 10 | `void FUN_00993000(void)` |
| 0x00993030 | FUN_00993030 | scan | other | ✅ | 10 | `void FUN_00993030(void)` |
| 0x00993060 | FUN_00993060 | scan | other | ✅ | 10 | `void FUN_00993060(void)` |
| 0x00993090 | FUN_00993090 | scan | other | ✅ | 10 | `void FUN_00993090(void)` |
| 0x009930c0 | FUN_009930c0 | scan | other | ✅ | 10 | `void FUN_009930c0(void)` |
| 0x009930f0 | FUN_009930f0 | scan | other | ✅ | 10 | `void FUN_009930f0(void)` |
| 0x00993120 | FUN_00993120 | scan | other | ✅ | 10 | `void FUN_00993120(void)` |
| 0x00993150 | FUN_00993150 | scan | other | ✅ | 10 | `void FUN_00993150(void)` |
| 0x00993180 | FUN_00993180 | scan | other | ✅ | 10 | `void FUN_00993180(void)` |
| 0x009931b0 | FUN_009931b0 | scan | other | ✅ | 8 | `void FUN_009931b0(void)` |
| 0x009931d0 | FUN_009931d0 | scan | other | ✅ | 10 | `void FUN_009931d0(void)` |
| 0x00993200 | FUN_00993200 | scan | other | ✅ | 10 | `void FUN_00993200(void)` |
| 0x00993230 | FUN_00993230 | scan | other | ✅ | 8 | `void FUN_00993230(void)` |
| 0x00993250 | FUN_00993250 | scan | other | ✅ | 8 | `void FUN_00993250(void)` |
| 0x00993270 | FUN_00993270 | scan | other | ✅ | 8 | `void FUN_00993270(void)` |
| 0x00993290 | FUN_00993290 | scan | other | ✅ | 8 | `void FUN_00993290(void)` |
| 0x009932b0 | FUN_009932b0 | scan | other | ✅ | 8 | `void FUN_009932b0(void)` |
| 0x009932d0 | FUN_009932d0 | scan | other | ✅ | 8 | `void FUN_009932d0(void)` |
| 0x009932f0 | FUN_009932f0 | scan | other | ✅ | 8 | `void FUN_009932f0(void)` |
| 0x00993310 | FUN_00993310 | scan | other | ✅ | 8 | `void FUN_00993310(void)` |
| 0x00993330 | FUN_00993330 | scan | other | ✅ | 8 | `void FUN_00993330(void)` |
| 0x00993350 | FUN_00993350 | scan | other | ✅ | 8 | `void FUN_00993350(void)` |
| 0x00993370 | FUN_00993370 | scan | other | ✅ | 8 | `void FUN_00993370(void)` |
| 0x00993390 | FUN_00993390 | scan | other | ✅ | 8 | `void FUN_00993390(void)` |
| 0x009933b0 | FUN_009933b0 | scan | other | ✅ | 8 | `void FUN_009933b0(void)` |
| 0x009933d0 | FUN_009933d0 | scan | other | ✅ | 8 | `void FUN_009933d0(void)` |
| 0x009933f0 | FUN_009933f0 | scan | other | ✅ | 8 | `void FUN_009933f0(void)` |
| 0x00993410 | FUN_00993410 | scan | other | ✅ | 8 | `void FUN_00993410(void)` |
| 0x00993430 | FUN_00993430 | scan | other | ✅ | 8 | `void FUN_00993430(void)` |
| 0x00993450 | FUN_00993450 | scan | other | ✅ | 8 | `void FUN_00993450(void)` |
| 0x00993470 | FUN_00993470 | scan | other | ✅ | 10 | `void FUN_00993470(void)` |
| 0x009934a0 | FUN_009934a0 | scan | other | ✅ | 8 | `void FUN_009934a0(void)` |
| 0x009934c0 | FUN_009934c0 | scan | other | ✅ | 13 | `void FUN_009934c0(undefined4 param_1,undefined4 param_2)` |
| 0x009934f0 | FUN_009934f0 | scan | other | ✅ | 8 | `void FUN_009934f0(void)` |
| 0x00993510 | FUN_00993510 | scan | other | ✅ | 8 | `void FUN_00993510(void)` |
| 0x00993530 | FUN_00993530 | scan | other | ✅ | 10 | `void FUN_00993530(void)` |
| 0x00993560 | FUN_00993560 | scan | other | ✅ | 10 | `void FUN_00993560(void)` |
| 0x00993590 | FUN_00993590 | scan | other | ✅ | 10 | `void FUN_00993590(void)` |
| 0x009935c0 | FUN_009935c0 | scan | other | ✅ | 10 | `void FUN_009935c0(void)` |
| 0x009935f0 | FUN_009935f0 | scan | other | ✅ | 10 | `void FUN_009935f0(void)` |
| 0x00993620 | FUN_00993620 | scan | other | ✅ | 10 | `void FUN_00993620(void)` |
| 0x00993650 | FUN_00993650 | scan | other | ✅ | 10 | `void FUN_00993650(void)` |
| 0x00993680 | FUN_00993680 | scan | other | ✅ | 8 | `void FUN_00993680(void)` |
| 0x009936a0 | FUN_009936a0 | scan | other | ✅ | 8 | `void FUN_009936a0(void)` |
| 0x009936c0 | FUN_009936c0 | scan | other | ✅ | 8 | `void FUN_009936c0(void)` |
| 0x009936e0 | FUN_009936e0 | scan | other | ✅ | 15 | `void FUN_009936e0(undefined4 param_1,undefined8 param_2)` |
| 0x00993720 | FUN_00993720 | scan | other | ✅ | 8 | `void FUN_00993720(void)` |
| 0x00993740 | FUN_00993740 | scan | other | ✅ | 13 | `void FUN_00993740(undefined4 param_1,undefined4 param_2)` |
| 0x00993770 | FUN_00993770 | scan | other | ✅ | 8 | `void FUN_00993770(void)` |
| 0x00993790 | FUN_00993790 | scan | other | ✅ | 8 | `void FUN_00993790(void)` |
| 0x009937b0 | FUN_009937b0 | scan | other | ✅ | 8 | `void FUN_009937b0(void)` |
| 0x009937d0 | FUN_009937d0 | scan | other | ✅ | 8 | `void FUN_009937d0(void)` |
| 0x009937f0 | FUN_009937f0 | scan | other | ✅ | 8 | `void FUN_009937f0(void)` |
| 0x00993810 | FUN_00993810 | scan | other | ✅ | 17 | `void FUN_00993810(undefined4 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00993850 | FUN_00993850 | scan | other | ✅ | 8 | `void FUN_00993850(void)` |
| 0x00993870 | FUN_00993870 | scan | other | ✅ | 15 | `void FUN_00993870(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009938b0 | FUN_009938b0 | scan | other | ✅ | 8 | `void FUN_009938b0(void)` |
| 0x009938d0 | FUN_009938d0 | scan | other | ✅ | 8 | `void FUN_009938d0(void)` |
| 0x009938f0 | FUN_009938f0 | scan | other | ✅ | 8 | `void FUN_009938f0(void)` |
| 0x00993910 | FUN_00993910 | scan | other | ✅ | 8 | `void FUN_00993910(void)` |
| 0x00993930 | FUN_00993930 | scan | other | ✅ | 8 | `void FUN_00993930(void)` |
| 0x00993950 | FUN_00993950 | scan | other | ✅ | 19 | `void FUN_00993950(undefined4 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x009939a0 | FUN_009939a0 | scan | other | ✅ | 8 | `void FUN_009939a0(void)` |
| 0x009939c0 | FUN_009939c0 | scan | other | ✅ | 17 | `void FUN_009939c0(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x00993a10 | FUN_00993a10 | scan | other | ✅ | 8 | `void FUN_00993a10(void)` |
| 0x00993a30 | FUN_00993a30 | scan | other | ✅ | 8 | `void FUN_00993a30(void)` |
| 0x00993a50 | FUN_00993a50 | scan | other | ✅ | 8 | `void FUN_00993a50(void)` |
| 0x00993a70 | FUN_00993a70 | scan | other | ✅ | 8 | `void FUN_00993a70(void)` |
| 0x00993a90 | FUN_00993a90 | scan | other | ✅ | 8 | `void FUN_00993a90(void)` |
| 0x00993ab0 | FUN_00993ab0 | scan | other | ✅ | 21 | `` |
| 0x00993b10 | FUN_00993b10 | scan | other | ✅ | 8 | `void FUN_00993b10(void)` |
| 0x00993b30 | FUN_00993b30 | scan | other | ✅ | 19 | `` |
| 0x00993b80 | FUN_00993b80 | scan | other | ✅ | 8 | `void FUN_00993b80(void)` |
| 0x00993ba0 | FUN_00993ba0 | scan | other | ✅ | 8 | `void FUN_00993ba0(void)` |
| 0x00993bc0 | FUN_00993bc0 | scan | other | ✅ | 8 | `void FUN_00993bc0(void)` |
| 0x00993be0 | FUN_00993be0 | scan | other | ✅ | 8 | `void FUN_00993be0(void)` |
| 0x00993c00 | FUN_00993c00 | scan | other | ✅ | 8 | `void FUN_00993c00(void)` |
| 0x00993c20 | FUN_00993c20 | scan | other | ✅ | 8 | `void FUN_00993c20(void)` |
| 0x00993c40 | FUN_00993c40 | scan | other | ✅ | 12 | `void FUN_00993c40(undefined4 param_1)` |
| 0x00993c70 | FUN_00993c70 | scan | other | ✅ | 8 | `void FUN_00993c70(void)` |
| 0x00993c90 | FUN_00993c90 | scan | other | ✅ | 8 | `void FUN_00993c90(void)` |
| 0x00993cb0 | FUN_00993cb0 | scan | other | ✅ | 8 | `void FUN_00993cb0(void)` |
| 0x00993cd0 | FUN_00993cd0 | scan | other | ✅ | 8 | `void FUN_00993cd0(void)` |
| 0x00993cf0 | FUN_00993cf0 | scan | other | ✅ | 8 | `void FUN_00993cf0(void)` |
| 0x00993d10 | FUN_00993d10 | scan | other | ✅ | 8 | `void FUN_00993d10(void)` |
| 0x00993d30 | FUN_00993d30 | scan | other | ✅ | 8 | `void FUN_00993d30(void)` |
| 0x00993d50 | FUN_00993d50 | scan | other | ✅ | 10 | `void FUN_00993d50(void)` |
| 0x00993d80 | FUN_00993d80 | scan | other | ✅ | 10 | `void FUN_00993d80(void)` |
| 0x00993db0 | FUN_00993db0 | scan | other | ✅ | 10 | `void FUN_00993db0(void)` |
| 0x00993de0 | FUN_00993de0 | scan | other | ✅ | 20 | `` |
| 0x00993e40 | FUN_00993e40 | scan | other | ✅ | 20 | `` |
| 0x00993ea0 | FUN_00993ea0 | scan | other | ✅ | 10 | `void FUN_00993ea0(void)` |
| 0x00993ed0 | FUN_00993ed0 | scan | other | ✅ | 10 | `void FUN_00993ed0(void)` |
| 0x00993f00 | FUN_00993f00 | scan | other | ✅ | 17 | `void FUN_00993f00(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x00993f40 | FUN_00993f40 | scan | other | ✅ | 17 | `void FUN_00993f40(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x00993f80 | FUN_00993f80 | scan | other | ✅ | 8 | `void FUN_00993f80(void)` |
| 0x00993fa0 | FUN_00993fa0 | scan | other | ✅ | 8 | `void FUN_00993fa0(void)` |
| 0x00993fc0 | FUN_00993fc0 | scan | other | ✅ | 8 | `void FUN_00993fc0(void)` |
| 0x00993fe0 | FUN_00993fe0 | scan | other | ✅ | 8 | `void FUN_00993fe0(void)` |
| 0x00994000 | FUN_00994000 | scan | other | ✅ | 8 | `void FUN_00994000(void)` |
| 0x00994020 | FUN_00994020 | scan | other | ✅ | 8 | `void FUN_00994020(void)` |
| 0x00994040 | FUN_00994040 | scan | other | ✅ | 8 | `void FUN_00994040(void)` |
| 0x00994060 | FUN_00994060 | scan | other | ✅ | 8 | `void FUN_00994060(void)` |
| 0x00994080 | FUN_00994080 | scan | other | ✅ | 8 | `void FUN_00994080(void)` |
| 0x009940a0 | FUN_009940a0 | scan | other | ✅ | 8 | `void FUN_009940a0(void)` |
| 0x009940c0 | FUN_009940c0 | scan | other | ✅ | 8 | `void FUN_009940c0(void)` |
| 0x009940e0 | FUN_009940e0 | scan | other | ✅ | 17 | `void FUN_009940e0(undefined8 param_1,undefined8 param_2)` |
| 0x00994120 | FUN_00994120 | scan | other | ✅ | 17 | `void FUN_00994120(undefined8 param_1,undefined8 param_2)` |
| 0x00994160 | FUN_00994160 | scan | other | ✅ | 17 | `void FUN_00994160(undefined8 param_1,undefined8 param_2)` |
| 0x009941a0 | FUN_009941a0 | scan | other | ✅ | 10 | `void FUN_009941a0(void)` |
| 0x009941d0 | FUN_009941d0 | scan | other | ✅ | 10 | `void FUN_009941d0(void)` |
| 0x00994200 | FUN_00994200 | scan | other | ✅ | 10 | `void FUN_00994200(void)` |
| 0x00994230 | FUN_00994230 | scan | other | ✅ | 15 | `void FUN_00994230(undefined4 param_1,undefined4 param_2)` |
| 0x00994270 | FUN_00994270 | scan | other | ✅ | 15 | `void FUN_00994270(undefined4 param_1,undefined4 param_2)` |
| 0x009942b0 | FUN_009942b0 | scan | other | ✅ | 15 | `void FUN_009942b0(undefined4 param_1,undefined4 param_2)` |
| 0x009942f0 | FUN_009942f0 | scan | other | ✅ | 10 | `void FUN_009942f0(void)` |
| 0x00994320 | FUN_00994320 | scan | other | ✅ | 10 | `void FUN_00994320(void)` |
| 0x00994350 | FUN_00994350 | scan | other | ✅ | 10 | `void FUN_00994350(void)` |
| 0x00994380 | FUN_00994380 | scan | other | ✅ | 10 | `void FUN_00994380(void)` |
| 0x009943b0 | FUN_009943b0 | scan | other | ✅ | 10 | `void FUN_009943b0(void)` |
| 0x009943e0 | FUN_009943e0 | scan | other | ✅ | 10 | `void FUN_009943e0(void)` |
| 0x00994410 | FUN_00994410 | scan | other | ✅ | 10 | `void FUN_00994410(void)` |
| 0x00994440 | FUN_00994440 | scan | other | ✅ | 10 | `void FUN_00994440(void)` |
| 0x00994470 | FUN_00994470 | scan | other | ✅ | 10 | `void FUN_00994470(void)` |
| 0x009944a0 | FUN_009944a0 | scan | other | ✅ | 10 | `void FUN_009944a0(void)` |
| 0x009944d0 | FUN_009944d0 | scan | other | ✅ | 10 | `void FUN_009944d0(void)` |
| 0x00994500 | FUN_00994500 | scan | other | ✅ | 10 | `void FUN_00994500(void)` |
| 0x00994530 | FUN_00994530 | scan | other | ✅ | 10 | `void FUN_00994530(void)` |
| 0x00994560 | FUN_00994560 | scan | other | ✅ | 10 | `void FUN_00994560(void)` |
| 0x00994590 | FUN_00994590 | scan | other | ✅ | 10 | `void FUN_00994590(void)` |
| 0x009945c0 | FUN_009945c0 | scan | other | ✅ | 19 | `void FUN_009945c0(undefined8 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00994610 | FUN_00994610 | scan | other | ✅ | 19 | `void FUN_00994610(undefined8 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x00994660 | FUN_00994660 | scan | other | ✅ | 19 | `void FUN_00994660(undefined8 param_1,undefined8 param_2,undefined8 param_3)` |
| 0x009946b0 | FUN_009946b0 | scan | other | ✅ | 10 | `void FUN_009946b0(void)` |
| 0x009946e0 | FUN_009946e0 | scan | other | ✅ | 10 | `void FUN_009946e0(void)` |
| 0x00994710 | FUN_00994710 | scan | other | ✅ | 10 | `void FUN_00994710(void)` |
| 0x00994740 | FUN_00994740 | scan | other | ✅ | 17 | `void FUN_00994740(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x00994790 | FUN_00994790 | scan | other | ✅ | 17 | `void FUN_00994790(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009947e0 | FUN_009947e0 | scan | other | ✅ | 17 | `void FUN_009947e0(undefined4 param_1,undefined4 param_2,undefined4 param_3)` |
| 0x00994830 | FUN_00994830 | scan | other | ✅ | 10 | `void FUN_00994830(void)` |
| 0x00994860 | FUN_00994860 | scan | other | ✅ | 10 | `void FUN_00994860(void)` |
| 0x00994890 | FUN_00994890 | scan | other | ✅ | 10 | `void FUN_00994890(void)` |
| 0x009948c0 | FUN_009948c0 | scan | other | ✅ | 10 | `void FUN_009948c0(void)` |
| 0x009948f0 | FUN_009948f0 | scan | other | ✅ | 10 | `void FUN_009948f0(void)` |
| 0x00994920 | FUN_00994920 | scan | other | ✅ | 10 | `void FUN_00994920(void)` |
| 0x00994950 | FUN_00994950 | scan | other | ✅ | 10 | `void FUN_00994950(void)` |
| 0x00994980 | FUN_00994980 | scan | other | ✅ | 10 | `void FUN_00994980(void)` |
| 0x009949b0 | FUN_009949b0 | scan | other | ✅ | 10 | `void FUN_009949b0(void)` |
| 0x009949e0 | FUN_009949e0 | scan | other | ✅ | 10 | `void FUN_009949e0(void)` |
| 0x00994a10 | FUN_00994a10 | scan | other | ✅ | 10 | `void FUN_00994a10(void)` |
| 0x00994a40 | FUN_00994a40 | scan | other | ✅ | 10 | `void FUN_00994a40(void)` |
| 0x00994a70 | FUN_00994a70 | scan | other | ✅ | 10 | `void FUN_00994a70(void)` |
| 0x00994aa0 | FUN_00994aa0 | scan | other | ✅ | 10 | `void FUN_00994aa0(void)` |
| 0x00994ad0 | FUN_00994ad0 | scan | other | ✅ | 10 | `void FUN_00994ad0(void)` |
| 0x00994b00 | FUN_00994b00 | scan | other | ✅ | 20 | `void FUN_00994b00(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)` |
| 0x00994b50 | FUN_00994b50 | scan | other | ✅ | 8 | `void FUN_00994b50(void)` |
| 0x00994b70 | FUN_00994b70 | scan | other | ✅ | 18 | `void FUN_00994b70(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x00994bc0 | FUN_00994bc0 | scan | other | ✅ | 8 | `void FUN_00994bc0(void)` |
| 0x00994be0 | FUN_00994be0 | scan | other | ✅ | 8 | `void FUN_00994be0(void)` |
| 0x00994c00 | FUN_00994c00 | scan | other | ✅ | 8 | `void FUN_00994c00(void)` |
| 0x00994c20 | FUN_00994c20 | scan | other | ✅ | 8 | `void FUN_00994c20(void)` |
| 0x00994c40 | FUN_00994c40 | scan | other | ✅ | 8 | `void FUN_00994c40(void)` |
| 0x00994c60 | FUN_00994c60 | scan | other | ✅ | 8 | `void FUN_00994c60(void)` |
| 0x00994c80 | FUN_00994c80 | scan | other | ✅ | 15 | `undefined4 * __thiscall FUN_00994c80(undefined4 *param_1,byte param_2)` |
| 0x00994cc0 | FUN_00994cc0 | scan | other | ✅ | 15 | `undefined4 * __thiscall FUN_00994cc0(undefined4 *param_1,byte param_2)` |
| 0x00994d00 | FUN_00994d00 | scan | other | ✅ | 16 | `void __thiscall FUN_00994d00(int *param_1,float param_2)` |
| 0x00994d50 | FUN_00994d50 | scan | other | ✅ | 24 | `` |
| 0x00994db0 | FUN_00994db0 | scan | other | ✅ | 9 | `undefined4 __thiscall FUN_00994db0(int param_1,undefined4 param_2)` |
| 0x00994dd0 | FUN_00994dd0 | scan | other | ✅ | 226 | `` |
| 0x00995140 | FUN_00995140 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_00995140(undefined4 param_1,byte param_2)` |
| 0x00995170 | FUN_00995170 | scan | other | ✅ | 147 | `void __fastcall FUN_00995170(undefined4 *param_1)` |
| 0x00995330 | FUN_00995330 | scan | other | ✅ | 17 | `undefined4 * __thiscall FUN_00995330(undefined4 *param_1,int param_2)` |
| 0x00995360 | FUN_00995360 | scan | other | ✅ | 17 | `undefined4 * __thiscall FUN_00995360(undefined4 *param_1,byte param_2)` |
| 0x00995390 | FUN_00995390 | scan | other | ✅ | 82 | `void __fastcall FUN_00995390(int param_1)` |
| 0x009954f0 | FUN_009954f0 | scan | other | ✅ | 54 | `void __fastcall FUN_009954f0(int param_1)` |
| 0x00995590 | FUN_00995590 | scan | other | ✅ | 15 | `undefined4 * __thiscall FUN_00995590(undefined4 *param_1,byte param_2)` |
| 0x009955d0 | FUN_009955d0 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009955d0(undefined4 param_1,byte param_2)` |
| 0x00995600 | FUN_00995600 | scan | other | ✅ | 75 | `void __fastcall FUN_00995600(undefined4 *param_1)` |
| 0x00995780 | FUN_00995780 | scan | other | ✅ | 74 | `` |
| 0x00995840 | FUN_00995840 | scan | other | ✅ | 75 | `` |
| 0x00995900 | FUN_00995900 | scan | other | ✅ | 80 | `` |
| 0x009959e0 | FUN_009959e0 | scan | other | ✅ | 44 | `` |
| 0x00995a50 | FUN_00995a50 | scan | other | ✅ | 62 | `` |
| 0x00995ae0 | FUN_00995ae0 | scan | other | ✅ | 44 | `` |
| 0x00995b50 | FUN_00995b50 | scan | other | ✅ | 43 | `` |
| 0x00995bd0 | FUN_00995bd0 | scan | other | ✅ | 42 | `` |
| 0x00995c50 | FUN_00995c50 | scan | other | ✅ | 74 | `void __thiscall FUN_00995c50(int param_1,undefined4 *param_2)` |
| 0x00995d40 | FUN_00995d40 | scan | other | ✅ | 21 | `void __thiscall FUN_00995d40(int param_1,char *param_2)` |
| 0x00995d80 | FUN_00995d80 | scan | other | ✅ | 43 | `void __thiscall FUN_00995d80(int *param_1,char *param_2,char param_3)` |
| 0x00995df0 | FUN_00995df0 | scan | other | ✅ | 285 | `void __thiscall FUN_00995df0(int param_1,int param_2)` |
| 0x00996140 | FUN_00996140 | scan | other | ✅ | 18 | `void __thiscall FUN_00996140(int param_1,int *param_2,char param_3)` |
| 0x009961a0 | FUN_009961a0 | scan | other | ✅ | 18 | `` |
| 0x009961e0 | FUN_009961e0 | scan | other | ✅ | 12 | `void __thiscall FUN_009961e0(int param_1,undefined4 param_2)` |
| 0x00996210 | FUN_00996210 | scan | other | ✅ | 32 | `void __thiscall FUN_00996210(int param_1,int param_2,int param_3,undefined4 param_4)` |
| 0x00996260 | FUN_00996260 | scan | other | ✅ | 32 | `void __thiscall FUN_00996260(int param_1,int param_2,int param_3,undefined4 param_4)` |
| 0x009962b0 | FUN_009962b0 | callee | other | — | 34 | `` |
| 0x00996320 | FUN_00996320 | scan | other | ✅ | 29 | `bool FUN_00996320(void)` |
| 0x00996360 | FUN_00996360 | callee | other | — | 44 | `` |
| 0x009963d0 | FUN_009963d0 | scan | other | ✅ | 41 | `bool __fastcall FUN_009963d0(int param_1)` |
| 0x00996440 | FUN_00996440 | scan | other | ✅ | 11 | `void __fastcall FUN_00996440(int param_1)` |
| 0x00996460 | FUN_00996460 | scan | other | ✅ | 19 | `void __fastcall FUN_00996460(int param_1)` |
| 0x009964a0 | FUN_009964a0 | scan | other | ✅ | 34 | `long __fastcall FUN_009964a0(int param_1)` |
| 0x00996500 | FUN_00996500 | scan | other | ✅ | 30 | `void __thiscall FUN_00996500(int param_1,long param_2,int param_3)` |
| 0x00996560 | FUN_00996560 | callee | other | — | 16 | `` |
| 0x00996560 | FUN_00996560 | scan | other | ✅ | 16 | `int __thiscall FUN_00996560(int param_1,void *param_2,size_t param_3,size_t param_4)` |
| 0x00996590 | FUN_00996590 | scan | other | ✅ | 16 | `int __thiscall FUN_00996590(int param_1,void *param_2,size_t param_3,size_t param_4)` |
| 0x009965d0 | FUN_009965d0 | scan | other | ✅ | 60 | `undefined4 __fastcall FUN_009965d0(int param_1,uint param_2)` |
| 0x00996680 | FUN_00996680 | scan | other | ✅ | 30 | `void __fastcall FUN_00996680(int param_1)` |
| 0x009966e0 | FUN_009966e0 | scan | other | ✅ | 29 | `void __fastcall FUN_009966e0(int param_1)` |
| 0x00996740 | FUN_00996740 | scan | other | ✅ | 37 | `void __fastcall FUN_00996740(int param_1)` |
| 0x009967c0 | FUN_009967c0 | scan | other | ✅ | 32 | `void __fastcall FUN_009967c0(int param_1)` |
| 0x00996830 | FUN_00996830 | scan | other | ✅ | 35 | `uint FUN_00996830(void)` |
| 0x00996890 | FUN_00996890 | scan | other | ✅ | 31 | `int __fastcall FUN_00996890(undefined4 param_1,uint param_2)` |
| 0x009971d0 | FUN_009971d0 | scan | other | ✅ | 122 | `LRESULT FUN_009971d0(HWND param_1,uint param_2,uint param_3,LONG *param_4)` |
| 0x00997f30 | FUN_00997f30 | scan | other | ✅ | 123 | `bool __fastcall FUN_00997f30(LPVOID param_1,int *param_2,undefined4 param_3)` |
| 0x00998110 | FUN_00998110 | scan | other | ✅ | 23 | `void __fastcall FUN_00998110(int param_1)` |
| 0x00998170 | FUN_00998170 | scan | other | ✅ | 183 | `undefined4 __fastcall FUN_00998170(int param_1,int param_2,int param_3)` |
| 0x009983c0 | FUN_009983c0 | scan | other | ✅ | 51 | `void __fastcall FUN_009983c0(int param_1,int param_2,int param_3)` |
| 0x00998470 | FUN_00998470 | scan | other | ✅ | 13 | `void __fastcall FUN_00998470(int param_1)` |
| 0x009984b0 | FUN_009984b0 | scan | other | ✅ | 158 | `void FUN_009984b0(void)` |
| 0x009986a0 | FUN_009986a0 | scan | other | ✅ | 26 | `void __fastcall FUN_009986a0(int param_1)` |
| 0x009986f0 | FUN_009986f0 | scan | other | ✅ | 139 | `char * __fastcall FUN_009986f0(char *param_1,char *param_2,char param_3,byte param_4)` |
| 0x00998840 | FUN_00998840 | scan | other | ✅ | 139 | `byte __fastcall FUN_00998840(char *param_1,char *param_2)` |
| 0x00998980 | FUN_00998980 | scan | other | ✅ | 15 | `undefined4 * __thiscall FUN_00998980(undefined4 *param_1,byte param_2)` |
| 0x009989b0 | FUN_009989b0 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009989b0(undefined4 param_1,byte param_2)` |
| 0x009989e0 | FUN_009989e0 | scan | other | ✅ | 36 | `void __fastcall FUN_009989e0(undefined4 *param_1)` |
| 0x00998a50 | FUN_00998a50 | scan | other | ✅ | 115 | `` |
| 0x00998bf0 | FUN_00998bf0 | scan | other | ✅ | 34 | `void __fastcall FUN_00998bf0(int param_1)` |
| 0x00998c50 | FUN_00998c50 | scan | other | ✅ | 22 | `void FUN_00998c50(int *param_1)` |
| 0x00998c80 | FUN_00998c80 | scan | other | ✅ | 55 | `void FUN_00998c80(void)` |
| 0x00998d60 | FUN_00998d60 | scan | other | ✅ | 85 | `void __fastcall FUN_00998d60(char param_1)` |
| 0x00998e90 | FUN_00998e90 | scan | other | ✅ | 26 | `void FUN_00998e90(void)` |
| 0x00998f10 | FUN_00998f10 | scan | other | ✅ | 13 | `void __fastcall FUN_00998f10(byte *param_1)` |
| 0x00998f40 | FUN_00998f40 | scan | other | ✅ | 100 | `void __thiscall FUN_00998f40(int *param_1,int *param_2)` |
| 0x00999050 | FUN_00999050 | scan | other | ✅ | 7 | `void __fastcall FUN_00999050(int param_1)` |
| 0x00999070 | FUN_00999070 | scan | other | ✅ | 48 | `void __fastcall FUN_00999070(int *param_1,LPCSTR param_2,LPCSTR param_3,char param_4)` |
| 0x00999140 | FUN_00999140 | scan | other | ✅ | 56 | `int __fastcall FUN_00999140(int param_1)` |
| 0x009991e0 | FUN_009991e0 | scan | other | ✅ | 42 | `undefined4 __fastcall FUN_009991e0(char *param_1,char *param_2)` |
| 0x00999240 | FUN_00999240 | scan | other | ✅ | 83 | `uint __fastcall FUN_00999240(byte *param_1,byte param_2)` |
| 0x00999310 | FUN_00999310 | scan | other | ✅ | 9 | `void __fastcall FUN_00999310(undefined4 param_1)` |
| 0x00999330 | FUN_00999330 | scan | other | ✅ | 29 | `void __fastcall FUN_00999330(LPCSTR param_1)` |
| 0x00999390 | FUN_00999390 | scan | other | ✅ | 5 | `void FUN_00999390(void)` |
| 0x009993c0 | FUN_009993c0 | scan | other | ✅ | 155 | `void __thiscall FUN_009993c0(int *param_1,undefined4 param_2,int param_3,char param_4)` |
| 0x00999570 | FUN_00999570 | scan | other | ✅ | 12 | `void FUN_00999570(void)` |
| 0x00999590 | FUN_00999590 | scan | other | ✅ | 12 | `void FUN_00999590(undefined4 *param_1)` |
| 0x009995b0 | FUN_009995b0 | scan | other | ✅ | 186 | `void FUN_009995b0(void)` |
| 0x00999860 | FUN_00999860 | scan | other | ✅ | 152 | `int FUN_00999860(int param_1,int param_2)` |
| 0x00999a60 | FUN_00999a60 | scan | other | ✅ | 43 | `void __fastcall FUN_00999a60(undefined4 *param_1,undefined4 *param_2,undefined4 *param_3)` |
| 0x00999b10 | FUN_00999b10 | scan | other | ✅ | 45 | `void __fastcall FUN_00999b10(undefined4 *param_1)` |
| 0x00999ba0 | FUN_00999ba0 | caller | other | — | 80 | `` |
| 0x00999c97 | FUN_00999c97 | scan | other | ✅ | 96 | `undefined4 FUN_00999c97(void)` |
| 0x00999db0 | FUN_00999db0 | scan | other | ✅ | 205 | `void __fastcall FUN_00999db0(int param_1)` |
| 0x0099a050 | FUN_0099a050 | scan | other | ✅ | 20 | `undefined4 * __thiscall FUN_0099a050(undefined4 *param_1,byte param_2)` |
| 0x0099a090 | FUN_0099a090 | scan | other | ✅ | 44 | `void * __thiscall FUN_0099a090(int param_1,size_t param_2,undefined4 param_3,undefined4 param_4)` |
| 0x0099a100 | FUN_0099a100 | scan | other | ✅ | 85 | `void __thiscall FUN_0099a100(int param_1,void *param_2)` |
| 0x0099a1c0 | FUN_0099a1c0 | scan | other | ✅ | 8 | `void __fastcall FUN_0099a1c0(int param_1)` |
| 0x0099a1e0 | FUN_0099a1e0 | scan | other | ✅ | 22 | `void __thiscall FUN_0099a1e0(int param_1,undefined4 param_2)` |
| 0x0099a210 | FUN_0099a210 | scan | other | ✅ | 59 | `undefined8 __thiscall FUN_0099a210(int param_1,int param_2)` |
| 0x0099a2d0 | FUN_0099a2d0 | scan | other | ✅ | 59 | `undefined8 __thiscall FUN_0099a2d0(int param_1,int param_2)` |
| 0x0099a390 | FUN_0099a390 | scan | other | ✅ | 108 | `undefined8 __thiscall FUN_0099a390(int param_1,uint param_2)` |
| 0x0099a490 | FUN_0099a490 | scan | other | ✅ | 34 | `int __thiscall FUN_0099a490(int param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x0099a4e0 | FUN_0099a4e0 | scan | other | ✅ | 75 | `void __thiscall FUN_0099a4e0(int param_1,uint param_2)` |
| 0x0099a590 | FUN_0099a590 | scan | other | ✅ | 9 | `void __thiscall FUN_0099a590(int *param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x0099a5b0 | FUN_0099a5b0 | scan | other | ✅ | 5 | `void __fastcall FUN_0099a5b0(int *param_1)` |
| 0x0099a5c0 | FUN_0099a5c0 | scan | other | ✅ | 11 | `void __thiscall FUN_0099a5c0(int *param_1,undefined4 param_2,undefined4 param_3)` |
| 0x0099a5e0 | FUN_0099a5e0 | scan | other | ✅ | 11 | `void __thiscall FUN_0099a5e0(int *param_1,undefined4 param_2,undefined4 param_3)` |
| 0x0099a600 | FUN_0099a600 | scan | other | ✅ | 5 | `void __fastcall FUN_0099a600(int *param_1)` |
| 0x0099a610 | FUN_0099a610 | scan | other | ✅ | 9 | `void __thiscall FUN_0099a610(int *param_1,undefined4 param_2,undefined4 param_3)` |
| 0x0099a630 | FUN_0099a630 | scan | other | ✅ | 135 | `uint __fastcall FUN_0099a630(int param_1)` |
| 0x0099a7d0 | FUN_0099a7d0 | scan | other | ✅ | 165 | `int * __fastcall FUN_0099a7d0(int *param_1,int param_2,int param_3)` |
| 0x0099a980 | FUN_0099a980 | scan | other | ✅ | 208 | `undefined4 FUN_0099a980(void)` |
| 0x0099ac50 | FUN_0099ac50 | scan | other | ✅ | 48 | `undefined4 __fastcall FUN_0099ac50(char *param_1,char *param_2)` |
| 0x0099acc0 | FUN_0099acc0 | scan | other | ✅ | 27 | `void __fastcall FUN_0099acc0(LPVOID param_1)` |
| 0x0099ad20 | FUN_0099ad20 | scan | other | ✅ | 136 | `undefined4 __fastcall FUN_0099ad20(byte *param_1)` |
| 0x0099ae80 | FUN_0099ae80 | scan | other | ✅ | 292 | `` |
| 0x0099b230 | FUN_0099b230 | scan | other | ✅ | 102 | `void __fastcall FUN_0099b230(int param_1,undefined4 param_2)` |
| 0x0099b3c0 | FUN_0099b3c0 | scan | other | ✅ | 61 | `void __fastcall FUN_0099b3c0(undefined4 **param_1)` |
| 0x0099b480 | FUN_0099b480 | scan | other | ✅ | 28 | `int FUN_0099b480(int param_1,int param_2)` |
| 0x0099b720 | FUN_0099b720 | scan | other | ✅ | 54 | `void __fastcall FUN_0099b720(void *param_1,int param_2)` |
| 0x0099b7a0 | FUN_0099b7a0 | scan | other | ✅ | 64 | `void FUN_0099b7a0(undefined4 param_1,int param_2)` |
| 0x0099b8a0 | FUN_0099b8a0 | scan | other | ✅ | 15 | `undefined4 * __thiscall FUN_0099b8a0(undefined4 *param_1,byte param_2)` |
| 0x0099b8d0 | FUN_0099b8d0 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_0099b8d0(undefined4 param_1,byte param_2)` |
| 0x0099b900 | FUN_0099b900 | scan | other | ✅ | 60 | `void __fastcall FUN_0099b900(undefined4 *param_1)` |
| 0x0099b9a0 | FUN_0099b9a0 | scan | other | ✅ | 8 | `void __thiscall FUN_0099b9a0(int *param_1,undefined4 param_2)` |
| 0x0099b9c0 | FUN_0099b9c0 | scan | other | ✅ | 58 | `void __thiscall FUN_0099b9c0(int *param_1,int param_2,uint param_3)` |
| 0x0099bae0 | FUN_0099bae0 | scan | other | ✅ | 30 | `bool __thiscall FUN_0099bae0(int param_1,uint param_2)` |
| 0x0099bb30 | FUN_0099bb30 | scan | other | ✅ | 39 | `undefined4 __thiscall FUN_0099bb30(int param_1,uint param_2)` |
| 0x0099bb90 | FUN_0099bb90 | scan | other | ✅ | 187 | `void FUN_0099bb90(undefined4 param_1)` |
| 0x0099bdb0 | FUN_0099bdb0 | scan | other | ✅ | 13 | `int FUN_0099bdb0(undefined4 param_1)` |
| 0x0099bdd0 | FUN_0099bdd0 | scan | other | ✅ | 153 | `void __thiscall FUN_0099bdd0(int *param_1,int *param_2,uint *param_3)` |
| 0x0099bfa0 | FUN_0099bfa0 | caller | archive-loader | — | 66 | `` |
| 0x0099bfa0 | FUN_0099bfa0 | seed | archive-loader | ✅ | 66 | `undefined4 * __thiscall FUN_0099bfa0(undefined4 *param_1,int *param_2)` |
| 0x0099c080 | FUN_0099c080 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_0099c080(undefined4 param_1,byte param_2)` |
| 0x0099c0b0 | FUN_0099c0b0 | callee | other | — | 55 | `` |
| 0x0099c0b0 | FUN_0099c0b0 | scan | other | ✅ | 55 | `void __fastcall FUN_0099c0b0(undefined4 *param_1)` |
| 0x0099c170 | FUN_0099c170 | callee | archive-init | ✅ | 76 | `void __fastcall FUN_0099c170(int param_1)` |
| 0x0099c270 | FUN_0099c270 | callee | mode0x02-readblock | — | 282 | `` |
| 0x0099c270 | FUN_0099c270 | seed | mode0x02-readblock | ✅ | 282 | `void __fastcall FUN_0099c270(int param_1)` |
| 0x0099c690 | FUN_0099c690 | caller | archive-io | ✅ | 65 | `void __thiscall FUN_0099c690(int param_1,uint param_2,int param_3)` |
| 0x0099c750 | FUN_0099c750 | caller | other | ✅ | 73 | `uint __thiscall FUN_0099c750(int param_1,void *param_2,uint param_3,int param_4)` |
| 0x0099c820 | FUN_0099c820 | scan | other | ✅ | 33 | `int __thiscall FUN_0099c820(int *param_1,char *param_2)` |
| 0x0099c8d0 | FUN_0099c8d0 | scan | other | ✅ | 14 | `bool __fastcall FUN_0099c8d0(int *param_1)` |
| 0x0099c8f0 | FUN_0099c8f0 | scan | other | ✅ | 54 | `int __thiscall FUN_0099c8f0(int *param_1,int param_2,int param_3)` |
| 0x0099c970 | FUN_0099c970 | scan | other | ✅ | 20 | `LRESULT FUN_0099c970(HWND param_1,UINT param_2,WPARAM param_3,int param_4)` |
| 0x0099ca00 | FUN_0099ca00 | scan | other | ✅ | 78 | `undefined4 FUN_0099ca00(void)` |
| 0x0099cb50 | FUN_0099cb50 | scan | other | ✅ | 137 | `undefined4 __fastcall FUN_0099cb50(int *param_1)` |
| 0x0099cd10 | FUN_0099cd10 | scan | other | ✅ | 14 | `undefined4 FUN_0099cd10(int param_1,int param_2)` |
| 0x0099cd40 | FUN_0099cd40 | scan | other | ✅ | 7 | `undefined4 FUN_0099cd40(undefined4 param_1,int param_2)` |
| 0x0099cd60 | FUN_0099cd60 | scan | other | ✅ | 196 | `undefined4 FUN_0099cd60(int param_1,int param_2)` |
| 0x0099cfe0 | FUN_0099cfe0 | scan | other | ✅ | 14 | `undefined4 FUN_0099cfe0(undefined4 param_1,int param_2)` |
| 0x0099d010 | FUN_0099d010 | scan | other | ✅ | 253 | `undefined4 FUN_0099d010(int param_1)` |
| 0x0099d310 | FUN_0099d310 | scan | other | ✅ | 61 | `void __fastcall FUN_0099d310(uint param_1)` |
| 0x0099d3b0 | FUN_0099d3b0 | scan | other | ✅ | 165 | `void FUN_0099d3b0(void)` |
| 0x0099d5e0 | FUN_0099d5e0 | scan | other | ✅ | 86 | `void __fastcall FUN_0099d5e0(int param_1,int param_2,float param_3)` |
| 0x0099d720 | FUN_0099d720 | scan | other | ✅ | 1668 | `void FUN_0099d720(void)` |
| 0x0099f210 | FUN_0099f210 | scan | other | ✅ | 16 | `undefined4 * __thiscall FUN_0099f210(undefined4 *param_1,byte param_2)` |
| 0x0099f240 | FUN_0099f240 | scan | other | ✅ | 166 | `undefined1 __thiscall FUN_0099f240(int *param_1,int *param_2)` |
| 0x0099f430 | FUN_0099f430 | scan | other | ✅ | 12 | `void __fastcall FUN_0099f430(int param_1)` |
| 0x0099f470 | FUN_0099f470 | scan | other | ✅ | 34 | `undefined * __thiscall FUN_0099f470(int param_1,uint param_2)` |
| 0x0099f4f0 | FUN_0099f4f0 | scan | other | ✅ | 46 | `float10 __thiscall FUN_0099f4f0(int param_1,int param_2)` |
| 0x0099f570 | FUN_0099f570 | scan | other | ✅ | 96 | `void __thiscall FUN_0099f570(int *param_1,float *param_2,int param_3)` |
| 0x0099f770 | FUN_0099f770 | scan | other | ✅ | 204 | `void __fastcall FUN_0099f770(int param_1)` |
| 0x0099fa00 | FUN_0099fa00 | scan | other | ✅ | 16 | `undefined4 * __thiscall FUN_0099fa00(undefined4 *param_1,byte param_2)` |
| 0x0099fa30 | FUN_0099fa30 | scan | other | ✅ | 505 | `undefined4 __thiscall FUN_0099fa30(int param_1,int param_2)` |
| 0x009a00a0 | FUN_009a00a0 | scan | other | ✅ | 18 | `undefined * __thiscall FUN_009a00a0(int param_1,uint param_2)` |
| 0x009a00e0 | FUN_009a00e0 | scan | other | ✅ | 14 | `bool __thiscall FUN_009a00e0(int param_1,uint param_2)` |
| 0x009a0110 | FUN_009a0110 | scan | other | ✅ | 17 | `undefined4 __thiscall FUN_009a0110(int param_1,uint param_2)` |
| 0x009a0150 | FUN_009a0150 | scan | other | ✅ | 25 | `uint __fastcall FUN_009a0150(int *param_1)` |
| 0x009a0190 | FUN_009a0190 | scan | other | ✅ | 8 | `void FUN_009a0190(uint param_1)` |
| 0x009a01d0 | FUN_009a01d0 | scan | other | ✅ | 25 | `undefined4 __fastcall FUN_009a01d0(int *param_1)` |
| 0x009a0210 | FUN_009a0210 | scan | other | ✅ | 163 | `undefined4 __fastcall FUN_009a0210(int *param_1)` |
| 0x009a0520 | FUN_009a0520 | scan | other | ✅ | 18 | `void FUN_009a0520(undefined4 param_1,uint param_2,undefined4 param_3,int param_4)` |
| 0x009a0560 | FUN_009a0560 | scan | other | ✅ | 29 | `int __fastcall FUN_009a0560(byte *param_1)` |
| 0x009a05b0 | FUN_009a05b0 | scan | other | ✅ | 35 | `undefined4 * __thiscall FUN_009a05b0(undefined4 *param_1,byte param_2)` |
| 0x009a0630 | FUN_009a0630 | caller | other | — | 54 | `` |
| 0x009a06b0 | FUN_009a06b0 | scan | other | ✅ | 324 | `undefined4 __thiscall FUN_009a06b0(int *param_1,int *param_2,undefined4 param_3,char *param_4)` |
| 0x009a0b50 | FUN_009a0b50 | scan | other | ✅ | 28 | `undefined1 __fastcall FUN_009a0b50(int *param_1)` |
| 0x009a0bd0 | FUN_009a0bd0 | scan | other | ✅ | 35 | `undefined4 * __thiscall FUN_009a0bd0(undefined4 *param_1,byte param_2)` |
| 0x009a0c50 | FUN_009a0c50 | caller | other | — | 52 | `` |
| 0x009a0cd0 | FUN_009a0cd0 | scan | other | ✅ | 98 | `undefined1 FUN_009a0cd0(int param_1,undefined4 param_2,char *param_3)` |
| 0x009a0e10 | FUN_009a0e10 | scan | other | ✅ | 529 | `undefined4 __thiscall FUN_009a0e10(int *param_1,int *param_2,undefined4 param_3)` |
| 0x009a1690 | FUN_009a1690 | scan | other | ✅ | 35 | `undefined4 * __thiscall FUN_009a1690(undefined4 *param_1,byte param_2)` |
| 0x009a1710 | FUN_009a1710 | scan | other | ✅ | 238 | `undefined4 __thiscall FUN_009a1710(int *param_1,uint *param_2)` |
| 0x009a1a90 | FUN_009a1a90 | scan | other | ✅ | 35 | `undefined4 * __thiscall FUN_009a1a90(undefined4 *param_1,byte param_2)` |
| 0x009a1b10 | FUN_009a1b10 | scan | other | ✅ | 35 | `undefined4 * __thiscall FUN_009a1b10(undefined4 *param_1,byte param_2)` |
| 0x009a1b90 | FUN_009a1b90 | scan | other | ✅ | 114 | `uint __thiscall FUN_009a1b90(int param_1,undefined4 *param_2,undefined4 param_3,char *param_4)` |
| 0x009a1f30 | FUN_009a1f30 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009a1f30(undefined4 param_1,byte param_2)` |
| 0x009a1f60 | FUN_009a1f60 | scan | other | ✅ | 117 | `void __fastcall FUN_009a1f60(int *param_1)` |
| 0x009a20e0 | FUN_009a20e0 | scan | other | ✅ | 86 | `int __thiscall FUN_009a20e0(int *param_1,int param_2)` |
| 0x009a21e0 | FUN_009a21e0 | scan | other | ✅ | 27 | `uint __fastcall FUN_009a21e0(int *param_1)` |
| 0x009a22d0 | FUN_009a22d0 | caller | other | — | 69 | `` |
| 0x009a2390 | FUN_009a2390 | caller | other | — | 125 | `` |
| 0x009a24f0 | FUN_009a24f0 | scan | other | ✅ | 68 | `void __fastcall FUN_009a24f0(int *param_1)` |
| 0x009a25b0 | FUN_009a25b0 | scan | other | ✅ | 70 | `void __fastcall FUN_009a25b0(int *param_1)` |
| 0x009a26c0 | FUN_009a26c0 | scan | other | ✅ | 82 | `undefined4 * __thiscall FUN_009a26c0(undefined4 *param_1,byte param_2)` |
| 0x009a27f0 | FUN_009a27f0 | scan | other | ✅ | 528 | `uint __thiscall FUN_009a27f0(int param_1,void *param_2)` |
| 0x009a2f60 | FUN_009a2f60 | caller | other | — | 291 | `` |
| 0x009a3280 | FUN_009a3280 | scan | other | ✅ | 90 | `void __fastcall FUN_009a3280(int param_1)` |
| 0x009a33e0 | FUN_009a33e0 | scan | other | ✅ | 139 | `void FUN_009a33e0(int param_1,int param_2,int param_3)` |
| 0x009a35c0 | FUN_009a35c0 | scan | other | ✅ | 68 | `undefined4 * __thiscall FUN_009a35c0(undefined4 *param_1,byte param_2)` |
| 0x009a36a0 | FUN_009a36a0 | caller | other | — | 190 | `` |
| 0x009a38f0 | FUN_009a38f0 | scan | other | ✅ | 14 | `void __thiscall FUN_009a38f0(int param_1,int param_2)` |
| 0x009a3940 | FUN_009a3940 | scan | other | ✅ | 54 | `undefined4 * __thiscall FUN_009a3940(undefined4 *param_1,undefined4 param_2)` |
| 0x009a39e0 | FUN_009a39e0 | scan | other | ✅ | 38 | `undefined4 __fastcall FUN_009a39e0(int *param_1)` |
| 0x009a3a40 | FUN_009a3a40 | scan | other | ✅ | 70 | `undefined4 * __thiscall FUN_009a3a40(undefined4 *param_1,byte param_2)` |
| 0x009a3b30 | FUN_009a3b30 | caller | other | — | 99 | `` |
| 0x009a3c40 | FUN_009a3c40 | scan | other | ✅ | 17 | `void __thiscall FUN_009a3c40(int param_1,int param_2)` |
| 0x009a3cb0 | FUN_009a3cb0 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009a3cb0(undefined4 param_1,byte param_2)` |
| 0x009a3ce0 | FUN_009a3ce0 | scan | other | ✅ | 124 | `void __fastcall FUN_009a3ce0(undefined4 *param_1)` |
| 0x009a3e70 | FUN_009a3e70 | caller | other | — | 719 | `` |
| 0x009a4750 | FUN_009a4750 | scan | other | ✅ | 7 | `void FUN_009a4750(void)` |
| 0x009a4780 | FUN_009a4780 | scan | other | ✅ | 73 | `void __fastcall FUN_009a4780(int param_1)` |
| 0x009a4860 | FUN_009a4860 | scan | other | ✅ | 139 | `void FUN_009a4860(int param_1,int param_2,int param_3)` |
| 0x009a4a40 | FUN_009a4a40 | scan | other | ✅ | 43 | `undefined4 * __thiscall FUN_009a4a40(undefined4 *param_1,byte param_2)` |
| 0x009a4ae0 | FUN_009a4ae0 | scan | other | ✅ | 24 | `uint __thiscall FUN_009a4ae0(int param_1,undefined4 param_2)` |
| 0x009a4b20 | FUN_009a4b20 | caller | other | — | 30 | `` |
| 0x009a4bb0 | FUN_009a4bb0 | scan | other | ✅ | 26 | `int __fastcall FUN_009a4bb0(undefined4 *param_1)` |
| 0x009a4c00 | FUN_009a4c00 | scan | other | ✅ | 35 | `int __fastcall FUN_009a4c00(int *param_1)` |
| 0x009a4c60 | FUN_009a4c60 | scan | other | ✅ | 354 | `void __thiscall FUN_009a4c60(int *param_1,int param_2)` |
| 0x009a51e0 | FUN_009a51e0 | scan | other | ✅ | 28 | `void __fastcall FUN_009a51e0(int *param_1)` |
| 0x009a5230 | FUN_009a5230 | scan | other | ✅ | 69 | `void __thiscall FUN_009a5230(int *param_1,int param_2)` |
| 0x009a5300 | FUN_009a5300 | scan | other | ✅ | 42 | `undefined4 __fastcall FUN_009a5300(int *param_1)` |
| 0x009a5370 | FUN_009a5370 | scan | other | ✅ | 25 | `void __fastcall FUN_009a5370(int *param_1)` |
| 0x009a53b0 | FUN_009a53b0 | scan | other | ✅ | 35 | `undefined4 * __fastcall FUN_009a53b0(undefined4 *param_1,char *param_2)` |
| 0x009a5420 | FUN_009a5420 | scan | other | ✅ | 84 | `void __fastcall FUN_009a5420(int *param_1)` |
| 0x009a5550 | FUN_009a5550 | scan | other | ✅ | 87 | `void __fastcall FUN_009a5550(undefined4 *param_1)` |
| 0x009a5690 | FUN_009a5690 | scan | other | ✅ | 40 | `void FUN_009a5690(void)` |
| 0x009a5720 | FUN_009a5720 | scan | other | ✅ | 11 | `undefined4 FUN_009a5720(void)` |
| 0x009a5740 | FUN_009a5740 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009a5740(undefined4 param_1,byte param_2)` |
| 0x009a5770 | FUN_009a5770 | scan | other | ✅ | 98 | `void __fastcall FUN_009a5770(undefined4 *param_1)` |
| 0x009a58c0 | FUN_009a58c0 | scan | other | ✅ | 43 | `void __fastcall FUN_009a58c0(int param_1)` |
| 0x009a59e0 | FUN_009a59e0 | scan | other | ✅ | 33 | `` |
| 0x009a5a70 | FUN_009a5a70 | scan | other | ✅ | 325 | `void __thiscall FUN_009a5a70(int param_1,undefined4 *param_2,char *param_3)` |
| 0x009a5f10 | FUN_009a5f10 | scan | other | ✅ | 159 | `undefined4 * __thiscall FUN_009a5f10(int *param_1,undefined4 *param_2,undefined4 *param_3)` |
| 0x009a60e0 | FUN_009a60e0 | scan | other | ✅ | 189 | `undefined4 __fastcall FUN_009a60e0(int param_1,int param_2)` |
| 0x009a6360 | FUN_009a6360 | scan | other | ✅ | 168 | `undefined4 * __fastcall FUN_009a6360(int *param_1)` |
| 0x009a6580 | FUN_009a6580 | scan | other | ✅ | 169 | `void * __fastcall FUN_009a6580(int param_1,int *param_2)` |
| 0x009a67a0 | FUN_009a67a0 | scan | other | ✅ | 74 | `void __fastcall FUN_009a67a0(int param_1,LONG *param_2)` |
| 0x009a6880 | FUN_009a6880 | scan | other | ✅ | 487 | `undefined4 __thiscall FUN_009a6880(int param_1,undefined4 *param_2)` |
| 0x009a6ea0 | FUN_009a6ea0 | scan | other | ✅ | 333 | `undefined4 __fastcall FUN_009a6ea0(LPVOID param_1,int param_2)` |
| 0x009a73a0 | FUN_009a73a0 | scan | other | ✅ | 37 | `undefined4 FUN_009a73a0(void)` |
| 0x009a7400 | FUN_009a7400 | scan | other | ✅ | 19 | `undefined4 FUN_009a7400(void)` |
| 0x009a7430 | FUN_009a7430 | scan | other | ✅ | 134 | `undefined4 FUN_009a7430(void)` |
| 0x009a7610 | FUN_009a7610 | scan | other | ✅ | 56 | `void FUN_009a7610(void)` |
| 0x009a76d0 | FUN_009a76d0 | scan | other | ✅ | 53 | `undefined4 FUN_009a76d0(undefined4 *param_1)` |
| 0x009a7780 | FUN_009a7780 | scan | other | ✅ | 26 | `bool __fastcall FUN_009a7780(int param_1)` |
| 0x009a77f0 | FUN_009a77f0 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009a77f0(undefined4 param_1,byte param_2)` |
| 0x009a7820 | FUN_009a7820 | scan | other | ✅ | 60 | `void __fastcall FUN_009a7820(undefined4 *param_1)` |
| 0x009a78f0 | FUN_009a78f0 | scan | other | ✅ | 77 | `` |
| 0x009a79c0 | FUN_009a79c0 | scan | other | ✅ | 69 | `` |
| 0x009a7a70 | FUN_009a7a70 | scan | other | ✅ | 71 | `` |
| 0x009a7b30 | FUN_009a7b30 | scan | other | ✅ | 23 | `void __thiscall FUN_009a7b30(int param_1,int *param_2,char param_3)` |
| 0x009a7b70 | FUN_009a7b70 | scan | other | ✅ | 18 | `void __thiscall FUN_009a7b70(int param_1,int *param_2,char param_3)` |
| 0x009a7ba0 | FUN_009a7ba0 | scan | other | ✅ | 48 | `void __thiscall FUN_009a7ba0(int param_1,int *param_2,char param_3)` |
| 0x009a7c50 | FUN_009a7c50 | scan | other | ✅ | 16 | `undefined4 * __thiscall FUN_009a7c50(undefined4 *param_1,byte param_2)` |
| 0x009a7c80 | FUN_009a7c80 | scan | other | ✅ | 432 | `void __fastcall FUN_009a7c80(undefined4 param_1,int *param_2,int param_3)` |
| 0x009a83c0 | FUN_009a83c0 | scan | other | ✅ | 16 | `void __fastcall FUN_009a83c0(undefined4 param_1,undefined2 param_2)` |
| 0x009a83f0 | FUN_009a83f0 | scan | other | ✅ | 17 | `void FUN_009a83f0(undefined4 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)` |
| 0x009a8430 | FUN_009a8430 | scan | other | ✅ | 8 | `void FUN_009a8430(void)` |
| 0x009a8470 | FUN_009a8470 | scan | other | ✅ | 8 | `void FUN_009a8470(void)` |
| 0x009a8490 | FUN_009a8490 | scan | other | ✅ | 8 | `void FUN_009a8490(void)` |
| 0x009a84b0 | FUN_009a84b0 | scan | other | ✅ | 8 | `void FUN_009a84b0(void)` |
| 0x009a84d0 | FUN_009a84d0 | scan | other | ✅ | 8 | `void FUN_009a84d0(void)` |
| 0x009a84f0 | FUN_009a84f0 | scan | other | ✅ | 8 | `void FUN_009a84f0(void)` |
| 0x009a8510 | FUN_009a8510 | scan | other | ✅ | 8 | `void FUN_009a8510(void)` |
| 0x009a8530 | FUN_009a8530 | scan | other | ✅ | 8 | `void FUN_009a8530(void)` |
| 0x009a8550 | FUN_009a8550 | scan | other | ✅ | 8 | `void FUN_009a8550(void)` |
| 0x009a8570 | FUN_009a8570 | scan | other | ✅ | 8 | `void FUN_009a8570(void)` |
| 0x009a8590 | FUN_009a8590 | scan | other | ✅ | 8 | `void FUN_009a8590(void)` |
| 0x009a85b0 | FUN_009a85b0 | scan | other | ✅ | 8 | `void FUN_009a85b0(void)` |
| 0x009a85d0 | FUN_009a85d0 | scan | other | ✅ | 8 | `void FUN_009a85d0(void)` |
| 0x009a85f0 | FUN_009a85f0 | scan | other | ✅ | 8 | `void FUN_009a85f0(void)` |
| 0x009a8610 | FUN_009a8610 | scan | other | ✅ | 8 | `void FUN_009a8610(void)` |
| 0x009a8630 | FUN_009a8630 | scan | other | ✅ | 8 | `void FUN_009a8630(void)` |
| 0x009a8650 | FUN_009a8650 | scan | other | ✅ | 8 | `void FUN_009a8650(void)` |
| 0x009a8670 | FUN_009a8670 | scan | other | ✅ | 8 | `void FUN_009a8670(void)` |
| 0x009a8690 | FUN_009a8690 | scan | other | ✅ | 8 | `void FUN_009a8690(void)` |
| 0x009a86b0 | FUN_009a86b0 | scan | other | ✅ | 8 | `void FUN_009a86b0(void)` |
| 0x009a86d0 | FUN_009a86d0 | scan | other | ✅ | 8 | `void FUN_009a86d0(void)` |
| 0x009a86f0 | FUN_009a86f0 | scan | other | ✅ | 8 | `void FUN_009a86f0(void)` |
| 0x009a8710 | FUN_009a8710 | scan | other | ✅ | 8 | `void FUN_009a8710(void)` |
| 0x009a8730 | FUN_009a8730 | scan | other | ✅ | 8 | `void FUN_009a8730(void)` |
| 0x009a8750 | FUN_009a8750 | scan | other | ✅ | 8 | `void FUN_009a8750(void)` |
| 0x009a8770 | FUN_009a8770 | scan | other | ✅ | 8 | `void FUN_009a8770(void)` |
| 0x009a8790 | FUN_009a8790 | scan | other | ✅ | 8 | `void FUN_009a8790(void)` |
| 0x009a87b0 | FUN_009a87b0 | scan | other | ✅ | 8 | `void FUN_009a87b0(void)` |
| 0x009a87d0 | FUN_009a87d0 | scan | other | ✅ | 8 | `void FUN_009a87d0(void)` |
| 0x009a87f0 | FUN_009a87f0 | scan | other | ✅ | 8 | `void FUN_009a87f0(void)` |
| 0x009a8810 | FUN_009a8810 | scan | other | ✅ | 8 | `void FUN_009a8810(void)` |
| 0x009a8830 | FUN_009a8830 | scan | other | ✅ | 13 | `void FUN_009a8830(undefined4 param_1,undefined4 param_2)` |
| 0x009a8860 | FUN_009a8860 | scan | other | ✅ | 8 | `void FUN_009a8860(void)` |
| 0x009a8880 | FUN_009a8880 | scan | other | ✅ | 8 | `void FUN_009a8880(void)` |
| 0x009a88a0 | FUN_009a88a0 | scan | other | ✅ | 8 | `void FUN_009a88a0(void)` |
| 0x009a88c0 | FUN_009a88c0 | scan | other | ✅ | 8 | `void FUN_009a88c0(void)` |
| 0x009a88e0 | FUN_009a88e0 | scan | other | ✅ | 8 | `void FUN_009a88e0(void)` |
| 0x009a8900 | FUN_009a8900 | scan | other | ✅ | 8 | `void FUN_009a8900(void)` |
| 0x009a8920 | FUN_009a8920 | scan | other | ✅ | 8 | `void FUN_009a8920(void)` |
| 0x009a8940 | FUN_009a8940 | scan | other | ✅ | 8 | `void FUN_009a8940(void)` |
| 0x009a8960 | FUN_009a8960 | scan | other | ✅ | 8 | `void FUN_009a8960(void)` |
| 0x009a89a0 | FUN_009a89a0 | scan | other | ✅ | 8 | `void FUN_009a89a0(void)` |
| 0x009a89e0 | FUN_009a89e0 | scan | other | ✅ | 8 | `void FUN_009a89e0(void)` |
| 0x009a8a20 | FUN_009a8a20 | scan | other | ✅ | 8 | `void FUN_009a8a20(void)` |
| 0x009a8a40 | FUN_009a8a40 | scan | other | ✅ | 8 | `void FUN_009a8a40(void)` |
| 0x009a8a60 | FUN_009a8a60 | scan | other | ✅ | 8 | `void FUN_009a8a60(void)` |
| 0x009a8a80 | FUN_009a8a80 | scan | other | ✅ | 8 | `void FUN_009a8a80(void)` |
| 0x009a8aa0 | FUN_009a8aa0 | scan | other | ✅ | 8 | `void FUN_009a8aa0(void)` |
| 0x009a8ac0 | FUN_009a8ac0 | scan | other | ✅ | 8 | `void FUN_009a8ac0(void)` |
| 0x009a8ae0 | FUN_009a8ae0 | scan | other | ✅ | 8 | `void FUN_009a8ae0(void)` |
| 0x009a8b00 | FUN_009a8b00 | scan | other | ✅ | 8 | `void FUN_009a8b00(void)` |
| 0x009a8b20 | FUN_009a8b20 | scan | other | ✅ | 8 | `void FUN_009a8b20(void)` |
| 0x009a8b40 | FUN_009a8b40 | scan | other | ✅ | 8 | `void FUN_009a8b40(void)` |
| 0x009a8b60 | FUN_009a8b60 | scan | other | ✅ | 8 | `void FUN_009a8b60(void)` |
| 0x009a8bc0 | FUN_009a8bc0 | scan | other | ✅ | 5 | `void FUN_009a8bc0(void)` |
| 0x009a8c20 | FUN_009a8c20 | scan | other | ✅ | 10 | `void FUN_009a8c20(void)` |
| 0x009a8c50 | FUN_009a8c50 | scan | other | ✅ | 8 | `void FUN_009a8c50(void)` |
| 0x009a8c70 | FUN_009a8c70 | scan | other | ✅ | 8 | `void FUN_009a8c70(void)` |
| 0x009a8cb0 | FUN_009a8cb0 | scan | other | ✅ | 8 | `void FUN_009a8cb0(void)` |
| 0x009a8cd0 | FUN_009a8cd0 | scan | other | ✅ | 8 | `void FUN_009a8cd0(void)` |
| 0x009a8cf0 | FUN_009a8cf0 | scan | other | ✅ | 8 | `void FUN_009a8cf0(void)` |
| 0x009a8d10 | FUN_009a8d10 | scan | other | ✅ | 8 | `void FUN_009a8d10(void)` |
| 0x009a8d30 | FUN_009a8d30 | scan | other | ✅ | 8 | `void FUN_009a8d30(void)` |
| 0x009a8d50 | FUN_009a8d50 | scan | other | ✅ | 8 | `void FUN_009a8d50(void)` |
| 0x009a8d70 | FUN_009a8d70 | scan | other | ✅ | 8 | `void FUN_009a8d70(void)` |
| 0x009a8d90 | FUN_009a8d90 | scan | other | ✅ | 8 | `void FUN_009a8d90(void)` |
| 0x009a8db0 | FUN_009a8db0 | scan | other | ✅ | 8 | `void FUN_009a8db0(void)` |
| 0x009a8dd0 | FUN_009a8dd0 | scan | other | ✅ | 8 | `void FUN_009a8dd0(void)` |
| 0x009a8df0 | FUN_009a8df0 | scan | other | ✅ | 8 | `void FUN_009a8df0(void)` |
| 0x009a8e10 | FUN_009a8e10 | scan | other | ✅ | 8 | `void FUN_009a8e10(void)` |
| 0x009a8e30 | FUN_009a8e30 | scan | other | ✅ | 8 | `void FUN_009a8e30(void)` |
| 0x009a8e50 | FUN_009a8e50 | scan | other | ✅ | 8 | `void FUN_009a8e50(void)` |
| 0x009a8e70 | FUN_009a8e70 | scan | other | ✅ | 8 | `void FUN_009a8e70(void)` |
| 0x009a8e90 | FUN_009a8e90 | scan | other | ✅ | 8 | `void FUN_009a8e90(void)` |
| 0x009a8eb0 | FUN_009a8eb0 | scan | other | ✅ | 8 | `void FUN_009a8eb0(void)` |
| 0x009a8ed0 | FUN_009a8ed0 | scan | other | ✅ | 8 | `void FUN_009a8ed0(void)` |
| 0x009a8f10 | FUN_009a8f10 | scan | other | ✅ | 8 | `void FUN_009a8f10(void)` |
| 0x009a8f30 | FUN_009a8f30 | scan | other | ✅ | 8 | `void FUN_009a8f30(void)` |
| 0x009a8f50 | FUN_009a8f50 | scan | other | ✅ | 8 | `void FUN_009a8f50(void)` |
| 0x009a8f70 | FUN_009a8f70 | scan | other | ✅ | 8 | `void FUN_009a8f70(void)` |
| 0x009a8f90 | FUN_009a8f90 | scan | other | ✅ | 8 | `void FUN_009a8f90(void)` |
| 0x009a8fb0 | FUN_009a8fb0 | scan | other | ✅ | 8 | `void FUN_009a8fb0(void)` |
| 0x009a8fd0 | FUN_009a8fd0 | scan | other | ✅ | 8 | `void FUN_009a8fd0(void)` |
| 0x009a8ff0 | FUN_009a8ff0 | scan | other | ✅ | 8 | `void FUN_009a8ff0(void)` |
| 0x009a9010 | FUN_009a9010 | scan | other | ✅ | 8 | `void FUN_009a9010(void)` |
| 0x009a9030 | FUN_009a9030 | scan | other | ✅ | 8 | `void FUN_009a9030(void)` |
| 0x009a9050 | FUN_009a9050 | scan | other | ✅ | 8 | `void FUN_009a9050(void)` |
| 0x009a9070 | FUN_009a9070 | scan | other | ✅ | 8 | `void FUN_009a9070(void)` |
| 0x009a9090 | FUN_009a9090 | scan | other | ✅ | 8 | `void FUN_009a9090(void)` |
| 0x009a90b0 | FUN_009a90b0 | scan | other | ✅ | 8 | `void FUN_009a90b0(void)` |
| 0x009a90d0 | FUN_009a90d0 | scan | other | ✅ | 8 | `void FUN_009a90d0(void)` |
| 0x009a90f0 | FUN_009a90f0 | scan | other | ✅ | 8 | `void FUN_009a90f0(void)` |
| 0x009a9110 | FUN_009a9110 | scan | other | ✅ | 8 | `void FUN_009a9110(void)` |
| 0x009a9130 | FUN_009a9130 | scan | other | ✅ | 8 | `void FUN_009a9130(void)` |
| 0x009a9150 | FUN_009a9150 | scan | other | ✅ | 8 | `void FUN_009a9150(void)` |
| 0x009a9170 | FUN_009a9170 | scan | other | ✅ | 8 | `void FUN_009a9170(void)` |
| 0x009a9190 | FUN_009a9190 | scan | other | ✅ | 8 | `void FUN_009a9190(void)` |
| 0x009a91b0 | FUN_009a91b0 | scan | other | ✅ | 8 | `void FUN_009a91b0(void)` |
| 0x009a91d0 | FUN_009a91d0 | scan | other | ✅ | 8 | `void FUN_009a91d0(void)` |
| 0x009a91f0 | FUN_009a91f0 | scan | other | ✅ | 8 | `void FUN_009a91f0(void)` |
| 0x009a9210 | FUN_009a9210 | scan | other | ✅ | 8 | `void FUN_009a9210(void)` |
| 0x009a9230 | FUN_009a9230 | scan | other | ✅ | 8 | `void FUN_009a9230(void)` |
| 0x009a9250 | FUN_009a9250 | scan | other | ✅ | 8 | `void FUN_009a9250(void)` |
| 0x009a9270 | FUN_009a9270 | scan | other | ✅ | 8 | `void FUN_009a9270(void)` |
| 0x009a9290 | FUN_009a9290 | scan | other | ✅ | 8 | `void FUN_009a9290(void)` |
| 0x009a92b0 | FUN_009a92b0 | scan | other | ✅ | 8 | `void FUN_009a92b0(void)` |
| 0x009a92d0 | FUN_009a92d0 | scan | other | ✅ | 8 | `void FUN_009a92d0(void)` |
| 0x009a92f0 | FUN_009a92f0 | scan | other | ✅ | 8 | `void FUN_009a92f0(void)` |
| 0x009a9310 | FUN_009a9310 | scan | other | ✅ | 8 | `void FUN_009a9310(void)` |
| 0x009a9330 | FUN_009a9330 | scan | other | ✅ | 8 | `void FUN_009a9330(void)` |
| 0x009a9350 | FUN_009a9350 | scan | other | ✅ | 8 | `void FUN_009a9350(void)` |
| 0x009a9370 | FUN_009a9370 | scan | other | ✅ | 8 | `void FUN_009a9370(void)` |
| 0x009a9390 | FUN_009a9390 | scan | other | ✅ | 8 | `void FUN_009a9390(void)` |
| 0x009a93b0 | FUN_009a93b0 | scan | other | ✅ | 8 | `void FUN_009a93b0(void)` |
| 0x009a93d0 | FUN_009a93d0 | scan | other | ✅ | 8 | `void FUN_009a93d0(void)` |
| 0x009a93f0 | FUN_009a93f0 | scan | other | ✅ | 8 | `void FUN_009a93f0(void)` |
| 0x009a9410 | FUN_009a9410 | scan | other | ✅ | 8 | `void FUN_009a9410(void)` |
| 0x009a9430 | FUN_009a9430 | scan | other | ✅ | 18 | `` |
| 0x009a9470 | FUN_009a9470 | scan | other | ✅ | 8 | `void FUN_009a9470(void)` |
| 0x009a9490 | FUN_009a9490 | scan | other | ✅ | 8 | `void FUN_009a9490(void)` |
| 0x009a94b0 | FUN_009a94b0 | scan | other | ✅ | 19 | `` |
| 0x009a94f0 | FUN_009a94f0 | scan | other | ✅ | 8 | `void FUN_009a94f0(void)` |
| 0x009a9510 | FUN_009a9510 | scan | other | ✅ | 8 | `void FUN_009a9510(void)` |
| 0x009a9530 | FUN_009a9530 | scan | other | ✅ | 20 | `` |
| 0x009a9580 | FUN_009a9580 | scan | other | ✅ | 20 | `` |
| 0x009a95d0 | FUN_009a95d0 | scan | other | ✅ | 20 | `` |
| 0x009a9620 | FUN_009a9620 | scan | other | ✅ | 21 | `` |
| 0x009a9660 | FUN_009a9660 | scan | other | ✅ | 17 | `` |
| 0x009a96a0 | FUN_009a96a0 | scan | other | ✅ | 37 | `undefined4 * __fastcall FUN_009a96a0(undefined4 *param_1)` |
| 0x009a9740 | FUN_009a9740 | scan | other | ✅ | 26 | `undefined4 * __thiscall FUN_009a9740(undefined4 *param_1,byte param_2)` |
| 0x009a97c0 | FUN_009a97c0 | scan | other | ✅ | 40 | `void __thiscall FUN_009a97c0(int param_1,int param_2,int param_3)` |
| 0x009a9820 | FUN_009a9820 | scan | other | ✅ | 85 | `size_t __thiscall FUN_009a9820(int param_1,void *param_2,size_t param_3,int param_4)` |
| 0x009a98f0 | FUN_009a98f0 | scan | other | ✅ | 114 | `uint __thiscall FUN_009a98f0(int param_1,void *param_2,int param_3,int param_4)` |
| 0x009a9a20 | FUN_009a9a20 | scan | other | ✅ | 19 | `` |
| 0x009a9a60 | FUN_009a9a60 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009a9a60(undefined4 param_1,byte param_2)` |
| 0x009a9a90 | FUN_009a9a90 | scan | other | ✅ | 43 | `` |
| 0x009a9b60 | FUN_009a9b60 | scan | other | ✅ | 185 | `void __fastcall FUN_009a9b60(undefined4 *param_1)` |
| 0x009a9db0 | FUN_009a9db0 | scan | other | ✅ | 468 | `void __thiscall FUN_009a9db0(int param_1,undefined4 param_2)` |
| 0x009aa420 | FUN_009aa420 | scan | other | ✅ | 193 | `undefined4 __fastcall FUN_009aa420(int param_1)` |
| 0x009aa6d0 | FUN_009aa6d0 | scan | other | ✅ | 166 | `undefined4 __fastcall FUN_009aa6d0(int *param_1)` |
| 0x009aa900 | FUN_009aa900 | scan | other | ✅ | 264 | `float10 __fastcall FUN_009aa900(int *param_1)` |
| 0x009aacf0 | FUN_009aacf0 | scan | other | ✅ | 61 | `void __fastcall FUN_009aacf0(int param_1)` |
| 0x009aada0 | FUN_009aada0 | scan | other | ✅ | 435 | `void __fastcall FUN_009aada0(int *param_1)` |
| 0x009ab3b0 | FUN_009ab3b0 | scan | other | ✅ | 96 | `void __fastcall FUN_009ab3b0(int param_1)` |
| 0x009ab510 | FUN_009ab510 | scan | other | ✅ | 259 | `undefined4 __thiscall FUN_009ab510(int param_1,int param_2,char param_3)` |
| 0x009ab8a0 | FUN_009ab8a0 | scan | other | ✅ | 528 | `void __fastcall FUN_009ab8a0(int param_1)` |
| 0x009ac030 | FUN_009ac030 | scan | other | ✅ | 527 | `undefined4 * __fastcall FUN_009ac030(undefined4 *param_1)` |
| 0x009ac7a0 | FUN_009ac7a0 | scan | other | ✅ | 115 | `undefined4 * __thiscall FUN_009ac7a0(undefined4 *param_1,byte param_2)` |
| 0x009ac900 | FUN_009ac900 | scan | other | ✅ | 151 | `void FUN_009ac900(void)` |
| 0x009acaf0 | FUN_009acaf0 | scan | other | ✅ | 405 | `` |
| 0x009ad0c0 | FUN_009ad0c0 | scan | other | ✅ | 285 | `void FUN_009ad0c0(int *param_1)` |
| 0x009ad490 | FUN_009ad490 | scan | other | ✅ | 137 | `void __thiscall FUN_009ad490(int param_1,int param_2)` |
| 0x009ad6a0 | FUN_009ad6a0 | scan | other | ✅ | 295 | `int FUN_009ad6a0(undefined4 param_1)` |
| 0x009ada70 | FUN_009ada70 | scan | other | ✅ | 45 | `undefined4 * __thiscall FUN_009ada70(undefined4 *param_1,byte param_2)` |
| 0x009adb00 | FUN_009adb00 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009adb00(int param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009adb30 | FUN_009adb30 | scan | other | ✅ | 11 | `void __thiscall FUN_009adb30(int param_1,undefined4 param_2)` |
| 0x009adb70 | FUN_009adb70 | scan | other | ✅ | 10 | `void __fastcall FUN_009adb70(int param_1)` |
| 0x009adb90 | FUN_009adb90 | scan | other | ✅ | 70 | `undefined4 * __thiscall FUN_009adb90(undefined4 *param_1,byte param_2)` |
| 0x009adc70 | FUN_009adc70 | scan | other | ✅ | 64 | `void __thiscall FUN_009adc70(int param_1,float param_2)` |
| 0x009add40 | FUN_009add40 | scan | other | ✅ | 11 | `void __fastcall FUN_009add40(int param_1)` |
| 0x009add60 | FUN_009add60 | scan | other | ✅ | 11 | `void __fastcall FUN_009add60(int param_1)` |
| 0x009add80 | FUN_009add80 | scan | other | ✅ | 33 | `void __thiscall FUN_009add80(int param_1,float param_2)` |
| 0x009addf0 | FUN_009addf0 | scan | other | ✅ | 143 | `void __thiscall FUN_009addf0(int param_1,int param_2,int param_3)` |
| 0x009adfd0 | FUN_009adfd0 | scan | other | ✅ | 18 | `float10 __fastcall FUN_009adfd0(int param_1)` |
| 0x009ae010 | FUN_009ae010 | scan | other | ✅ | 38 | `undefined4 __fastcall FUN_009ae010(int param_1)` |
| 0x009ae080 | FUN_009ae080 | scan | other | ✅ | 92 | `` |
| 0x009ae1d0 | FUN_009ae1d0 | scan | other | ✅ | 20 | `undefined4 * __thiscall FUN_009ae1d0(undefined4 *param_1,byte param_2)` |
| 0x009ae210 | FUN_009ae210 | scan | other | ✅ | 84 | `void __thiscall FUN_009ae210(int param_1,int *param_2)` |
| 0x009ae2f0 | FUN_009ae2f0 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009ae2f0(undefined4 param_1,byte param_2)` |
| 0x009ae320 | FUN_009ae320 | scan | other | ✅ | 76 | `void __fastcall FUN_009ae320(undefined4 *param_1)` |
| 0x009ae400 | FUN_009ae400 | scan | other | ✅ | 15 | `void __thiscall FUN_009ae400(int param_1,undefined4 param_2)` |
| 0x009ae430 | FUN_009ae430 | scan | other | ✅ | 61 | `void __fastcall FUN_009ae430(int param_1)` |
| 0x009ae4c0 | FUN_009ae4c0 | scan | other | ✅ | 170 | `int __thiscall FUN_009ae4c0(int param_1,uint param_2,int param_3,int param_4)` |
| 0x009ae670 | FUN_009ae670 | scan | other | ✅ | 16 | `undefined4 * __thiscall FUN_009ae670(undefined4 *param_1,byte param_2)` |
| 0x009ae6a0 | FUN_009ae6a0 | scan | other | ✅ | 85 | `void __thiscall FUN_009ae6a0(int param_1,undefined4 param_2,size_t param_3,undefined4 *param_4)` |
| 0x009ae7b0 | FUN_009ae7b0 | scan | other | ✅ | 38 | `int __thiscall FUN_009ae7b0(int param_1,int param_2,int *param_3,undefined1 *param_4)` |
| 0x009ae820 | FUN_009ae820 | scan | other | ✅ | 40 | `uint __thiscall FUN_009ae820(int *param_1,byte param_2)` |
| 0x009ae880 | FUN_009ae880 | callee | other | ✅ | 223 | `int __thiscall FUN_009ae880(uint *param_1,undefined4 param_2,int param_3,uint param_4)` |
| 0x009ae880 | FUN_009ae880 | caller | other | — | 223 | `` |
| 0x009aeb00 | FUN_009aeb00 | callee | other | ✅ | 1751 | `else if (((int)uVar19 >> 9 != 0) && ((uint)((int)uVar19 >> 9) <= pbVar30)) break;` |
| 0x009b06f0 | FUN_009b06f0 | callee | other | ✅ | 42 | `void __thiscall FUN_009b06f0(int *param_1,int param_2,uint param_3)` |
| 0x009b06f0 | FUN_009b06f0 | caller | other | — | 42 | `` |
| 0x009b0760 | FUN_009b0760 | scan | other | ✅ | 53 | `undefined4 * __thiscall FUN_009b0760(undefined4 *param_1,undefined4 param_2)` |
| 0x009b0830 | FUN_009b0830 | scan | other | ✅ | 19 | `undefined4 * __thiscall FUN_009b0830(undefined4 *param_1,byte param_2)` |
| 0x009b0870 | FUN_009b0870 | scan | other | ✅ | 8 | `void __fastcall FUN_009b0870(undefined4 *param_1)` |
| 0x009b0890 | FUN_009b0890 | scan | other | ✅ | 42 | `void __fastcall FUN_009b0890(int *param_1)` |
| 0x009b0920 | FUN_009b0920 | scan | other | ✅ | 93 | `undefined4 __thiscall FUN_009b0920(int *param_1,undefined4 *param_2)` |
| 0x009b0a50 | FUN_009b0a50 | scan | other | ✅ | 17 | `void __fastcall FUN_009b0a50(int param_1)` |
| 0x009b0a90 | FUN_009b0a90 | scan | other | ✅ | 34 | `void __thiscall FUN_009b0a90(int param_1,int param_2,int param_3)` |
| 0x009b0b00 | FUN_009b0b00 | scan | other | ✅ | 38 | `void __thiscall FUN_009b0b00(int param_1,int param_2,int param_3)` |
| 0x009b0b70 | FUN_009b0b70 | scan | other | ✅ | 75 | `else if (param_1[6] == 2) {` |
| 0x009b0c70 | FUN_009b0c70 | scan | other | ✅ | 68 | `float * __thiscall FUN_009b0c70(int *param_1,float *param_2,uint param_3,uint param_4)` |
| 0x009b0d50 | FUN_009b0d50 | scan | other | ✅ | 48 | `` |
| 0x009b0e00 | FUN_009b0e00 | scan | other | ✅ | 70 | `uint __fastcall FUN_009b0e00(int param_1,uint param_2,uint param_3)` |
| 0x009b0ea0 | FUN_009b0ea0 | scan | other | ✅ | 49 | `` |
| 0x009b0f20 | FUN_009b0f20 | scan | other | ✅ | 12 | `void FUN_009b0f20(int param_1,void *param_2)` |
| 0x009b0f40 | FUN_009b0f40 | scan | other | ✅ | 100 | `void __fastcall FUN_009b0f40(int param_1,void *param_2)` |
| 0x009b1040 | FUN_009b1040 | scan | other | ✅ | 106 | `` |
| 0x009b11c0 | FUN_009b11c0 | scan | other | ✅ | 236 | `void __fastcall FUN_009b11c0(int param_1,int param_2)` |
| 0x009b1500 | FUN_009b1500 | scan | other | ✅ | 301 | `void __fastcall FUN_009b1500(int param_1,void *param_2)` |
| 0x009b1940 | FUN_009b1940 | scan | other | ✅ | 182 | `void __fastcall FUN_009b1940(int param_1)` |
| 0x009b1be0 | FUN_009b1be0 | scan | other | ✅ | 75 | `void __fastcall FUN_009b1be0(undefined4 *param_1,undefined4 *param_2,undefined4 *param_3)` |
| 0x009b1c90 | FUN_009b1c90 | scan | other | ✅ | 234 | `void __fastcall FUN_009b1c90(undefined4 *param_1,int param_2,int param_3)` |
| 0x009b1f20 | FUN_009b1f20 | scan | other | ✅ | 14 | `void __fastcall FUN_009b1f20(int param_1)` |
| 0x009b1f70 | FUN_009b1f70 | scan | other | ✅ | 673 | `void __fastcall FUN_009b1f70(int param_1)` |
| 0x009b2b10 | FUN_009b2b10 | scan | other | ✅ | 116 | `void __fastcall FUN_009b2b10(int param_1,int *param_2)` |
| 0x009b2c70 | FUN_009b2c70 | scan | other | ✅ | 512 | `void __fastcall FUN_009b2c70(int param_1)` |
| 0x009b3310 | FUN_009b3310 | scan | other | ✅ | 182 | `uint __fastcall FUN_009b3310(int *param_1,byte *param_2,byte *param_3)` |
| 0x009b3530 | FUN_009b3530 | scan | other | ✅ | 109 | `void __fastcall FUN_009b3530(int *param_1,int param_2)` |
| 0x009b3640 | FUN_009b3640 | scan | other | ✅ | 99 | `void __fastcall FUN_009b3640(int *param_1,int param_2)` |
| 0x009b3750 | FUN_009b3750 | scan | other | ✅ | 6 | `void __fastcall FUN_009b3750(uint *param_1,int param_2,undefined4 param_3,byte param_4)` |
| 0x009b375a | FUN_009b375a | scan | other | ✅ | 232 | `void __fastcall FUN_009b375a(uint *param_1,int param_2)` |
| 0x009b39e0 | FUN_009b39e0 | scan | other | ✅ | 126 | `void __fastcall FUN_009b39e0(int *param_1,int param_2)` |
| 0x009b3b70 | FUN_009b3b70 | scan | other | ✅ | 1336 | `else if (bVar6 == 0) {` |
| 0x009b4be0 | FUN_009b4be0 | scan | other | ✅ | 351 | `void __fastcall FUN_009b4be0(int *param_1,byte *param_2,int param_3,int param_4,byte param_5)` |
| 0x009b4fc0 | FUN_009b4fc0 | scan | other | ✅ | 231 | `void __fastcall FUN_009b4fc0(uint *param_1,int param_2,int param_3,int param_4,int param_5)` |
| 0x009b5250 | FUN_009b5250 | scan | other | ✅ | 333 | `void __fastcall FUN_009b5250(int *param_1,int param_2,int param_3)` |
| 0x009b5610 | FUN_009b5610 | scan | other | ✅ | 123 | `void __fastcall FUN_009b5610(int *param_1,byte *param_2,int param_3,int param_4)` |
| 0x009b5770 | FUN_009b5770 | scan | other | ✅ | 439 | `void __fastcall FUN_009b5770(int param_1)` |
| 0x009b5e40 | FUN_009b5e40 | scan | other | ✅ | 191 | `` |
| 0x009b6120 | FUN_009b6120 | scan | other | ✅ | 19 | `undefined4 * __thiscall FUN_009b6120(undefined4 *param_1,byte param_2)` |
| 0x009b6160 | FUN_009b6160 | scan | other | ✅ | 73 | `undefined4 __fastcall FUN_009b6160(int *param_1)` |
| 0x009b6280 | FUN_009b6280 | scan | other | ✅ | 2 | `undefined2 __fastcall FUN_009b6280(undefined2 *param_1)` |
| 0x009b6290 | FUN_009b6290 | scan | other | ✅ | 100 | `void __fastcall FUN_009b6290(byte *param_1,byte *param_2,byte *param_3,uint param_4)` |
| 0x009b63b0 | FUN_009b63b0 | scan | other | ✅ | 537 | `byte * __fastcall FUN_009b63b0(byte *param_1,undefined4 *param_2,int param_3,int param_4)` |
| 0x009b6a10 | FUN_009b6a10 | scan | other | ✅ | 25 | `void * __fastcall FUN_009b6a10(int param_1,int param_2)` |
| 0x009b6a50 | FUN_009b6a50 | scan | other | ✅ | 32 | `uint __fastcall FUN_009b6a50(uint param_1)` |
| 0x009b6ac0 | FUN_009b6ac0 | scan | other | ✅ | 42 | `int __fastcall FUN_009b6ac0(uint param_1)` |
| 0x009b6b60 | FUN_009b6b60 | scan | other | ✅ | 188 | `undefined4 __fastcall FUN_009b6b60(int param_1,int param_2,int param_3,int *param_4)` |
| 0x009b6e10 | FUN_009b6e10 | scan | other | ✅ | 233 | `void __fastcall FUN_009b6e10(int param_1,int param_2,int param_3)` |
| 0x009b7110 | FUN_009b7110 | scan | other | ✅ | 300 | `undefined4 __fastcall FUN_009b7110(int param_1,int param_2,int param_3)` |
| 0x009b7530 | FUN_009b7530 | scan | other | ✅ | 15 | `uint FUN_009b7530(ushort *param_1,ushort *param_2)` |
| 0x009b7550 | FUN_009b7550 | scan | other | ✅ | 38 | `undefined1 __fastcall FUN_009b7550(uint param_1)` |
| 0x009b75a0 | FUN_009b75a0 | scan | other | ✅ | 136 | `int __fastcall FUN_009b75a0(uint param_1)` |
| 0x009b76f0 | FUN_009b76f0 | scan | other | ✅ | 37 | `undefined4 __fastcall FUN_009b76f0(int param_1,void *param_2,size_t param_3)` |
| 0x009b7740 | FUN_009b7740 | scan | other | ✅ | 51 | `undefined4 __fastcall FUN_009b7740(int param_1,uint param_2)` |
| 0x009b77d0 | FUN_009b77d0 | scan | other | ✅ | 136 | `undefined4 __fastcall FUN_009b77d0(int param_1)` |
| 0x009b7970 | FUN_009b7970 | scan | other | ✅ | 52 | `undefined4 __fastcall FUN_009b7970(uint param_1)` |
| 0x009b79f0 | FUN_009b79f0 | scan | other | ✅ | 125 | `undefined4 __fastcall FUN_009b79f0(uint param_1)` |
| 0x009b7b70 | FUN_009b7b70 | scan | other | ✅ | 41 | `undefined4 __fastcall FUN_009b7b70(int param_1)` |
| 0x009b7c00 | FUN_009b7c00 | scan | other | ✅ | 51 | `char __fastcall FUN_009b7c00(int param_1)` |
| 0x009b7cd0 | FUN_009b7cd0 | scan | other | ✅ | 65 | `uint __fastcall FUN_009b7cd0(uint param_1)` |
| 0x009b7d80 | FUN_009b7d80 | scan | other | ✅ | 53 | `void __fastcall FUN_009b7d80(uint param_1)` |
| 0x009b7e20 | FUN_009b7e20 | scan | other | ✅ | 113 | `uint __fastcall FUN_009b7e20(uint param_1,int param_2)` |
| 0x009b7f80 | FUN_009b7f80 | scan | other | ✅ | 157 | `int __fastcall FUN_009b7f80(int param_1,int param_2)` |
| 0x009b8170 | FUN_009b8170 | scan | other | ✅ | 70 | `int __fastcall FUN_009b8170(int param_1,int param_2)` |
| 0x009b8270 | FUN_009b8270 | scan | other | ✅ | 194 | `undefined4 __fastcall FUN_009b8270(undefined4 param_1,uint *param_2,uint *param_3,uint param_4)` |
| 0x009b84d0 | FUN_009b84d0 | scan | other | ✅ | 187 | `else if (0 < local_c) {` |
| 0x009b8740 | FUN_009b8740 | scan | other | ✅ | 226 | `else if (0 < local_c) {` |
| 0x009b8a10 | FUN_009b8a10 | scan | other | ✅ | 652 | `else if (0 < (int)local_28) {` |
| 0x009b9260 | FUN_009b9260 | scan | other | ✅ | 116 | `void __fastcall FUN_009b9260(uint param_1,int param_2,int param_3,int param_4,float *param_5)` |
| 0x009b9430 | FUN_009b9430 | scan | other | ✅ | 112 | `` |
| 0x009b95f0 | FUN_009b95f0 | scan | other | ✅ | 124 | `` |
| 0x009b97e0 | FUN_009b97e0 | scan | other | ✅ | 149 | `void __fastcall FUN_009b97e0(int param_1,int param_2,int param_3,int param_4,int param_5)` |
| 0x009b9a60 | FUN_009b9a60 | scan | other | ✅ | 632 | `void __fastcall FUN_009b9a60(float *param_1,int param_2,int param_3,int param_4)` |
| 0x009ba2a0 | FUN_009ba2a0 | scan | other | ✅ | 194 | `` |
| 0x009ba500 | FUN_009ba500 | scan | other | ✅ | 128 | `` |
| 0x009ba690 | FUN_009ba690 | scan | other | ✅ | 644 | `else if (fVar4 <= 0.0) {` |
| 0x009bb0e0 | FUN_009bb0e0 | scan | other | ✅ | 130 | `int __fastcall FUN_009bb0e0(int param_1,int param_2,int param_3,int param_4)` |
| 0x009bb260 | FUN_009bb260 | scan | other | ✅ | 45 | `void __fastcall FUN_009bb260(int param_1)` |
| 0x009bb2e0 | FUN_009bb2e0 | scan | other | ✅ | 112 | `undefined4 __fastcall FUN_009bb2e0(int param_1)` |
| 0x009bb410 | FUN_009bb410 | scan | other | ✅ | 2240 | `undefined4 __fastcall FUN_009bb410(int *param_1)` |
| 0x009bd310 | FUN_009bd310 | scan | other | ✅ | 230 | `void __fastcall FUN_009bd310(int param_1)` |
| 0x009bd5d0 | FUN_009bd5d0 | scan | other | ✅ | 20 | `void * __fastcall FUN_009bd5d0(int param_1)` |
| 0x009bd610 | FUN_009bd610 | scan | other | ✅ | 19 | `int __fastcall FUN_009bd610(int param_1)` |
| 0x009bd640 | FUN_009bd640 | scan | other | ✅ | 91 | `int __thiscall FUN_009bd640(int param_1,int *param_2)` |
| 0x009bd740 | FUN_009bd740 | scan | other | ✅ | 87 | `int * __thiscall FUN_009bd740(int *param_1,undefined4 param_2,int *param_3)` |
| 0x009bd8b0 | FUN_009bd8b0 | scan | other | ✅ | 83 | `` |
| 0x009bd9e0 | FUN_009bd9e0 | scan | other | ✅ | 270 | `void __fastcall FUN_009bd9e0(int param_1,int param_2,int param_3,int param_4,int param_5)` |
| 0x009bde50 | FUN_009bde50 | scan | other | ✅ | 108 | `else if ((param_1 == 2) \|\|` |
| 0x009bdf80 | FUN_009bdf80 | scan | other | ✅ | 71 | `int __fastcall FUN_009bdf80(int param_1,int param_2,undefined4 param_3,int param_4)` |
| 0x009be040 | FUN_009be040 | scan | other | ✅ | 17 | `undefined4 * __thiscall FUN_009be040(undefined4 *param_1,byte param_2)` |
| 0x009be080 | FUN_009be080 | scan | other | ✅ | 81 | `undefined4 __thiscall FUN_009be080(int *param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009be1d0 | FUN_009be1d0 | scan | other | ✅ | 26 | `void __fastcall FUN_009be1d0(int param_1)` |
| 0x009be3d0 | FUN_009be3d0 | scan | other | ✅ | 17 | `void __fastcall FUN_009be3d0(int *param_1)` |
| 0x009be410 | FUN_009be410 | scan | other | ✅ | 8 | `void __thiscall FUN_009be410(int param_1,char param_2)` |
| 0x009be430 | FUN_009be430 | scan | other | ✅ | 47 | `undefined4 * __fastcall FUN_009be430(undefined4 *param_1)` |
| 0x009be500 | FUN_009be500 | scan | other | ✅ | 17 | `undefined4 * __thiscall FUN_009be500(undefined4 *param_1,byte param_2)` |
| 0x009be530 | FUN_009be530 | scan | other | ✅ | 43 | `undefined4 __thiscall FUN_009be530(int *param_1,int param_2,int param_3)` |
| 0x009be5b0 | FUN_009be5b0 | scan | other | ✅ | 123 | `void __fastcall FUN_009be5b0(int *param_1)` |
| 0x009be760 | FUN_009be760 | scan | other | ✅ | 21 | `void __fastcall FUN_009be760(int *param_1)` |
| 0x009be7a0 | FUN_009be7a0 | scan | other | ✅ | 21 | `void __fastcall FUN_009be7a0(int *param_1)` |
| 0x009be7e0 | FUN_009be7e0 | scan | other | ✅ | 29 | `bool __fastcall FUN_009be7e0(int param_1)` |
| 0x009be840 | FUN_009be840 | scan | other | ✅ | 21 | `void __fastcall FUN_009be840(int *param_1)` |
| 0x009be880 | FUN_009be880 | scan | other | ✅ | 29 | `void __thiscall FUN_009be880(int param_1,char param_2)` |
| 0x009be8d0 | FUN_009be8d0 | scan | other | ✅ | 22 | `void __thiscall FUN_009be8d0(int param_1,undefined4 param_2)` |
| 0x009be930 | FUN_009be930 | scan | other | ✅ | 36 | `void __thiscall FUN_009be930(int param_1,float param_2)` |
| 0x009be9e0 | FUN_009be9e0 | scan | other | ✅ | 22 | `void __thiscall FUN_009be9e0(int param_1,undefined4 param_2)` |
| 0x009bea40 | FUN_009bea40 | scan | other | ✅ | 29 | `void __fastcall FUN_009bea40(int param_1)` |
| 0x009beaa0 | FUN_009beaa0 | scan | other | ✅ | 24 | `void __fastcall FUN_009beaa0(int *param_1)` |
| 0x009beaf0 | FUN_009beaf0 | scan | other | ✅ | 17 | `undefined4 * __thiscall FUN_009beaf0(undefined4 *param_1,byte param_2)` |
| 0x009beb20 | FUN_009beb20 | scan | other | ✅ | 40 | `void __thiscall FUN_009beb20(int param_1,undefined8 param_2,undefined4 param_3)` |
| 0x009beb90 | FUN_009beb90 | scan | other | ✅ | 24 | `void __thiscall FUN_009beb90(int param_1,undefined8 *param_2)` |
| 0x009bebd0 | FUN_009bebd0 | scan | other | ✅ | 3 | `bool __fastcall FUN_009bebd0(int param_1)` |
| 0x009bebf0 | FUN_009bebf0 | scan | other | ✅ | 12 | `undefined4 __thiscall FUN_009bebf0(int param_1,int param_2)` |
| 0x009bec10 | FUN_009bec10 | scan | other | ✅ | 52 | `void __fastcall FUN_009bec10(int param_1)` |
| 0x009beca0 | FUN_009beca0 | scan | other | ✅ | 6 | `void __thiscall FUN_009beca0(int param_1,undefined1 param_2)` |
| 0x009becb0 | FUN_009becb0 | scan | other | ✅ | 30 | `void __fastcall FUN_009becb0(undefined4 *param_1)` |
| 0x009bed20 | FUN_009bed20 | scan | other | ✅ | 46 | `undefined4 * __fastcall FUN_009bed20(undefined4 *param_1)` |
| 0x009bedd0 | FUN_009bedd0 | scan | other | ✅ | 38 | `undefined4 * __thiscall FUN_009bedd0(undefined4 *param_1,byte param_2)` |
| 0x009bee50 | FUN_009bee50 | scan | other | ✅ | 30 | `void __fastcall FUN_009bee50(undefined4 *param_1)` |
| 0x009beec0 | FUN_009beec0 | scan | other | ✅ | 71 | `undefined4 __fastcall FUN_009beec0(int *param_1)` |
| 0x009befe0 | FUN_009befe0 | scan | other | ✅ | 55 | `void __fastcall FUN_009befe0(int param_1)` |
| 0x009bf0a0 | FUN_009bf0a0 | scan | other | ✅ | 30 | `void __fastcall FUN_009bf0a0(int *param_1)` |
| 0x009bf100 | FUN_009bf100 | scan | other | ✅ | 103 | `void __fastcall FUN_009bf100(int *param_1)` |
| 0x009bf270 | FUN_009bf270 | scan | other | ✅ | 49 | `undefined4 * __thiscall FUN_009bf270(undefined4 *param_1,byte param_2)` |
| 0x009bf330 | FUN_009bf330 | scan | other | ✅ | 97 | `undefined4 __thiscall FUN_009bf330(int param_1,int *param_2)` |
| 0x009bf440 | FUN_009bf440 | scan | other | ✅ | 48 | `void __fastcall FUN_009bf440(int param_1)` |
| 0x009bf4c0 | FUN_009bf4c0 | scan | other | ✅ | 12 | `void __thiscall FUN_009bf4c0(int *param_1,undefined4 param_2)` |
| 0x009bf4e0 | FUN_009bf4e0 | scan | other | ✅ | 105 | `void __fastcall FUN_009bf4e0(int *param_1,undefined4 param_2,int param_3,char param_4)` |
| 0x009bf610 | FUN_009bf610 | scan | other | ✅ | 48 | `undefined4 * __fastcall FUN_009bf610(undefined4 *param_1,undefined4 param_2)` |
| 0x009bf690 | FUN_009bf690 | scan | other | ✅ | 70 | `undefined4 * __thiscall FUN_009bf690(undefined4 *param_1,int param_2)` |
| 0x009bf7b0 | FUN_009bf7b0 | scan | other | ✅ | 21 | `undefined4 * __thiscall FUN_009bf7b0(undefined4 *param_1,byte param_2)` |
| 0x009bf7f0 | FUN_009bf7f0 | scan | other | ✅ | 97 | `void __thiscall FUN_009bf7f0(int param_1,undefined4 *param_2)` |
| 0x009bfd60 | FUN_009bfd60 | scan | other | ✅ | 130 | `void FUN_009bfd60(void)` |
| 0x009bffb0 | FUN_009bffb0 | scan | other | ✅ | 4 | `void FUN_009bffb0(void)` |
| 0x009bffc0 | FUN_009bffc0 | scan | other | ✅ | 4 | `void FUN_009bffc0(void)` |
| 0x009bffd0 | FUN_009bffd0 | scan | other | ✅ | 4 | `void FUN_009bffd0(void)` |
| 0x009bffe0 | FUN_009bffe0 | scan | other | ✅ | 4 | `void FUN_009bffe0(void)` |
| 0x009bfff0 | FUN_009bfff0 | scan | other | ✅ | 24 | `undefined4 * __thiscall FUN_009bfff0(undefined4 *param_1,byte param_2)` |
| 0x009c0090 | FUN_009c0090 | scan | other | ✅ | 15 | `undefined4 __thiscall FUN_009c0090(int param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009c0100 | FUN_009c0100 | scan | other | ✅ | 40 | `void __thiscall FUN_009c0100(int param_1,int param_2,int param_3)` |
| 0x009c0160 | FUN_009c0160 | scan | other | ✅ | 86 | `size_t __thiscall FUN_009c0160(int *param_1,void *param_2,size_t param_3,int param_4)` |
| 0x009c0230 | FUN_009c0230 | scan | other | ✅ | 113 | `uint __thiscall FUN_009c0230(int *param_1,void *param_2,int param_3,int param_4)` |
| 0x009c0350 | FUN_009c0350 | scan | other | ✅ | 59 | `undefined4 __fastcall FUN_009c0350(int *param_1)` |
| 0x009c03e0 | FUN_009c03e0 | scan | other | ✅ | 57 | `undefined8 __fastcall FUN_009c03e0(int *param_1)` |
| 0x009c0470 | FUN_009c0470 | scan | other | ✅ | 33 | `undefined4 __fastcall FUN_009c0470(undefined4 *param_1)` |
| 0x009c04c0 | FUN_009c04c0 | scan | other | ✅ | 56 | `undefined4 __fastcall FUN_009c04c0(undefined4 *param_1,int param_2)` |
| 0x009c0550 | FUN_009c0550 | scan | other | ✅ | 83 | `undefined4 __fastcall FUN_009c0550(undefined4 *param_1,int param_2)` |
| 0x009c0620 | FUN_009c0620 | scan | other | ✅ | 57 | `void __fastcall FUN_009c0620(int *param_1)` |
| 0x009c06b0 | FUN_009c06b0 | scan | other | ✅ | 62 | `int __fastcall FUN_009c06b0(int *param_1,int param_2)` |
| 0x009c0750 | FUN_009c0750 | scan | other | ✅ | 154 | `int __fastcall FUN_009c0750(int *param_1,int *param_2)` |
| 0x009c08f0 | FUN_009c08f0 | scan | other | ✅ | 162 | `undefined4 __fastcall FUN_009c08f0(int *param_1,int *param_2)` |
| 0x009c0ad0 | FUN_009c0ad0 | scan | other | ✅ | 257 | `undefined4 __fastcall FUN_009c0ad0(int *param_1,int *param_2)` |
| 0x009c0e00 | FUN_009c0e00 | scan | other | ✅ | 21 | `undefined4 __fastcall FUN_009c0e00(int *param_1)` |
| 0x009c0e90 | FUN_009c0e90 | scan | other | ✅ | 86 | `undefined4 __fastcall FUN_009c0e90(int *param_1,int *param_2)` |
| 0x009c0f90 | FUN_009c0f90 | scan | other | ✅ | 34 | `int __fastcall FUN_009c0f90(int param_1,int param_2)` |
| 0x009c0ff0 | FUN_009c0ff0 | scan | other | ✅ | 38 | `void __fastcall FUN_009c0ff0(int param_1)` |
| 0x009c1060 | FUN_009c1060 | scan | other | ✅ | 321 | `undefined4 __fastcall FUN_009c1060(void *param_1,int param_2)` |
| 0x009c1430 | FUN_009c1430 | scan | other | ✅ | 388 | `void __fastcall FUN_009c1430(void *param_1)` |
| 0x009c1840 | FUN_009c1840 | scan | other | ✅ | 36 | `undefined4 __fastcall FUN_009c1840(int param_1)` |
| 0x009c18c0 | FUN_009c18c0 | scan | other | ✅ | 577 | `undefined4 __fastcall FUN_009c18c0(int param_1,int *param_2)` |
| 0x009c1f70 | FUN_009c1f70 | scan | other | ✅ | 92 | `void __fastcall FUN_009c1f70(int *param_1,byte *param_2,int param_3)` |
| 0x009c2070 | FUN_009c2070 | scan | other | ✅ | 48 | `void __fastcall FUN_009c2070(int *param_1)` |
| 0x009c20e0 | FUN_009c20e0 | scan | other | ✅ | 220 | `void __fastcall FUN_009c20e0(undefined4 *param_1)` |
| 0x009c2340 | FUN_009c2340 | scan | other | ✅ | 225 | `undefined4 __fastcall FUN_009c2340(int param_1,undefined4 param_2)` |
| 0x009c2610 | FUN_009c2610 | scan | other | ✅ | 261 | `/* WARNING: Removing unreachable block (ram,0x009c2675) */` |
| 0x009c2910 | FUN_009c2910 | scan | other | ✅ | 154 | `undefined4 __fastcall FUN_009c2910(int *param_1,int *param_2)` |
| 0x009c2ad0 | FUN_009c2ad0 | scan | other | ✅ | 20 | `void FUN_009c2ad0(int param_1)` |
| 0x009c2b10 | FUN_009c2b10 | scan | other | ✅ | 26 | `void FUN_009c2b10(int param_1)` |
| 0x009c2b60 | FUN_009c2b60 | scan | other | ✅ | 20 | `void FUN_009c2b60(int param_1)` |
| 0x009c2ba0 | FUN_009c2ba0 | scan | other | ✅ | 25 | `void FUN_009c2ba0(int param_1)` |
| 0x009c2bf0 | FUN_009c2bf0 | scan | other | ✅ | 20 | `void FUN_009c2bf0(int param_1)` |
| 0x009c2c30 | FUN_009c2c30 | scan | other | ✅ | 20 | `void FUN_009c2c30(int param_1)` |
| 0x009c2c70 | FUN_009c2c70 | scan | other | ✅ | 26 | `void FUN_009c2c70(int param_1)` |
| 0x009c2cc0 | FUN_009c2cc0 | scan | other | ✅ | 20 | `void FUN_009c2cc0(int param_1)` |
| 0x009c2d00 | FUN_009c2d00 | scan | other | ✅ | 25 | `void FUN_009c2d00(int param_1)` |
| 0x009c2d50 | FUN_009c2d50 | scan | other | ✅ | 20 | `void FUN_009c2d50(int param_1)` |
| 0x009c2d90 | FUN_009c2d90 | scan | other | ✅ | 16 | `undefined4 * __thiscall FUN_009c2d90(undefined4 *param_1,byte param_2)` |
| 0x009c2dc0 | FUN_009c2dc0 | scan | other | ✅ | 84 | `void FUN_009c2dc0(int param_1)` |
| 0x009c2f10 | FUN_009c2f10 | callee | isaac-keygen | ✅ | 69 | `uint * __thiscall FUN_009c2f10(uint *param_1,uint param_2)` |
| 0x009c2fd0 | FUN_009c2fd0 | callee | other | ✅ | 13 | `void __fastcall FUN_009c2fd0(int param_1)` |
| 0x009c30b0 | FUN_009c30b0 | callee | isaac-randinit | ✅ | 198 | `void __fastcall FUN_009c30b0(int param_1)` |
| 0x009c30b0 | FUN_009c30b0 | caller | isaac-randinit | — | 198 | `` |
| 0x009c3320 | FUN_009c3320 | scan | other | ✅ | 76 | `uint __fastcall FUN_009c3320(uint param_1,byte *param_2,uint param_3)` |
| 0x009c3420 | FUN_009c3420 | scan | other | ✅ | 15 | `void __fastcall FUN_009c3420(int param_1,undefined4 param_2)` |
| 0x009c3440 | FUN_009c3440 | scan | other | ✅ | 16 | `void __fastcall FUN_009c3440(int param_1,undefined4 param_2)` |
| 0x009c3470 | FUN_009c3470 | scan | other | ✅ | 64 | `void __fastcall FUN_009c3470(int param_1,int param_2,undefined4 *param_3)` |
| 0x009c3520 | FUN_009c3520 | scan | other | ✅ | 15 | `void __fastcall FUN_009c3520(undefined4 param_1,undefined4 param_2)` |
| 0x009c3550 | FUN_009c3550 | scan | other | ✅ | 13 | `void __fastcall FUN_009c3550(int *param_1,undefined4 param_2)` |
| 0x009c3580 | FUN_009c3580 | scan | other | ✅ | 23 | `undefined4 __fastcall FUN_009c3580(int param_1)` |
| 0x009c35d0 | FUN_009c35d0 | scan | other | ✅ | 75 | `undefined4 __fastcall FUN_009c35d0(int param_1)` |
| 0x009c36b0 | FUN_009c36b0 | scan | other | ✅ | 173 | `undefined4 __fastcall FUN_009c36b0(int param_1)` |
| 0x009c38a0 | FUN_009c38a0 | scan | other | ✅ | 286 | `int __fastcall FUN_009c38a0(int *param_1)` |
| 0x009c3c40 | FUN_009c3c40 | scan | other | ✅ | 11 | `undefined4 __fastcall FUN_009c3c40(undefined1 *param_1)` |
| 0x009c3c60 | FUN_009c3c60 | scan | other | ✅ | 38 | `void __fastcall FUN_009c3c60(int param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009c3cd0 | FUN_009c3cd0 | scan | other | ✅ | 153 | `undefined4 __fastcall FUN_009c3cd0(int param_1,uint param_2)` |
| 0x009c3eb0 | FUN_009c3eb0 | scan | other | ✅ | 231 | `void __fastcall FUN_009c3eb0(int param_1,uint *param_2,int param_3)` |
| 0x009c41e0 | FUN_009c41e0 | scan | other | ✅ | 139 | `void __fastcall FUN_009c41e0(int param_1,int param_2,uint param_3)` |
| 0x009c4380 | FUN_009c4380 | scan | other | ✅ | 40 | `void __thiscall FUN_009c4380(int param_1,int param_2)` |
| 0x009c43f0 | FUN_009c43f0 | scan | other | ✅ | 136 | `void __fastcall FUN_009c43f0(uint param_1,int param_2,int param_3)` |
| 0x009c4580 | FUN_009c4580 | scan | other | ✅ | 114 | `void __fastcall FUN_009c4580(int param_1,int param_2,uint param_3)` |
| 0x009c46e0 | FUN_009c46e0 | scan | other | ✅ | 517 | `void __fastcall FUN_009c46e0(int param_1,int param_2,int param_3)` |
| 0x009c4e50 | FUN_009c4e50 | scan | other | ✅ | 220 | `void __fastcall FUN_009c4e50(int param_1,int param_2,int param_3)` |
| 0x009c5170 | FUN_009c5170 | scan | other | ✅ | 171 | `void __fastcall FUN_009c5170(int param_1,int param_2,uint param_3)` |
| 0x009c53b0 | FUN_009c53b0 | scan | other | ✅ | 157 | `void __fastcall FUN_009c53b0(int param_1,int param_2,int param_3)` |
| 0x009c55b0 | FUN_009c55b0 | scan | other | ✅ | 152 | `void __fastcall FUN_009c55b0(int param_1,int param_2,int param_3)` |
| 0x009c5750 | FUN_009c5750 | scan | other | ✅ | 130 | `void __fastcall FUN_009c5750(int param_1,int param_2,int param_3)` |
| 0x009c58c0 | FUN_009c58c0 | scan | other | ✅ | 130 | `void __fastcall FUN_009c58c0(int param_1,int param_2,int param_3)` |
| 0x009c5a30 | FUN_009c5a30 | scan | other | ✅ | 304 | `void __fastcall FUN_009c5a30(int param_1,int param_2,int param_3)` |
| 0x009c5d60 | FUN_009c5d60 | scan | other | ✅ | 119 | `void __fastcall FUN_009c5d60(int param_1,int param_2,int param_3)` |
| 0x009c5eb0 | FUN_009c5eb0 | scan | other | ✅ | 92 | `void __thiscall FUN_009c5eb0(int param_1,int param_2)` |
| 0x009c5fb0 | FUN_009c5fb0 | scan | other | ✅ | 358 | `void __thiscall FUN_009c5fb0(int param_1,int param_2)` |
| 0x009c63f0 | FUN_009c63f0 | scan | other | ✅ | 48 | `void __fastcall FUN_009c63f0(int param_1)` |
| 0x009c6490 | FUN_009c6490 | scan | other | ✅ | 263 | `void __fastcall FUN_009c6490(int param_1,byte *param_2,uint param_3)` |
| 0x009c6760 | FUN_009c6760 | scan | other | ✅ | 377 | `void __fastcall FUN_009c6760(uint *param_1,int param_2,int param_3,uint param_4)` |
| 0x009c6bf0 | FUN_009c6bf0 | scan | other | ✅ | 311 | `void __fastcall FUN_009c6bf0(undefined4 param_1,int param_2,uint *param_3,uint *param_4,int param_5)` |
| 0x009c6fa0 | FUN_009c6fa0 | scan | other | ✅ | 200 | `void __fastcall FUN_009c6fa0(int param_1)` |
| 0x009c7270 | FUN_009c7270 | scan | other | ✅ | 179 | `void __fastcall FUN_009c7270(int param_1)` |
| 0x009c74c0 | FUN_009c74c0 | scan | other | ✅ | 18 | `void FUN_009c74c0(int param_1,undefined4 param_2,int param_3)` |
| 0x009c74f0 | FUN_009c74f0 | scan | other | ✅ | 42 | `void __fastcall FUN_009c74f0(int param_1)` |
| 0x009c7580 | FUN_009c7580 | scan | other | ✅ | 116 | `void __fastcall FUN_009c7580(uint *param_1,undefined1 *param_2)` |
| 0x009c76c0 | FUN_009c76c0 | scan | other | ✅ | 96 | `void __fastcall FUN_009c76c0(int param_1,int param_2,int param_3)` |
| 0x009c77d0 | FUN_009c77d0 | scan | other | ✅ | 11 | `void __fastcall FUN_009c77d0(undefined4 param_1)` |
| 0x009c77f0 | FUN_009c77f0 | scan | other | ✅ | 18 | `void __thiscall FUN_009c77f0(undefined4 param_1,int param_2)` |
| 0x009c7820 | FUN_009c7820 | scan | other | ✅ | 11 | `void __fastcall FUN_009c7820(undefined4 param_1)` |
| 0x009c7840 | FUN_009c7840 | scan | other | ✅ | 18 | `void __thiscall FUN_009c7840(undefined4 param_1,int param_2)` |
| 0x009c7870 | FUN_009c7870 | scan | other | ✅ | 12 | `void FUN_009c7870(int param_1)` |
| 0x009c7890 | FUN_009c7890 | scan | other | ✅ | 49 | `void __fastcall FUN_009c7890(int param_1,int param_2,int param_3)` |
| 0x009c7900 | FUN_009c7900 | scan | other | ✅ | 36 | `void FUN_009c7900(uint param_1)` |
| 0x009c7950 | FUN_009c7950 | scan | other | ✅ | 10 | `void FUN_009c7950(void)` |
| 0x009c7970 | FUN_009c7970 | scan | other | ✅ | 17 | `void FUN_009c7970(int param_1)` |
| 0x009c79a0 | FUN_009c79a0 | scan | other | ✅ | 10 | `void FUN_009c79a0(void)` |
| 0x009c79c0 | FUN_009c79c0 | scan | other | ✅ | 17 | `void FUN_009c79c0(int param_1)` |
| 0x009c79f0 | FUN_009c79f0 | scan | other | ✅ | 9 | `void FUN_009c79f0(int param_1)` |
| 0x009c7a10 | FUN_009c7a10 | scan | other | ✅ | 17 | `undefined4 * __thiscall FUN_009c7a10(undefined4 *param_1,byte param_2)` |
| 0x009c7a40 | FUN_009c7a40 | scan | other | ✅ | 13 | `undefined4 __fastcall FUN_009c7a40(int param_1)` |
| 0x009c7a80 | FUN_009c7a80 | scan | other | ✅ | 36 | `void __fastcall FUN_009c7a80(int param_1)` |
| 0x009c7af0 | FUN_009c7af0 | scan | other | ✅ | 62 | `void __fastcall FUN_009c7af0(int param_1)` |
| 0x009c7bc0 | FUN_009c7bc0 | scan | other | ✅ | 104 | `void FUN_009c7bc0(int *param_1,uint param_2,uint param_3)` |
| 0x009c7cf0 | FUN_009c7cf0 | scan | other | ✅ | 82 | `uint __fastcall FUN_009c7cf0(int *param_1,uint param_2)` |
| 0x009c7db0 | FUN_009c7db0 | scan | other | ✅ | 34 | `void __fastcall FUN_009c7db0(int *param_1,int param_2)` |
| 0x009c7e00 | FUN_009c7e00 | scan | other | ✅ | 98 | `uint __fastcall FUN_009c7e00(int *param_1,uint param_2)` |
| 0x009c7f00 | FUN_009c7f00 | scan | other | ✅ | 10 | `undefined4 __fastcall FUN_009c7f00(int param_1)` |
| 0x009c7f20 | FUN_009c7f20 | scan | other | ✅ | 149 | `uint * __fastcall FUN_009c7f20(undefined4 param_1,int param_2,int param_3)` |
| 0x009c80c0 | FUN_009c80c0 | scan | other | ✅ | 59 | `int __fastcall FUN_009c80c0(int *param_1)` |
| 0x009c8170 | FUN_009c8170 | scan | other | ✅ | 238 | `void * __fastcall FUN_009c8170(int *param_1,int param_2,int param_3)` |
| 0x009c8450 | FUN_009c8450 | scan | other | ✅ | 42 | `void __fastcall FUN_009c8450(void *param_1)` |
| 0x009c84b0 | FUN_009c84b0 | scan | other | ✅ | 17 | `int FUN_009c84b0(undefined4 *param_1,undefined4 *param_2)` |
| 0x009c84e0 | FUN_009c84e0 | scan | other | ✅ | 428 | `undefined4 __fastcall FUN_009c84e0(undefined4 *param_1,undefined4 *param_2)` |
| 0x009c89c0 | FUN_009c89c0 | scan | other | ✅ | 146 | `void __fastcall FUN_009c89c0(int param_1,int param_2,int param_3)` |
| 0x009c8b50 | FUN_009c8b50 | scan | other | ✅ | 395 | `` |
| 0x009c9100 | FUN_009c9100 | scan | other | ✅ | 314 | `void __fastcall FUN_009c9100(uint *param_1,float *param_2,float *param_3)` |
| 0x009c94f0 | FUN_009c94f0 | scan | other | ✅ | 377 | `void __fastcall FUN_009c94f0(uint *param_1,int param_2,uint *param_3,float param_4)` |
| 0x009c9980 | FUN_009c9980 | scan | other | ✅ | 81 | `` |
| 0x009c9aa0 | FUN_009c9aa0 | scan | other | ✅ | 17 | `int FUN_009c9aa0(undefined4 *param_1,undefined4 *param_2)` |
| 0x009c9ad0 | FUN_009c9ad0 | scan | other | ✅ | 49 | `` |
| 0x009c9b60 | FUN_009c9b60 | scan | other | ✅ | 256 | `` |
| 0x009c9eb0 | FUN_009c9eb0 | scan | other | ✅ | 647 | `` |
| 0x009ca740 | FUN_009ca740 | scan | other | ✅ | 213 | `void __fastcall FUN_009ca740(int *param_1,int param_2)` |
| 0x009caa20 | FUN_009caa20 | scan | other | ✅ | 134 | `void __fastcall FUN_009caa20(float *param_1)` |
| 0x009cac70 | FUN_009cac70 | scan | other | ✅ | 103 | `void __fastcall FUN_009cac70(int param_1,float *param_2,int param_3)` |
| 0x009cae10 | FUN_009cae10 | scan | other | ✅ | 323 | `void __fastcall FUN_009cae10(int param_1,float *param_2,int param_3)` |
| 0x009cb320 | FUN_009cb320 | scan | other | ✅ | 111 | `void __fastcall FUN_009cb320(int *param_1,int param_2)` |
| 0x009cb4d0 | FUN_009cb4d0 | scan | other | ✅ | 228 | `void __fastcall FUN_009cb4d0(int *param_1,float *param_2,int param_3)` |
| 0x009cb830 | FUN_009cb830 | scan | other | ✅ | 166 | `void __fastcall FUN_009cb830(int *param_1,int param_2,int param_3)` |
| 0x009cba60 | FUN_009cba60 | scan | other | ✅ | 160 | `void __fastcall FUN_009cba60(uint param_1,int param_2,float *param_3,float *param_4,int param_5)` |
| 0x009cbc80 | FUN_009cbc80 | scan | other | ✅ | 316 | `` |
| 0x009cc0d0 | FUN_009cc0d0 | scan | other | ✅ | 1200 | `else if (1 < iVar3) {` |
| 0x009ccfe0 | FUN_009ccfe0 | scan | other | ✅ | 194 | `void __fastcall FUN_009ccfe0(int param_1,int param_2,int param_3,int param_4,int param_5)` |
| 0x009cd200 | FUN_009cd200 | scan | other | ✅ | 189 | `` |
| 0x009cd440 | FUN_009cd440 | scan | other | ✅ | 310 | `uint * __fastcall FUN_009cd440(int *param_1)` |
| 0x009cd7f0 | FUN_009cd7f0 | scan | other | ✅ | 143 | `uint __fastcall FUN_009cd7f0(int param_1)` |
| 0x009cd970 | FUN_009cd970 | scan | other | ✅ | 243 | `undefined4 FUN_009cd970(int *param_1,int param_2,undefined4 param_3,int param_4)` |
| 0x009cdc60 | FUN_009cdc60 | scan | other | ✅ | 81 | `undefined4 FUN_009cdc60(int *param_1,int param_2,undefined4 param_3,int param_4)` |
| 0x009cde20 | FUN_009cde20 | scan | other | ✅ | 231 | `undefined4 __fastcall FUN_009cde20(int *param_1,undefined4 *param_2,undefined4 param_3,int param_4)` |
| 0x009ce090 | FUN_009ce090 | scan | other | ✅ | 191 | `` |
| 0x009ce2b0 | FUN_009ce2b0 | scan | other | ✅ | 108 | `` |
| 0x009ce3f0 | FUN_009ce3f0 | scan | other | ✅ | 108 | `` |
| 0x009ce530 | FUN_009ce530 | scan | other | ✅ | 108 | `` |
| 0x009ce670 | FUN_009ce670 | scan | other | ✅ | 65 | `void __fastcall FUN_009ce670(int param_1,int param_2)` |
| 0x009ce710 | FUN_009ce710 | scan | other | ✅ | 8 | `void FUN_009ce710(undefined4 param_1,size_t param_2,size_t param_3)` |
| 0x009ce730 | FUN_009ce730 | scan | other | ✅ | 7 | `void FUN_009ce730(undefined4 param_1,void *param_2)` |
| 0x009ce750 | FUN_009ce750 | scan | other | ✅ | 49 | `void __fastcall FUN_009ce750(int *param_1,int param_2,int *param_3)` |
| 0x009ce7d0 | FUN_009ce7d0 | scan | other | ✅ | 54 | `void __fastcall FUN_009ce7d0(uint *param_1,int *param_2,uint param_3)` |
| 0x009cf3d0 | FUN_009cf3d0 | scan | other | ✅ | 113 | `uint FUN_009cf3d0(uint param_1,byte *param_2,uint param_3)` |
| 0x009cf500 | FUN_009cf500 | scan | other | ✅ | 135 | `` |
| 0x009cf6a0 | FUN_009cf6a0 | scan | other | ✅ | 89 | `void __fastcall FUN_009cf6a0(int param_1,int param_2,undefined4 *param_3)` |
| 0x009cf7a0 | FUN_009cf7a0 | scan | other | ✅ | 17 | `undefined4 * __thiscall FUN_009cf7a0(undefined4 *param_1,byte param_2)` |
| 0x009cf7d0 | FUN_009cf7d0 | scan | other | ✅ | 9 | `void __thiscall FUN_009cf7d0(int param_1,undefined4 *param_2)` |
| 0x009cf820 | FUN_009cf820 | scan | other | ✅ | 43 | `void __thiscall FUN_009cf820(int param_1,undefined4 param_2,undefined4 param_3)` |
| 0x009cf8a0 | FUN_009cf8a0 | scan | other | ✅ | 47 | `void __thiscall FUN_009cf8a0(int param_1,int param_2)` |
| 0x009cf920 | FUN_009cf920 | scan | other | ✅ | 23 | `void __thiscall FUN_009cf920(int param_1,undefined4 param_2)` |
| 0x009cf950 | FUN_009cf950 | scan | other | ✅ | 36 | `void __fastcall FUN_009cf950(undefined4 *param_1)` |
| 0x009cf9c0 | FUN_009cf9c0 | scan | other | ✅ | 16 | `void FUN_009cf9c0(void *param_1)` |
| 0x009cf9f0 | FUN_009cf9f0 | scan | other | ✅ | 38 | `void FUN_009cf9f0(undefined4 *param_1)` |
| 0x009cfa50 | FUN_009cfa50 | scan | other | ✅ | 92 | `` |
| 0x009cfb50 | FUN_009cfb50 | scan | other | ✅ | 22 | `` |
| 0x009cfb90 | FUN_009cfb90 | scan | other | ✅ | 113 | `int FUN_009cfb90(int param_1,float param_2)` |
| 0x009cfcd0 | FUN_009cfcd0 | scan | other | ✅ | 165 | `undefined4 FUN_009cfcd0(int param_1,int *param_2,int param_3,void *param_4)` |
| 0x009cff50 | FUN_009cff50 | scan | other | ✅ | 16 | `void FUN_009cff50(void *param_1)` |
| 0x009cff80 | FUN_009cff80 | scan | other | ✅ | 142 | `void FUN_009cff80(int param_1,int *param_2,undefined4 param_3)` |
| 0x009eb08e | FUN_009eb08e | callee | other | ✅ | 7 | `void FUN_009eb08e(void *param_1)` |
| 0x009eb09c | FUN_009eb09c | callee | other | ✅ | 4 | `void FUN_009eb09c(uint param_1)` |