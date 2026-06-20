---
description: Oraxen 自定义方块机制概述
---

import { Callout } from 'nextra/components'

# 自定义方块机制

Oraxen 提供了多种创建自定义方块的机制，每种机制具有不同的特性。本指南帮助你根据自己的需求选择最合适的方案。

## 快速对比

| 机制 | 最大方块数 | 基础方块 | 最适合 |
|----------|------------|------------|----------|
| [音符盒 (NoteBlock)](/creating-content/blocks/noteblock) | ~800 | 音符盒 | 大多数自定义方块（矿石、石头、木材） |
| [绊线 (StringBlock)](/creating-content/blocks/stringblock) | 127 | 绊线 | 植物、花朵、装饰物 |
| [紫颂 (ChorusBlock)](/creating-content/blocks/chorusblock) | 63 | 紫颂植物 | 透明方块（树叶、玻璃类） |
| [形状 (ShapedBlock)](/creating-content/blocks/shapedblock) | 每种类型 4 个 | 涂蜡铜 | 楼梯、台阶、门、活板门、格栅 |
| [家具 (Furniture)](/creating-content/furniture) | 无限制 | 展示实体 | 复杂模型、可交互对象 |

## 选择合适的机制

### 使用音符盒 (NoteBlock) 适用于：
- **实心方块**，如矿石、石头变体、木板
- 需要**最多的方块槽位**（~800）
- 应具有**标准碰撞箱**的方块

### 使用绊线 (StringBlock) 适用于：
- 玩家可以穿过的**植物和花朵**
- 碰撞箱可通过的**小型装饰物**
- 需要**含水**的方块
- **高株植物**（2格高）

### 使用紫颂 (ChorusBlock) 适用于：
- **透明方块**，如自定义树叶或玻璃变体
- 需要透明度的**单格家具**（比展示实体性能更好）
- **透视渲染**很重要的方块

### 使用形状 (ShapedBlock) 适用于：
- **自定义楼梯、台阶、门、活板门和格栅**
- 需要**正确的方向摆放**的方块（楼梯朝向、台阶上半/下半）
- 具有开合动画的**功能性门和活板门**
- 每种类型限制为**4种变体**（使用涂蜡铜为基础）

### 使用家具 (Furniture) 适用于：
- **复杂的3D模型**（椅子、桌子、机器）
- **可交互对象**（存储、唱片机）
- **无限制的变体数量**（无槽位限制）
- 具有**自定义碰撞箱**或**座椅**的对象

## Paper 服务器配置

<Callout type="warning">
**强烈推荐 Paper 服务器使用**

为了获得最佳性能并防止物理错误，请在 `config/paper-global.yml` 中添加以下设置：

```yaml
block-updates:
  disable-noteblock-updates: true
  disable-tripwire-updates: true
  disable-chorus-plant-updates: true
```

没有这些设置，Oraxen 必须监听昂贵的物理事件，这可能导致卡顿。
</Callout>

## 功能对比

| 功能 | 音符盒 | 绊线 | 紫颂 | 形状 | 家具 |
|---------|-----------|-------------|-------------|-------------|-----------|
| 自定义音效 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 发光 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 掉落物 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 硬度 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 防爆 | ✅ | ✅ | ✅ | ❌ | ❌ |
| 不可推动 | ✅ | ✅ | ✅ | ❌ | ❌ |
| 下落方块 | ✅ | ✅ | ✅ | ❌ | ❌ |
| 含水 | ❌ | ✅ | ❌ | ✅ | ❌ |
| 存储 | ✅ | ✅ | ✅ | ❌ | ✅ |
| 方向性 | ✅ | ❌ | ❌ | ✅ | ✅ |
| 高株植物 | ❌ | ✅ | ❌ | ❌ | ❌ |
| 演化/生长 | ❌ | ✅ | ❌ | ❌ | ✅ |
| 座椅 | ❌ | ❌ | ✅ | ❌ | ✅ |
| 点击动作 | ✅ | ✅ | ✅ | ❌ | ✅ |
| 楼梯/台阶 | ❌ | ❌ | ❌ | ✅ | ❌ |
| 门/活板门 | ❌ | ❌ | ❌ | ✅ | ❌ |

## 旧版：方块机制（蘑菇柄）

<Callout type="info">
原有的使用蘑菇柄的 `block` 机制仍然存在，但**默认禁用**，被视为旧版。新项目请改用音符盒 (NoteBlock)。
</Callout>

如果你有使用蘑菇柄机制的现有配置，它们将继续工作。要启用它，请在 `mechanics.yml` 中设置 `enabled: true`：

```yaml
block:
  enabled: true  # 默认: false
  tool_types:
    - WOODEN
    - STONE
    - IRON
    - GOLDEN
    - DIAMOND
    - NETHERITE
```

配置与音符盒完全相同，只需在物品配置中使用 `block:` 而不是 `noteblock:`。

## 下一步

- [音符盒机制](/creating-content/blocks/noteblock) - 最适合大多数自定义方块
- [绊线机制](/creating-content/blocks/stringblock) - 最适合植物和装饰物
- [紫颂机制](/creating-content/blocks/chorusblock) - 透明方块
- [形状机制](/creating-content/blocks/shapedblock) - 楼梯、台阶、门、活板门、格栅
- [家具机制](/creating-content/furniture) - 复杂3D模型
