---
description: 如何使用音符盒状态创建自定义方块
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966827878706708560/unknown.png
coverY: 0
---

import { Callout } from 'nextra/components'

# 音符盒 (NoteBlock)

音符盒机制允许你使用 Minecraft 的音符盒状态来创建自定义方块。这提供了多达 **约800种独特的方块变体**，使其成为大多数自定义方块的最佳选择。

<Callout type="info">
不确定使用哪种方块机制？请参阅[方块概述](/creating-content/blocks)进行对比。
</Callout>

<Callout type="warning">
**推荐 Paper 服务器使用**

为了获得最佳性能，请在 `config/paper-global.yml` 中启用此设置：
```yaml
block-updates:
  disable-noteblock-updates: true
```
</Callout>

## 创建你的第一个方块

### 父模型

物品配置与任何 Oraxen 物品相同。要生成方块模型，请指定你的方块应使用的 `parent_model`。

**支持的父模型：**
| 模型 | 纹理数量 | 用例 |
|-------|----------|----------|
| `block/cube_all` | 1 | 所有面相同纹理 |
| `block/cube_column` | 2 | 原木、柱子（顶/底面 + 侧面） |
| `block/cross` | 1 | 植物、花朵 |
| `block/orientable` | 3 | 熔炉、侦测器 |
| `block/orientable_vertical` | 2 | 垂直朝向 |

```yaml
my_block:
  displayname: "My block"
  material: DIAMOND
  Pack:
    generate_model: true
    parent_model: "block/cube_all"
    textures:
      - my_block_texture.png
```

### 方块机制配置

要使用此机制，你需要告诉 Oraxen 使用哪个模型。然后你需要使用一个未被其他方块占用的 `custom_variation`。

```yaml
Mechanics:
  noteblock:
    custom_variation: 2
    model: my_block
    drop:
      silktouch: false
      minimal_type: STONE
      loots:
        - {oraxen_item: caveblock, probability: 1.0}
```

### 挖掘速度与工具

你可以通过 hardness 子节自定义挖掘速度和最适合的工具。

```yaml
Mechanics:
  noteblock:
    custom_variation: 2
    model: my_block
    hardness: 20 # 使其非常难挖
    drop:
      silktouch: false
      minimal_type: STONE
      best_tools:
        - PICKAXE # 使用镐挖掘更快
      loots:
        - {oraxen_item: caveblock, probability: 1.0}
```

## 方块功能

### 发光方块

```yaml
Mechanics:
  noteblock:
    custom_variation: 2
    model: my_block
    light: 5  # 光照等级 0-15
```

### 下落方块

模拟沙子和沙砾的行为：
```yaml
Mechanics:
  noteblock:
    is_falling: true
```

### 防爆

使方块在爆炸中存活：
```yaml
Mechanics:
  noteblock:
    blast_resistant: true
```

### 不可推动

防止活塞推动方块：
```yaml
Mechanics:
  noteblock:
    immovable: true
```

### 可点燃方块

允许方块被火焰/打火石点燃：
```yaml
Mechanics:
  noteblock:
    can_ignite: true
```

### 存储

创建自定义存储容器：

```yaml
Mechanics:
  noteblock:
    barrier: true
    storage:
      type: STORAGE      # STORAGE、PERSONAL、ENDERCHEST 或 DISPOSAL
      rows: 5            # 默认: 6
      title: "<red>My Storage"
      open_sound: entity.shulker.open
      close_sound: entity.shulker.close
```

存储类型：
- **STORAGE** - 普通箱子，任何人都可以访问
- **PERSONAL** - 每个玩家独立的物品栏，类似末影箱
- **ENDERCHEST** - 访问实际的末影箱
- **DISPOSAL** - 垃圾桶，物品在关闭时被删除

### 限制放置

限制方块的放置位置：

```yaml
Mechanics:
  noteblock:
    limited_placing:
      roof: true
      floor: true
      wall: true
      type: ALLOW  # 或 DENY
      block_types:
        - GRASS_BLOCK
        - DIRT
      block_tags:
        - base_stone_nether
      oraxen_blocks:
        - ruby_ore
```

### BlockLocker 保护

启用 [BlockLocker](https://www.spigotmc.org/resources/blocklocker.3268/) 保护：
```yaml
Mechanics:
  noteblock:
    blocklocker:
      can_protect: true
      protection_type: CONTAINER  # CONTAINER、DOOR 或 ATTACHABLE
```

### 点击动作

当玩家点击方块时执行命令、播放音效或发送消息。详情参见[点击动作](/creating-content/items/abilities/clickaction)。

## 完整矿石示例

```yaml
amethyst_ore:
  displayname: "<light_purple>Amethyst Ore"
  material: DIAMOND
  Pack:
    generate_model: true
    parent_model: "block/cube_all"
    textures:
      - amethyst_ore
  Mechanics:
    noteblock:
      block_sounds:
        place_sound: block.stone.place
        break_sound: block.stone.break
        hit_sound: block.stone.hit
        step_sound: block.stone.step
        fall_sound: block.stone.fall
        volume: 0.8
        pitch: 0.8
      custom_variation: 1
      model: amethyst_ore
      hardness: 6
      drop:
        silktouch: true
        fortune: true
        minimal_type: IRON
        best_tools:
          - PICKAXE
        loots:
          - oraxen_item: amethyst
            probability: 1.0
```

<Callout type="info">
这不会在你的世界中生成矿石。有关自然矿石生成，请参阅[世界生成器](/compatibility/world-generators)。
</Callout>

---

## 方向性方块

此子机制允许方块根据放置方向改变纹理，类似原木。

### 方向类型

| 类型 | 使用的变体数 | 方向 |
|------|-----------------|------------|
| `LOG` | 3 | Y、X、Z 轴 |
| `FURNACE` | 4 | 北、南、东、西 |
| `DROPPER` | 6 | 全部6个方向 |

### 父方块配置

```yaml
custom_log:
  displayname: "<white>Custom Log"
  material: PAPER
  Pack:
    generate_model: false
    model: custom_log_model
  Mechanics:
    noteblock:
      model: custom_log_model
      custom_variation: 1
      directional:
        directional_type: LOG
        y_block: custom_log_y
        x_block: custom_log_x
        z_block: custom_log_z
      hardness: 1
      drop:
        best_tools:
          - AXE
        loots:
          - {oraxen_item: custom_log, probability: 1.0}
```

### 子方块配置

```yaml
custom_log_y:
  excludeFromInventory: true
  material: PAPER
  Mechanics:
    noteblock:
      custom_variation: 1
      directional:
        parent_block: custom_log

custom_log_x:
  excludeFromInventory: true
  material: PAPER
  Mechanics:
    noteblock:
      custom_variation: 2
      directional:
        parent_block: custom_log

custom_log_z:
  excludeFromInventory: true
  material: PAPER
  Mechanics:
    noteblock:
      custom_variation: 3
      directional:
        parent_block: custom_log
```

<Callout type="info">
模型会根据放置方向自动旋转。在子方块上使用 `excludeFromInventory: true`，这样只有父方块会出现在 Oraxen 物品栏中。
</Callout>

---

## 去皮原木机制

*需要 Oraxen 1.134.0+*

允许自定义原木像原版原木一样被斧头去皮。

```yaml
Mechanics:
  noteblock:
    custom_variation: 2
    logStrip:
      stripped_log: stripped_custom_log  # 要转换成的方块
      drop: bark  # 可选的额外掉落物
```
