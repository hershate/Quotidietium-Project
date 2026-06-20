---
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966831327984893992/unknown.png
coverY: 0
---

import { Callout, Tabs } from 'nextra/components'

# 植物进化 / 农耕机制

Oraxen 有一个用于创建具有多个生长阶段的植物的系统。有两种配置方式：

1. **内联阶段（推荐）** - 在单个物品中定义所有阶段
2. **旧版多物品** - 每个阶段使用单独的物品

<Callout type="info">
**内联阶段**是推荐的方法，因为它：
- 减少物品数量（1 个物品代替 5 个以上）
- 提高性能（模型切换 vs 实体重建）
- 将所有配置集中在一处
</Callout>

## 内联阶段（推荐）

使用 `stages` 数组和 `Pack.models` 在单个物品中定义所有生长阶段：

```yaml
rose_seed:
  displayname: "<gradient:#46EEAA:#2CBFC7>Rose Seed"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - custom/plants/rose_seed
    # 在此定义所有生长阶段模型
    models:
      stage0: custom/plants/rose_stage_0
      stage1: custom/plants/rose_stage_1
      stage2: custom/plants/rose_stage_2
      stage3: custom/plants/rose_stage_3
  Mechanics:
    furniture:
      barrier: false
      farmblock_required: true
      initial_stage: 0  # 放置时从 stage0 开始
      stages:
        - model: stage0  # 引用 Pack.models 中的键名
          evolution:
            delay: 10000
            probability: 0.5
            light_boost: true
            bone_meal:
              chance: 50
          drop:
            silktouch: true
            loots:
              - { oraxen_item: rose_seed, probability: 1.0 }

        - model: stage1
          evolution:
            delay: 10000
            probability: 0.5
            light_boost: true
            bone_meal:
              chance: 50
          drop:
            silktouch: true
            loots:
              - { oraxen_item: rose_seed, probability: 1.0 }

        - model: stage2
          evolution:
            delay: 10000
            probability: 0.5
            light_boost: true
            bone_meal:
              chance: 50
          drop:
            silktouch: true
            loots:
              - { oraxen_item: rose_seed, probability: 1.0 }

        - model: stage3  # 最终阶段 - 无 evolution 部分
          drop:
            silktouch: true
            loots:
              - { oraxen_item: rose_seed, max_amount: 2, probability: 0.75 }
              - { oraxen_item: rose_plant, max_amount: 5, probability: 0.55 }
```

### 阶段配置选项

`stages` 数组中的每个阶段可以包含：

| 选项 | 描述 |
|--------|-------------|
| `model` | **必需。** 引用 `Pack.models` 中的键名 |
| `light` | 此阶段的可选光照等级（-1 = 从机制继承） |
| `evolution` | 进化设置。最终阶段省略此项 |
| `drop` | 阶段特定的掉落物。如果省略则从机制的 drop 继承 |

### 进化选项

```yaml
evolution:
  delay: 10000              # 进化检查之间的间隔刻数
  probability: 0.5          # 进化几率 (0.0 到 1.0)
  light_boost: true         # 启用光照加速（简写）
  # 或者详细的光照加速：
  light_boost:
    minimum_light_level: 9  # 加速所需的最低光照等级
    boost_tick: 500         # 有光照时每次检查额外增加的刻数
  rain_boost: true          # 启用雨天加速（简写）
  # 或者详细的雨天加速：
  rain_boost:
    boost_tick: 500         # 下雨时每次检查额外增加的刻数
  bone_meal: true           # 启用骨粉（默认 50%）
  # 或者详细的骨粉设置：
  bone_meal:
    chance: 50              # 成功百分比 (0-100)
```

---

## 旧版多物品模式

<Callout type="warning">
此模式仍然可用，但已**弃用**。你会看到控制台警告，建议迁移到内联阶段。
</Callout>

旧版方法需要为每个生长阶段创建单独的物品：

