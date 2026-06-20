---
description: 如何创建植物和装饰性方块
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966830020419014666/unknown.png
coverY: 0
---

import { Callout } from 'nextra/components'

# 绊线 (StringBlock)

绊线机制允许你使用 Minecraft 的绊线状态来创建自定义方块。这提供了多达 **127种独特的方块变体**，非常适合植物、花朵和其他装饰元素。

<Callout type="info">
不确定使用哪种方块机制？请参阅[方块概述](/creating-content/blocks)进行对比。
</Callout>

<Callout type="warning">
**推荐 Paper 服务器使用**

为了获得最佳性能，请在 `config/paper-global.yml` 中启用此设置：
```yaml
block-updates:
  disable-tripwire-updates: true
```
</Callout>

## 工作原理

绊线方块使用基于绊线的碰撞箱，允许你制作玩家可以穿过的小型装饰物。对于简单的装饰物，它们比家具更优化。

**主要特性：**
- 玩家可以穿过绊线方块
- 可含水（可以放置在水下）
- 变体 65-127 的碰撞箱比 1-64 更小

### 全局配置

```yaml
stringblock:
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
  enabled: true
```

## 创建装饰物

### 基本配置

```yaml
jasmine_flower:
  displayname: "<white>Jasmine Flower"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "block/cross"
    textures:
      - custom/flowers/jasmine_flower.png
  Mechanics:
    stringblock:
      custom_variation: 2
      model: jasmine_flower
      hardness: 2
      drop:
        silktouch: false
        loots:
          - { oraxen_item: jasmine_flower, probability: 1.0 }
```

## 方块功能

### 高株植物

创建像原版高草丛或向日葵那样的两格高植物：
```yaml
Mechanics:
  stringblock:
    custom_variation: 5
    is_tall: true  # 创建一个2格高的植物
```

### 随机放置

放置时从方块列表中随机选择（非常适合多样化的花丛）：
```yaml
Mechanics:
  stringblock:
    custom_variation: 10
    random_place:
      blocks:
        - red_flower
        - blue_flower
        - yellow_flower
```

### 发光

```yaml
Mechanics:
  stringblock:
    custom_variation: 6
    light: 10  # 0-15
```

### 防爆

```yaml
Mechanics:
  stringblock:
    blast_resistant: true
```

### 不可推动

防止活塞推动：
```yaml
Mechanics:
  stringblock:
    immovable: true
```

### BlockLocker 保护

```yaml
Mechanics:
  stringblock:
    blocklocker:
      can_protect: true
      protection_type: CONTAINER  # CONTAINER、DOOR 或 ATTACHABLE
```

### 下落方块

创建像沙子或沙砾一样下落的方块：
```yaml
Mechanics:
  stringblock:
    custom_variation: 8
    is_falling: true
```

### 存储

将你的方块变成容器：
```yaml
Mechanics:
  stringblock:
    custom_variation: 9
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

### 点击动作

点击时执行命令或播放音效。详情参见[点击动作机制](/creating-content/items/abilities/clickaction)。
```yaml
Mechanics:
  stringblock:
    custom_variation: 10
    clickActions:
      - conditions:
          - "has_permission{perm=my.permission}"
        actions:
          - "[console] say %player% clicked the block!"
```

## 可堆叠方块

*需要 Oraxen 1.212.0+*

创建右键点击可堆叠的方块，类似于原版的粉红色花瓣或蜡烛。每个堆叠级别使用不同的 `custom_variation` 和模型，破坏堆叠方块时会掉落与堆叠级别成比例数量的物品。

### 配置

在你的绊线方块机制下定义一个 `stackable` 列表。父方块始终是基础（第0阶段）。`stackable` 中的每个条目定义下一个堆叠级别：

```yaml
pink_petals:
  displayname: "<light_purple>Pink Petals"
  material: PAPER
  Pack:
    generate_model: false
    model: default/pink_petals_1
  Mechanics:
    stringblock:
      custom_variation: 40
      model: default/pink_petals_1
      hardness: 1
      drop:
        silktouch: false
        loots:
          - { oraxen_item: pink_petals, probability: 1.0 }
      stackable:
        - custom_variation: 41
          model: default/pink_petals_2
        - custom_variation: 42
          model: default/pink_petals_3
        - custom_variation: 43
          model: default/pink_petals_4
