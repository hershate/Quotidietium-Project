---
description: 学习如何使用 Oraxen 创建自定义物品、方块、家具、盔甲和 UI 元素
---

# 创建内容

Oraxen 允许你为你的 Minecraft 服务器创建多种多样的自定义内容。本章节涵盖了创建所需的一切知识：

## 内容类型

| 类型 | 描述 | 入门指引 |
|------|-------------|-------------|
| [物品](/creating-content/items) | 自定义武器、工具、食物等 | 从基础自定义内容开始 |
| [方块](/creating-content/blocks) | 自定义矿石、装饰性方块、植物 | 在 NoteBlock、StringBlock 或 ChorusBlock 之间选择 |
| [家具](/creating-content/furniture) | 椅子、桌子、机器等 3D 模型 | 用于复杂的可交互物体 |
| [盔甲](/creating-content/armors) | 具有独特纹理的自定义盔甲套装 | 针对不同 MC 版本的多种方法 |
| [字形与 HUD](/creating-content/glyphs-hud) | 自定义表情符号、GUI 纹理、HUD 元素 | 用于 UI 自定义 |

## 快速开始

刚接触 Oraxen？遵循以下推荐学习路径：

1. **[理解基础知识](/plugin-setup/understanding-the-basics)** - 了解 Oraxen 的工作原理
2. **[创建你的第一个物品](/creating-content/items)** - 制作一个简单的自定义物品
3. **[物品外观](/creating-content/items/appearance)** - 添加纹理和模型
4. **[添加能力](/creating-content/items/abilities)** - 赋予你的物品特殊能力

## 内容创作的工作原理

Oraxen 中所有自定义内容都遵循类似的模式：

```yaml
my_custom_item:
  displayname: "<gradient:#4B36B1:#6699FF>My Item"
  material: DIAMOND_SWORD
  Pack:
    generate_model: true
    parent_model: "item/handheld"
    textures:
      - my_texture.png
  Mechanics:
    # 在此添加特殊能力
```

1. **定义物品** - 设置显示名称、基础材质
2. **配置外观** - 纹理、模型、颜色
3. **添加机制** - 特殊能力和行为
4. **游戏内测试** - 使用 `/oraxen reload` 和 `/oraxen give`