<Tabs items={['种子物品', '阶段 1', '阶段 2', '最终阶段']}>
<Tabs.Tab>
```yaml
rose_seed:
  displayname: "<gradient:#46EEAA:#2CBFC7>Rose Seed"
  material: PAPER
  Mechanics:
    furniture:
      item: rose_plant_stage1
      barrier: false
      farmblock_required: true
      evolution:
        delay: 10000
        probability: 0.5
        light_boost: true
        next_stage: rose_plant_stage1  # 引用另一个物品
      drop:
        silktouch: true
        loots:
          - { oraxen_item: rose_seed, probability: 1.0 }
  Pack:
    generate_model: false
    model: custom/plants/rose_stage_1
```
</Tabs.Tab>
<Tabs.Tab>
```yaml
rose_plant_stage1:
  material: PAPER
  excludeFromInventory: true  # 从库存中隐藏
  Mechanics:
    furniture:
      barrier: false
      farmblock_required: true
      evolution:
        delay: 10000
        probability: 0.5
        light_boost: true
        next_stage: rose_plant_stage2
      drop:
        silktouch: true
        loots:
          - { oraxen_item: rose_seed, probability: 1.0 }
  Pack:
    generate_model: false
    model: custom/plants/rose_stage_1
```
</Tabs.Tab>
<Tabs.Tab>
```yaml
rose_plant_stage2:
  material: PAPER
  excludeFromInventory: true
  Mechanics:
    furniture:
      barrier: false
      farmblock_required: true
      evolution:
        delay: 10000
        probability: 0.5
        light_boost: true
        next_stage: rose_plant_stage3
      drop:
        silktouch: true
        loots:
          - { oraxen_item: rose_seed, probability: 1.0 }
  Pack:
    generate_model: false
    model: custom/plants/rose_stage_2
```
</Tabs.Tab>
<Tabs.Tab>
```yaml
rose_plant_stage3:
  material: PAPER
  excludeFromInventory: true
  Mechanics:
    furniture:
      barrier: false
      farmblock_required: true
      evolution:
        delay: 100000
        probability: 0.25
        light_boost: true
        # 没有 next_stage = 最终阶段
      drop:
        silktouch: true
        loots:
          - { oraxen_item: rose_seed, max_amount: 2, probability: 0.75 }
          - { oraxen_item: rose_plant, max_amount: 5, probability: 0.55 }
  Pack:
    generate_model: false
    model: custom/plants/rose_stage_3
```
</Tabs.Tab>
</Tabs>

---

## 配置参考

### 放置要求

| 选项 | 描述 |
|--------|-------------|
| `farmland_required` | 需要下方有原版耕地方块 |
| `farmblock_required` | 需要下方有自定义 Oraxen 耕地方块。参见 [farmblock 机制](/creating-content/blocks/noteblock#farmblock) |

### 进化选项（旧版）

| 选项 | 描述 |
|--------|-------------|
| `delay` | 进化检查前的时间（以刻计） |
| `probability` | 达到延迟后进化的几率 (0.0-1.0) |
| `light_boost` | 光照等级足够时生长更快 |
| `rain_boost` | 下雨时生长更快 |
| `bone_meal` | 允许骨粉推进生长 |
| `next_stage` | 要进化成的 Oraxen 物品 ID（仅旧版） |

---

## 迁移指南

从旧版多物品迁移到内联阶段：

1. **将模型移动到 `Pack.models`**：
   ```yaml
   Pack:
     models:
       stage0: path/to/stage0
       stage1: path/to/stage1
       # ...
   ```

2. **添加 `stages` 数组**，包含每个阶段的配置

3. **删除旧的阶段物品**（`*_stage1`、`*_stage2` 等）

4. **移除 `next_stage`** - 阶段按数组索引自动推进

参见[完整迁移指南](https://github.com/oraxen/oraxen/blob/master/MIGRATION_PACK_MODELS.md)了解更多详细示例。