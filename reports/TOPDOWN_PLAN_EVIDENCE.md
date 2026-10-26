# 俯视角改造规划（基于 Isaac 逆向实据 · 最终数据版）

> 本文档每一条数据都来自本机 Isaac 1.7.9B 的实际提取（见 `isaac_reverse/notes/ISAAC_REVERSE_REPORT.md`）。
> 与 `docs/topdown-pivot-plan.md` 的关系：那份是纯设计草案，本份是**有实据支撑的版本**。
> 最后更新：2026-10-26 —— 全部 27 张数据表已落地提取，下文用真实数值替换了此前的估算。

## 0. 实据来源一览（全部已落地）

| 数据 | 来源 | 状态 |
|---|---|---|
| 24 个房型 | `tools/RoomEditor/rooms.txt` | ✅ 明文直读 |
| 实体 ID 表 | `tools/RoomEditor/entities_custom.txt` | ✅ 明文直读 |
| 529 道具 ID→名 | `tools\IsaacItemPoolEditor\Config.ini` `[Items]` | ✅ 明文直读（base-game 清单） |
| 26 道具池 | 同上 `[Pools]` | ✅ 明文直读（base-game 清单） |
| 道具图标 | 解包 `*.a` → `extracted2/` | ✅ 已提取（占位图形方案下暂不用） |
| 31 个道具池 + 2058 条 | `extracted2/resources-dlc3/itempools.xml` | ✅ **已提取并解析** |
| 721 道具品质分层 | `extracted2/resources-dlc3/items_metadata.xml` | ✅ **已提取并解析** |
| 958 件道具总表 | `extracted2/resources-dlc3/items.xml` | ✅ **已提取并解析** |
| 1337 实体 / 197 Boss | `extracted2/resources-dlc3/entities2.xml` | ✅ **已提取并解析** |
| 30 个楼层 | `extracted2/resources-dlc3/stages.xml` | ✅ **已提取并解析** |

---

## 1. 房间系统：24 种房型 → 俯视化映射

Isaac 原版是「单屏房间 + 上下左右门」，**俯视化后每间房仍是一个格子空间，但内部按瓦片布局**。

| Isaac 房型 | 俯视化处理 |
|---|---|
| `DEFAULT` | 基础战斗房，随机障碍块 |
| `SHOP` | 固定布局：中央 1 个商店台 + 上下各 1 个 |
| `TREASURE` | 封闭房，中央宝箱，**开门需钥匙或炸弹** |
| `BOSS` | 大房，Boss 居中，四角柱子 |
| `MINIBOSS` | 中型房，2-3 只精英怪 |
| `SECRET` / `SUPERSECRET` | 单入口暗房，需炸弹破墙进入 |
| `CURSE` | 负面效果房（随机诅咒） |
| `DEVIL` / `ANGEL` | 契约房：一次交易（付血/付币） |
| `LIBRARY` | 强化房，2 个强化台 |
| `SACRIFICE` | 献祭房：献祭道具换 2 个强力道具 |
| `CHALLENGE` | 挑战房：完成条件给奖励 |
| `ARCADE` | 弹球机房，小奖励 |
| `DUNGEON` | 特殊道具房 |
| `BOSSRUSH` | 连续 BOSS 战 |
| `ISAACS` | 主角专属房 |
| `BARREN` | 空房（无敌人，纯装饰/陷阱） |
| `CHEST` | 大宝箱房 |
| `DICE` | 赌博房 |
| `BLACK_MARKET` | 付费购买房 |
| `GREED_EXIT` | 贪婪模式出口 |
| `ERROR` / `NULL` | 特殊/无效 |

**与当前项目对照**：`TerrainGen.cs` 现有 `Templates` 只有 6 类兜底房
（Boss/Event/Entrance/Elite/Combat/Chest）。**需扩展到上述 24 类的映射表。**

---

## 2. 道具系统（真实提取数据）

### 2.1 Isaac 的 31 个道具池（`itempools.xml` DLC3 忏悔版，实测）

下方为**实测条目数**（非估算）。基础游戏 `Config.ini` 仅 26 池，DLC3 增补到 31 池。

