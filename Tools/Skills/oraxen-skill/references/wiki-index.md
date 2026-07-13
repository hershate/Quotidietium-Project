# Oraxen Wiki 快速导航索引

本文件提供 Skill 内置参考资源的快速导航，所有路径均相对于 Skill 的 `references/` 目录。

---

## 一、入门与基础

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| 配置总览 | `Oraxen Docs Origin/Creating Content/Overview.md` | 物品/方块/家具/盔甲/Glyphs 的概览 |
| 物品快速入门 | `Oraxen Docs Origin/Creating Content/Items/Getting Started.md` | 第一个物品教程，基本结构 |
| 理解基础 | `Oraxen Docs Origin/Plugin Setup/Understanding the Basics.md` | Oraxen 工作原理 |
| 插件设置 | `Oraxen Docs Origin/Plugin Setup/Plugin Settings.md` | settings.yml |
| 资源包托管 | `Oraxen Docs Origin/Plugin Setup/Pack Hosting.md` | 资源包部署 |

## 二、物品 (Items)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| 物品入门 | `Oraxen Docs Origin/Creating Content/Items/Getting Started.md` | displayname, material, Pack, Mechanics 基础结构 |
| 外观与模型 | `Oraxen Docs Origin/Creating Content/Items/Appearance & Models.md` | Pack 配置：generate_model, parent_model, textures, model, 特殊武器模型 |
| 组件 (Components) | `Oraxen Docs Origin/Creating Content/Items/Components.md` | durability, food, consumable, tool, equippable, item_model, AttributeModifiers |
| 可染色物品 | `Oraxen Docs Origin/Creating Content/Items/Dyeable Items.md` | 使用 POTION/LEATHER_HORSE_ARMOR + color |

**外观与模型 Pack 配置要点（来自 Appearance & Models.md）：**
- `generate_model: true` + `parent_model` + `textures` — 自动生成模型
- `generate_model: false` + `model` — 使用自定义 JSON 模型
- 特殊模型：blocking_model（盾牌）、pulling_models（弓）、charged_model（弩）、cast_model（钓鱼竿）
- 1.21.4+：gui_model、oversized_in_gui、hand_animation_on_swap、swap_animation_scale
- 耐久度分层模型：damaged_models

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
| Thor（雷击） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | lightning_bolts_amount, random_location_variation, delay, charges |
| Lifeleech（生命偷取） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | amount |
| Bleeding（流血） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | chance, duration, damage_per_interval, interval |
| EnergyBlast（能量爆破） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | delay, length, damage, particle |
| WitherSkull（凋零头颅） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | charged, delay, charges |
| Fireball（火球） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | delay, yield, speed, charges |
| Knockback Strike（连击击退） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | required_hits, knockback_horizontal, knockback_vertical, reset_time, particle |
| Spear Lunge（长矛突刺） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Combat.md` | active_model, charge_ticks, lunge_velocity, damage, max_range |

### 农耕类 (Farming)

| 机制 | 文件路径 | 关键配置 |
|------|---------|---------|
| Harvesting（收割） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Farming.md` | cooldown, radius, height, lower_item_durability |
| BigMining（范围挖掘） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Farming.md` | radius, depth |
| Smelting（自动熔炼） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Farming.md` | enabled, play_sound |
| BottledExp（经验瓶） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Farming.md` | ratio |
| BedrockBreak（破基岩） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Farming.md` | hardness, probability（需要 ProtocolLib）|
| Watering（浇水） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Farming.md` | filledCanItem / emptyCanItem（需配对）|

### 杂项类 (Miscellaneous)

| 机制 | 文件路径 | 关键配置 |
|------|---------|---------|
| Food（食物，旧版） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | hunger, saturation, effects（1.20.5 以下用）|
| Backpack（背包） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | rows, title, open_sound, close_sound |
| Music Disc（唱片，旧版） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | song（1.21 以下用）|
| Durability（耐久，旧版） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | value（1.20.5 以下用）|
| Efficiency（效率） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | amount（正=急迫，负=疲劳）|
| Consumable（消耗品） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | {}（使物品可消耗）|
| Repair（修复） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | ratio / fixed_amount |
| Commands（命令） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | cooldown, permission, console, player, opped_player |
| Armor Effects（盔甲效果） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | 药水效果列表 + requires_full_set |
| Hat（帽子） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | enabled |
| Aura（光环） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | type(simple/ring/helix), particle |
| Soulbound（灵魂绑定） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | lose_chance |
| Skinnable/Skin（皮肤） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | skinnable: {} / skin: { consume: true } |
| Toggle Light（切换光照） | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Miscellaneous.md` | light, toggle_light |

