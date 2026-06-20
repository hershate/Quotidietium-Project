---
description: 如何使用 Oraxen 创建自定义配方
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966826759293136996/unknown.png
coverY: 0
---

# 配方

配方是 Minecraft 中已有的方式，允许玩家从其他物品创建物品。工作台允许您合成剑、盔甲等，这些物品的合成称为 ShapedRecipe（有序配方），因为它们是有特定形状的配方。还有 ShapelessRecipe（无序配方，您只需以任意顺序放入原料即可获得结果）和 FurnaceRecipe（熔炉配方，通过在熔炉中烧炼原料来获得物品）。Oraxen 的目标是支持所有这些类型，但目前仅支持有序配方。

## 如何创建配方？

您可以在[维基页面](commands#create-recipes)中查看所需的命令和权限列表。

### 第一步：打开配方构建器界面

首先输入 **/o recipe builder SHAPED**，它将为您打开一个工作台：

然后将原料按照您想要的顺序放置在左侧部分。将想要的结果放置在右侧的槽位中。

### 糟糕，我缺少原料，可以关闭界面吗？

完全可以，您可以随时关闭界面，重新打开只需输入 **/o recipes open**（您会发现在其中留下的物品还在）。

### 我完成了我的合成配方，如何加载它？

您必须注册您的合成配方。为此，您需要选择一个名称，然后输入命令 **/o recipes save your_name**。不幸的是，Oraxen 目前还不能在游戏中加载这些合成配方，需要等待服务器重启后才能使用它们。


您也可以使用 **/o recipes save \<name> \<permission>**，这样合成名为 \<name> 的物品就需要权限 \<permission>。


## 如何编辑我的配方？

您可以简单地编辑以您的合成类型命名的配置文件（例如 shaped.yml），然后找到您的合成配方并更改原料、结果或权限。

## 如何禁用原版或已有的配方？

您可以通过将配方的命名空间键添加到 recipes 文件夹中的 `disabled.yml` 文件来禁用任何原版 Minecraft 配方或已有配方。此文件在 Oraxen 首次加载时自动创建。

只需添加您想要禁用的配方键：

```yaml
disabled:
  - minecraft:diamond_sword # 与 /recipes 命令中所显示的相同的命名空间键
  - minecraft:iron_pickaxe
  - oraxen:custom_recipe
```

服务器需要重启才能使更改生效。无效的配方键或不存在的配方将在控制台中显示警告。