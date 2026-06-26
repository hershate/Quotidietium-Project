# Oraxen Wiki 快速导航索引

本文件提供 Oraxen Docs Origin（Wiki）的快速导航，方便在生成配置时快速定位参考文档。

---

## 一、入门与基础

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| 配置总览 | `Creating Content/Overview.md` | 物品/方块/家具/盔甲/Glyphs 的概览 |
| 物品快速入门 | `Creating Content/Items/Getting Started.md` | 第一个物品教程，基本结构 |
| 理解基础 | `Plugin Setup/Understanding the Basics.md` | Oraxen 工作原理 |
| 插件设置 | `Plugin Setup/Plugin Settings.md` | settings.yml |
| 资源包托管 | `Plugin Setup/Pack Hosting.md` | 资源包部署 |

## 二、物品 (Items)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| 物品入门 | `Creating Content/Items/Getting Started.md` | displayname, material, Pack, Mechanics 基础结构 |
| 外观与模型 | `Creating Content/Items/Appearance & Models.md` | Pack 配置：generate_model, parent_model, textures, model, 特殊武器模型 |
| 组件 (Components) | `Creating Content/Items/Components.md` | durability, food, consumable, tool, equippable, item_model, AttributeModifiers |
| 可染色物品 | `Creating Content/Items/Dyeable Items.md` | 使用 POTION/LEATHER_HORSE_ARMOR + color |

**外观与模型 Pack 配置要点（来自 Appearance & Models.md）：**
- `generate_model: true` + `parent_model` + `textures` — 自动生成模型
- `generate_model: false` + `model` — 使用自定义 JSON 模型
- 特殊模型：blocking_model（盾牌）、pulling_models（弓）、charged_model（弩）、cast_model（钓鱼竿）
- 1.21.4+：gui_model、oversized_in_gui、hand_animation_on_swap、swap_animation_scale

**Components 要点（来自 Components.md）：**
- 1.20.5+ 使用 Components 替代 NBT
- durability: 简单数值或带高级选项的对象
- food: nutrition + saturation + can_always_eat
- consumable (1.21.2+): consume_seconds + animation + sound + on_consume_effects
- tool: damage_per_block + default_mining_speed + rules
- equippable (1.21.2+): slot + model + equip_sound
- jukebox_playable (1.21+): show_in_tooltip + song_key
- 1.21.3+ 通用组件系统：可直接传递任意数据组件
- AttributeModifiers 现代格式：named subsections

## 三、Mechanics（机制）

### 战斗类 (Combat)

| 机制 | 文件路径 | 关键配置 |
|------|---------|---------|
| Thor（雷击） | `Items/Item Abilities/Combat.md` | lightning_bolts_amount, random_location_variation, delay, charges |
| Lifeleech（生命偷取） | `Items/Item Abilities/Combat.md` | amount |
| Bleeding（流血） | `Items/Item Abilities/Combat.md` | chance, duration, damage_per_interval, interval |
| EnergyBlast（能量爆破） | `Items/Item Abilities/Combat.md` | delay, length, damage, particle |
| WitherSkull（凋零头颅） | `Items/Item Abilities/Combat.md` | charged, delay, charges |
| Fireball（火球） | `Items/Item Abilities/Combat.md` | delay, yield, speed, charges |
| Knockback Strike（连击击退） | `Items/Item Abilities/Combat.md` | required_hits, knockback_horizontal, knockback_vertical, reset_time, particle |
| Spear Lunge（长矛突刺） | `Items/Item Abilities/Combat.md` | active_model, charge_ticks, lunge_velocity, damage, max_range |

### 农耕类 (Farming)

| 机制 | 文件路径 | 关键配置 |
|------|---------|---------|
| Harvesting（收割） | `Items/Item Abilities/Farming.md` | cooldown, radius, height, lower_item_durability |
| BigMining（范围挖掘） | `Items/Item Abilities/Farming.md` | radius, depth |
| Smelting（自动熔炼） | `Items/Item Abilities/Farming.md` | enabled, play_sound |
| BottledExp（经验瓶） | `Items/Item Abilities/Farming.md` | ratio |
| BedrockBreak（破基岩） | `Items/Item Abilities/Farming.md` | hardness, probability（需要 ProtocolLib）|
| Watering（浇水） | `Items/Item Abilities/Farming.md` | filledCanItem / emptyCanItem（需配对）|