### 点击动作 (Click Actions)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| ClickAction | `Oraxen Docs Origin/Creating Content/Items/Item Abilities/Click Actions.md` | conditions + actions 完整语法 |
| 动作类型 | 同上 | [console], [player], [message], [actionbar], [sound] |
| 条件语法 | 同上 | Spigot Player/Server get 方法 |

## 四、方块 (Blocks)

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| **机制总览** | `Oraxen Docs Origin/Creating Content/Blocks/Overview.md` | NoteBlock vs StringBlock vs ChorusBlock vs ShapedBlock vs Furniture 对比 |
| NoteBlock | `Oraxen Docs Origin/Creating Content/Blocks/NoteBlock.md` | custom_variation(0~799), model, hardness, light, drop, directional, logStrip |
| StringBlock | `Oraxen Docs Origin/Creating Content/Blocks/StringBlock.md` | 类似 NoteBlock，可含水，适合植物 |
| ChorusBlock | `Oraxen Docs Origin/Creating Content/Blocks/ChorusBlock.md` | 透明方块，适合玻璃/树叶 |
| ShapedBlock | `Oraxen Docs Origin/Creating Content/Blocks/ShapedBlock.md` | 楼梯/台阶/门/活板门/栅栏，每类最多4种 |
| FarmBlock | `Oraxen Docs Origin/Creating Content/Blocks/FarmBlock.md` | 自定义耕地系统，需配 watering 浇水 |

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
| **总览** | `Oraxen Docs Origin/Creating Content/Furniture/Overview.md` | 所有家具功能列表 |
| Display Entities | `Oraxen Docs Origin/Creating Content/Furniture/Display Entities.md` | DISPLAY_ENTITY type, hitbox, display_entity_properties |
| 位置与旋转 | `Oraxen Docs Origin/Creating Content/Furniture/Position & Rotation.md` | rotatable, restricted_rotation |
| 进化/种植 | `Oraxen Docs Origin/Creating Content/Furniture/Farming & Evolution.md` | 作物阶段：inline stages（推荐）或 legacy multi-item |

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
| **总览** | `Oraxen Docs Origin/Creating Content/Armors/Overview.md` | 三种方法对比：Components(1.21.2+) / Trims(1.20-1.21.1) / Shaders(1.18-1.19.4) |
| Components 方法 | `Oraxen Docs Origin/Creating Content/Armors/Components(1.21.2+).md` | equippable + model + 任意材质，推荐 |
| Trims 方法 | `Oraxen Docs Origin/Creating Content/Armors/Trims (1.20-1.21.1).md` | 使用 chainmail 基础，trim_pattern |
| Shaders 方法 | `Oraxen Docs Origin/Creating Content/Armors/Shaders (1.18-1.19.4).md` | 使用 leather 基础，需要 CIT |

## 七、Commands、Recipes、配置参考

| 内容 | 文件路径 | 关键信息 |
|------|---------|---------|
| 命令 | `Oraxen Docs Origin/Commands & Recipes/Commands.md` | /o inv, /o give, /o reload, /o recipe |
| 默认物品 | `Oraxen Docs Origin/Commands & Recipes/Default items.md` | Oraxen 默认物品列表 |
| 配方 | `Oraxen Docs Origin/Commands & Recipes/Recipes.md` | /o recipe builder, 仅支持 ShapedRecipe |
| sound.yml | `Oraxen Docs Origin/Configuration Reference/sound.yml.md` | 自定义音效配置 |
| mechanics.yml | `Oraxen Docs Origin/Configuration Reference/mechanics.yml.md` | 全局机械开关 |
| 品牌自定义 | `Oraxen Docs Origin/Configuration Reference/Branding & Customization.md` | 自定义消息、GUI 标题 |
| 高级资源包生成 | `Oraxen Docs Origin/Configuration Reference/Advanced Pack Generation.md` | 资源包高级配置 |

