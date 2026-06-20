---
description: Iris 是一个付费世界生成器，具有一流的 Oraxen 集成
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966832733290627072/unknown.png
coverY: 0
---

import { Callout } from 'nextra/components'

# Iris World Generator

Iris World Generator 允许你轻松生成具有自定义地形、生物群系和结构的美丽世界。它具有**一流的 Oraxen 集成**，允许你直接在世界生成配置中使用 Oraxen 的自定义方块和物品。

<Callout type="info">
  Oraxen 会自动向 Iris 注册为外部数据提供者。只需安装这两个插件，集成即可开箱即用——无需额外设置。
</Callout>

**Spigot 链接：** [Iris World Generator](https://www.spigotmc.org/resources/iris-world-gen-the-dimension-engine.84586/)

## 在 Iris 中使用 Oraxen 方块

你可以使用 `oraxen:` 前缀后跟方块 ID 来引用任何 Oraxen 自定义方块。Iris 将通过 Oraxen 的数据提供者自动解析这些引用。

```
oraxen:your_block_id
```

## 如何创建自定义矿物

在此示例中，我们假设你已经按照[此示例](/creating-content/blocks/noteblock#ores)在你的 Oraxen 配置中添加了一个方块（例如紫水晶矿石）。

### 1) 找到你的维度配置

前往 `Iris/pack/YOUR_PACK_NAME/dimensions/YOUR_DIMENSION_NAME.json`，默认情况下应为：`Iris/packs/overworld/dimensions/overworld.json`

然后，打开该文件（或在 VSCode 工作区中打开以享受酷炫的 VSCode 集成体验）。

### 2) 添加你的矿物！

找到配置中的这一部分：

```yaml
    "ORES": "关于矿藏的所有设置。包含在你的世界中生成的矿物。",
    "deposits": [
        {
            "minHeight": 19,
            "maxPerChunk": 4,
            "maxHeight": 150,
            "minPerChunk": 1,
            "minSize": 25,
            "maxSize": 25,
            "palette": [{"block": "granite"}],
            "varience": 2
        },
```

使用在第一步中找到的自定义矿物属性来添加你自己的配置。例如：

```yaml
    {
      "minHeight": 2,
      "maxPerChunk": 2,
      "maxHeight": 30,
      "minPerChunk": 0,
      "minSize": 3,
      "maxSize": 6,
      "palette": [{ "block": "oraxen:amethyst_ore" }],
      "varience": 5
    },
```

现在你可以保存文件，重置你的世界并重启！
