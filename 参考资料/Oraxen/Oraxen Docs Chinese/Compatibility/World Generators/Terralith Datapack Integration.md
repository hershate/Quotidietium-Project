---
description: 了解如何将 Oraxen 自定义方块与 Terralith 数据包集成以进行世界生成
---

import { Callout } from 'nextra/components'

# Terralith 数据包集成

Terralith 是一个流行的数据包，它通过新的生物群系和地形特性彻底改造了世界生成。你可以通过修改数据包文件来将你的 Oraxen 自定义方块集成到 Terralith 的世界生成中，从而包含你的自定义矿物和方块。

<Callout type="warning">
  此方法需要手动修改数据包，并且应在世界生成之前完成。在进行更改之前，请确保备份你的数据包文件。
</Callout>

**下载 Terralith -** [Terralith on PlanetMinecraft](https://www.planetminecraft.com/data-pack/terralith-overworld-evolved-100-biomes-caves-and-more/)

## 前提条件

- 已下载并解压 Terralith 数据包
- 已配置 Oraxen 自定义方块（特别是矿物）
- 基本了解 JSON 文件编辑
- 文本编辑器（推荐使用 VS Code 进行批量编辑）

## 步骤 1 - 获取你的方块信息

首先，你需要使用 `/oraxen blockinfo` 命令获取自定义 Oraxen 方块的音符盒数据。

```
/oraxen blockinfo [your_block_id]
```

例如，如果你有一个名为 `deepslate_valorite_ore` 的自定义矿物：

```
/oraxen blockinfo deepslate_valorite_ore
```

这将返回如下信息：
- **Note** 6
- **Instrument** bassdrum

<Callout type="info">
  记下这些值，配置文件中会需要用到它们。
</Callout>

## 步骤 2 - 创建 Configured Feature

导航到 `Terralith.zip\data\terralith\worldgen\configured_feature` 并为你的矿物创建一个新的 JSON 文件（例如 `valorite_ore.json`）。

```json
{
  "type": "minecraft:ore",
  "config": {
    "discard_chance_on_air_exposure": 0.0,
    "size": 8,
    "targets": [
      {
        "state": {
          "Name": "minecraft:note_block",
          "Properties": {
            "instrument": "basedrum",
            "note": "6",
            "powered": "false"
          }
        },
        "target": {
          "predicate_type": "minecraft:tag_match",
          "tag": "minecraft:deepslate_ore_replaceables"
        }
      }
    ]
  }
}
```

**配置选项**
- `size` - 控制矿脉的大小（8 是中等大小）
- `instrument` 和 `note` - 使用 `/oraxen blockinfo` 命令获取的值
- `tag` - 选择适当的替换目标（`minecraft:stone_ore_replaceables` 用于石头，`minecraft:deepslate_ore_replaceables` 用于深板岩）

## 步骤 3 - 创建 Placed Feature

导航到 `Terralith.zip\data\terralith\worldgen\placed_feature` 并创建另一个同名的 JSON 文件（例如 `valorite_ore.json`）。

```json
{
  "feature": "terralith:valorite_ore",
  "placement": [
    {
      "type": "minecraft:count",
      "count": 4
    },
    {
      "type": "minecraft:in_square"
    },
    {
      "type": "minecraft:height_range",
      "height": {
        "type": "minecraft:uniform",
        "min_inclusive": { "absolute": -64 },
        "max_inclusive": { "absolute": -5 }
      }
    },
    {
      "type": "minecraft:biome"
    }
  ]
}
```

**配置选项**
- `feature` - 必须与你的 configured feature 名称匹配（`terralith:your_ore_name`）
- `count` - 每个区块的矿脉数量（4 是中等数量）
- `min_inclusive`/`max_inclusive` - 矿物生成的 Y 轴范围（-64 到 -5 用于深层地下）

## 步骤 4 - 添加到生物群系文件

导航到 `Terralith.zip\data\terralith\worldgen\biome` 并选择你希望矿物生成的生物群系文件。

<Callout type="info">
  **专业提示 -** 使用 VS Code 的"在文件中查找和替换"功能，可以一次性将你的矿物添加到多个生物群系。当需要向许多生物群系添加矿物时，这可以节省大量时间。
</Callout>

在每个生物群系文件中，找到 `features` 部分并定位到**第七个数组**（索引 6）。添加你的矿物引用：

```json
{
  "features": [
    [...],
    [...],
    [...],
    [...],
    [...],
    [...],
    [
      "existing_features...",
      "terralith:valorite_ore"
    ]
  ]
}
```

## 步骤 5 - 打包并部署

1. **归档数据包** - 将修改后的 Terralith 文件夹重新压缩为 ZIP 文件
2. **部署到服务器** - 将数据包放入你的 `world/datapacks` 文件夹中
3. **生成新世界** - 数据包必须在世界生成**之前**存在

<Callout type="warning">
  数据包仅影响新生成的区块。现有的世界区块将不会包含你的自定义矿物。
</Callout>

## 高级用法

### 添加非矿物方块

此方法不仅限于矿物。你可以通过以下方式将任何 Oraxen 自定义方块添加到世界生成中：

1. 使用适当的 feature 类型（例如，`minecraft:simple_block` 用于单个方块）
2. 根据你的具体用例调整放置规则
3. 修改相应的生物群系 features 数组

### 多方块变体

对于具有多个变体的方块，为每个变体创建单独的 configured feature 和 placed feature，确保每个都具有唯一的 note/instrument 组合。

## 故障排除

- **矿物不生成** - 验证 note/instrument 值与你的 `/oraxen blockinfo` 输出是否匹配
- **生物群系不对** - 检查你是否将 feature 添加到了正确的数组索引（第 7 个数组）
- **数据包错误** - 使用 JSON 验证器验证你的 JSON 语法

<Callout type="info">
  虽然此过程最初可能看起来很复杂，但它提供了对你的 Oraxen 方块如何与 Terralith 增强的世界生成集成的完全控制。
</Callout>