```

### 工作原理

- 父方块（`custom_variation: 40`）首先被放置
- 使用相同物品右键点击会推进到下一个堆叠级别（`41`、`42`、`43`）
- 达到最大堆叠级别后，不再继续堆叠
- 破坏方块时掉落与堆叠级别相等数量的物品（例如，在级别3破坏会掉落3个物品）
- 每个堆叠变体必须使用唯一的 `custom_variation` 值

<Callout type="info">
堆叠列表中的每个 `custom_variation` 都会消耗127个可用绊线变体中的一个。请相应规划你的变体ID。
</Callout>

## 自定义模型

使用你自己的3D模型：

```yaml
oak_log_mini:
  displayname: "<white>oak_log_mini"
  material: PAPER
  Pack:
    generate_model: false
    model: custom/furniture/oak_log_mini
  Mechanics:
    stringblock:
      custom_variation: 3
      model: custom/furniture/oak_log_mini
      hardness: 2
      drop:
        silktouch: false
        loots:
          - { oraxen_item: oak_log_mini, probability: 1.0 }
```

![](https://cdn.discordapp.com/attachments/958524021035647046/961424759718047784/unknown.png)

---

## 树苗机制

*需要 Oraxen 1.136.0+*

创建可以生长为结构（树木、植物等）的自定义树苗。

### 全局配置

```yaml
stringblock:
  sapling_growth_check_delay: 4000  # 生长检查间隔（刻）
  enabled: true
```

### 树苗配置

```yaml
custom_sapling:
  Mechanics:
    stringblock:
      custom_variation: 20
      sapling:
        canGrowNaturally: true       # 随时间生长
        naturalGrowthTime: 6000      # 自然生长所需刻数
        canGrowFromBoneMeal: true    # 可用骨粉催熟
        boneMealGrowChance: 50       # 每次使用骨粉的生长几率百分比
        growSound: block.grass.break
        minLightLevel: 4             # 生长所需最低光照等级
        requiresWaterSource: false   # 是否需要附近有水源
        replaceBlocks: false         # 粘贴 schematic 时是否替换现有方块
        schematicName: custom_tree   # 要生成的结构
```

| 设置 | 默认值 | 描述 |
|---------|---------|-------------|
| `canGrowNaturally` | `true` | 树苗是否随时间生长 |
| `naturalGrowthTime` | `6000` | 自然生长所需刻数 |
| `canGrowFromBoneMeal` | `true` | 骨粉是否可以触发生长 |
| `boneMealGrowChance` | `50` | 每次使用骨粉的生长几率百分比 |
| `growSound` | — | 生长时播放的音效 |
| `minLightLevel` | `4` | 生长所需最低光照等级 |
| `requiresWaterSource` | `false` | 生长是否需要在附近有水源 |
| `replaceBlocks` | `false` | 当设为 `true` 时，生长时会替换 schematic 覆盖范围内现有的方块。当设为 `false` 时，如果覆盖范围内存在不可替换的方块，则生长被阻止。 |
| `schematicName` | — | 树苗生长时要粘贴的 schematic 文件名 |

<Callout type="info">
`schematicName` 指向一个 schematic 文件，当树苗生长时该文件将被放置。这允许你创建自定义树木或任何结构。需要安装 WorldEdit。
</Callout>

<Callout type="warning">
在 1.212.1 之前的版本中，配置键为 `shouldReplaceBlocks` — 这仍然有效，但推荐使用 `replaceBlocks`。此外，在 1.212.1 之前，`requiresWaterSource` 的水源检查在 `SaplingListener` 中是反转的 — 如果树苗在水边没有正确生长，请更新到最新版本。
</Callout>
