---
description: 关于 Oraxen 如何工作的简单说明
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966825489098489856/unknown.png
coverY: 0
---

# 理解基础知识

如前所述，Oraxen 能够生成自定义物品，包括配套的纹理包。
它还使这些物品能够与被称为"机制"的特殊能力或功能关联起来。

## 颜色和其他 Minecraft 格式化

Minecraft 过去仅支持 16 种颜色，大多数插件使用带有 & 字符的特殊格式。然而，1.16 版本为文本添加了十六进制颜色，鉴于格式化可能性之多（例如可点击消息），由于 PaperMC 支持 [MiniMessage 格式](https://docs.adventure.kyori.net/minimessage.html#format)，您能够对物品使用十六进制颜色以及其他一些额外的技巧。如果您想尝试 MiniMessage 格式化，[请点此](https://webui.advntr.dev/)！

示例：
* 十六进制颜色 - `<#FF5555>我从红色开始 <#55FF55>现在我是绿色了！`
* 简单颜色 - `<green>我是绿色 <gold>现在我是金色</gold> 我又变回绿色了！`
* 自动渐变 - `<gradient:red:green:blue>此示例自动对渐变开始和结束之间的任何内容应用渐变</gradient>`

![image](/assets/minimessage_example.png)

## Oraxen 文件夹的内容

<PluginFileTree initialTreeData={[
  {
    id: "oraxen",
    name: "Oraxen",
    hoverText: "主插件文件夹，包含所有 Oraxen 配置和资源。",
    children: [
      {
        id: "settings",
        name: "settings.yml",
        isLeaf: true,
        hoverText: "Oraxen 的各种设置，包括资源包生成、分发操作和插件行为。"
      },
      {
        id: "mechanics",
        name: "mechanics.yml",
        isLeaf: true,
        hoverText: "应用于使用该机制的所有物品的全局机制设置。"
      },
      {
        id: "items",
        name: "items",
        hoverText: "包含所有物品配置。您可以将物品整理到子文件夹中，或保留在单个文件中。",
        children: [
          { id: "example_item", name: "example.yml", isLeaf: true, hoverText: "示例物品配置文件。根据需要创建任意数量！" }
        ]
      },
      {
        id: "glyphs",
        name: "glyphs",
        hoverText: "用于表情符号、HUD 和自定义 GUI 元素的自定义字体/字形配置。",
        children: [
          { id: "example_glyph", name: "example.yml", isLeaf: true }
        ]
      },
      {
        id: "pack",
        name: "pack",
        hoverText: "资源包文件夹。Oraxen 会生成大部分文件，但您需要在此处添加纹理和模型。",
        children: [
          {
            id: "textures",
            name: "textures",
            hoverText: "在此处添加您的自定义纹理（PNG 文件）。",
            children: [
              { id: "example_texture", name: "my_item.png", isLeaf: true }
            ]
          },
          {
            id: "models",
            name: "models",
            hoverText: "在此处添加自定义3D模型（JSON 文件）用于具有自定义几何体的物品。",
            children: [
              { id: "example_model", name: "my_model.json", isLeaf: true }
            ]
          },
          {
            id: "assets",
            name: "assets",
            hoverText: "通过在此处放置您自己的版本来覆盖 Oraxen 生成的文件（例如 assets/minecraft/sounds.json）。",
            children: [
              {
                id: "minecraft",
                name: "minecraft",
                children: [
                  { id: "sounds_override", name: "sounds.json", isLeaf: true, hoverText: "覆盖生成的 sounds.json 文件。" }
                ]
              }
            ]
          }
        ]
      },
      {
        id: "recipes",
        name: "recipes",
        hoverText: "按类型排序的配方配置。通过游戏内的 /oraxen recipes 命令管理更方便。",
        children: [
          { id: "shaped", name: "shaped.yml", isLeaf: true, hoverText: "有序合成配方（如镐的图案）。" },
          { id: "shapeless", name: "shapeless.yml", isLeaf: true, hoverText: "无序配方（材料可以任意放置）。" },
          { id: "furnace", name: "furnace.yml", isLeaf: true, hoverText: "熔炉烧炼配方。" },
          { id: "campfire", name: "campfire.yml", isLeaf: true, hoverText: "营火烹饪配方。" }
        ]
      }
    ]
  }
]} />

### 全局配置

在此配置文件夹的根目录下，您会找到两个文件：
`settings.yml` 包含 Oraxen 的各种设置，`mechanics.yml` 包含全局机制设置。

### 物品配置

子文件夹 `Oraxen/items` 包含所有已创建/已购买的物品配置。您可以为您想要的任何物品创建新文件，或删除现有的文件。虽然所有内容都可以放在一个文件中，但将它们存储在具有明确名称的文件夹中有助于保持井井有条。

### 资源包

资源包是 Oraxen 的关键元素，即使它能够生成您需要的大部分文件，您仍然需要自己提供自定义物品的纹理，所有这些都在 `Oraxen/pack` 文件夹中管理。

您可以使用 `Oraxen/pack/textures` 子文件夹添加纹理，使用 `Oraxen/pack/models` 子文件夹添加模型（例如，如果您想使用 3D 物品）。
您也可以从 `Oraxen/pack` 文件夹本身更改资源包的基本文件（pack.mcmeta、资源包图标等）。

如果您需要覆盖 Oraxen 的特定文件，您可以创建 `Oraxen/pack/assets` 文件夹，并插入例如 `assets/minecraft/sounds.json` 以覆盖该文件（如果由 Oraxen 生成）。

### 配方

此文件夹包含您添加的不同配方配置，按配方类型排序。
例如，`Oraxen/recipes/shaped.yml` 将包含所有有序配方，而 `Oraxen/recipes/campfire.yml` 将包含任何营火配方。

*此文件夹很少被直接操作，因为通过游戏内的 [oraxen recipe 命令](/usage/commands#manage-recipes)直接生成配方配置更简单/更快。*