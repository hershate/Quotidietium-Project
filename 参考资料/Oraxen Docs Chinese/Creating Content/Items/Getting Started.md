---
description: 如何创建具有独特纹理和能力的自定义物品
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966825011857981471/unknown.png
coverY: 0
---

import { Callout } from 'nextra/components'

# 自定义物品

Oraxen 让你能够创建具有独特纹理、模型和能力的自定义物品。物品是 Oraxen 中所有自定义内容的基础。

## 你可以创建什么

| 物品类型 | 示例 | 关键特性 |
|-----------|----------|--------------|
| 武器 | 剑、斧、弓 | 自定义伤害、能力、耐久度 |
| 工具 | 镐、锹、锄 | 采矿能力、自定义效率 |
| 食物 | 自定义消耗品 | 饥饿值、药水效果、自定义食用方式 |
| 材料 | 宝石、锭、组件 | 用于合成配方 |
| 装备 | 护甲部件 | 参见[自定义护甲](/creating-content/armors) |

## 配置概览

| 部分 | 用途 | 文档 |
|---------|---------|---------------|
| `displayname` | 带颜色的物品名称 | 使用 MiniMessage 格式 |
| `material` | 基础 Minecraft 物品 | 任何有效的材质 |
| `Pack` | 纹理和模型 | [物品外观](/creating-content/items/appearance) |
| `Components` | 原版数据组件 | [组件](/creating-content/items/components) |
| `Mechanics` | 特殊能力 | [能力](/creating-content/items/abilities) |

## 基本物品结构

```yaml
my_item:
  displayname: "<gradient:#4B36B1:#6699FF>My Item"
  material: DIAMOND_SWORD
  Pack:
    generate_model: true
    parent_model: "item/handheld"
    textures:
      - my_item.png
  Mechanics:
    durability:
      value: 2000
```

<Callout type="info">
将你的纹理文件放在 `plugins/Oraxen/pack/textures/` 文件夹中。Oraxen 会自动生成资源包。
</Callout>

## 下一步

- [物品外观](/creating-content/items/appearance) - 纹理、模型和自定义视觉效果
- [组件](/creating-content/items/components) - 附魔、属性、描述
- [能力](/creating-content/items/abilities) - 特殊能力和机制

---

## 教程：创建你的第一个物品

让我们逐步创建一个自定义的 Onyx 斧头。

## 1. 首先创建纹理

在本教程中，我将制作一个简单的 2D 物品，由 Oraxen 生成模型，但如果你愿意，也可以使用像 [cubik.studio](https://cubik.studio/)（付费）或 [blockbench](https://www.blockbench.net)（免费且开源）这样的软件，它们都非常出色。

这是我在 Photoshop 中以 16x16 分辨率（使其看起来仍然像原版 Minecraft）制作的效果：

![photoshop screenshot](/assets/photoshop.png)

然后我将文件保存为 _onyx_axe.png_。

## 2. 基本配置

我无法决定将我的斧头放在哪里（它更像是工具还是武器？），所以我在 items 目录下创建了 **super_cool_items.yml** 文件。以下是我写的内容：

```yaml
onyx_axe:
  displayname: "<#6f737d>Onyx Axe"
  material: DIAMOND_AXE
```

我给我的物品起了个名字，并选择使用钻石斧作为基础物品。在[组件](/creating-content/items/components)部分，你将看到许多其他额外修改的可能性（例如如何使用附魔、物品标志、属性等）。

## 3. 让我们为物品分配纹理

通常你需要手动创建 JSON 文件：一个用于模型，另一个用于指定何时显示它。使用 Oraxen，你只需要为你的物品指定纹理。Oraxen 会自动处理所有资源包生成——完整细节参见[物品外观](/creating-content/items/appearance)。

```yaml
onyx_axe:
  displayname: "<black>Onyx Axe"
  material: DIAMOND_AXE
  Pack:
    generate_model: true
    parent_model: "item/handheld"
    textures:
      - onyx_axe.png
```

如你所见，我将 parent_model 设置为 "item/handheld"，这是工具使用的父模型，而像钻石之类的物品使用的则是 "item/generated"，这决定了物品在手中的显示方式（如果你不这样做，你的武器可能会以奇怪的方式握持）。

我还需要将我的 **onyx_axe.png** 纹理拖入 Oraxen 的 **/pack/textures** 文件夹。有了这个配置，我通常已经可以重启服务器并看到我的物品，但我想给它添加酷炫的能力。


你也可以使用 JSON 模型来创建 3D 物品，有关文档请参见[物品外观](/creating-content/items/appearance)。


## 4. 让我们通过机制改进我们的物品

在每个物品的配置中，你可以添加一个 mechanics 部分并在其中添加许多酷炫的功能。顺便说一下，如果你觉得酷炫的功能不够多（尽管我尽量添加尽可能多的功能），你可以通过其他使用 Oraxen API 的插件来添加（参见[创建你自己的机制](/developers/mechanics)）。我希望我的斧头有巨大的耐久度，并且能够破坏基岩。以下是我写的内容：

```yaml
onyx_axe:
  displayname: "<black>Onyx Axe"
  material: DIAMOND_AXE
  Pack:
    generate_model: true
    parent_model: "item/handheld"
    textures:
      - onyx_axe.png
  Mechanics:
    durability:
      value: 20000
    bedrockbreak:
      delay: 0
      period: 10
      probability: 0.5
```

20,000 的耐久度是荒谬的，相比之下，钻石工具只有 1,561。我将开采基岩时的掉落概率设置为 0.5，因为我希望基岩块仍然难以获得。


对于某些机制，需要使用 ProtocolLib，bedrockbreak 就是这种情况。


## 5. 让我们试试看！

我首先重启服务器，当一切就绪后，我将安装 Oraxen 的 /pack/ 文件夹中生成的 texture pack.zip 资源包。

我通过 /o inv 从物品栏中给自己拿了斧头，这就是我得到的：

![Me and my onyx axe](/assets/2019-11-01_10.02.47.png)

我也能够挖掘基岩：

![Me breaking bedrock with my onyx axe](/assets/2019-11-01_10.03.22.png)


如果你读到了这里，恭喜你已经创建了自己的物品 👍


### 视频教程