| 池名 | 条目数 | 含义 | 俯视化用途 |
|---|---:|---|---|
| `treasure` | **407** | 宝藏房 | 主掉落池 |
| `greedTreasure` | 348 | 贪婪宝藏 | greed 模式主池 |
| `craneGame` | 96 | 夹娃娃机 | 小游戏池 |
| `ultraSecret` | 93 | 超级秘密 | 隐藏池 |
| `devil` | 94 | 恶魔房 | 付血交易池 |
| `babyShop` | 84 | 宝宝商店 | 强化池 |
| `greedDevil` | 81 | 贪婪恶魔 | greed 恶魔池 |
| `greedShop` | 87 | 贪婪商店 | greed 商店池 |
| `angel` | 66 | 天使房 | 付币交易池 |
| `boss` | **59** | Boss 房 | 每层 Boss 掉落 |
| `greedBoss` | 64 | 贪婪 Boss | — |
| `greedAngel` | 50 | 贪婪天使 | — |
| `greedSecret` | 57 | 贪婪秘密 | — |
| `secret` | 62 | 密室 | — |
| `demonBeggar` | 35 | 恶魔乞丐 | — |
| `momsChest` | 20 | 妈妈宝箱 | — |
| `oldChest` | 25 | 旧宝箱 | — |
| `goldenChest` | 25 | 金宝箱 | 稀有池 |
| `beggar` | 27 | 乞丐 | — |
| `greedCurse` | 30 | 贪婪诅咒 | — |
| `curse` | 34 | 诅咒房 | 负面池 |
| `keyMaster` | 22 | 钥匙商 | — |
| `rottenBeggar` | 9 | 腐烂乞丐 | — |
| `redChest` | 15 | 红宝箱 | 稀有池 |
| `library` | 15 | 强化房 | 强化池 |
| `planetarium` | 11 | 天文馆 | 特殊池 |
| `woodenChest` | 11 | 木宝箱 | — |
| `batteryBum` | 10 | 电池乞丐 | — |
| `bombBum` | 20 | 炸弹乞丐 | — |
| `shellGame` | 6 | 贝壳游戏 | 小游戏池 |
| `shop` | 95 | 商店 | 购买池 |

**合计 31 池、2058 条。** 俯视化落地时，P1 阶段优先实现：`treasure` / `shop` / `boss` / `devil` / `angel` / `secret` / `library` / `goldenChest` / `redChest` / `curse` / `keyMaster` 这 11 个「房型相关池」，其余（greed*/beggar*/游戏机类）可二期。

### 2.2 质量分层（真实！`items_metadata.xml` 的 quality 0–4）

Isaac 用 **0–4 共 5 级品质**，这是俯视化道具池分层的**直接依据**（此前草案的 4 级是估算，应以这 5 级为准）：

| quality | 件数 | 含义 | 俯视化对应层 |
|---|---:|---|---|
| **0** | 51 | 最差/垃圾 | 垃圾层（基本不进池） |
| **1** | 197 | 普通 | common |
| **2** | 249 | 良好 | uncommon |
| **3** | 184 | 稀有 | rare |
| **4** | 40 | 传说 | legendary |

**俯视化落地**：把当前 `Run.cs` 的单一 Offer 池改为**多层池**，分层依据就是 `items_metadata.xml` 的 `quality` 字段（不是按池名硬猜）。
按房间类型决定各层权重；`tags` 字段（如 `offensive` 542 / `summonable` 476 / `tearsup` / `baby`）还可做「build 倾向」过滤。

`items_metadata.xml` top tags（标签频率，可作 build 分类）：
`offensive` 542 / `summonable` 476 / `nolostbr` 106 / `nocantrip` 102 / `monstermanual` 59 / `tearsup` 34 / `baby` 31 / `stars` 31 / `fly` 24 / `mom` 21 / `angel` 17

### 2.3 道具总表（`items.xml` DLC3，958 件）

| 类别 | 件数 | 说明 |
|---|---:|---|
| `passive` | 425 | 被动道具（常驻增益） |
| `familiar` | 126 | 跟班（自动攻击/辅助） |
| `active` | 170 | 主动道具（按键触发） |
| `trinket` | 188 | 小饰品（弱被动） |
| `null` | 49 | 占位/无效 |

→ 俯视化道具拾取物可直接参照此分类：被动→属性增益、主动→技能、跟班→自动泪弹、饰品→弱修正。

### 2.4 道具图标

546 个 32×32 PNG 已提取（文件名含 ID 与 slug：`collectibles_001_thesadonion.png` …）。
**占位图形方案下暂不用原版贴图**（版权 + 用户已选占位优先），但尺寸基准 32×32 = 俯视 2×2 格可直接复用。

---

## 3. 实体系统

`entities_custom.txt` 为 `type,variant,subtype,name` 四元组，实据：

| type | 含义 | 实例 |
|---|---|---|
| 0 | Decoration（装饰） | Decoration 1/2/3 |
| 5 | 拾取物 | Pickup / Heart / Coin / Key / Bomb / Pill / Card / Rune |
| 40 | Guts（血量器官） | Guts 1-4 |
| 202 | 石头射手 | Constant Stone Shooter |
| 203 | 硫磺火 | Brimstone Head |
| 218 | 墙爬怪 | Wall Hugger |
| 1000+ | 岩石/地形 | Rock / Bomb Rock / Alt Rock |
| 1300 | TNT | TNT |
| 1400+ | 火焰 | Fireplace |
| 1490+ | 粪堆 | Poop（可破障碍载体） |
| 1930 | 尖刺 | Spikes / ON-OFF Spikes（静态伤害） |
| 1940 | 蜘蛛网 | Spiderweb |
| 3000 | 坑 | Pit |
| 4000 | 锁 | Lock |
| 4500 | 门按钮 | Door Button / Reward Button（门开关机制） |
| 5000 | 雕像 | Devil Statue / Angel Statue |
| 9000 | 陷阱门 | Trap Door |
| 9100 | 楼梯 | Staircase |
| 10000 | 重力 | Gravity |

