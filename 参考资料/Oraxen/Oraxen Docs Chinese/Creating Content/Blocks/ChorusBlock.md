---
description: 如何使用紫颂植物状态添加自定义方块
---

import { Callout } from 'nextra/components'

# 紫颂方块机制 (ChorusBlock)

紫颂方块机制允许你使用 Minecraft 的紫颂植物方块状态来创建自定义方块。这提供了多达 **63种独特的方块变体**。

**最适合透明方块**，如自定义树叶、玻璃变体，或需要透视渲染的单格家具。对于简单的透明方块，紫颂方块的性能优于展示实体。

<Callout type="info">
不确定使用哪种方块机制？请参阅[自定义方块概述](/creating-content/blocks)进行对比。
</Callout>

<Callout type="warning">
**推荐 Paper 服务器使用**

为了获得最佳性能和稳定性，请在 `config/paper-global.yml` 中启用此设置：
```yaml
block-updates:
  disable-chorus-plant-updates: true
```
如果不设置此项，Oraxen 必须监听昂贵的物理事件，可能导致卡顿和轻微错误。
</Callout>

## 基本配置

```yaml
my_chorus_block:
  displayname: "<gray>Custom Block"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "block/cube_all"
    textures:
      - my_block_texture.png
  Mechanics:
    chorusblock:
      custom_variation: 1  # 必须唯一，范围 1-63
      model: my_chorus_block
      hardness: 5
      drop:
        silktouch: false
        loots:
          - { oraxen_item: my_chorus_block, probability: 1.0 }
```

## 配置选项

| 选项 | 类型 | 描述 |
|--------|------|-------------|
| `custom_variation` | integer | **必填。** 唯一 ID，范围 1-63 |
| `model` | string | 方块模型路径 |
| `hardness` | integer | 破坏时间倍率（默认：1） |
| `light` | integer | 光照等级 0-15（默认：0） |
| `is_falling` | boolean | 像沙子/沙砾一样下落（默认：false） |
| `blast_resistant` | boolean | 抵抗爆炸（默认：false） |
| `immovable` | boolean | 不能被活塞移动（默认：false） |
| `drop` | object | 掉落物配置 |
| `block_sounds` | object | 自定义音效 |
| `limited_placing` | object | 放置限制 |
| `blocklocker` | object | BlockLocker 保护 |
| `clickActions` | list | 点击时执行的动作 |
| `storage` | object | 容器配置 |
| `seat` | object | 座椅配置 |

## 自定义变体

每个紫颂方块必须有一个唯一的 `custom_variation`，范围在 1 到 63 之间。此 ID 决定了使用哪个紫颂植物状态来表示你的方块。

```yaml
# 方块 1
ruby_ore:
  Mechanics:
    chorusblock:
      custom_variation: 1
      # ...

# 方块 2
sapphire_ore:
  Mechanics:
    chorusblock:
      custom_variation: 2
      # ...
```

<Callout type="error">
永远不要重复使用 `custom_variation` 值。每个值必须在所有紫颂方块物品中唯一。
</Callout>

## 掉落物配置

配置方块被破坏时掉落的内容：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    drop:
      silktouch: true  # 仅精准采集时掉落
      loots:
        - oraxen_item: my_block
          probability: 1.0
        - oraxen_item: bonus_item
          probability: 0.25
          max_amount: 3
```

## 自定义音效

为方块交互添加自定义音效：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    block_sounds:
      place_sound: block.stone.place
      break_sound: block.stone.break
      hit_sound: block.stone.hit
      step_sound: block.stone.step
      fall_sound: block.stone.fall
```

你也可以自定义音量和音调：

```yaml
Mechanics:
  chorusblock:
    block_sounds:
      place:
        sound: block.amethyst_block.place
        volume: 1.0
        pitch: 0.8
      break_sound: block.amethyst_block.break
```

## 发光

使方块发光：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    light: 12  # 光照等级 0-15
```

## 下落方块

创建像沙子或沙砾一样下落的方块：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    is_falling: true
```

