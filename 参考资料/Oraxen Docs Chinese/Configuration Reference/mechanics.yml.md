---
description: mechanics.yml 完整参考 - 所有机制及其配置选项
---

# mechanics.yml 配置

配置 Oraxen 44种内置机制的完整指南。启用、禁用和配置机制以添加自定义游戏功能。

## 概述

`mechanics.yml` 文件控制所有插件机制——可应用于物品、方块和家具的游戏功能。

**位置:** `plugins/Oraxen/mechanics.yml`

**格式：**
```yaml
mechanic_name:
  enabled: true/false  # 启用或禁用此机制
  # 每个机制特定的附加设置
```

## 机制分类

Oraxen 将 44 种机制分为 5 个类别：

| 类别 | 数量 | 用途 |
|----------|-------|---------|
| **杂项** | 9 | 核心物品行为（命令、消耗品、灵魂绑定等） |
| **游戏玩法** | 13 | 方块、家具、耐久度、修复系统 |
| **战斗** | 7 | 武器能力（雷神、火球、生命汲取等） |
| **农耕** | 6 | 资源采集（收获、熔炼、大型采矿等） |
| **装饰** | 5 | 视觉效果（帽子、皮肤、光环、背包） |

---

## 杂项机制

### commands
在物品使用时执行自定义命令。

```yaml
commands:
  enabled: true
```

**用法**: 通过 `Mechanics.custom` 配合事件触发器应用于物品。

**示例**：
```yaml
magic_wand:
  Mechanics:
    custom:
      one_usage:
        event: CLICK:right:all
        actions:
          console:
            - "give %player% diamond 1"
```

### armor_effects
穿戴盔甲时施加药水效果。

```yaml
armor_effects:
  enabled: true
  delay_in_ticks: 20  # 检查盔甲效果的间隔
```

**设置**：
- `delay_in_ticks` - 检查盔甲并应用效果的频率（默认: 20 = 1秒）

**用法**: 向盔甲物品添加药水效果。

**示例**：
```yaml
speed_boots:
  Mechanics:
    armor_effects:
      - SPEED:1
```

### consumable
使物品可以消耗（食用/饮用）并带有自定义效果。

```yaml
consumable:
  enabled: true
```

**用法**: 使物品可食用并带有自定义结果。

### consumable_potion_effects
在物品被消耗时施加药水效果。

```yaml
consumable_potion_effects:
  enabled: true
```

**用法**: 向可消耗物品添加药水效果。

**示例**：
```yaml
magic_apple:
  Mechanics:
    consumable:
      effects:
        - REGENERATION:5:60
        - ABSORPTION:2:120
```

### custom
具有事件、条件和命令的高级自定义动作系统。

```yaml
custom:
  enabled: true
```

**用法**: 创建复杂的物品行为，包括：
- 事件触发器（CLICK、BREAK、PLACE、KILL 等）
- 条件（权限、位置）
- 动作（命令、音效、消息）
- 冷却时间

**示例**：
```yaml
teleport_stick:
  Mechanics:
    custom:
      teleport:
        event: CLICK:right:all
        cooldown: 10
        actions:
          player:
            - "spawn"
```

### itemtype
设置自定义物品类型以与其他插件兼容。

```yaml
itemtype:
  enabled: true
```

**用法**: 定义物品类别（SWORD、HELMET 等）以进行插件集成。

### soulbound
防止物品在死亡时掉落。

```yaml
soulbound:
  enabled: true
```

**用法**: 使物品在玩家死亡时保留在背包中。

**示例**：
```yaml
legendary_sword:
  Mechanics:
    soulbound:
      enabled: true
```

### backpack
便携式存储系统——功能性背包。

```yaml
backpack:
  enabled: true
```

**用法**: 创建打开自定义 GUI 进行存储的物品。

**注意**: 与 `backpack_cosmetic`（仅装饰）不同。

### music_disc
为唱片机创建自定义音乐唱片。

```yaml
music_disc:
  enabled: true
```

**用法**: 配合 `sound.yml` 唱片机歌曲使用。

**示例**：
```yaml
epic_disc:
  material: MUSIC_DISC_13
  Components:
    jukebox_playable:
      song_key: "oraxen:epic_theme"
```

### misc
不属于其他类别的杂项功能。

```yaml
misc:
  enabled: true
```

---

## 游戏机制