**俯视化落地要点**：
- `type=5` 拾取物 → 掉落物系统（心/币/钥匙/炸弹/药丸/卡/符文 7 类）
- `type=1490+` 粪堆 → 可破坏障碍（**炸弹破墙**机制载体）
- `type=1930` 尖刺 → 静态伤害地形
- `type=4500` 门按钮 → 门开关机制（配合四向门）
- `type=1000+` 岩石 → 障碍块（当前 `TerrainGen` 随机障碍应换成按 type 选型）

`entities2.xml` 实测：**1337 实体、197 Boss**。Boss 样例：Larry Jr / The Hollow / Monstro / Chub / Chad / Carrion Queen / Gurdy / Gish / Mom…

`blacklist.txt`（35 条）= 不可放置实体的格子约束 —— 对应俯视化的障碍生成规则。

---

## 4. 尺寸基准（从实际精灵图量得）

| 类别 | 实测尺寸 | 俯视化含义 |
|---|---|---|
| 收集类道具 | **32×32**（全部一致） | 2×2 格拾取物 |
| 怪物 | 64×64 主流，128/256 次之 | 4×4 / 8×8 格敌人 |
| Boss | 192×192 / 256×256 / 512×512 | 大型敌人 |
| 角色 | 256×32 / 256×64 精灵条 | 单帧 32×32 或 64×64 |
| 网格贴图 | 104×260 / 128×240 / 160×32 | 地面砖块 |

**当前项目对照**：`Defs.TILE = 16`，`PLAYER_W/H = 14`。
→ 32×32 道具 = 2 格；玩家 14px ≈ 1 格内，比例吻合。

---

## 5. 楼层地图（`stages.xml` DLC3，30 个楼层）

Isaac 的楼层是「楼层 → 该层一组房型模板 → 2D 地图拼接」。实测 `stages.xml` 含 30 个楼层定义，
id 0–36（有跳号）：

```
id 0  Special Rooms       id 14 Sheol          id 27 Downpour
id 1  Basement            id 15 Cathedral      id 28 Dross
id 2  Cellar             id 16 Dark Room      id 29 Mines
id 3  Burning Basement   id 17 Chest          id 30 Ashpit
id 4  Caves              id 24 The Shop       id 31 Mausoleum
id 5  Catacombs          id 25 Ultra Greed    id 32 Gehenna
id 6  Flooded Caves      id 26 The Void       id 33 Corpse
id 7  Depths             id 35 Home           id 36 Backwards
id 8  Necropolis
id 9  Dank Depths
id 10 Womb
id 11 Utero
id 12 Scarred Womb
id 13 Blue Womb
```

**俯视化落地**：P1 阶段的「2D 楼层地图 + 四向门」应参照这套楼层深度结构——
每层从对应 `stage` 的房型模板池里抽取 N 个房间拼成 2D 网格，房与房之间用四向门连接。
当前 `LevelGen.cs` 的「线性 4 房链」需升级为「楼层 → 2D 房间图」。

---

## 6. 改造清单（对照当前代码，更新为真实数据）

| # | 事项 | 当前状态 | 依据 |
|---|---|---|---|
| 1 | 房型表 6→24 类 | `TerrainGen.cs` `Templates` | §1 房型表（24 种） |
| 2 | 道具池分层（5 级品质） | `Run.cs` 单池 Offer | §2.2 `items_metadata.xml` quality 0–4（51/197/249/184/40） |
| 3 | 掉落物系统 | 无 | §3 type=5（7 类） |
| 4 | 障碍按 type 选型 | 随机方块 | §3 岩石/粪堆/尖刺/坑 |
| 5 | 炸弹破墙 | 无 | §3 粪堆 + §1 SECRET 房 |
| 6 | 门按钮机制 | 无 | §3 type=4500 |
| 7 | 道具贴图 | 占位方块 | §2.4 546 张 32×32（暂用占位） |
| 8 | 楼层地图 | 线性 4 房 | §5 stages.xml（30 楼层） |
| 9 | 拾取物尺寸 | 待定 | §4 32×32 = 2 格 |
| 10 | 敌人/Boss 俯视 AI | 侧视高度语义 | §3 entities2.xml（1337 实体/197 Boss） |
| 11 | 主控只做伊布 | `MainCharLoadout.All` 含 4 主控 | 用户拍板（`players.xml` 是 Isaac 角色，**伊布是本项目自创宝可梦角色，不取自 Isaac**） |

> ⚠️ 修正旧文档一处错误：旧 §5 写「`players.xml`（伊布可参照）」——Isaac 没有伊布，
> `players.xml` 是 Isaac 自带的 41 个角色（Isaac/Magdalene/Cain/Judas/…）。
> 伊布是本项目的原创宝可梦主控，仅能**参照其角色属性结构模式**（hp/bombs/items 字段），
> 不照搬任何数值。