## 防爆

使方块抵抗爆炸：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    blast_resistant: true
```

## 不可推动

防止活塞移动方块：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    immovable: true
```

## 限制放置

限制方块的放置位置：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    limited_placing:
      roof: false
      floor: true
      wall: false
      type: ALLOW  # 或 DENY
      block_types:
        - GRASS_BLOCK
        - DIRT
      block_tags:
        - base_stone_overworld
      oraxen_blocks:
        - custom_stone
```

## BlockLocker 保护

启用 [BlockLocker](https://www.spigotmc.org/resources/blocklocker.3268/) 保护：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    blocklocker:
      can_protect: true
      protection_type: CONTAINER  # CONTAINER、DOOR 或 ATTACHABLE
```

## 点击动作

点击时执行命令或播放音效。详情参见[点击动作机制](/creating-content/items/abilities/clickaction)。

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    clickActions:
      - conditions:
          - "has_permission{perm=my.permission}"
        actions:
          - "[console] say %player% clicked the block!"
```

## 存储

将你的方块变成容器：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    storage:
      type: STORAGE       # STORAGE、SHULKER、PERSONAL、DISPOSAL 或 ENDERCHEST
      rows: 3             # 行数 (1-6)
      title: "My Storage" # 容器标题
      open_sound: block.chest.open
      close_sound: block.chest.close
```

存储类型：
- `STORAGE` - 标准共享容器
- `SHULKER` - 破坏时物品保留在方块中
- `PERSONAL` - 每个玩家独立的存储
- `DISPOSAL` - 关闭时物品被删除
- `ENDERCHEST` - 打开玩家的末影箱

## 座椅

让玩家坐在你的方块上（非常适合椅子和长凳）：

```yaml
Mechanics:
  chorusblock:
    custom_variation: 1
    seat:
      height: 0.5  # 从方块顶部的高度偏移
      yaw: 0       # 可选：坐下时的固定旋转角度
```

<Callout type="info">
当玩家右键点击带有座椅的方块时，他们会坐在上面。座椅使用一个隐形的盔甲架实体。
</Callout>

## 完整示例

以下是一个自定义矿石方块的完整示例：

```yaml
chorus_ruby_ore:
  displayname: "<red>Ruby Ore"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "block/cube_all"
    textures:
      - ruby_ore.png
  Mechanics:
    chorusblock:
      custom_variation: 5
      model: chorus_ruby_ore
      hardness: 8
      light: 3
      blast_resistant: true
      block_sounds:
        place_sound: block.deepslate.place
        break_sound: block.deepslate.break
        step_sound: block.deepslate.step
      drop:
        silktouch: true
        loots:
          - oraxen_item: ruby
            probability: 1.0
            max_amount: 2
      limited_placing:
        floor: true
        roof: true
        wall: true
        type: ALLOW
        block_tags:
          - base_stone_overworld
          - base_stone_nether
```

## 与其他方块机制的对比

| 功能 | 音符盒 | 绊线 | 紫颂 |
|---------|-----------|-------------|-------------|
| 最大变体数 | ~800 | 127 | 63 |
| 基础方块 | 音符盒 | 绊线 | 紫颂植物 |
| 自定义音效 | 是 | 是 | 是 |
| 发光 | 是 | 是 | 是 |
| 下落方块 | 是 | 是 | 是 |
| 防爆 | 是 | 是 | 是 |
| 不可推动 | 是 | 是 | 是 |
| 存储 | 是 | 是 | 是 |
| 点击动作 | 是 | 是 | 是 |
| 座椅 | 否 | 否 | 是 |
| 方向性 | 是 | 否 | 否 |
| 含水 | 否 | 是 | 否 |

对于透视渲染很重要的**透明方块**（树叶、玻璃类方块、简单的透明家具），或者在需要方块上有**座椅**时，请选择紫颂方块。对于不透明的方块，推荐使用音符盒，因为它有更多的可用槽位（约800 vs 63）。
