---
description: 如何向游戏中添加你自己的方块
cover: >-
  https://cdn.discordapp.com/attachments/896841661580185620/969663283445510214/Screenshot_20220429_131532.jpg
coverY: 0
---

# 农场方块机制 (FarmBlock)

如果你希望在服务器中添加可自定义的农耕机制，我们强烈推荐考虑使用 [CustomCrops](https://polymart.org/resource/customcrops.2625)。
它是一个制作精良的插件，与 Oraxen 完全兼容。


## 工作原理

这是一个用于自定义植物和作物的方块系统，你可以拥有自己的浇水系统来使植物生长。

## 全局配置

必须使用全局配置来激活或停用此机制。

```yaml
noteblock:
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
  farmblock_check_delay: 1000 # 每次检查干旱的间隔（刻）
  enabled: true

harvesting:
  enabled: true

watering:
  enabled: true
```

## 如何创建一个简单的农场方块？

### Oraxen 物品和资源包配置

在这种情况下，你无法在没有预制模型的情况下使用此机制创建方块，并且你需要为每个物品创建2个模型，一个带水，一个不带水。

```yaml
epic_box_dry:
  displayname: "<white>Epic Box"
  material: PAPER
  Pack:
    generate_model: false
    model: epic_box_dry
  Mechanics:
    noteblock:
      custom_variation: 49
      model: epic_box_dry
      hardness: 5
      farmblock:
        moistFarmBlockPath: epic_box_wet
        farmBlockDryOutTime: 30000 # 以毫秒为单位 (30000ms = 30s)

epic_box_wet:
  displayname: "<white>Epic Box Wet"
  excludeFromInventory: true # 使物品栏只包含基础方块
  material: PAPER
  Pack:
    generate_model: false
    model: epic_box_wet
  Mechanics:
    noteblock:
      custom_variation: 48
      hardness: 5
      model: epic_box_wet
      farmblock:
        farmBlockPath: epic_box_dry
        farmBlockDryOutTime: 30000 # 以毫秒为单位 (30000ms = 30s)
```

在这个例子中，有2个方块分别配置：
epic_box_dry 是干旱的农场方块，
epic_box_wet 是带水的模型。

farmBlockPath 是没有水时要转换成的 Oraxen 物品。
moistFarmBlockPath 是有水时要变成的 Oraxen 物品。
farmBlockDryOutTime 是水分耗尽的时间。


### 如何给方块浇水？

Oraxen 有一个洒水壶系统，允许使用自定义物品给农场方块浇水，这同样需要2个模型，一个带水，一个不带水，这是一个例子。

```yaml
epic_watering_vacuum:
  displayname: '<white>Epic Watering Vacuum'
  material: LEATHER_HORSE_ARMOR
  Mechanics:
    watering:
      filledCanItem: epic_watering_full #水壶装满时要替换成的物品
  Pack:
    generate_model: false
    model: items/epic_watering_vacuum

epic_watering_full:
  displayname: '<white>Epic Watering Full'
  material: LEATHER_HORSE_ARMOR
  Mechanics:
    watering:
      emptyCanItem: epic_watering_vacuum #水壶清空时要替换成的物品
  Pack:
    generate_model: false
    model: custom/plants/epic_watering_full
```



### 想了解如何制作自定义植物？[点击这里](/creating-content/furniture/farming)
