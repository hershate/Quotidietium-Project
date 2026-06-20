---
description: 如何创建自定义楼梯、台阶、门、活板门、格栅和灯泡
---

import { Callout } from 'nextra/components'

# 形状方块 (ShapedBlock)

形状方块机制允许你使用涂蜡铜方块作为基础材质来创建自定义的**楼梯、台阶、门、活板门、格栅和灯泡**。每种方块类型最多支持**4种自定义变体**。

![游戏中的自定义楼梯、门、活板门和树叶](/shaped_blocks.webp)

<Callout type="info">
不确定使用哪种方块机制？请参阅[方块概述](/creating-content/blocks)进行对比。
</Callout>

## 工作原理

形状方块使用 Minecraft 的涂蜡铜方块变体（楼梯、台阶、门、活板门、格栅）作为底层材质。Oraxen 会自动：

1. 将原版涂蜡铜方块转换为带有氧化防止标记的未涂蜡等价物
2. 为自定义方块保留涂蜡铜材质
3. 处理原版铜的蜜脾涂蜡和斧头除蜡
4. 转换世界生成中的涂蜡铜（试炼密室等）

<Callout type="warning">
此机制会修改涂蜡铜在你的世界中的行为方式。原版涂蜡铜方块将被转换为普通铜（带有氧化防止标记），以便为自定义方块保留涂蜡变体。
</Callout>

## 方块类型

| 类型 | 基础材质 | 变体数 | 特性 |
|------|---------------|------------|----------|
| `STAIR` | 涂蜡铜楼梯 | 4 | 方向性放置、含水 |
| `SLAB` | 涂蜡铜台阶 | 4 | 上半/下半/双层放置、含水 |
| `DOOR` | 涂蜡铜门 | 4 | 两格高、可开合、红石供能 |
| `TRAPDOOR` | 涂蜡铜活板门 | 4 | 可开合、红石供能、含水 |
| `GRATE` | 涂蜡铜格栅 | 4 | 透明（非常适合树叶）、含水 |
| `BULB` | 涂蜡铜灯泡 | 4 | 可切换光源、红石供能 |

## 全局配置

在 `mechanics.yml` 中，你可以配置形状方块机制：

```yaml
shaped_block:
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
  # 将原版涂蜡铜转换为带有氧化防止标记的未涂蜡版本
  convert_vanilla_waxed: true
  # 处理世界生成中的涂蜡铜（试炼密室等）
  handle_world_generation: true
  enabled: true
```

<Callout type="info">
如果你禁用此机制（`enabled: false`），原版涂蜡铜的行为将被完全恢复。玩家将能够正常使用涂蜡铜方块，不会有任何转换。
</Callout>

## 创建形状方块

### 自定义楼梯

```yaml
custom_oak_stairs:
  displayname: "<#8B4513>Custom Oak Stairs"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: block/stairs
    textures:
      - custom_oak_planks
  Mechanics:
    shaped_block:
      type: STAIR
      custom_variation: 1  # 可用范围 1-4
      hardness: 2
      block_sounds:
        break_sound: block.wood.break
        place_sound: block.wood.place
      drop:
        silktouch: false
        loots:
          - oraxen_item: custom_oak_stairs
            probability: 1.0
```

### 自定义台阶

台阶支持上半、下半和双层放置。双层台阶被破坏时自动掉落2个物品。

```yaml
custom_stone_slab:
  displayname: "<#808080>Custom Stone Slab"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: block/slab
    textures:
      - block/stone
  Mechanics:
    shaped_block:
      type: SLAB
      custom_variation: 1
      hardness: 4
      block_sounds:
        break_sound: block.stone.break
        place_sound: block.stone.place
      drop:
        silktouch: false
        loots:
          - oraxen_item: custom_stone_slab
            probability: 1.0
```

### 自定义门

门需要特殊处理：在 Pack 部分使用 `item/generated` 作为手持显示图标，并在 mechanism 部分指定方块纹理以用于放置后的门外观。

```yaml
custom_oak_door:
  displayname: "<#8B4513>Custom Oak Door"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - custom_oak_door_icon  # 手持/物品栏显示的平面图标
  Mechanics:
    shaped_block:
      type: DOOR
      custom_variation: 1
      hardness: 2
      # 放置后门的方块纹理（下半和上半部分）
      textures:
        bottom: block/oak_door_bottom
        top: block/oak_door_top
      block_sounds:
        break_sound: block.wood.break
        place_sound: block.wood.place
      drop:
        silktouch: false
        loots:
          - oraxen_item: custom_oak_door
            probability: 1.0
```

<Callout type="info">
门是两格高的，会自动处理上半/下半方块的放置。破坏任一半都会掉落门物品。
</Callout>