### custom_block_sounds
控制自定义方块和家具的音效系统。

```yaml
custom_block_sounds:
  noteblock_and_block: true       # 为 NoteBlock 机制启用音效
  stringblock_and_furniture: true # 为 StringBlock 和家具启用音效
  chorusblock: true                # 为 ChorusBlock 机制启用音效
```

**重要**: 如果两种机制都被禁用，这些类型的音效将被强制关闭。

**何时禁用**：
- 有许多自定义方块的服务器性能优化
- 与其他音效插件冲突
- 调试音效问题

### noteblock
使用音符盒作为自定义方块（最快，兼容性最好）。

```yaml
noteblock:
  enabled: true
  tool_types:  # 可以破坏自定义方块的工���
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
  farmblock_check_delay: 1000  # 农田干燥检查间隔（刻）
  remove_mineable_tag: false   # 防止斧头快速破坏自定义方块
```

**关键设置**：

**`remove_mineable_tag`**（默认: `false`）
- 当 `false` 时：斧头可以快速破坏音符盒（原版行为）
- 当 `true` 时：移除 `mineable/axe` 标签，防止快速破坏
- **用途**: 如果玩家使用斧头破坏自定义方块太快，设为 `true`

**`farmblock_check_delay`**（默认: `1000`）
- 检查农田是否应该干燥的间隔（刻）
- 更高 = 更少的检查频率 = 更好的性能
- 更低 = 更灵敏的干燥 = 更差的性能

### stringblock
使用绊线作为自定义方块（支持树苗、生长）。

```yaml
stringblock:
  enabled: true
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
  sapling_growth_check_delay: 4000  # 树苗生长检查间隔（刻）
  disable_vanilla_strings: false     # 禁用原版绊线放置
```

**关键设置**：

**`disable_vanilla_strings`**（默认: `false`）
- 当 `true` 时：玩家无法放置原版绊线
- 当 `false` 时：原版绊线正常工作
- **用途**: 设为 `true` 以将绊线仅保留给自定义方块

**`sapling_growth_check_delay`**（默认: `4000`）
- 检查自定义树苗是否应该生长的频率
- 影响自定义树木生长机制

### chorusblock
使用紫颂植株作为自定义方块（自然外观）。

```yaml
chorusblock:
  enabled: true
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
```

**用法**: 最适合装饰性/自然外观的方块。

### shaped_block
使用涂蜡铜块作为自定义楼梯、台阶、门、活板门。

```yaml
shaped_block:
  enabled: true
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
  convert_vanilla_waxed: true       # 将原版涂蜡铜块转换为未涂蜡版本
  handle_world_generation: true     # 处理生成结构中的涂蜡铜块
```

**关键设置**：

**`convert_vanilla_waxed`**（默认: `true`）
- 将现有的涂蜡铜块转换为未涂蜡版本
- 将涂蜡铜材料专门保留给自定义方块
- 通过标记系统防止转换后方块的氧化

**`handle_world_generation`**（默认: `true`）
- 处理自然生成结构中的涂蜡铜块（试炼密室等）
- 确保自定义方块在生成的结构中正常工作

### block
旧版蘑菇柄方块（已弃用——请改用 noteblock）。

```yaml
block:
  enabled: false  # 默认禁用
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
```

**注意**: 这是旧的方块系统。新项目请使用 `noteblock`。

### furniture
使用 Display Entity 或 Item Frame 的自定义3D家具。

```yaml
furniture:
  enabled: true
  default_furniture_type: DISPLAY_ENTITY  # DISPLAY_ENTITY、ITEM_FRAME、GLOW_ITEM_FRAME
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
  evolution_check_delay: 200    # 植物生长检查间隔（刻）
  detect_viabackwards: true     # 阻止 Display Entity 在 <1.19.4 的客户端上显示
```

**关键设置**：

**`default_furniture_type`**（默认: `DISPLAY_ENTITY`）
- `DISPLAY_ENTITY` - 现代系统（1.19.4+），最佳视觉效果
- `ITEM_FRAME` - 旧版系统，更好的兼容性
- `GLOW_ITEM_FRAME` - ITEM_FRAME 的发光变体

**`detect_viabackwards`**（默认: `true`）
- 当 `true` 时：通过 ViaBackwards 阻止 Display Entity 家具在 <1.19.4 的客户端上显示
- 防止旧客户端崩溃/出现问题
- **用途**: 如果您有 ViaBackwards 并支持 <1.19.4 的客户端，保持 `true`

