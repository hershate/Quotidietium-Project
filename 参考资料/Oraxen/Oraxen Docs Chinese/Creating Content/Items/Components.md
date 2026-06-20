---
description: Minecraft 1.20.5+ 中引入的数据驱动物品组件
---

import { Tabs, Callout } from 'nextra/components'

# 物品组件

从 Minecraft 1.20.5 开始，物品使用数据驱动组件而非 NBT 标签。Oraxen 通过物品配置中的 `Components` 部分支持这些组件。

<Callout type="info">
  组件是特定于版本的。请务必查看以下部分，了解你的 Minecraft 版本中可用的组件。
</Callout>

---

## 基础组件

这些组件在所有支持组件的版本中均可用（1.20.5+）。

### durability

为物品设置自定义耐久度。对于非工具材质（如 PAPER），你还可以配置耐久度何时消耗。

<Tabs items={['简单', '高级']}>
<Tabs.Tab>
```yaml
Components:
  durability: 100
```
</Tabs.Tab>
<Tabs.Tab>
```yaml
Components:
  durability:
    value: 100
    damage_block_break: true   # 破坏方块时消耗耐久度
    damage_entity_hit: true    # 攻击实体时消耗耐久度
```
</Tabs.Tab>
</Tabs>

### fire_resistant

使物品免疫火焰和岩浆伤害。

```yaml
Components:
  fire_resistant: true
```

### hide_tooltip

隐藏悬停在物品上时的所有提示框。

```yaml
Components:
  hide_tooltip: true
```

---

## 工具组件

为类似工具的物配置挖掘行为。

```yaml
Components:
  tool:
    damage_per_block: 1           # 每个方块消耗的耐久度（默认：1）
    default_mining_speed: 1.0     # 基础挖掘速度（默认：1.0）
    rules:
      - speed: 2.0
        correct_for_drops: true   # 方块是否掉落物品
        material: DIAMOND_BLOCK   # 单个材质
        # 或使用列表：
        # materials:
        #   - DIAMOND_BLOCK
        #   - NETHERITE_BLOCK
        tag: minecraft:mineable/axe   # 方块标签
        # 或使用列表：
        # tags:
        #   - minecraft:mineable/axe
        #   - minecraft:mineable/shovel
```

