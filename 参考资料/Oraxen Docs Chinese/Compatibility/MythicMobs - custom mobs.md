---
description: >-
  MythicMobs 允许你创建具有高级技能和属性的自定义生物和 Boss
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966831974004174858/unknown.png
coverY: 0
---

# MythicMobs

如果插件与 MythicMobs 不兼容，请使用 5.0.2 版本。

此功能由 [yzl210](https://github.com/yzl210) 提供，不要忘记感谢他！

## 如何使用 Oraxen 物品作为掉落物？

### 用法

`oraxen [oraxen 物品名称] [掉落数量（数字或范围）] [掉落概率（0-1）]`

### 示例

`oraxen custom_material 3-4 0.75`
这意味着有 **75%** 的概率掉落 **3 到 4 个 custom_material** 物品。

## 如何为你的生物装备 Oraxen 物品？

### 用法

`oraxen [槽位] [oraxen 物品（装备）名称]`

#### 槽位

* 0, mainhand, weapon
* 1, boots, shoes
* 2, leggings, pants
* 3, chestpiece, chestplate, body
* 4, helmet, helm
* 5, shield

_5 是副手，但你不能使用 **offhand**，因为 MythicMobs 的作者没有添加该别名。_

### 示例

`oraxen mainhand custom_sword`
这意味着你将 **custom_sword** 物品装备在 **主手**。
`oraxen 3 custom_chestplate`
这意味着你将 **custom_chestplate** 物品装备在 **胸甲** 槽位（作为盔甲）。