**`evolution_check_delay`**（默认: `200`）
- 检查具有植物机制的家具是否应该生长的频率
- 用于自定义植物家具

### durability
物品的自定义耐久度系统。

```yaml
durability:
  enabled: true
```

**用法**: 在物品上设置自定义耐久度值。

**示例**：
```yaml
crystal_sword:
  Mechanics:
    durability:
      value: 500
```

### efficiency
工具的挖掘速度修改器。

```yaml
efficiency:
  enabled: true
```

**用法**: 使工具挖掘更快或更慢。

**示例**：
```yaml
super_pickaxe:
  Mechanics:
    efficiency:
      amount: 10
```

### repair
自定义物品修复系统。

```yaml
repair:
  enabled: true
  oraxen_durability_only: false  # 仅修复具有自定义耐久度的 Oraxen 物品
```

**关键设置**：

**`oraxen_durability_only`**（默认: `false`）
- 当 `true` 时：`/oraxen repair` 命令仅修复具有自定义耐久度的 Oraxen 物品
- 当 `false` 时：命令也可修复原版物品
- **用途**: 设为 `true` 以防止修复原版物品

### food
具有饱和度和营养值的自定义食物物品。

```yaml
food:
  enabled: true
```

**用法**: 创建自定义食物物品。

### toggle_light
手持/放置时发光的物品。

```yaml
toggle_light:
  enabled: true
```

**用法**: 创建便携式光源。

---

## 装饰机制

### aura
玩家周围的粒子效果。

```yaml
aura:
  enabled: true
```

**用法**: 向物品或玩家效果添加粒子光环。

### backpack_cosmetic
玩家背上的可视化背包（仅装饰，无存储功能）。

```yaml
backpack_cosmetic:
  enabled: true
```

**注意**: 使用基于数据包的盔甲架进行显示。与 `backpack`（提供存储功能）不同。

### hat
将物品当作帽子穿戴。

```yaml
hat:
  enabled: true
```

**用法**: 允许玩家将物品装备为装饰性帽子。

### skin
自定义物品皮肤/纹理。

```yaml
skin:
  enabled: true
```

**用法**: 动态地将不同纹理应用于物品。

### skinnable
外观可以更改的物品。

```yaml
skinnable:
  enabled: true
```

**注意**: 与 `skin` 不同——`skinnable` 标记物品为可自定义，`skin` 应用皮肤。

---

## 战斗机制

### lifeleech
造成伤害时治疗。

```yaml
lifeleech:
  enabled: true
```

**用法**: 击中时恢复生命值的武器。

**示例**：
```yaml
vampire_sword:
  Mechanics:
    lifeleech:
      amount: 0.5  # 治疗造成伤害的 50%
```

### bleeding
攻击造成持续伤害。

```yaml
bleeding:
  enabled: true
```

**用法**: 施加流血效果的武器。

### thor
召唤雷击。

```yaml
thor:
  enabled: true
```

**用法**: 召唤闪电的物品。

### energyblast
投射能量攻击。

```yaml
energyblast:
  enabled: true
```

**用法**: 发射能量弹的武器。

### fireball
发射火球。

```yaml
fireball:
  enabled: true
```

**用法**: 发射火球的物品。

### witherskull
发射凋零头颅。

```yaml
witherskull:
  enabled: true
```

**用法**: 发射凋零头颅弹射物的物品。

### knockback_strike
击中时击退实体。

```yaml
knockback_strike:
  enabled: true
```

**用法**: 具有增强击退效果的武器。

### spear_lunge
攻击时向前冲刺。

```yaml
spear_lunge:
  enabled: true
```

**用法**: 具有冲刺机制的长矛或武器。

---

## 农耕机制

### bigmining
同时挖掘多个方块（连锁挖矿）。

```yaml
bigmining:
  enabled: true
  call_events: true  # Oraxen 是否调用 BlockBreakEvent 还是仅监听
```

**关键设置**：

**`call_events`**（默认: `true`）
- 当 `true` 时：Oraxen 为每个被破坏的方块调用 `BlockBreakEvent`
- 当 `false` 时：Oraxen 仅监听事件
- **已知问题**: 某些附魔插件在 `true` 时会有问题
- **用途**: 如果您有附魔插件冲突，设为 `false`