### 杂项类 (Miscellaneous)

| 机制 | 文件路径 | 关键配置 |
|------|---------|---------|
| Food（食物，旧版） | `Items/Item Abilities/Miscellaneous.md` | hunger, saturation, effects（1.20.5 以下用）|
| Backpack（背包） | `Items/Item Abilities/Miscellaneous.md` | rows, title, open_sound, close_sound |
| Music Disc（唱片，旧版） | `Items/Item Abilities/Miscellaneous.md` | song（1.21 以下用）|
| Durability（耐久，旧版） | `Items/Item Abilities/Miscellaneous.md` | value（1.20.5 以下用）|
| Efficiency（效率） | `Items/Item Abilities/Miscellaneous.md` | amount（正=急迫，负=疲劳）|
| Consumable（消耗品） | `Items/Item Abilities/Miscellaneous.md` | {}（使物品可消耗）|
| Repair（修复） | `Items/Item Abilities/Miscellaneous.md` | ratio / fixed_amount |
| Commands（命令） | `Items/Item Abilities/Miscellaneous.md` | cooldown, permission, console, player, opped_player |
| Armor Effects（盔甲效果） | `Items/Item Abilities/Miscellaneous.md` | 药水效果列表 + requires_full_set |
| Hat（帽子） | `Items/Item Abilities/Miscellaneous.md` | enabled |
| Aura（光环） | `Items/Item Abilities/Miscellaneous.md` | type(simple/ring/helix), particle |
| Soulbound（灵魂绑定） | `Items/Item Abilities/Miscellaneous.md` | lose_chance |
| Skinnable/Skin（皮肤） | `Items/Item Abilities/Miscellaneous.md` | skinnable: {} / skin: { consume: true } |
| Toggle Light（切换光照） | `Items/Item Abilities/Miscellaneous.md` | light, toggle_light |

### 点击动作 (Click Actions)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| ClickAction | `Items/Item Abilities/Click Actions.md` | conditions + actions 完整语法 |
| 动作类型 | 同上 | [console], [player], [message], [actionbar], [sound] |
| 条件语法 | 同上 | Spigot Player/Server get 方法 |

## 四、方块 (Blocks)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| **机制总览** | `Blocks/Overview.md` | NoteBlock vs StringBlock vs ChorusBlock vs ShapedBlock vs Furniture 对比 |
| NoteBlock | `Blocks/NoteBlock.md` | custom_variation(0~799), model, hardness, light, drop, directional, logStrip |
| StringBlock | `Blocks/StringBlock.md` | 类似 NoteBlock，可含水，适合植物 |
| ChorusBlock | `Blocks/ChorusBlock.md` | 透明方块，适合玻璃/树叶 |
| ShapedBlock | `Blocks/ShapedBlock.md` | 楼梯/台阶/门/活板门/栅栏，每类最多4种 |
| FarmBlock | `Blocks/FarmBlock.md` | 自定义耕地系统，需配 watering 浇水 |

**NoteBlock block_sounds（自定义音效）：**
```yaml
block_sounds:
  place_sound: block.stone.place
  break_sound: block.stone.break
  hit_sound: block.stone.hit
  step_sound: block.stone.step
  fall_sound: block.stone.fall
  volume: 0.8        # 可选
  pitch: 0.8         # 可选
```

## 五、家具 (Furniture)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| **总览** | `Furniture/Overview.md` | 所有家具功能列表 |
| Display Entities | `Furniture/Display Entities.md` | DISPLAY_ENTITY type, hitbox, display_entity_properties |
| 位置与旋转 | `Furniture/Position & Rotation.md` | rotatable, restricted_rotation |
| 进化/种植 | `Furniture/Farming & Evolution.md` | 作物阶段：inline stages（推荐）或 legacy multi-item |

**家具特有功能速查：**
- barrier / barriers — 碰撞箱
- hitbox (DISPLAY_ENTITY) — 简化碰撞箱
- seat — 座椅（需要 barrier: true）
- light — 光照（1-15）
- storage — 存储容器（type: STORAGE/PERSONAL/ENDERCHEST/DISPOSAL）
- jukebox — 唱片机
- evolution — 进化（作物生长用）
- stages — inline stages（推荐，替代 evolution + next_stage）
- text_entity / text_entities — 文字标签显示
- rotatable — 可旋转
- limited_placing — 放置限制
- block_sounds — 自定义音效
- hardness — 硬度
- Pack.models — 多模型变体

