# CraftEngine 配置模板参考手册

> **版本:** 26.2+ | **适用:** Minecraft 1.21+ | **语言:** 中文
>
> 本手册是 CraftEngine 配置模板库的完整目录与速查索引。每个模板文件均附有对应的 Wiki 文档引用路径（相对于 `../CraftEngine Wiki/`）。

---

## 目录

1. [模板文件结构总览](#1-模板文件结构总览)
2. [General 目录 — 综合示例与教学模板](#2-general-目录--综合示例与教学模板)
   - 2.1 [General/方块/](#21-general方块)
   - 2.2 [General/物品/](#22-general物品)
   - 2.3 [General/装备/](#23-general装备)
   - 2.4 [General/家具/](#24-general家具)
   - 2.5 [General/配方/](#25-general配方)
   - 2.6 [General/其他配置/](#26-general其他配置)
3. [方块配置目录](#3-方块配置目录)
   - 3.1 [方块/行为/ — 方块行为完整参考](#31-方块行为--方块行为完整参考)
   - 3.2 [方块/设置/ — 方块全部设置项](#32-方块设置--方块全部设置项)
   - 3.3 [方块/属性状态/ — 属性与状态参考](#33-方块属性状态--属性与状态参考)
4. [物品配置目录](#4-物品配置目录)
   - 4.1 [物品/行为/ — 物品行为完整参考](#41-物品行为--物品行为完整参考)
   - 4.2 [物品/设置/ — 物品全部设置项](#42-物品设置--物品全部设置项)
   - 4.3 [物品/数据组件/ — 全部数据组件参考](#43-物品数据组件--全部数据组件参考)
   - 4.4 [物品/模型类型/ — 物品模型类型参考](#44-物品模型类型--物品模型类型参考)
5. [家具配置目录](#5-家具配置目录)
   - 5.1 [家具/行为/ — 家具行为参考](#51-家具行为--家具行为参考)
   - 5.2 [家具/设置/ — 家具设置项](#52-家具设置--家具设置项)
   - 5.3 [家具/变体/ — 家具变体配置](#53-家具变体--家具变体配置)
6. [其他配置目录](#6-其他配置目录)
7. [CraftEngine 根配置键速查](#7-craftengine-根配置键速查)
8. [方块行为类型速查表](#8-方块行为类型速查表)
9. [物品行为类型速查表](#9-物品行为类型速查表)
10. [家具行为类型速查表](#10-家具行为类型速查表)
11. [物品模型类型速查表](#11-物品模型类型速查表)
12. [方块设置键速查表](#12-方块设置键速查表)
13. [物品设置键速查表](#13-物品设置键速查表)
14. [物品数据组件速查表](#14-物品数据组件速查表)
15. [事件函数类型速查表](#15-事件函数类型速查表)
16. [条件类型速查表](#16-条件类型速查表)
17. [属性类型速查表](#17-属性类型速查表)
18. [家具设置键速查表](#18-家具设置键速查表)

---

## 1. 模板文件结构总览

```
CraftEngine Template/
├── General/                          # 综合示例与教学模板（推荐初学者先看）
│   ├── 方块/
│   │   ├── 基础方块.yml              # 从最简到完整，方块配置全流程教学
│   │   ├── 功能方块.yml              # 15种功能方块完整示例（门、活板门、按钮等）
│   │   ├── 农作物.yml                # 9种农作物/植物行为方块（作物、茎、灌木等）
│   │   └── 物理机制方块.yml          # 物理机制方块（下落、附着等）
│   ├── 物品/
│   │   ├── 基础材料与宝石.yml        # 基础材料/宝石物品配置示例
│   │   ├── 工具.yml                  # 自定义工具（镐、斧等）
│   │   ├── 武器.yml                  # 自定义武器（剑、弓等）
│   │   ├── 食物.yml                  # 自定义食物配置
│   │   ├── 消耗品与药水.yml          # 消耗品与药水配置
│   │   └── 音乐唱片.yml              # 音乐唱片物品配置
│   ├── 家具/
│   │   └── 基础家具.yml              # 家具配置基础示例
│   ├── 装备/
│   │   └── 盔甲套装.yml              # 完整盔甲套装配置
│   ├── 配方/
│   │   └── 全部配方类型.yml          # 所有配方类型示例
│   └── 其他配置/
│       ├── 事件与函数参考.yml        # 全部事件触发器、函数类型、条件类型
│       ├── 全局变量.yml              # 全局变量定义与使用
│       ├── 分类配置.yml              # 物品浏览器分类配置
│       ├── 图像配置.yml              # 自定义图像/纹理配置
│       ├── 战利品表参考.yml          # 战利品表结构参考
│       ├── 数字格式.yml              # 数字格式配置
│       ├── 文本格式.yml              # 文本格式与 MiniMessage 参考
│       ├── 方块标签.yml              # 方块标签参考
│       ├── 模板系统.yml              # 模板系统（参数、工厂、组合）
│       ├── 画配置.yml                # 自定义画配置
│       ├── 表情配置.yml              # 自定义表情/颜文字配置
│       ├── 语言配置.yml              # 语言文件配置参考
│       └── 音效配置.yml              # 自定义音效配置
│
├── 方块/                             # 方块按主题拆分的详细参考
│   ├── 行为/                         # 48 种方块行为模板（每个文件一种行为）
│   ├── 设置/                         # 方块设置全部键参考
│   └── 属性状态/                     # 方块属性（properties）与状态（state/states）参考
│
├── 物品/                             # 物品按主题拆分的详细参考
│   ├── 行为/                         # 11 种物品行为模板
│   ├── 设置/                         # 物品设置全部键参考（25 项设置）
│   ├── 数据组件/                     # 物品数据组件完整参考（34 组件）
│   └── 模型类型/                     # 6 种物品模型类型 + 简化模型
│
├── 家具/                             # 家具配置参考
│   ├── 行为/                         # 3 种家具行为
│   ├── 设置/                         # 家具设置项
│   └── 变体/                         # 家具变体配置
│
└── 其他配置/                         # 独立配置文件参考
    ├── 字体配置.yml                  # 自定义字体配置
    ├── 数字格式.yml                  # 数字格式配置（独立版）
    ├── 文件冲突配置.yml              # 文件冲突解决方案
    ├── 文本格式.yml                  # 文本格式配置（独立版）
    ├── 物品更新器.yml                # 物品数据更新迁移
    └── 链式参数.yml                  # 链式参数完整引用
```

---

## 2. General 目录 — 综合示例与教学模板

`General/` 目录包含完整的教学性配置示例，推荐初学者先从这些文件入手。每个文件涵盖了从基础到进阶的完整配置流程。

### 2.1 General/方块/

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `基础方块.yml` | **从最简到完整的方块配置全流程教学**。涵盖单状态/多状态方块、设置项、战利品表、事件、行为、复合行为、实体渲染器等 10 个完整示例。**推荐作为方块配置的起点。** | `configuration/block.md`、`configuration/block/states.md`、`configuration/block/settings.md` |
| `功能方块.yml` | **15 种功能方块完整示例**。包含门、活板门、按钮、压力板、栅栏、栅栏门、楼梯、台阶、灯、可切换灯、震响、简单存储、抽屉、粒子方块、墙上火把。每个示例均附带完整的 properties/appearances/variants 配置。 | `configuration/block/behaviors.md` |
| `农作物.yml` | **9 种农作物/植物行为方块**。涵盖 crop_block、stem_block、attached_stem_block、bush_block、sapling_block、vertical_crop_block、change_over_time_block、spreading_block、surface_spreading_block。 | `configuration/block/behaviors/` 系列 |
| `物理机制方块.yml` | 物理机制相关方块（下落、附着、弹跳等）。 | `configuration/block/behaviors/` |

### 2.2 General/物品/

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `基础材料与宝石.yml` | **基础材料/宝石物品配置**。涵盖最小化配置到完整配置，含 material、data（item_name/lore/enchantment）、model、settings（fuel_time/tags）。 | `configuration/item.md`、`configuration/item/data.md`、`configuration/item/settings.md` |
| `工具.yml` | **自定义工具**（镐、斧、锹、锄等）。含 attribute_modifiers、enchantment、max_damage、model（handheld 模型）、settings（repairable/anvil_repair_item）、events。 | `configuration/item.md` |
| `武器.yml` | **自定义武器**（剑、弓、弩、三叉戟等）。含简化模型写法（bow/crossbow/fishing_rod）、attribute_modifiers、events（攻击粒子效果）。 | `configuration/item.md`、`configuration/item/models.md` |
| `食物.yml` | 自定义食物配置，含 food 组件（nutrition/saturation/can_always_eat）。 | `configuration/item/data.md` |
| `消耗品与药水.yml` | 消耗品与药水，含 consume_replacement、potion_effect 等。 | `configuration/item/settings.md` |
| `音乐唱片.yml` | 自定义音乐唱片物品配置（jukebox_playable）。 | `configuration/item/data.md` |

### 2.3 General/装备/

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `盔甲套装.yml` | **完整盔甲套装配置**。含 equipment（asset_id/slot/camera_overlay）、repairable、dyeable、attribute_modifiers、model（多纹理层 chestplate 模型）。 | `configuration/equipment.md`、`configuration/item/settings.md` |

### 2.4 General/家具/

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `基础家具.yml` | 家具配置基础示例，含 settings、variants。 | `configuration/furniture.md` |

### 2.5 General/配方/

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `全部配方类型.yml` | **所有配方类型示例**。涵盖 shaped（有序）、shapeless（无序）、smelting（熔炼）、blasting（高炉）、smoking（烟熏）、campfire_cooking（营火）、stonecutting（切石）、smithing_trim（锻造纹饰）、smithing_transform（锻造转换）、brewing（酿造）等。 | `configuration/recipe.md` |

### 2.6 General/其他配置/

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `事件与函数参考.yml` | **完整的事件系统参考**。涵盖所有事件触发器（物品：break/right_click/left_click/consume/pick_up/attack；方块：break/place/right_click/left_click/step；家具：break/place/right_click）、全部 40+ 函数类型、全部 20+ 条件类型。 | `reference/events.md`、`reference/conditions.md` |
| `全局变量.yml` | 全局变量定义（global_variables 根键）、带参数的变量、跨插件变量。 | `configuration/global_variable.md` |
| `分类配置.yml` | **物品浏览器（/ce）分类配置**。主分类 + 子分类、priority、icon、list。 | `configuration/category.md` |
| `图像配置.yml` | 自定义图像/纹理映射配置。 | `configuration/image.md` |
| `战利品表参考.yml` | **战利品表结构参考**。含基础掉落、权重多物品、精准采集/时运备选、家具物品、经验值、函数链（apply_bonus/explosion_decay/limit_count/drop_exp）。 | `reference/loot_table.md` |
| `数字格式.yml` | 数字格式配置（number_format 根键），用于全局数字显示格式化。 | `reference/number_format.md` |
| `文本格式.yml` | 文本格式与 MiniMessage 参考。 | `reference/text_format.md` |
| `方块标签.yml` | 方块标签（block_tags）参考。 | `reference/block_tags.md` |
| `模板系统.yml` | **模板系统完整参考**。含基础模板、多模板组合（template 列表）、参数占位符（`${param}`）、合并（merges）、覆写（overrides）、`${__NAMESPACE__}`/`${__ID__}` 内置变量、扩展参数类型（列表/映射/条件/匹配/大小写转换/自增整数/表达式）、配置工厂（config_factory）批量实例化。 | `reference/template.md` |
| `画配置.yml` | 自定义画（painting）配置。 | `configuration/painting.md` |
| `表情配置.yml` | 自定义表情/颜文字配置。 | `configuration/emoji.md` |
| `语言配置.yml` | 语言文件（i18n/lang）配置参考。 | `configuration/i18n.md`、`configuration/lang.md` |
| `音效配置.yml` | 自定义音效（sound）配置。 | `configuration/sound.md` |

---

## 3. 方块配置目录

### 3.1 方块/行为/ — 方块行为完整参考

每个文件对应一种方块行为类型（behavior/behaviors），共 **48 个行为模板**。

| 文件名 | 行为类型 | 功能说明 | 对应 Wiki |
|--------|---------|----------|-----------|
| `attached_stem_block.yml` | `attached_stem_block` | 附着茎方块（西瓜/南瓜果实旁的茎），含 facing 朝向属性 | `configuration/block/behaviors/attached_stem_block.md` |
| `bouncing_block.yml` | `bouncing_block` | 弹跳方块，为玩家同步弹性碰撞系数 | `configuration/block/behaviors/bouncing_block.md` |
| `budding_block.yml` | `budding_block` | budding 方块（类似紫水晶母岩），可生长出子方块 | `configuration/block/behaviors/budding_block.md` |
| `bush_block.yml` | `bush_block` | 灌木方块（浆果丛/花朵风格），可设置生长阶段和采摘 | `configuration/block/behaviors/bush_block.md` |
| `button_block.yml` | `button_block` | 按钮方块，红石电源（powered 属性），需组合 face_attached_horizontal_directional_block | `configuration/block/behaviors/button_block.md` |
| `change_over_time_block.yml` | `change_over_time_block` | 随时间更改方块（铜氧化/果实成熟），按时间/随机刻逐步转换 | `configuration/block/behaviors/change_over_time_block.md` |
| `chime_block.yml` | `chime_block` | 震响方块，被弹射物击中时发出音效（类似紫水晶块） | `configuration/block/behaviors/chime_block.md` |
| `concrete_powder_block.yml` | `concrete_powder_block` | 混凝土粉末，遇水凝固为指定方块 | `configuration/block/behaviors/concrete_powder_block.md` |
| `crop_block.yml` | `crop_block` | 农作物方块（小麦/马铃薯风格），age 生长阶段、光照要求 | `configuration/block/behaviors/crop_block.md` |
| `decay_block.yml` | `decay_block` | 衰变方块，在无支撑时随时间消失 | `configuration/block/behaviors/decay_block.md` |
| `directional_attached_block.yml` | `directional_attached_block` | 定向附着方块，附着在其他方块表面的定向方块 | `configuration/block/behaviors/directional_attached_block.md` |
| `display_item_block.yml` | `display_item_block` | 展示物品方块，在方块位置展示物品模型 | `configuration/block/behaviors/display_item_block.md` |
| `door_block.yml` | `door_block` | 门方块，双格高结构（half/hinge/facing/open/powered 属性） | `configuration/block/behaviors/door_block.md` |
| `double_high_block.yml` | `double_high_block` | 双格高方块（花/植物等），上下两部分同步破坏 | `configuration/block/behaviors/double_high_block.md` |
| `drawer_block.yml` | `drawer_block` | 抽屉方块，单物品大量存储容器（展示物品+数量文本） | `configuration/block/behaviors/drawer_block.md` |
| `drop_experience_block.yml` | `drop_experience_block` | 掉落经验方块，破坏时掉落经验值 | `configuration/block/behaviors/drop_experience_block.md` |
| `face_attached_horizontal_directional_block.yml` | `face_attached_horizontal_directional_block` | 水平面定向附着（face+facing 属性），支持黑/白名单附着限制 | `configuration/block/behaviors/face_attached_horizontal_directional_block.md` |
| `falling_block.yml` | `falling_block` | 下落方块（重力方块，类似沙/砂砾） | `configuration/block/behaviors/falling_block.md` |
| `fence_block.yml` | `fence_block` | 栅栏方块，四面连接（north/east/south/west 属性），拴绳系留 | `configuration/block/behaviors/fence_block.md` |
| `fence_gate_block.yml` | `fence_gate_block` | 栅栏门方块，带 in_wall 属性与墙体联动 | `configuration/block/behaviors/fence_gate_block.md` |
| `grass_block.yml` | `grass_block` | 草方块，可传播草皮到上方泥土 | `configuration/block/behaviors/grass_block.md` |
| `hangable_block.yml` | `hangable_block` | 可悬挂方块（类似灯笼/钟），附在天花板下方 | `configuration/block/behaviors/hangable_block.md` |
| `hanging_block.yml` | `hanging_block` | 悬挂方块，从上方悬挂下来 | `configuration/block/behaviors/hanging_block.md` |
| `item_frame_block.yml` | `item_frame_block` | 物品展示框方块，可放置/展示物品 | `configuration/block/behaviors/item_frame_block.md` |
| `lamp_block.yml` | `lamp_block` | 灯方块，红石点亮（4 刻延迟熄灭），lit 属性 | `configuration/block/behaviors/lamp_block.md` |
| `leaves_block.yml` | `leaves_block` | 树叶方块，距离检测、枯萎消失 | `configuration/block/behaviors/leaves_block.md` |
| `liquid_flowable_block.yml` | `liquid_flowable_block` | 液体可流过方块 | `configuration/block/behaviors/liquid_flowable_block.md` |
| `multi_high_block.yml` | `multi_high_block` | 多格高方块（2-4 格），可自定义每格外观 | `configuration/block/behaviors/multi_high_block.md` |
| `near_liquid_block.yml` | `near_liquid_block` | 近液体方块，靠近液体时转换 | `configuration/block/behaviors/near_liquid_block.md` |
| `on_liquid_block.yml` | `on_liquid_block` | 液体上浮方块（类似睡莲），浮在液体表面 | `configuration/block/behaviors/on_liquid_block.md` |
| `pressure_plate_block.yml` | `pressure_plate_block` | 压力板方块，实体检测红石输出，sensitivity 和 pressed_time | `configuration/block/behaviors/pressure_plate_block.md` |
| `sapling_block.yml` | `sapling_block` | 树苗方块，可长成指定方块 | `configuration/block/behaviors/sapling_block.md` |
| `seat_block.yml` | `seat_block` | 座椅方块（玩家可坐下） | `configuration/block/behaviors/seat_block.md` |
| `simple_particle_block.yml` | `simple_particle_block` | 简单粒子方块，定时生成粒子效果（支持 dust/item/block 等多类粒子） | `configuration/block/behaviors/simple_particle_block.md` |
| `simple_storage_block.yml` | `simple_storage_block` | 简单存储方块，自定义行数容器（1-6 行），比较器输出 | `configuration/block/behaviors/simple_storage_block.md` |
| `slab_block.yml` | `slab_block` | 台阶方块，双层合并（type: top/bottom/double），含水 | `configuration/block/behaviors/slab_block.md` |
| `snowy_block.yml` | `snowy_block` | 雪方块，积雪覆盖效果 | `configuration/block/behaviors/snowy_block.md` |
| `sofa_block.yml` | `sofa_block` | 沙发方块，可坐下的多人沙发（sofa_shape 属性） | `configuration/block/behaviors/sofa_block.md` |
| `spreading_block.yml` | `spreading_block` | 扩散方块（蘑菇/菌丝传播），随机刻扩散到相邻方块 | `configuration/block/behaviors/spreading_block.md` |
| `stackable_block.yml` | `stackable_block` | 可堆叠方块，多层堆叠（类似雪层） | `configuration/block/behaviors/stackable_block.md` |
| `stairs_block.yml` | `stairs_block` | 楼梯方块，自动形状计算（straight/inner_left/inner_right/outer_left/outer_right） | `configuration/block/behaviors/stairs_block.md` |
| `stem_block.yml` | `stem_block` | 茎方块（西瓜/南瓜茎），age 生长+连接果实 | `configuration/block/behaviors/stem_block.md` |
| `strippable_block.yml` | `strippable_block` | 可剥皮方块（斧右键剥皮转化为指定方块） | `configuration/block/behaviors/strippable_block.md` |
| `sturdy_base_block.yml` | `sturdy_base_block` | 坚固基底方块，提供完整支撑面 | `configuration/block/behaviors/sturdy_base_block.md` |
| `surface_spreading_block.yml` | `surface_spreading_block` | 表面扩散方块（草/藤蔓蔓延），在方块表面扩散 | `configuration/block/behaviors/surface_spreading_block.md` |
| `tint_source_block.yml` | `tint_source_block` | 着色源方块，影响周围方块颜色 | `configuration/block/behaviors/tint_source_block.md` |
| `toggleable_lamp_block.yml` | `toggleable_lamp_block` | 可切换灯方块，红石+手动双模式切换 lit 状态 | `configuration/block/behaviors/toggleable_lamp_block.md` |
| `trapdoor_block.yml` | `trapdoor_block` | 活板门方块，铰链面板（open/powered/half/facing/waterlogged 属性） | `configuration/block/behaviors/trapdoor_block.md` |
| `vertical_crop_block.yml` | `vertical_crop_block` | 垂直作物方块（甘蔗/海带风格），向上生长 | `configuration/block/behaviors/vertical_crop_block.md` |
| `wall_torch_particle_block.yml` | `wall_torch_particle_block` | 墙上火把粒子方块，带朝向感知的粒子效果 | `configuration/block/behaviors/wall_torch_particle_block.md` |

### 3.2 方块/设置/ — 方块全部设置项

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `全部设置项.yml` | **方块设置完整参考**。涵盖所有稳定设置、不稳定设置、扩展别名、未文档化设置。包含详细的速查表。 | `configuration/block/settings.md` |

**稳定的方块设置键（24 项）：**

| 设置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `item` | string / null | null | 方块对应物品 ID |
| `hardness` | float | 2.0 | 挖掘硬度（-1.0 = 不可破坏） |
| `resistance` | float | 2.0 | 爆炸抗性 |
| `push_reaction` | enum | NORMAL | 活塞行为：NORMAL/DESTROY/BLOCK/IGNORE/PUSH_ONLY |
| `map_color` | int | 0 | 地图颜色基色 |
| `burnable` | boolean | false | 熔岩可燃性 |
| `fire_spread_chance` | int(0-100) | 0 | 烧毁几率 |
| `burn_chance` | int(0-100) | 0 | 引燃几率 |
| `replaceable` | boolean | false | 可被其他方块替代 |
| `is_redstone_conductor` | boolean | undefined | 红石导体 |
| `is_suffocating` | boolean | undefined | 窒息生物 |
| `is_view_blocking` | boolean | undefined | 视野阻挡 |
| `sounds` | map | null | 音效（break/step/place/hit/fall） |
| `require_correct_tools` | boolean | false | 需要合适挖掘工具 |
| `respect_tool_component` | boolean | false | 尊重 tool 组件 |
| `correct_tools` | list[string] | null | 合适挖掘工具列表 |
| `incorrect_tool_dig_speed` | float(0-1) | 0.3 | 挖掘惩罚倍率 |
| `tags` | list[string] | null | 方块标签 |
| `client_bound_tags` | list[string] | null | 客户端侧标签（仅原版） |
| `instrument` | string | harp | 音符盒乐器 |
| `fluid_state` | string | empty | 流体状态（empty/water） |
| `support_shape` | string | null | 支撑形状 |

**不稳定的方块设置键（8 项）：**

| 设置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `bounce_restitution` | float(0-1) | 0.0 | 弹性碰撞系数（26.2+，仅非玩家实体） |
| `friction` | float | 0.6 | 阻力系数/滑动性（仅非玩家实体） |
| `jump_factor` | float | 1.0 | 跳跃高度乘数（仅非玩家实体） |
| `speed_factor` | float | 1.0 | 移动速度乘数（仅非玩家实体） |
| `luminance` | int(0-15) | 0 | 亮度等级（仅非玩家实体） |
| `can_occlude` | boolean | undefined | 阻挡光线（仅自身发光） |
| `block_light` | int(0-15) | undefined | 光线衰减（仅自身发光） |
| `propagate_skylight` | boolean | undefined | 传播天空光照 |

### 3.3 方块/属性状态/ — 属性与状态参考

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `属性与状态.yml` | **方块属性（properties）与状态（state/states）完整参考**。涵盖 auto_state 所有可用组、state 精确指定、model 四种配置方式、entity_renderer、states 的 properties/appearances/variants 三件套、属性类型速查、纹理数量推断规则、模型配置方式对比。 | `configuration/block/states.md`、`configuration/block/states/properties.md`、`configuration/block/states/entity_renderer.md` |

---

## 4. 物品配置目录

### 4.1 物品/行为/ — 物品行为完整参考

| 文件名 | 行为类型 | 功能说明 | 对应 Wiki |
|--------|---------|----------|-----------|
| `block_item.yml` | `block_item` | **方块物品** — 放置出方块的物品，block 指定放置的方块 ID | `configuration/item/behaviors/block_item.md` |
| `ceiling_block_item.yml` | `ceiling_block_item` | **天花板方块物品** — 放置在天花板上的方块物品 | `configuration/item/behaviors/ceiling_block_item.md` |
| `compostable_item.yml` | `compostable_item` | **可堆肥物品** — 可用于堆肥桶的物品 | `configuration/item/behaviors/compostable_item.md` |
| `double_high_block_item.yml` | `double_high_block_item` | **双格高方块物品** — 放置双格高结构的物品 | `configuration/item/behaviors/double_high_block_item.md` |
| `furniture_item.yml` | `furniture_item` | **家具物品** — 可放置家具的物品 | `configuration/item/behaviors/furniture_item.md` |
| `ground_block_item.yml` | `ground_block_item` | **地面方块物品** — 放置在地面的方块物品 | `configuration/item/behaviors/ground_block_item.md` |
| `liquid_collision_block_item.yml` | `liquid_collision_block_item` | **液体碰撞方块物品** — 在液体中放置的带碰撞方块 | `configuration/item/behaviors/liquid_collision_block_item.md` |
| `liquid_collision_furniture_item.yml` | `liquid_collision_furniture_item` | **液体碰撞家具物品** — 在液体中放置的带碰撞家具 | `configuration/item/behaviors/liquid_collision_furniture_item.md` |
| `multi_high_block_item.yml` | `multi_high_block_item` | **多格高方块物品** — 放置多格高结构的物品 | `configuration/item/behaviors/multi_high_block_item.md` |
| `range_mining_item.yml` | `range_mining_item` | **范围挖掘物品** — 可同时挖掘多格范围的工具 | `configuration/item/behaviors/range_mining_item.md` |
| `wall_block_item.yml` | `wall_block_item` | **墙壁方块物品** — 放置在墙壁上的方块物品 | `configuration/item/behaviors/wall_block_item.md` |

### 4.2 物品/设置/ — 物品全部设置项

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `全部设置项.yml` | **物品设置完整参考**。涵盖 25 项设置的详细参数说明与组合示例。 | `configuration/item/settings.md` |

**完整的物品设置键（25 项）：**

| 编号 | 设置项 | 类型 | 默认值 | 说明 |
|------|--------|------|--------|------|
| 1 | `fuel_time` | int | - | 烧炼时间（刻） |
| 2 | `tags` | list[string] | - | 物品标签 |
| 3 | `equipment` | object | - | 装备属性（asset_id/slot/camera_overlay 等） |
| 4 | `repairable` | bool/object | true | 可修复性 |
| 5 | `anvil_repair_item` | list[object] | - | 铁砧修复材料（amount/percent） |
| 6 | `renameable` | bool | true | 可重命名 |
| 7 | `allowed_projectiles` | list[string] | - | 可装载弹射物 |
| 8 | `projectile` | object | - | 弹射物实体定义（display/sounds/damage 等） |
| 9 | `dyeable` | bool | undefined | 可染色 |
| 10 | `enchantable` | bool | true | 可附魔 |
| 11 | `compost_probability` | float | 0.5 | 堆肥成功率 |
| 12 | `respect_repairable_component` | bool | false | 尊重 repairable 组件 |
| 13 | `dye_color` | string(R,G,B) | - | 染色颜色 |
| 14 | `firework_color` | string(R,G,B) | - | 烟火颜色 |
| 15 | `food` | object | - | 食物属性（插件实现） |
| 16 | `consume_replacement` | string | null | 消耗后返还物品 |
| 17 | `craft_remainder` | string/object | - | 合成剩余物品（fixed/hurt_and_break/recipe_based） |
| 18 | `fuel_remainder` | string | - | 燃料剩余物品 |
| 19 | `invulnerable` | list[string] | - | 伤害免疫类型 |
| 20 | `ingredient_substitute` | list[string] | - | 合成原料替代 |
| 21 | `hat_height` | float | - | 帽子高度（需 CustomNameplates） |
| 22 | `keep_on_death_chance` | float | - | 死亡保留概率（0-1） |
| 23 | `destroy_on_death_chance` | float | - | 死亡损毁概率（0-1） |
| 24 | `drop_display` | bool/string | - | 掉落物显示名称 |
| 25 | `glow_color` | string | - | 发光颜色 |

### 4.3 物品/数据组件/ — 全部数据组件参考

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `全部数据组件.yml` | **物品数据组件完整参考**。涵盖 34 个组件的配置示例与详细注释。 | `configuration/item/data.md` |

**完整的物品数据组件列表（34 项）：**

| 序号 | 组件名 | 版本要求 | 类型 | 说明 |
|------|--------|----------|------|------|
| 1 | `item_name` | 1.20.5+ | 硬编码 | 物品名称（最低优先级，不可铁砧修改） |
| 2 | `custom_name` | 1.20.5+ | 硬编码 | 自定义名称（类似铁砧命名） |
| 3 | `lore` | 全部 | 硬编码 | 提示框描述（支持 priority/split_lines/conditions） |
| 4 | `overwritable_lore` | 全部 | 硬编码 | 可覆写提示框描述（商店插件友好） |
| 5 | `insert_lore` | 全部 | 硬编码 | 动态插入提示框行（AFTER/BEFORE/HEAD/TAIL） |
| 6 | `remove_lore` | 全部 | 硬编码 | 按正则移除提示框行 |
| 7 | `overwritable_item_name` | 全部 | 硬编码 | 可覆写物品名称 |
| 8 | `unbreakable` | 全部 | 硬编码 | 无法破坏 |
| 9 | `enchantment` | 全部 | 硬编码 | 魔咒（支持 merge 选项） |
| 10 | `dyed_color` | 全部 | 硬编码 | 染色颜色（R,G,B） |
| 11 | `custom_model_data` | 全部 | 硬编码 | 自定义模型数据（整数） |
| 12 | `hide_tooltip` | 全部 | 硬编码 | 隐藏指定组件提示框 |
| 13 | `block_state` | 全部 | 硬编码 | 方块状态键值对 |
| 14 | `attribute_modifiers` | 全部 | 硬编码 | 属性修饰符（type/amount/operation/slot/id/display） |
| 15 | `food` | 1.20.5+ | 硬编码 | 食物属性（nutrition/saturation/can_always_eat） |
| 16 | `max_damage` | 1.20.5+ | 硬编码 | 最大耐久度 |
| 17 | `damage` | 1.20.5+ | 硬编码 | 耐久度损伤 |
| 18 | `jukebox_playable` | 1.21+ | 硬编码 | 唱片机播放曲目 |
| 19 | `item_model` | 1.21.2+ | 硬编码 | 物品模型映射 |
| 20 | `tooltip_style` | 1.21.2+ | 硬编码 | 提示框样式（纹理路径） |
| 21 | `use_remainder` | 1.21.2+ | 硬编码 | 使用后返还物品 |
| 22 | `trim` | 全部 | 硬编码 | 盔甲纹饰（pattern + material） |
| 23 | `equippable` | 1.21.2+ | 硬编码 | 可穿戴性（slot/asset_id/dispensable 等） |
| 24 | `pdc` | 全部 | 硬编码 | 持久化数据容器（自定义键值） |
| 25 | `profile` | 全部 | 硬编码 | 玩家档案（头颅：玩家名/URL/Base64） |
| 26 | `conditional` | 付费版 | 硬编码 | 条件数据（权限判断切换显示） |
| 27 | `painting_variant` | 全部 | 硬编码 | 画变种 |
| 28 | `charged_projectile` | 1.21+ | 硬编码 | 充能弹射物（弩箭/风弹） |
| 29 | `debug_stick` | 全部 | 硬编码 | 调试棒状态 |
| 30 | `nbt` | 1.20-1.20.4 | 自定义 | NBT 原始数据（已过时，仅旧版兼容） |
| 31 | `components` | 1.20.5+ | 自定义 | 原生组件（严格遵循 Minecraft Wiki 格式） |
| 32 | `remove_components` | 1.20.5+ | 自定义 | 移除指定组件 |
| 33 | `external` | 全部 | 外部兼容 | 外部插件物品引用（NeigeItems/MMOItems 等） |
| 34 | `client_bound_data` | 付费版 | 客户端侧 | 客户端专属数据（可实时更新提示框） |

### 4.4 物品/模型类型/ — 物品模型类型参考

| 文件名 | 模型类型 | 功能说明 | 对应 Wiki |
|--------|----------|----------|-----------|
| `minecraft_model.yml` | `minecraft:model` | **标准物品模型**。支持 path、generation（parent+textures）、transformation（缩放/平移/旋转 1.26.1+）、tints（8 种着色类型：constant/custom_model_data/dye/firework/grass/map_color/potion/team） | `configuration/item/models/model.md` |
| `minecraft_composite.yml` | `minecraft:composite` | **复合模型** — 组合多个子模型 | `configuration/item/models/composite.md` |
| `minecraft_condition.yml` | `minecraft:condition` | **条件模型** — 根据条件切换模型（如 damage/using_item 等谓词） | `configuration/item/models/condition.md` |
| `minecraft_range_dispatch.yml` | `minecraft:range_dispatch` | **范围调度模型** — 根据数值范围选择模型 | `configuration/item/models/range_dispatch.md` |
| `minecraft_select.yml` | `minecraft:select` | **选择模型** — 从多个选项中按条件选择 | `configuration/item/models/select.md` |
| `minecraft_special.yml` | `minecraft:special` | **特殊模型** — 特殊渲染类型（如盾牌/三叉戟/床/旗帜等） | `configuration/item/models/special.md` |
| `简化模型.yml` | simplified | **简化模型（1.21.4+）** — 自动分析基础材质推断模型。支持 2D 图标（texture）、手持工具、复合纹理、钓鱼竿、鞘翅、弓、弩、盾牌、自定义模型路径。 | `configuration/item/models.md` |

**简化模型字段速查：**

| 场景 | 字段 | 值类型 |
|------|------|--------|
| 2D 图标（flat/generated） | `texture` | 单个材质路径 |
| 手持工具（handheld） | `texture` | 单个材质路径 |
| 复合纹理层叠 | `textures` | 材质路径列表 |
| 钓鱼竿 | `textures` | [未抛竿, 已抛竿] |
| 鞘翅 | `textures` | [完好, 破损] |
| 弓 | `textures` | [待拉, 拉0, 拉1, 拉2] |
| 弩 | `textures` | [待拉, 拉0, 拉1, 拉2, 箭, 烟花] |
| 盾牌 | `models` | [举盾模型, 格挡模型] |
| 自定义单模型 | `model` | 单个模型路径 |
| 自定义多模型 | `models` | 模型路径列表 |

**Tint（着色）类型速查：**

| Tint 类型 | 说明 |
|-----------|------|
| `minecraft:constant` | 固定颜色值 |
| `minecraft:custom_model_data` | 根据 CustomModelData 值着色 |
| `minecraft:dye` | 根据染料颜色着色 |
| `minecraft:firework` | 根据烟火颜色着色 |
| `minecraft:grass` | 根据生物群系草地颜色着色 |
| `minecraft:map_color` | 根据地图颜色着色 |
| `minecraft:potion` | 根据药水颜色着色 |
| `minecraft:team` | 根据队伍颜色着色 |

---

## 5. 家具配置目录

### 5.1 家具/行为/ — 家具行为参考

| 文件名 | 行为类型 | 功能说明 | 对应 Wiki |
|--------|---------|----------|-----------|
| `display_item_furniture.yml` | `display_item_furniture` | 展示物品家具，在家具中展示物品模型 | `configuration/furniture/behaviors/display_item_furniture.md` |
| `glowing_furniture.yml` | `glowing_furniture` | 发光家具，产生光照效果 | `configuration/furniture/behaviors/glowing_furniture.md` |
| `simple_storage_furniture.yml` | `simple_storage_furniture` | 简单存储家具，带存储功能的家具 | `configuration/furniture/behaviors/simple_storage_furniture.md` |

### 5.2 家具/设置/ — 家具设置项

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `设置.yml` | 家具设置模板，涵盖所有家具可用的设置项。 | `configuration/furniture/settings.md` |

### 5.3 家具/变体/ — 家具变体配置

| 文件名 | 说明 | 对应 Wiki |
|--------|------|-----------|
| `变体配置.yml` | 家具变体（variants）配置，定义家具的不同摆放形态（地面/墙壁/天花板等）。 | `configuration/furniture/variants.md` |

---

## 6. 其他配置目录

| 文件名 | 根配置键 | 功能说明 | 对应 Wiki |
|--------|----------|----------|-----------|
| `字体配置.yml` | `fonts` | 自定义字体配置（资源包字体定义） | `configuration/font.md` |
| `数字格式.yml` | `number_format` | 数字格式配置（独立版），控制数字的显示格式 | `reference/number_format.md` |
| `文件冲突配置.yml` | `file_conflict` | 文件冲突解决方案，配置自动合并策略 | `reference/file_conflict.md` |
| `文本格式.yml` | `text_format` | 文本格式配置（独立版） | `reference/text_format.md` |
| `物品更新器.yml` | `item_updater` | **物品数据更新迁移工具**。用于服务器升级时自动更新旧版物品到新版格式。 | `configuration/item/updater.md` |
| `链式参数.yml` | - | **链式参数完整引用**。所有可用的 `<arg:对象.属性.子属性>` 链。涵盖 player/block/world/entity/position/item/furniture 共 7 个对象。 | `reference/text_format/chain_arguments.md` |

**链式参数对象速查：**

| 对象 | 说明 | 示例 |
|------|------|------|
| `player` | 玩家 | `<arg:player.name>`、`<arg:player.x>`、`<arg:player.main_hand_item.id>`、`<arg:player.world.name>` |
| `block` | 方块 | `<arg:block.block_x>`、`<arg:block.block_state>`、`<arg:block.world.name>` |
| `world` | 世界 | `<arg:player.world.name>`、`<arg:player.world.time>` |
| `entity` | 实体 | `<arg:entity.name>`、`<arg:entity.item.id>`、`<arg:entity.world.time>` |
| `position` | 位置 | `<arg:player.position.x>`、`<arg:player.position.yaw>`、`<arg:player.position.pitch>` |
| `item` | 物品 | `<arg:player.main_hand_item.count>`、`<arg:player.main_hand_item.is_custom>` |
| `furniture` | 家具 | `<arg:furniture.id>`、`<arg:furniture.variant>`、`<arg:furniture.position.world.name>` |

---

## 7. CraftEngine 根配置键速查

| 根键 | 类型 | 说明 | 对应 Wiki |
|------|------|------|-----------|
| `blocks` | map | **自定义方块** — 所有自定义方块定义在此根键下 | `configuration/block.md` |
| `items` | map | **自定义物品** — 所有自定义物品定义在此根键下 | `configuration/item.md` |
| `furniture` | map | **自定义家具** — 所有自定义家具定义在此根键下 | `configuration/furniture.md` |
| `categories` | map | **分类系统** — 物品浏览器（/ce）中的分类排列 | `configuration/category.md` |
| `global_variables` | map | **全局变量** — 可在任意上下文中访问的变量 | `configuration/global_variable.md` |
| `templates` | map | **模板系统** — 可复用的配置模板定义 | `reference/template.md` |
| `config_factory` | map | **配置工厂** — 批量实例化配置的工厂模式 | `reference/template.md` |
| `loot` | map | **战利品表** — 独立战利品表定义（pools/entries/functions） | `reference/loot_table.md` |
| `recipes` | map | **合成配方** — 自定义合成配方（shaped/shapeless/smelting 等） | `configuration/recipe.md` |
| `sounds` | map | **音效** — 自定义音效定义 | `configuration/sound.md` |
| `paintings` | map | **画** — 自定义画作变种 | `configuration/painting.md` |
| `fonts` | map | **字体** — 自定义字体定义 | `configuration/font.md` |
| `emoji` | map | **表情** — 自定义颜文字/表情 | `configuration/emoji.md` |
| `lang` | map | **语言** — 语言文件配置 | `configuration/lang.md` |
| `number_format` | map | **数字格式** — 数字显示格式化 | `reference/number_format.md` |
| `text_format` | map | **文本格式** — 文本格式化配置 | `reference/text_format.md` |
| `jukebox_song` | map | **唱片曲目** — 唱片机自定义音乐曲目 | `configuration/jukebox_song.md` |
| `conditions` | map | **条件定义** — 可复用的条件声明（在事件上下文内） | `reference/conditions.md` |
| `events` | list | **事件定义** — 事件触发器配置 | `reference/events.md` |
| `block_tags` | map | **方块标签** — 方块标签定义 | `reference/block_tags.md` |

---

## 8. 方块行为类型速查表

方块行为通过 `behavior`（单数）或 `behaviors`（复数列表）配置。

| 行为类型 | 说明 | 方块实体 | 常用属性 |
|----------|------|----------|----------|
| `attached_stem_block` | 附着茎方块 | 否 | facing |
| `bouncing_block` | 弹跳方块 | 否 | - |
| `budding_block` | 芽体方块 | 否 | - |
| `bush_block` | 灌木方块 | 否 | age |
| `button_block` | 按钮红石电源 | 否 | powered、ticks_to_stay_pressed |
| `change_over_time_block` | 随时间转换方块 | 否 | age、conversion |
| `chime_block` | 弹射物震响 | 否 | - |
| `concrete_powder_block` | 混凝土粉末凝固 | 否 | solid_block |
| `crop_block` | 农作物生长 | 否 | age、grow_speed、light_requirement |
| `decay_block` | 衰变消失 | 否 | - |
| `directional_attached_block` | 定向附着 | 否 | facing |
| `display_item_block` | 展示物品 | 是 | - |
| `door_block` | 双格高门 | 否 | open/powered/half/facing/hinge |
| `double_high_block` | 双格高结构 | 否 | half |
| `drawer_block` | 单物品存储抽屉 | 是 | facing、max_stacks |
| `drop_experience_block` | 掉落经验 | 否 | - |
| `face_attached_horizontal_directional_block` | 水平附着 | 否 | face/facing、blacklist、attached_blocks |
| `falling_block` | 重力下落 | 否 | - |
| `fence_block` | 栅栏连接 | 否 | north/east/south/west、connectable_block_tag |
| `fence_gate_block` | 栅栏门 | 否 | open/powered/in_wall/facing |
| `grass_block` | 草方块传播 | 否 | - |
| `hangable_block` | 可悬挂 | 否 | - |
| `hanging_block` | 悬挂方块 | 否 | - |
| `item_frame_block` | 物品展示框 | 是 | - |
| `lamp_block` | 红石灯 | 否 | lit |
| `leaves_block` | 树叶枯萎 | 否 | distance/persistent |
| `liquid_flowable_block` | 液体可流过 | 否 | - |
| `multi_high_block` | 多格高方块 | 否 | 自定义高度属性 |
| `near_liquid_block` | 近液体转换 | 否 | - |
| `on_liquid_block` | 液体上浮 | 否 | - |
| `pressure_plate_block` | 压力板 | 否 | powered、sensitivity、pressed_time |
| `sapling_block` | 树苗生长 | 否 | stage |
| `seat_block` | 座椅坐下 | 否 | - |
| `simple_particle_block` | 定时粒子 | 是 | tick_interval、particles |
| `simple_storage_block` | 存储容器 | 是 | open、rows、has_signal |
| `slab_block` | 台阶 | 否 | type、waterlogged |
| `snowy_block` | 积雪覆盖 | 否 | snowy |
| `sofa_block` | 沙发 | 否 | shape |
| `spreading_block` | 扩散传播 | 否 | - |
| `stackable_block` | 可堆叠 | 否 | layers |
| `stairs_block` | 楼梯 | 否 | shape/half/facing/waterlogged |
| `stem_block` | 茎方块 | 否 | age、facing |
| `strippable_block` | 可剥皮 | 否 | stripped |
| `sturdy_base_block` | 坚固基底 | 否 | - |
| `surface_spreading_block` | 表面扩散 | 否 | - |
| `tint_source_block` | 着色源 | 否 | - |
| `toggleable_lamp_block` | 可切换灯 | 否 | lit/powered、can_open_with_hand |
| `trapdoor_block` | 活板门 | 否 | open/powered/half/facing/waterlogged |
| `vertical_crop_block` | 垂直作物 | 否 | age |
| `wall_torch_particle_block` | 墙上火把粒子 | 是 | facing、tick_interval、particles |

> **带方块实体的行为：** display_item_block、drawer_block、simple_particle_block、wall_torch_particle_block、simple_storage_block、item_frame_block

---

## 9. 物品行为类型速查表

物品行为通过 `behavior`（单数）或 `behaviors`（复数列表）配置。

| 行为类型 | 说明 | 对应 Wiki |
|----------|------|-----------|
| `block_item` | 放置方块物品，`block` 指定放置的方块 ID | `configuration/item/behaviors/block_item.md` |
| `ceiling_block_item` | 放置天花板方块 | `configuration/item/behaviors/ceiling_block_item.md` |
| `compostable_item` | 可堆肥物品 | `configuration/item/behaviors/compostable_item.md` |
| `double_high_block_item` | 放置双格高方块 | `configuration/item/behaviors/double_high_block_item.md` |
| `furniture_item` | 放置家具 | `configuration/item/behaviors/furniture_item.md` |
| `ground_block_item` | 放置地面方块 | `configuration/item/behaviors/ground_block_item.md` |
| `liquid_collision_block_item` | 液体中放置方块 | `configuration/item/behaviors/liquid_collision_block_item.md` |
| `liquid_collision_furniture_item` | 液体中放置家具 | `configuration/item/behaviors/liquid_collision_furniture_item.md` |
| `multi_high_block_item` | 放置多格高方块 | `configuration/item/behaviors/multi_high_block_item.md` |
| `range_mining_item` | 范围挖掘工具 | `configuration/item/behaviors/range_mining_item.md` |
| `wall_block_item` | 放置墙壁方块 | `configuration/item/behaviors/wall_block_item.md` |

---

## 10. 家具行为类型速查表

| 行为类型 | 说明 | 对应 Wiki |
|----------|------|-----------|
| `display_item_furniture` | 展示物品家具 | `configuration/furniture/behaviors/display_item_furniture.md` |
| `glowing_furniture` | 发光家具 | `configuration/furniture/behaviors/glowing_furniture.md` |
| `simple_storage_furniture` | 存储家具 | `configuration/furniture/behaviors/simple_storage_furniture.md` |

---

## 11. 物品模型类型速查表

通过物品配置中的 `model` 键（或 `legacy_model` 键）配置。

| type 值 | 说明 | 对应 Wiki |
|---------|------|-----------|
| `minecraft:model`（默认） | 标准模型，含 generation/transformation/tints | `configuration/item/models/model.md` |
| `minecraft:composite` | 复合模型，组合多个子模型 | `configuration/item/models/composite.md` |
| `minecraft:condition` | 条件模型，根据谓词切换模型 | `configuration/item/models/condition.md` |
| `minecraft:range_dispatch` | 范围调度，按数值区间选择模型 | `configuration/item/models/range_dispatch.md` |
| `minecraft:select` | 选择模型，从候选中条件选择 | `configuration/item/models/select.md` |
| `minecraft:special` | 特殊渲染（盾牌/三叉戟/床等） | `configuration/item/models/special.md` |
| simplified（简化模型） | 自动推断模型结构，快速配置 | `configuration/item/models.md` |

---

## 12. 方块设置键速查表

完整的方块 `settings` 下可用键一览。

```yaml
blocks:
  custom:example:
    settings:
      # ---- 稳定设置（24 项）----
      item: "custom:example_item"              # 方块对应物品 ID
      hardness: 2.0                            # 挖掘硬度
      resistance: 2.0                          # 爆炸抗性
      push_reaction: NORMAL                    # 活塞行为
      map_color: 11                            # 地图颜色
      burnable: false                          # 熔岩可燃性
      fire_spread_chance: 0                    # 烧毁几率
      burn_chance: 0                           # 引燃几率
      replaceable: false                       # 可替代
      is_redstone_conductor: true              # 红石导体
      is_suffocating: true                     # 窒息生物
      is_view_blocking: true                   # 视野阻挡
      sounds: {}                               # 音效
      require_correct_tools: true              # 需要合适工具
      respect_tool_component: false            # 尊重 tool 组件
      correct_tools: []                        # 合适挖掘工具
      incorrect_tool_dig_speed: 0.3            # 挖掘惩罚
      tags: []                                 # 方块标签
      client_bound_tags: []                    # 客户端侧标签
      instrument: harp                         # 音符盒乐器
      fluid_state: empty                       # 流体状态
      support_shape: null                      # 支撑形状

      # ---- 不稳定设置（8 项，仅非玩家实体）----
      bounce_restitution: 0.0                 # 弹性碰撞
      friction: 0.6                           # 摩擦力
      jump_factor: 1.0                        # 跳跃乘数
      speed_factor: 1.0                       # 速度乘数
      luminance: 0                            # 亮度
      can_occlude: true                       # 阻挡光线
      block_light: 0                          # 散射光照
      propagate_skylight: false               # 传播天空光
```

---

## 13. 物品设置键速查表

完整的物品 `settings` 下可用键一览。

```yaml
items:
  custom:example:
    settings:
      fuel_time: 100                         # 烧炼时间（刻）
      tags: []                               # 物品标签
      equipment:                             # 装备属性
        asset_id: "custom:example"
        slot: head
      repairable: true                       # 可修复
      anvil_repair_item: []                  # 铁砧修复材料
      renameable: true                       # 可重命名
      allowed_projectiles: []                # 可装载弹射物
      projectile: {}                         # 弹射物实体
      dyeable: true                          # 可染色
      enchantable: true                      # 可附魔
      compost_probability: 0.5               # 堆肥成功率
      respect_repairable_component: false     # 尊重 repairable
      dye_color: "255,140,0"                 # 染色颜色
      firework_color: "255,140,0"            # 烟火颜色
      food: {}                               # 食物属性
      consume_replacement: null              # 消耗返还物品
      craft_remainder: null                  # 合成剩余物品
      fuel_remainder: null                   # 燃料剩余物品
      invulnerable: []                       # 伤害免疫
      ingredient_substitute: []              # 原料替代
      hat_height: 1.5                        # 帽子高度
      keep_on_death_chance: 0.0             # 死亡保留
      destroy_on_death_chance: 0.0          # 死亡损毁
      drop_display: true                     # 掉落物显示
      glow_color: yellow                     # 发光颜色
```

---

## 14. 物品数据组件速查表

完整的 `data` / `client_bound_data` 下可用键一览。

```yaml
items:
  custom:example:
    data:
      # ---- 硬编码组件（29 项）----
      item_name: "<gold>物品名"             # 物品名称
      custom_name: "<red>自定义名"          # 自定义名称
      lore: []                              # 提示框描述
      overwritable_lore: []                 # 可覆写描述
      insert_lore: []                       # 动态插入描述
      remove_lore: ""                       # 移除描述行
      overwritable_item_name: ""            # 可覆写名称
      unbreakable: true                     # 无法破坏
      enchantment: {}                       # 魔咒
      dyed_color: "255,100,50"             # 染色颜色
      custom_model_data: 100                # 自定义模型数据
      hide_tooltip: []                      # 隐藏提示框项
      block_state: {}                       # 方块状态
      attribute_modifiers: []               # 属性修饰符
      food: {}                              # 食物 (1.20.5+)
      max_damage: 100                       # 最大耐久 (1.20.5+)
      damage: 50                            # 耐久损伤 (1.20.5+)
      jukebox_playable: ""                  # 唱片曲目 (1.21+)
      item_model: ""                        # 物品模型 (1.21.2+)
      tooltip_style: ""                     # 提示框样式 (1.21.2+)
      use_remainder: ""                     # 使用返还 (1.21.2+)
      trim: {}                              # 盔甲纹饰
      equippable: {}                        # 可穿戴 (1.21.2+)
      pdc: {}                               # 持久化数据
      profile: ""                           # 玩家档案
      painting_variant: ""                  # 画变种
      charged_projectile: {}                # 充能弹射物 (1.21+)
      debug_stick: {}                       # 调试棒状态

      # ---- 自定义数据组件（3 项）----
      nbt: {}                               # NBT 原始数据 (1.20-1.20.4)
      components: {}                        # 原生组件 (1.20.5+)
      remove_components: []                 # 移除组件 (1.20.5+)

      # ---- 外部兼容（1 项）----
      external:                             # 外部插件引用
        plugin: "neigeitems"
        id: "example_item"

    client_bound_data:                       # 客户端侧数据（付费版）
      item_name: ""                          # 客户端显示名称
      overwritable_lore: []                  # 可覆写描述
      overwritable_item_name: ""             # 可覆写名称
      conditional#1: {}                      # 条件数据
      components: {}                         # 客户端组件
```

---

## 15. 事件函数类型速查表

所有函数通过 `events` -> `functions` 列表中的 `type` 字段指定。

| 函数类型 | 说明 | 主要参数 |
|----------|------|----------|
| `cancel_event` | 取消原始事件 | 无 |
| `run` | 按顺序运行函数链 | delay、functions |
| `command` | 执行命令 | command、target、as_player、as_op、as_event |
| `message` | 发送聊天消息 | message、target、overlay |
| `actionbar` | 发送动作栏消息 | actionbar、target |
| `title` | 发送屏幕标题 | title、subtitle、fade_in、stay、fade_out |
| `open_window` | 打开 GUI 窗口 | gui_type（anvil/enchantment 等）、title、target |
| `break_block` | 破坏方块 | x、y、z |
| `place_block` | 放置方块 | block_state、x、y、z |
| `update_block_property` | 更新方块属性 | properties、x、y、z |
| `transform_block` | 转换方块（保留属性） | block、properties、x、y、z |
| `drop_loot` | 掉落战利品 | x、y、z、to_inventory、loot |
| `update_interaction_tick` | 更新交互刻 | 无 |
| `set_count` | 设置物品数量 | add、count、target |
| `set_food` | 设置饥饿值 | add、food、target |
| `set_saturation` | 设置饱和度 | add、saturation、target |
| `swing_hand` | 挥手动画 | hand |
| `particle` | 生成粒子 | particle、x/y/z、count、offset、speed、特殊参数 |
| `potion_effect` | 添加状态效果 | potion_effect、duration、amplifier |
| `remove_potion_effect` | 移除状态效果 | potion_effect、all |
| `leveler_exp` | 添加技能经验 | plugin、leveler、count |
| `set_cooldown` | 设置冷却 | time、id、add |
| `remove_cooldown` | 移除冷却 | id、all |
| `play_sound` | 播放音效 | sound、x/y/z、target、pitch、volume、source |
| `cast_mythic_skill` | 释放 MythicMobs 技能 | skill、power |
| `spawn_furniture` | 生成家具 | furniture_id、x/y/z、pitch、yaw、variant |
| `remove_furniture` | 移除家具 | drop_loot、play_sound |
| `replace_furniture` | 替换家具 | furniture_id、x/y/z、pitch、yaw、variant |
| `rotate_furniture` | 旋转家具 | degree、on_success、on_failure |
| `teleport` | 传送 | x、y、z、pitch、yaw、world |
| `toast` | 发送弹窗 | toast、advancement_type、icon |
| `damage` | 伤害玩家 | target、amount、damage_type |
| `set_variable` | 设置变量 | name、number/text |
| `merchant_trade` | 打开村民交易 | title、offers |
| `remove_entity` | 移除实体 | 无 |
| `if_else` | 条件分支 | rules（conditions + functions） |
| `when` | 条件匹配（switch-case） | source、cases、fallback |
| `damage_item` | 消耗耐久 | amount、slot |
| `cycle_block_property` | 循环方块属性 | property、inverse、rules |
| `set_exp` | 设置经验 | count、add、target |
| `set_level` | 设置等级 | count、add、target |
| `play_totem_animation` | 播放图腾动画 | item、sound、pitch、volume |
| `close_inventory` | 关闭容器 | target |
| `clear_item` | 清理物品 | id、count |
| `heal` | 治疗玩家 | amount、target |
| `spawn_mythic_mob` | 生成 MythicMobs | mob、level、world、x/y/z |

> **事件触发器（on）：** 物品 — break / right_click / left_click / consume / pick_up / attack；方块 — break / place / right_click / left_click / step；家具 — break / place / right_click / open / close

---

## 16. 条件类型速查表

条件通过 `conditions` 列表中的 `type` 字段指定。类型前加 `!` 可反转判断逻辑。

| 条件类型 | 说明 | 主要参数 |
|----------|------|----------|
| `any_of` | 满足任意子条件 | terms |
| `all_of` | 满足所有子条件 | terms |
| `inverted` | 反转子条件结果 | term |
| `permission` | 检查权限 | permission |
| `expression` | 检查表达式 | expression |
| `random` | 随机概率 | value (0-1) |
| `has_item` | 是否手持物品 | 无 |
| `match_item` | 匹配物品 ID | id、regex |
| `match_block` | 匹配方块类型 | x、y、z、id、regex |
| `match_block_property` | 匹配方块属性 | properties |
| `match_entity` | 匹配实体类型 | id、regex |
| `match_furniture_variant` | 匹配家具变体 | variants |
| `enchantment` | 检测魔咒 | predicate（如 `silk_touch>=1`） |
| `table_bonus` | 魔咒概率表 | enchantment、chances |
| `survives_explosion` | 爆炸存活判定 | 无 |
| `falling_block` | 由下落方块掉落 | 无 |
| `string_equals` | 字符串相等 | value1、value2 |
| `string_contains` | 字符串包含 | value1、value2 |
| `regex` | 正则匹配 | value、regex |
| `is_null` | 参数是否为空 | argument |
| `hand` | 检查交互手 | hand (main_hand/off_hand) |
| `on_cooldown` | 是否冷却中 | id |
| `distance` | 距离检测 | min、max |
| `test_flag` | 权限标志 | flag (break/place/interact/open_container) |
| `has_player` | 玩家是否存在 | 无 |
| `is_bedrock_player` | 是否基岩版 | 无 |
| `inventory_has_item` | 背包检测 | id、count |
| `worldguard:region` | WorldGuard 区域 | mode、regions |

---

## 17. 属性类型速查表

用于方块 `states` -> `properties` 中的 `type` 字段。

| 属性类型 | 值域 | 说明 |
|----------|------|------|
| `boolean` | true / false | 布尔值 |
| `int` | 整数范围（通过 range 指定） | 整数，如 age: range=0~7 |
| `string` | 自定义选项集合 | 通过 values 指定 |
| `axis` | x / y / z | 轴向 |
| `direction` | east / south / west / north / up / down | 六方向 |
| `horizontal_direction` | east / south / west / north | 水平四方向 |
| `single_block_half` | top / bottom | 单格半块 |
| `double_block_half` | upper / lower | 双格半块 |
| `hinge` | left / right | 铰链侧 |
| `slab_type` | top / bottom / double | 台阶类型 |
| `stairs_shape` | straight / inner_left / inner_right / outer_left / outer_right | 楼梯形状 |
| `sofa_shape` | straight / inner_left / inner_right | 沙发形状 |
| `anchor_type` | floor / wall / ceiling | 锚点类型 |

**硬编码的特殊属性名（放置时自动行为）：**

| 属性名 | 自动行为 |
|--------|----------|
| `axis` | 放置时对齐玩家朝向的轴向 |
| `facing` | 放置时对齐玩家朝向（六方向） |
| `facing_clockwise` | 放置时对齐玩家朝向（四方向，旋转 90 度） |
| `rotation` | 精确旋转控制（int 0~7 或 0~15） |
| `waterlogged` | 决定方块是否含水 |

---

## 18. 家具设置键速查表

完整的家具 `settings` 下可用键一览。

```yaml
furniture:
  custom:example:
    settings:
      item: "namespace:item_id"             # 家具对应物品 ID
      hit_times: 3                          # 击打破坏次数
      sounds: {}                            # 音效（break/place/hit）
      adventure_mode_breaking: true         # 冒险模式可破坏
      correct_tools: []                     # 合适挖掘工具（支持标签）
```

---

## 附录 A：auto_state 可用组速查

所有 auto_state 可选组及其包含的原版方块：

| 组名 | 说明 |
|------|------|
| `solid` | 音符盒 + 蘑菇方块（最通用） |
| `note_block` | 仅音符盒（可用数量最多） |
| `mushroom_stem` | 蘑菇柄 |
| `red_mushroom_block` | 红色蘑菇方块 |
| `brown_mushroom_block` | 棕色蘑菇方块 |
| `mushroom` | 所有蘑菇方块 |
| `tintable_leaves` | 可着色树叶，不含水 |
| `waterlogged_tintable_leaves` | 可着色树叶，含水 |
| `non_tintable_leaves` | 不可着色树叶，不含水 |
| `waterlogged_non_tintable_leaves` | 不可着色树叶，含水 |
| `leaves` | 所有树叶，不含水 |
| `waterlogged_leaves` | 所有树叶，含水 |
| `lower_tripwire` | 绊线（矮碰撞箱） |
| `higher_tripwire` | 绊线（高碰撞箱） |
| `tripwire` | 所有绊线 |
| `sapling` | 所有树苗 |
| `pressure_plate` | 所有测重压力板 |
| `cactus` | 仙人掌 |
| `sugar_cane` | 甘蔗 |
| `weeping_vine` | 垂泪藤 |
| `twisting_vine` | 缠怨藤 |
| `cave_vine` | 洞穴藤蔓 |
| `kelp` | 海带 |
| `chorus` | 紫颂植株 |

---

## 附录 B：纹理数量推断规则

在方块 model 中按纹理数量自动推断模型结构：

| 纹理数量 | 推断模型 | path 要求 | 纹理顺序 |
|----------|----------|-----------|----------|
| 1 张 | `cube_all` | 可省略 | - |
| 2 张 | `cube_column` | 必需 | end, side |
| 3 张 | `cube_bottom_top` | 必需 | bottom, side, top |
| 4 张 | `orientable` | 必需 | bottom, front, side, top |
| 5+ 张 | `block/cube` | 必需 | down, up, north, south, west, east |

> 纹理前加 `^` 前缀表示也用作粒子纹理。示例：`"^custom:block/custom/top"`

---

## 附录 C：方块配置结构速览

```yaml
blocks:
  <namespace:block_id>:
    state:          # 单状态（必填，与 states 二选一）
      auto_state: note_block    # 或 state: "minecraft:..."
      model:                    # 或 models: []（多模型加权随机）
        texture: "..."          # 或 path: "..." + generation/tints/transformation
      entity_renderer: []       # 实体渲染器（可选）
      transparent: true         # 透明模式（可选）

    states:         # 多状态（必填，与 state 二选一）
      properties:   # 属性定义
        <prop>: { type: boolean, default: false }
      appearances:  # 外观定义
        <name>: { auto_state: ..., model: ... }
      variants:     # 变体映射
        <prop=value,...>: { appearance: <name>, settings: {} }

    settings:       # 方块设置（可选）
      hardness: 2.0
      # ... 见上述设置键速查表

    behavior:       # 单一行为（与 behaviors 二选一）
      type: <behavior_type>
      # ... 行为特有参数

    behaviors:      # 复合行为列表（与 behavior 二选一）
      - type: <behavior_type>
      - type: <other_behavior_type>

    loot:           # 战利品表（可选）
      pools:
        - rolls: 1
          entries: []

    events:         # 事件响应（可选）
      - on: right_click
        functions: []
```

---

## 附录 D：物品顶级配置键速览

```yaml
items:
  <namespace:item_id>:
    material: diamond              # 基础材质（必填）
    custom_model_data: 10001       # 自定义模型数据（生成资源包）
    item_model: "custom:..."       # 物品模型映射（生成资源包）
    client_bound_material: ...     # 客户端侧材质（付费版）
    client_bound_model: ...        # 客户端侧模型（付费版）
    texture: "..."                 # 简化模型：单纹理
    textures: []                   # 简化模型：多纹理（弓/弩/钓鱼竿等）
    model: "..."                   # 简化模型：单模型路径
    models: []                     # 简化模型：多模型路径（盾牌等）
    model:                         # 标准模型配置
      type: "minecraft:model"      # 模型类型
      path: "minecraft:item/..."   # 模型路径
      generation: {}               # 模型自动生成
      transformation: {}           # 模型变换（1.26.1+）
      tints: []                    # 着色配置
    legacy_model: {}               # 旧版模型回退（1.21.3-）
    data: {}                       # 物品数据组件
    client_bound_data: {}          # 客户端侧数据（付费版）
    settings: {}                   # 物品设置
    behavior:                      # 物品行为（单一）
      type: block_item
    behaviors: []                  # 物品行为（复合）
    events: []                     # 事件响应
    category: "custom:..."         # 物品分类
    oversized_in_gui: false        # GUI 中是否大图标显示
    hand_animation_on_swap: false  # 切换物品时播放动画
    swap_animation_scale: 1.0      # 切换动画缩放
    template: "custom:..."         # 引用模板
    template: []                   # 引用多模板
    arguments: {}                  # 模板参数
    merges: {}                     # 深度合并
    overrides: {}                  # 覆写路径
    use_remainder: "custom:..."    # 使用后返还
```

---

> **文件位置:** `F:/Github/repo/Quotidietium-Project/参考资料/CraftEngine/CraftEngine Template/`
> **Wiki 位置:** `F:/Github/repo/Quotidietium-Project/参考资料/CraftEngine/CraftEngine Wiki/`
> **最后更新:** 2026-06-23
