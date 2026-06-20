---
description: 使用基于数据包的隐形盔甲架在玩家身上显示装饰性背包
---

import { Callout } from 'nextra/components'

# 背包装饰

背包装饰机制在玩家将特定物品装备到指定槽位时，在玩家背部显示装饰性背包。它使用基于数据包的隐形盔甲架实现高效的客户端渲染。

![Player with cosmetic backpack](/backpack_cosmetic.webp)

<Callout type="info">
这是一个**纯装饰**机制。对于功能性存储背包，请参见[背包机制](/creating-content/items/abilities)（即将推出）或使用家具上的[存储](/creating-content/furniture#storage)功能。
</Callout>

## 工作原理

当玩家装备带有 `backpack_cosmetic` 机制的物品时：

1. 生成一个隐形盔甲架并将其挂载到玩家身上
2. 背包模型显示为盔甲架的装备
3. 盔甲架跟随玩家的移动和旋转
4. 其他玩家（以及可选地，佩戴者本人）可以看到背包

## 基本配置

```yaml
leather_backpack:
  displayname: "<#8B4513>Leather Backpack"
  material: LEATHER_CHESTPLATE
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - leather_backpack
  Mechanics:
    backpack_cosmetic:
      slot: CHEST
      offset:
        x: 0.0
        y: 0.2
        z: -0.2
      scale: 0.8
      view_distance: 48
```

## 配置选项

| 选项 | 类型 | 默认值 | 描述 |
|--------|------|---------|-------------|
| `slot` | String | 必需 | 触发装饰的槽位：`HEAD`、`CHEST`、`LEGS`、`FEET`、`HAND`、`OFF_HAND` 或 `INVENTORY` |
| `model` | String | 物品模型 | 覆盖盔甲架上显示的模型（可选） |
| `offset` | Object | `{x:0, y:0.3, z:-0.3}` | 相对于玩家的位置偏移 |
| `scale` | Number | `1.0` | 背包模型的大小倍率 |
| `view_distance` | Number | `48` | 背包可见的最大距离（以方块计） |
| `hide_in_spectator` | Boolean | `true` | 玩家处于旁观模式时隐藏背包 |
| `small` | Boolean | `false` | 使用小型盔甲架以获得更低的位置 |
| `visible_to_self` | Boolean | `true` | 佩戴者是否可以看到自己的背包 |

<Callout type="info">
`INVENTORY` 槽位会在物品位于玩家物品栏中任何位置（不包括手中）时触发背包显示。这对于始终可见的装饰品非常有用。
</Callout>

### 偏移配置

偏移量用于定位背包相对于玩家的位置：

```yaml
offset:
  x: 0.5   # 正 = 右，负 = 左
  y: 0.2   # 正 = 上，负 = 下
  z: -0.2  # 正 = 前，负 = 后（朝向玩家背部）
```

<Callout type="info">
使用挂载系统时，偏移值的效果可能有限。`small` 选项通过使用较小的盔甲架提供显著的垂直偏移。
</Callout>

## 示例

### 标准背包

一个居中于玩家背部的背包：

```yaml
adventurer_backpack:
  displayname: "<#2E8B57>Adventurer's Backpack"
  material: LEATHER_CHESTPLATE
  color: 46139  # 深绿色调
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - adventurer_backpack
  Mechanics:
    backpack_cosmetic:
      slot: CHEST
      offset:
        x: 0.0
        y: 0.45
        z: -0.35
      scale: 0.9
      view_distance: 64
      hide_in_spectator: true
      small: true
      visible_to_self: true
```

### 肩部背包

一个偏向一侧的小型背包：

```yaml
explorer_pack:
  displayname: "<#4169E1>Explorer's Pack"
  material: LEATHER_CHESTPLATE
  color: 4286945  # 蓝色调
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - explorer_pack
  Mechanics:
    backpack_cosmetic:
      slot: CHEST
      offset:
        x: 0.5  # 偏移到右侧
        y: 0.35
        z: -0.25
      scale: 0.75
      view_distance: 48
      hide_in_spectator: true
      small: false
      visible_to_self: true
```

### 使用现有模型

如果你有预先制作好的模型，禁用生成并直接引用它：

```yaml
custom_bag:
  displayname: "<#8B4513>Custom Bag"
  material: LEATHER_CHESTPLATE
  Pack:
    generate_model: false
    model: items/bag  # 现有模型的路径
  Mechanics:
    backpack_cosmetic:
      slot: CHEST
      offset:
        x: 0.0
        y: 0.0
        z: 0.0
      scale: 1.0
      view_distance: 48
      hide_in_spectator: true
      small: true
      visible_to_self: true
```

## 全局配置

在 `mechanics.yml` 中全局启用或禁用该机制：

```yaml
backpack_cosmetic:
  enabled: true
```

## 技术细节

### 渲染方法

背包使用基于数据包的盔甲架进行渲染：
- **无服务端实体** - 仅向客户端发送数据包数据
- **高效** - 与真实实体相比，服务器开销最小
- **挂载** - 盔甲架挂载到玩家身上，以实现平滑的位置跟随
- **旋转同步** - 头部和身体旋转都会更新，以实现正确的朝向

### 性能考量

- `view_distance` 选项限制渲染距离以减少数据包开销
- 背包在以下情况下会自动清理：
  - 玩家卸下物品时
  - 玩家断开连接时
  - 服务器关闭或重载时

### 槽位行为

物品位于指定槽位时显示背包：
- `CHEST` - 最常用于背包（胸甲槽位）
- `HEAD` - 可用于头部挂载物品
- `LEGS` - 护腿槽位
- `FEET` - 靴子槽位
- `HAND` - 主手槽位
- `OFF_HAND` - 副手槽位
- `INVENTORY` - 玩家物品栏中任意位置（不包括手中）

## 提示

1. **使用 `small: true`** 将背包定位到玩家背部的较低位置
2. **调整 `scale`** 在 0.5-1.0 之间以获得逼真的大小
3. **设置 `visible_to_self: true`** 让玩家看到自己的装饰品（尤其是在第三人称视角）
4. **使用 `LEATHER_CHESTPLATE`** 作为基础材质，如果你想要可染色的背包（添加 `color` 属性）
5. **在第三人称下测试**（F5），以验证从其他玩家视角看位置是否正确