### 自定义活板门

```yaml
custom_oak_trapdoor:
  displayname: "<#8B4513>Custom Oak Trapdoor"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: block/template_trapdoor_bottom
    textures:
      - block/oak_trapdoor
  Mechanics:
    shaped_block:
      type: TRAPDOOR
      custom_variation: 1
      hardness: 2
      block_sounds:
        break_sound: block.wood.break
        place_sound: block.wood.place
      drop:
        silktouch: false
        loots:
          - oraxen_item: custom_oak_trapdoor
            probability: 1.0
```

### 自定义格栅 / 树叶

格栅是使用裁剪渲染的透明方块，非常适合自定义树叶或其他透视方块。

```yaml
# 使用 GRATE 类型实现透明度的自定义树叶
crystalmush_leaves:
  displayname: "<gradient:#9966FF:#FF66CC>Crystal Mushroom Leaves"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: block/leaves
    textures:
      - default/crystalmush/crystalmush_leaves_anim
  Mechanics:
    shaped_block:
      type: GRATE
      custom_variation: 2
      light: 12  # 发光
      hardness: 0.2
      block_sounds:
        break_sound: block.grass.break
        place_sound: block.grass.place
      drop:
        silktouch: true  # 仅精准采集时掉落
        loots:
          - oraxen_item: crystalmush_leaves
            probability: 1.0
```

<Callout type="info">
使用 `block/leaves` 作为父模型以获得正确的透明度渲染。GRATE 类型使用裁剪规则渲染，允许纹理的透明通道像真实树叶一样透出。
</Callout>

### 自定义灯泡

灯泡是可以被红石供能的可切换光源。

```yaml
custom_light_bulb:
  displayname: "<#FFD700>Custom Light Bulb"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: block/cube_all
    textures:
      - custom_bulb_texture
  Mechanics:
    shaped_block:
      type: BULB
      custom_variation: 1
      hardness: 3
      block_sounds:
        break_sound: block.copper.break
        place_sound: block.copper.place
      drop:
        silktouch: false
        loots:
          - oraxen_item: custom_light_bulb
            probability: 1.0
```

## 配置选项

### 通用属性

| 属性 | 描述 | 默认值 |
|----------|-------------|---------|
| `type` | 方块类型：`STAIR`、`SLAB`、`DOOR`、`TRAPDOOR`、`GRATE`、`BULB` | 必填 |
| `custom_variation` | 变体编号 (1-4) | 必填 |
| `hardness` | 挖掘硬度 | `3` |
| `light` | 发光等级 (0-15) | `0` |

### 方块音效

```yaml
block_sounds:
  break_sound: block.wood.break
  place_sound: block.wood.place
  hit_sound: block.wood.hit
  step_sound: block.wood.step
  fall_sound: block.wood.fall
  volume: 1.0
  pitch: 1.0
```

### 掉落物配置

```yaml
drop:
  silktouch: false        # 需要精准采集才会掉落
  fortune: false          # 启用时运附魔加成
  minimal_type: WOODEN    # 所需的最低工具等级
  best_tools:
    - PICKAXE
  loots:
    - oraxen_item: my_block
      probability: 1.0
```

## 方块行为

### 楼梯
- 根据玩家朝向自动定向
- 支持含水
- 根据点击位置放置在正确的半层（上半/下半）

### 台阶
- 根据点击位置放置为上半、下半或双层台阶
- 双层台阶被破坏时掉落2个物品
- 支持含水

### 门
- 两格高，自动放置上下两半
- 右键点击开合
- 红石供能
- 破坏任一半都会移除整扇门

### 活板门
- 右键点击开合
- 红石供能
- 支持含水
- 根据点击位置放置在方块顶部或底部

### 格栅
- 使用裁剪渲染的透明（透视）效果
- 支持含水
- 光线可以透过
- 非常适合自定义树叶或玻璃类方块

### 灯泡
- 可切换光源
- 红石供能
- 点击切换开/关状态

## 父模型参考

| 方块类型 | 推荐的父模型 |
|------------|-------------------------|
| 楼梯 | `block/stairs` |
| 台阶 | `block/slab` |
| 门 | `item/generated`（用于物品），门纹理在机制中指定 |
| 活板门 | `block/template_trapdoor_bottom` |
| 格栅 | `block/cube_all` 或 `block/leaves`（用于植被） |
| 灯泡 | `block/cube_all` |

## 限制

- 每种方块类型最多**4种自定义变体**（楼梯、台阶等）
- 你的世界中的涂蜡铜方块将被转换为普通铜
- 当此机制启用时，玩家无法将涂蜡铜材质用于原版的用途