### harvesting
收获时自动补种作物。

```yaml
harvesting:
  enabled: true
```

**用法**: 自动补种农田的工具。

### smelting
自动熔炼挖掘的方块。

```yaml
smelting:
  enabled: true
  blacklist_cooked:  # 不应自动熔炼的物品
    - WET_SPONGE
```

**关键设置**：

**`blacklist_cooked`** - 永不自动熔炼的物品列表
- 默认: `WET_SPONGE`（熔炼会将其变成普通海绵）
- 如果熔炼导致问题，将物品添加到此列表

**示例**：
```yaml
smelting:
  blacklist_cooked:
    - WET_SPONGE
    - ICE  # 不要融化冰块
```

### watering
在区域内灌溉农田。

```yaml
watering:
  enabled: true
```

**用法**: 浇灌作物的工具。

### bottledexp
在瓶子中存储和使用经验值。

```yaml
bottledexp:
  enabled: true
  durability_cost: 10  # 每次使用消耗的耐久度
```

**关键设置**：

**`durability_cost`**（默认: `10`）
- 使用瓶装经验时消耗的耐久度
- 设为 `0` 表示不消耗耐久度

### bedrockbreak
使用自定义工具破坏基岩。

```yaml
bedrockbreak:
  enabled: true
  disable_on_first_layer: false  # 防止破坏基岩底层
  durability_cost: 500           # 每个基岩方块消耗的耐久度
```

**关键设置**：

**`disable_on_first_layer`**（默认: `false`）
- 当 `true` 时：无法破坏 Y=0 的基岩（防止掉入虚空）
- 当 `false` 时：可以破坏所有基岩层
- **重要**: 设为 `true` 以防止玩家掉入虚空

**`durability_cost`**（默认: `500`）
- 破坏一个基岩方块时消耗的耐久度
- 高消耗可防止过度开采基岩

---

## 机制组合

某些机制可以在同一物品上组合使用：

**常见组合**：
```yaml
legendary_pickaxe:
  Mechanics:
    durability:
      value: 5000
    efficiency:
      amount: 15
    bigmining:
      vein_miner: true
      blocks: 10
    smelting: {}
```

**不兼容的组合**：
- 不能在同一物品上组合多个方块机制（noteblock、stringblock、chorusblock）
- 不能组合 `backpack` 和 `backpack_cosmetic`（请选择其一）
- 不能以冲突方式组合 `skin` 和 `skinnable`

---

## 性能优化

### 高性能设置

适用于资源有限的服务器：

```yaml
# 禁用装饰机制
aura:
  enabled: false
backpack_cosmetic:
  enabled: false
hat:
  enabled: false

# 增加检查延迟
armor_effects:
  delay_in_ticks: 40  # 降低检查频率（2秒）

noteblock:
  farmblock_check_delay: 2000  # 降低检查频率

stringblock:
  sapling_growth_check_delay: 8000

furniture:
  evolution_check_delay: 400
```

### 低资源使用

适用于轻量级服务器的最小机制：

```yaml
# 仅启用必要的机制
durability:
  enabled: true
repair:
  enabled: true
custom:
  enabled: true

# 禁用其他所有机制
aura:
  enabled: false
# ... 等等
```

---

## 故障排除

### "机制不工作"
- 验证 mechanics.yml 中 `enabled: true`
- 检查物品是否正确配置了机制
- 重载: `/oraxen reload all`
- 检查控制台是否有错误

### "自定义方块被斧头破坏太快"
```yaml
noteblock:
  remove_mineable_tag: true
```

### "附魔插件与 bigmining 冲突"
```yaml
bigmining:
  call_events: false
```

### "Display Entity 家具导致旧客户端崩溃"
```yaml
furniture:
  detect_viabackwards: true
```

### "玩家开采基岩掉入虚空"
```yaml
bedrockbreak:
  disable_on_first_layer: true
```

### "原版绊线与自定义方块冲突"
```yaml
stringblock:
  disable_vanilla_strings: true
```

---

## 另请参阅

- [自定义物品能力](../creating-content/items/abilities/) - 如何将机制应用于物品
- [自定义方块](../creating-content/blocks/) - 方块机制用法
- [家具指南](../creating-content/furniture/) - 家具机制详情
- [插件设置](../plugin-setup/plugin-settings) - 通用插件配置