## 六、盔甲 (Armors)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| **总览** | `Armors/Overview.md` | 三种方法对比：Components(1.21.2+) / Trims(1.20-1.21.1) / Shaders(1.18-1.19.4) |
| Components 方法 | `Armors/Components(1.21.2+).md` | equippable + model + 任意材质，推荐 |
| Trims 方法 | `Armors/Trims (1.20-1.21.1).md` | 使用 chainmail 基础，trim_pattern |
| Shaders 方法 | `Armors/Shaders (1.18-1.19.4).md` | 使用 leather 基础，需要 CIT |

## 七、Commands、Recipes、配置参考

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| 命令 | `Commands & Recipes/Commands.md` | /o inv, /o give, /o reload, /o recipe |
| 默认物品 | `Commands & Recipes/Default items.md` | Oraxen 默认物品列表 |
| 配方 | `Commands & Recipes/Recipes.md` | /o recipe builder, 仅支持 ShapedRecipe |
| sound.yml | `Configuration Reference/sound.yml.md` | 自定义音效配置 |
| mechanics.yml | `Configuration Reference/mechanics.yml.md` | 全局机械开关 |
| 品牌自定义 | `Configuration Reference/Branding & Customization.md` | 自定义消息、GUI 标题 |
| 高级资源包生成 | `Configuration Reference/Advanced Pack Generation.md` | 资源包高级配置 |

## 八、兼容性

| 内容 | 文件路径 |
|------|---------|
| PackLayer | `Compatibility/PackLayer - Proxy Optimization.md` |
| MythicCrucible | `Compatibility/MythicCrucible.md` |
| MythicHUD | `Compatibility/MythicHUD.md` |
| MMoItems | `Compatibility/MMoItems.md` |
| ModelEngine | `Compatibility/ModelEngine - custom mobs.md` |
| MythicMobs | `Compatibility/MythicMobs - custom mobs.md` |
| Skript | `Compatibility/Skript.md` |

---

## Oraxen Template 索引

| 模板文件 | 适用配置类型 | 亮点示例 |
|---------|-------------|---------|
| `items.yml` | 基础物品、食物、唱片、背包 | amethyst, welcome_disk, miner_sandwitch, leather_backpack |
| `weapons.yml` | 武器 | glass_sword, storm_sword(thor), blood_sword(lifeleech+bleeding) |
| `tools.yml` | 工具 | 各类锤子(bigmining), iron_serpe(harvesting), cog 系列(repair) |
| `blocks.yml` | 方块 | amethyst_ore, ruby_ore, caveblock 等 NoteBlock 完整示例 |
| `furniture.yml` | 家具 | table, chair, cart(DISPLAY_ENTITY), turntable(jukebox+Pack.models) |
| `armors.yml` | 盔甲 | emerald/obsidian/ruby 全套装（含 equippable+AttributeModifiers）|
| `cooking_expansion.yml` | 食物 | 100+ 食物，含 Components.food+consumable 完整配置 |
| `hats.yml` | 帽子 | Hat mechanic 示例 |
| `skins.yml` | 皮肤 | Skin + Skinnable 示例 |
| `mystical.yml` | 神秘主题 | 特殊物品示例 |
| `plants.yml`/`flowers.yml` | 植物 | 植物/花卉示例 |
| `customcrops/crops/` | 作物 | 各类作物示例（cabbage, corn, tomato 等）|
| `customcrops/fertilizers.yml` | 肥料 | 肥料配置 |
| `customcrops/watering_cans.yml` | 浇水壶 | 浇水系统完整示例 |
| `customcrops/sprinklers.yml` | 洒水器 | 自动灌溉配置 |
| `crystalmush.yml` | 水晶蘑菇 | 特殊主题 |
| `guis.yml` | GUI | 自定义 GUI |
| `onexhs/onexhs_music.yml` | 音乐唱片 | 自定义唱片示例 |
| `festival/dragon_boat_fest.yml` | 节日物品 | 节日主题物品 |