<Callout>
  参见 [Minecraft Wiki - 方块标签](https://minecraft.wiki/w/Tag#Block_tags_2) 获取所有可用的方块标签。
</Callout>

---

## 食物和消耗品组件

使物品可食用或可消耗，并带有各种效果。

<Tabs items={['1.21.2+', '1.20.5 - 1.21']}>
<Tabs.Tab>
在 1.21.2+ 中，食物和消耗品行为被拆分为单独的组件，以提供更大的灵活性。

### consumable

使物品可消耗，并对消耗行为进行详细控制。

<Tabs items={['简单', '完整示例']}>
<Tabs.Tab>
```yaml
Components:
  consumable: true
```
</Tabs.Tab>
<Tabs.Tab>
```yaml
Components:
  consumable:
    consume_seconds: 1.6          # 消耗时间（默认：1.6）
    animation: EAT                # EAT, DRINK, BLOCK, BOW, SPEAR, CROSSBOW, SPYGLASS, TOOT_HORN, BRUSH
    sound: entity.generic.eat     # 消耗时播放的声音
    has_consume_particles: true   # 消耗时显示粒子
    on_consume_effects:           # 消耗时应用的效果
      - type: apply_effects
        effects:
          minecraft:haste:
            duration: 200           # 持续时间（秒，内部转换为刻）
            amplifier: 0
            ambient: false
            show_particles: true
            show_icon: true
        probability: 1.0          # 应用概率（0.0 - 1.0）
      - type: remove_effects
        effects:
          - minecraft:poison
          - minecraft:wither
      - type: clear_all_effects
      - type: teleport_randomly
        diameter: 16              # 传送半径
      - type: play_sound
        sound: entity.enderman.teleport
```
</Tabs.Tab>
</Tabs>

#### 消耗效果类型

| 类型 | 描述 | 参数 |
|------|-------------|------------|
| `apply_effects` | 应用药水效果 | `effects`（映射表）, `probability` |
| `remove_effects` | 移除特定效果 | `effects`（效果 ID 列表） |
| `clear_all_effects` | 清除所有药水效果 | 无 |
| `teleport_randomly` | 随机传送玩家 | `diameter`（默认：16） |
| `play_sound` | 播放声音 | `sound` |

### food

为消耗品添加营养值和饱和度。在 1.21.2+ 中，这仅处理饥饿值恢复——消耗行为请使用 `consumable`。

```yaml
Components:
  food:
    nutrition: 4
    saturation: 2.5
    can_always_eat: false  # 可选，允许不饿时也能食用
```

### use_remainder

指定消耗后返还的物品。

```yaml
Components:
  use_remainder:
    oraxen_item: empty_bottle
    # 或使用其他物品类型：
    # minecraft_type: BOWL
    # crucible_item: crucibleid
    # mmoitems_id: id
    # mmoitems_type: type
    # ecoitem_id: ecoid
    amount: 1  # 返还的物品数量
```

### use_cooldown

使用物品后应用冷却时间。

```yaml
Components:
  use_cooldown:
    seconds: 2.5                  # 冷却时间（默认：1.0）
    group: oraxen:healing_items   # 同组物品共享冷却时间
    # 设置为 "" 以影响所有相同材质的物品
```
</Tabs.Tab>
<Tabs.Tab>
### food

在 1.20.5 到 1.21 版本中，food 组件在一个地方处理所有消耗品属性。

```yaml
Components:
  food:
    nutrition: 4                  # 恢复的饥饿值点数
    saturation: 2.5               # 饱和度修饰符
    can_always_eat: false         # 可选，允许不饿时也能食用
    eat_seconds: 1.6              # 消耗时间（默认：1.6）
    effects:                      # 消耗时的药水效果
      haste:
        duration: 200             # 持续时间（刻）
        amplifier: 0
        ambient: false
        show_particles: true
        show_icon: true
        probability: 1.0          # 应用概率（0.0 - 1.0）
```
</Tabs.Tab>
</Tabs>

---

## 装备组件

<Callout type="warning">
  这些组件仅在 **Minecraft 1.21.2+** 中可用。
</Callout>

### equippable

使物品可以装备在护甲槽位中。

```yaml
Components:
  equippable:
    slot: HEAD                    # HEAD, CHEST, LEGS, FEET, BODY
    model: oraxen:custom_armor    # 自定义护甲模型（可选）
    camera_overlay: minecraft:pumpkin_blur  # 装备时的覆盖纹理（可选）
    equip_sound: item.armor.equip_chain     # 装备时的声音（仅 Paper）
    allowed_entity_types:         # 可以装备的实体（可选，默认为全部）
      - PLAYER
      - SKELETON
      - ZOMBIE
    dispensable: true             # 可通过发射器装备（默认：true）
    swappable: true               # 可与已装备物品交换（默认：true）
    damage_on_hurt: true          # 受伤时消耗耐久度（默认：true）
```

<Callout>
  `equip_sound` 选项需要 **Paper** 服务器。实体类型列表：[Spigot EntityType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html)
</Callout>

---

## 视觉组件

<Callout type="warning">
  这些组件仅在 **Minecraft 1.21.2+** 中可用。
</Callout>

### item_model

为物品设置自定义模型。这是在 1.21.4+ 中设置物品外观的推荐方式。

```yaml
Components:
  item_model: oraxen:custom_sword
```

引用模型路径：`assets/oraxen/items/custom_sword.json`

<Callout type="info">
  有关物品模型如何与 Oraxen 资源包生成配合使用的更多详细信息，请参见[物品外观](/creating-content/items/appearance)。
</Callout>

### tooltip_style

使用自定义精灵图自定义提示框外观。

```yaml
Components:
  tooltip_style: oraxen:fancy
```

这需要自定义纹理：
- `assets/oraxen/textures/gui/sprites/tooltip/fancy_background.png`
- `assets/oraxen/textures/gui/sprites/tooltip/fancy_frame.png`

<Callout>
  提示框精灵图可以使用 `.mcmeta` 文件进行动画处理。有关详细信息，请参见 [Minecraft Wiki](https://minecraft.wiki/w/Resource_pack#Animation)。
</Callout>

---

## 音频组件

### jukebox_playable

<Callout type="warning">
  此组件需要 **Minecraft 1.21+** 和 **Paper** 服务器。
</Callout>

使此物品可在唱片机中播放。

```yaml
Components:
  jukebox_playable:
    show_in_tooltip: true
    song_key: minecraft:music_disc.cat  # 或自定义: oraxen:custom_song
```

<Callout>
  自定义歌曲需要一个数据包来注册歌曲。使用 Oraxen 的声音系统创建自定义音乐唱片，并自动生成数据包。
</Callout>

---

## 通用组件系统（1.21.3+）

<Callout type="info">
  从 **Minecraft 1.21.3** 开始，Oraxen 支持通过通用组件系统设置任意数据组件。这允许你使用 Oraxen 未显式处理的 Minecraft 数据组件。
</Callout>

具有对象/小节值（非原始类型）的组件可以直接传递给 Minecraft 的数据组件系统。这对于 Oraxen 尚未作为专用选项公开的原版组件非常有用。

示例（`repairable`）：

```yaml
Components:
  repairable:
    items:
      - minecraft:diamond
```

自定义对象组件遵循相同的模式：

```yaml
Components:
  # 支持通用对象组件
  custom_component:
    some_property: value
    another_property: 123
```

Oraxen 在将这些组件对象应用到最终物品之前，会通过 Minecraft 的组件编解码器进行验证和反序列化。

---

## AttributeModifiers（现代格式）

<Callout type="info">
  需要 **Minecraft 1.20.5+**（用于 `EquipmentSlotGroup` API）。提示框显示模式需要 **1.21.6+**。
</Callout>

除了旧版列表格式外，Oraxen 1.212.0+ 还支持基于小节的 `AttributeModifiers` 配置。每个修饰符定义为命名的小节：

```yaml
emerald_helmet:
  material: PAPER
  AttributeModifiers:
    armor:
      attribute: ARMOR
      amount: 3
      operation: ADD_NUMBER
      slot: HEAD
    toughness:
      attribute: ARMOR_TOUGHNESS
      amount: 2
      operation: ADD_NUMBER
      slot: HEAD
    health_boost:
      attribute: MAX_HEALTH
      amount: 4
      operation: ADD_NUMBER
      slot: HEAD
```

### 字段

| 字段 | 必需 | 描述 |
|-------|----------|-------------|
| `attribute` | 是 | 要修改的属性（例如 `ARMOR`, `ATTACK_DAMAGE`, `MAX_HEALTH`） |
| `amount` | 是 | 修饰符数值 |
| `operation` | 否 | `ADD_NUMBER`（默认）, `ADD_SCALAR`, 或 `MULTIPLY_SCALAR_1` |
| `slot` | 否 | 装备槽位组：`HAND`, `OFFHAND`, `HEAD`, `CHEST`, `LEGS`, `FEET`, `ARMOR`, `ANY`（默认） |

### 显示模式（1.21.6+）

控制每个修饰符在物品提示框中的显示方式：

```yaml
AttributeModifiers:
  hidden_armor:
    attribute: ARMOR
    amount: 5
    operation: ADD_NUMBER
    slot: CHEST
    display:
      type: hidden  # 完全从提示框中隐藏
  custom_text:
    attribute: ATTACK_DAMAGE
    amount: 10
    operation: ADD_NUMBER
    slot: HAND
    display:
      type: override
      text: "<red>+10 Fire Damage"  # 自定义 MiniMessage 提示框文本
```

| 显示类型 | 描述 |
|-------------|-------------|
| `hidden` | 完全从提示框中隐藏修饰符 |
| `reset`（或 `default`） | 显示默认的原版提示框格式 |
| `override`（或 `custom`） | 用自定义文本替换提示框行（需要 `text` 字段） |

<Callout type="warning">
旧版列表格式（`AttributeModifiers: [{...}]`）仍然有效。如果 Oraxen 检测到小节格式，它会使用现代解析器。如果发现列表，则回退到旧版格式。两种格式可以在不同物品中共存。
</Callout>

---

## 完整示例

### 自定义护甲（1.21.2+）

<Tabs items={['现代格式 (1.20.5+)', '旧版格式']}>
<Tabs.Tab>
```yaml
emerald_helmet:
  itemname: <gradient:#89E59D:#37C6BA>Emerald Helmet
  material: PAPER
  Components:
    durability:
      value: 437
      damage_entity_hit: true
    equippable:
      slot: HEAD
      model: oraxen:emerald
  AttributeModifiers:
    health:
      attribute: MAX_HEALTH
      amount: 2
      operation: ADD_NUMBER
      slot: HEAD
    armor:
      attribute: ARMOR
      amount: 3
      operation: ADD_NUMBER
      slot: HEAD
    toughness:
      attribute: ARMOR_TOUGHNESS
      amount: 2
      operation: ADD_NUMBER
      slot: HEAD
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - default/armors/emerald_helmet
```
</Tabs.Tab>
<Tabs.Tab>
```yaml
emerald_helmet:
  itemname: <gradient:#89E59D:#37C6BA>Emerald Helmet
  material: PAPER
  Components:
    durability:
      value: 437
      damage_entity_hit: true
    equippable:
      slot: HEAD
      model: oraxen:emerald
  AttributeModifiers:
    - { attribute: MAX_HEALTH, amount: 2, operation: 0, slot: HEAD }
    - { attribute: ARMOR, amount: 3, operation: 0, slot: HEAD }
    - { attribute: ARMOR_TOUGHNESS, amount: 2, operation: 0, slot: HEAD }
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - default/armors/emerald_helmet
```
</Tabs.Tab>
</Tabs>

### 带效果的自定义食物（1.21.2+）

```yaml
miner_sandwich:
  itemname: <gradient:#F69D84:#FAD98D>Miner's Sandwich
  material: PAPER
  Components:
    food:
      nutrition: 8
      saturation: 12.8
      can_always_eat: true
    consumable:
      consume_seconds: 5
      animation: EAT
      sound: entity.generic.eat
      has_consume_particles: true
      on_consume_effects:
        - type: apply_effects
          effects:
            minecraft:haste:
              duration: 3600
              amplifier: 0
              ambient: true
              show_particles: true
              show_icon: true
          probability: 1.0
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - default/sandwich.png
```

### 自定义音乐唱片（1.21+）

```yaml
welcome_disk:
  itemname: <gradient:#9055FF:#13E2DA>Welcome Disk
  material: PAPER
  Components:
    jukebox_playable:
      show_in_tooltip: true
      song_key: oraxen:welcome
  Pack:
    generate_model: true
    parent_model: item/handheld
    textures:
      - default/welcome_disk.png
```

### 带挖掘规则的自定义工具

```yaml
super_pickaxe:
  itemname: <gradient:#59A7EA:#F1D2FF>Super Pickaxe
  material: DIAMOND_PICKAXE
  Components:
    durability: 2000
    fire_resistant: true
    tool:
      damage_per_block: 1
      default_mining_speed: 2.0
      rules:
        - speed: 10.0
          correct_for_drops: true
          tags:
            - minecraft:mineable/pickaxe
            - minecraft:needs_diamond_tool
```