## 八、兼容性

| 内容 | 文件路径 |
|------|---------|
| PackLayer | `Oraxen Docs Origin/Compatibility/PackLayer - Proxy Optimization.md` |
| MythicCrucible | `Oraxen Docs Origin/Compatibility/MythicCrucible.md` |
| MythicHUD | `Oraxen Docs Origin/Compatibility/MythicHUD.md` |
| MMoItems | `Oraxen Docs Origin/Compatibility/MMoItems.md` |
| ModelEngine | `Oraxen Docs Origin/Compatibility/ModelEngine - custom mobs.md` |
| MythicMobs | `Oraxen Docs Origin/Compatibility/MythicMobs - custom mobs.md` |
| Skript | `Oraxen Docs Origin/Compatibility/Skript.md` |

---

## Oraxen Template 索引

Skill 内置的 Oraxen Template 位于 `references/Oraxen Template/`，分为 `General/`（通用参考）和 `Example/`（完整示例）两类。

### General 通用参考

| 模板文件 | 适用配置类型 | 说明 |
|---------|-------------|------|
| `General/基础物品.md` | 基础物品、材料、合成组件 | items.yml 对应参考 |
| `General/1.21.2+ 组件物品.md` | 所有使用 Components 的物品 | Components 完整参考 |
| `General/武器.md` | 武器 | AttributeModifiers + 战斗 Mechanics |
| `General/工具.md` | 工具 | bigmining + smelting + harvesting |
| `General/食物.md` | 食物 | food + consumable 组件参考 |
| `General/音符盒方块.md` | NoteBlock 方块 | custom_variation + drop + directional |
| `General/绊线方块.md` | StringBlock 方块 | 植物、花草、水溶性 |
| `General/紫颂方块.md` | ChorusBlock 方块 | 透明方块、玻璃/树叶 |
| `General/形状方块.md` | ShapedBlock 方块 | 楼梯/台阶/门/活板门 |
| `General/农场方块.md` | FarmBlock 方块 | 自定义耕地系统 |
| `General/基础家具.md` | 家具 | barrier + seat + light |
| `General/展示实体.md` | DISPLAY_ENTITY 家具 | hitbox + display_entity_properties |
| `General/家具存储.md` | 家具存储容器 | STORAGE/PERSONAL/ENDERCHEST/DISPOSAL |
| `General/家具进化.md` | 作物/植物 | inline stages + evolution |
| `General/家具唱片机.md` | 唱片机家具 | jukebox + active_model |
| `General/ModelEngine家具.md` | ModelEngine 家具 | modelengine_id |
| `General/盔甲_组件_1.21.2+.md` | 盔甲（1.21.2+） | equippable + model |
| `General/盔甲_纹饰_1.20-1.21.1.md` | 盔甲（1.20-1.21.1） | trim_pattern |
| `General/盔甲_着色器_1.18-1.19.4.md` | 盔甲（1.18-1.19.4 旧版） | leather base + CIT |
| `General/可染色物品.md` | 染色物品 | POTION/LEATHER_HORSE_ARMOR + tint |
| `General/配方.md` | 合成配方 | /o recipe builder |
| `General/物品能力总览.md` | Mechanics 概览 | 全部机制类型总览 |
| `General/战斗机制参考.md` | 战斗 Mechanics | thor/lifeleech/bleeding/energyblast 等 |
| `General/农耕机制参考.md` | 农耕 Mechanics | bigmining/smelting/harvesting/watering |
| `General/杂项机制参考.md` | 杂项 Mechanics | backpack/repair/hat/aura/soulbound 等 |
| `General/自定义能力与点击动作.md` | 自定义能力 + 点击动作 | custom mechanic + clickActions |
| `General/综合机制配置参考.md` | 综合 Mechanics 组合 | 多种 Mechanics 组合示例 |
| `General/自定义音效.md` | 自定义音效 | sound.yml 配置 |
| `General/字形.md` | 字形/Glyphs | 自定义 emoji 和字体 |
| `General/自定义GUI.md` | 自定义 GUI | GUI 纹理和界面 |
| `General/自定义HUD.md` | 自定义 HUD | 状态条和 HUD 元素 |
| `General/文字特效.md` | 文字特效 | Text Effects 配置 |

