---
description: 用于工具的农业和采矿机制
---

# 农业机制

### 收割（Harvesting）

收割允许你在一定半径内自动收获和重新种植小麦。

#### 每个物品的配置

```yaml
Mechanics:
  harvesting:
    cooldown: 10000 # 每次使用间隔 10 秒
    radius: 5 # 点击方块周围的方块范围
    height: 3 # 点击方块上方的方块范围
    lower_item_durability: true # 收割是否降低工具耐久度（默认：true）
```

### 范围挖掘（BigMining）

范围挖掘允许你同时挖掘多个不同的方块。默认情况下，此机制用于锤子，允许你挖掘 3x3 及更大的方形区域。

#### 每个物品的配置

```yaml
Mechanics:
  bigmining:
    radius: 1 # 破坏方块周围的方块范围
    depth: 1
```

### 熔炼（Smelting）

熔炼允许你在挖掘铁和金矿石时即时熔炼它们。这支持时运和精准采集。

#### 每个物品的配置

```yaml
Mechanics:
  smelting:
    enabled: true
    play_sound: true
```

### 瓶装经验（BottledExp）

这允许你通过右键将经验转化为经验瓶。你可以配置损失百分比。

#### 每个物品的配置

ratio 对应的是将 1 点经验转化为一个瓶子的经验量。

```yaml
Mechanics:
  bottledexp:
    ratio: 0.95 # 因此转换时会损失 1/20 的经验
```

#### 全局配置

```yaml
bottledexp:
  enabled: true
  durability_cost: 1
```

### 基岩破坏（BedrockBreak）


此机制依赖于 ProtocolLib，如果你无法使用 ProtocolLib，则需要禁用它


#### 每个物品的配置

hardness 是破坏动画切换之间的刻数，probability 是获得基岩的概率百分比（0.10 表示 10%，0.5 表示 50%，1.0 表示 100%）。

```yaml
Mechanics:
  bedrockbreak:
    hardness: 10
    probability: 1
```

#### 全局配置

如果你将 disable_on_first_layer 设置为 true，你的玩家将不再能够破坏地面（第 0 层），durability_cost 是你设置 bedrockbreak 的物品每次消耗的耐久度。

```yaml
bedrockbreak:
  enabled: true
  disable_on_first_layer: false
  durability_cost: 500
```

### 浇水（Watering）

为你的农场创建一个洒水壶系统。此机制需要两个物品：一个空壶和一个装满水的壶。空壶在右键水或含水炼药锅时装水。装满水的壶可以浇灌农田（原版或 Oraxen 农场方块）。

#### 每个物品的配置

你需要定义两个物品并将它们链接在一起：

```yaml
empty_watering_can:
  displayname: "<gray>Empty Watering Can"
  material: PAPER
  Mechanics:
    watering:
      filledCanItem: filled_watering_can

filled_watering_can:
  displayname: "<aqua>Filled Watering Can"
  material: PAPER
  Mechanics:
    watering:
      emptyCanItem: empty_watering_can
```

空壶在装水时变为装满水的壶，反之亦然，浇灌农田时亦然。