### Example 完整示例

| 示例文件 | 适用配置类型 | 亮点 |
|---------|-------------|------|
| `Example/物品/1. 基础材料与宝石.md` | 基础物品 | 宝石、材料、Component 示例 |
| `Example/物品/2. 武器.md` | 武器 | 剑的 AttributeModifiers + Durability |
| `Example/物品/3. 工具.md` | 工具 | 工具组件 + 挖掘规则 |
| `Example/物品/4. 食物.md` | 食物 | 完整 food + consumable 配置 |
| `Example/物品/5. 消耗品与药水.md` | 消耗品/药水 | on_consume_effects 示例 |
| `Example/物品/6. 音乐唱片.md` | 唱片 | jukebox_playable + sound.yml |
| `Example/物品/7. 背包.md` | 背包 | backpack（存储）+ backpack_cosmetic（装饰，独立物品，二者不兼容） |
| `Example/物品/8. 皮肤系统.md` | 皮肤系统 | skin + skinnable 示例 |
| `Example/物品/9. 帽子与头部装备.md` | 帽子 | hat mechanic 示例 |
| `Example/方块/音符盒矿石.md` | 矿石方块 | 完整 ore 配置 + drop loot |
| `Example/方块/绊线花朵与植物.md` | 植物方块 | StringBlock 植物示例 |
| `Example/方块/紫颂透明方块.md` | 透明方块 | ChorusBlock 玻璃/树叶示例 |
| `Example/方块/形状方块.md` | 形状方块 | ShapedBlock 楼梯配置 |
| `Example/方块/农场方块与种植盆.md` | 农场方块 | farmblock 完整示例 |
| `Example/家具/基础家具.md` | 基础家具 | 桌子/椅子/储物架 |
| `Example/家具/座椅与大型家具.md` | 座椅/大型家具 | seat + barriers 配置 |
| `Example/家具/进化植物.md` | 进化植物/作物 | inline stages 完整示例 |
| `Example/家具/唱片机.md` | 唱片机家具 | jukebox + active_model |
| `Example/盔甲/完整盔甲套装_绿宝石.md` | 绿宝石盔甲 | equippable 全套装示例 |
| `Example/盔甲/完整盔甲套装_黑曜石.md` | 黑曜石盔甲 | 高耐久全套装示例 |
| `Example/盔甲/头盔与药水效果.md` | 头盔 + 药水效果 | armor_effects 示例 |
| `Example/盔甲/自定义鞘翅.md` | 自定义鞘翅 | 鞘翅自定义示例 |
| `Example/其他配置/配方.md` | 合成配方 | 合成配方完整示例 |
| `Example/其他配置/自定义能力_点击动作.md` | 自定义能力/点击 | custom + clickActions 示例 |
| `Example/其他配置/战斗机制完整参考.md` | 战斗机制 | 全部战斗机制完整配置 |
| `Example/其他配置/农耕机制完整参考.md` | 农耕机制 | 全部农耕机制完整配置 |
| `Example/其他配置/杂项机制完整参考.md` | 杂项机制 | 全部杂项机制完整配置 |
| `Example/其他配置/自定义音效.md` | 自定义音效 | 音效配置完整示例 |
| `Example/其他配置/综合配置示例.md` | 综合配置 | 多机制组合示例 |
| `Example/UI与字形/界面字形.md` | 界面字形 | Glyph 配置示例 |
| `Example/UI与字形/表情字形.md` | 表情字形 | Emoji 配置示例 |
| `Example/UI与字形/GUI物品.md` | GUI 物品 | GUI 物品示例 |
| `Example/UI与字形/自定义HUD.md` | 自定义 HUD | HUD 配置示例 |
| `Example/UI与字形/文字特效.md` | 文字特效 | Text Effect 示例 |

### 食物速查

| 文件 | 说明 |
|------|------|
| `Oraxen_food_template.md` | 食物 Components 速查模板（nutrition/saturation/consumable 字段参考）|
