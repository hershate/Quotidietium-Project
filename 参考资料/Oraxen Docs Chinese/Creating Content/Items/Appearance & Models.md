---
description: 如何自定义你的物品外观？
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966824489490976798/unknown.png
coverY: 0
---

import { Callout } from 'nextra/components'

# 物品外观

与大多数其他允许创建自定义物品的插件不同，Oraxen 支持创建纹理包：你可以直接在配置中定义你想要的物品外观，它会自动生成资源包。对于 Minecraft 来说，每个物品的外观由一个名为模型的 JSON 文件管理。Oraxen 可以自动生成这些文件。

### Oraxen 如何处理物品模型

Oraxen 在 1.21.4+ 上支持多种物品外观系统。**这些系统可以组合使用**以获得最大的兼容性。1.21.4 之前的服务器始终使用旧的谓词覆盖。

<Callout type="info">
**默认行为：**
- **1.21.4 之前**：旧版谓词（强制使用，无论设置如何）
- **1.21.4+**：物品模型定义（`item_properties: true`）
</Callout>

### 外观系统（1.21.4+）

在 1.21.4+ 上，你可以在 `settings.yml` 中启用多种外观系统：

```yaml
Pack:
  generation:
    appearance:
      item_properties: true        # 使用 item_model 组件（默认）
      model_data_ids: false        # 使用 custom_model_data.strings 配合 select
      model_data_float: false      # 使用 custom_model_data.floats 配合 range_dispatch
      generate_predicates: false   # 生成旧版谓词（1.21.4+ 上不需要）
```

**可用系统：**

| 设置 | 资源包输出 | 物品组件 | 使用场景 |
|---------|-------------|----------------|----------|
| `item_properties` | `assets/oraxen/items/<id>.json` | `item_model` 组件 | **默认。** 使用物品模型定义的干净 1.21.4+ 设置。 |
| `model_data_ids` | `assets/minecraft/items/<material>.json` | `custom_model_data.strings[0]` | 使用 `minecraft:select` 配合字符串键（`oraxen:<item_id>`）。适合基于 CMD 且需要稳定标识符的工作流。 |
| `model_data_float` | `assets/minecraft/items/<material>.json` | `custom_model_data.floats[0]` | 使用 `minecraft:range_dispatch` 配合数字阈值。在物品上设置整数 CMD。 |
| `generate_predicates` | `assets/minecraft/models/item/*.json` | — | 生成旧版谓词覆盖。**1.21.4+ 上不需要。** |

<Callout type="info">
**我应该启用哪些系统？**
- **仅 `item_properties`** — 最适合新设置。干净、现代，不与其他插件冲突。
- **`item_properties` + `model_data_ids`** — 混合设置。物品同时具有 `item_model` 组件和 `custom_model_data.strings[0]`。
- **`model_data_float` + `generate_predicates`** — 完整的旧版兼容性，包含谓词覆盖和整数 CMD。
</Callout>

### 组合系统

你可以启用多个系统来在物品上设置多个组件：

```yaml
appearance:
  item_properties: true   # 设置 item_model 组件
  model_data_ids: true    # 也设置 custom_model_data.strings[0]
```

这让你获得两全其美的效果：通过 `item_model` 实现原生 1.21.4+ 渲染，同时为读取 `custom_model_data` 的插件提供字符串形式的 CMD。

<Callout type="warning">
**注意：** `model_data_ids` 和 `model_data_float` 不能同时启用——它们写入相同的资源包文件路径（`assets/minecraft/items/*.json`）。如果两者都启用，`model_data_ids` 在资源包生成中优先。
</Callout>

### 旧版谓词生成

`generate_predicates` 选项生成旧版谓词覆盖（`assets/minecraft/models/item/*.json`）：

```yaml
appearance:
  model_data_float: true       # 使用基于浮点数的 CMD
  generate_predicates: true    # 同时生成旧版谓词
```

<Callout type="info">
**我什么时候需要 `generate_predicates`？**

在 1.21.4+ 上，Minecraft 使用新的物品定义系统（`assets/minecraft/items/*.json`），因此游戏客户端**不需要**旧版谓词覆盖来显示自定义模型。

仅在以下情况下启用 `generate_predicates`：
- 外部工具需要读取旧版谓词 JSON 文件
- 你使用的资源包分析工具不支持 1.21.4+ 物品定义
- 你需要与旧版资源包格式向后兼容
</Callout>

### 每个物品的系统排除

你可以从任一系统中排除特定物品：

```yaml
my_item:
  Pack:
    generate_model: true
    textures:
      - my_texture
    exclude_from_predicates: false   # 不添加到谓词文件
    exclude_from_item_model: false   # 不生成物品模型定义
```

**使用场景：**
- `exclude_from_predicates: true` - 物品仅使用 item_model（更干净的资源包）
- `exclude_from_item_model: true` - 物品仅使用 CMD（用于插件兼容性）

<details>
<summary>**高级**：每个系统的工作原理</summary>

**物品模型定义（1.21.4+）**

Oraxen 在 `assets/oraxen/items/` 中为每个自定义物品生成文件。例如，ID 为 `my_sword` 的物品会创建：

```
assets/oraxen/items/my_sword.json
```

此文件定义了要显示的模型。然后物品会被赋予一个指向 `oraxen:my_sword` 的 `item_model` 组件。

如果你需要自定义命名空间或模型路径，可以使用 Components 部分覆盖：

```yaml
my_item:
  Components:
    item_model: "custom:weapons/legendary_sword"
```

这将在资源包中引用 `assets/custom/items/weapons/legendary_sword.json`。

**谓词（自定义模型数据）**

Oraxen 在基础物品模型文件中生成谓词覆盖（例如 `assets/minecraft/models/item/diamond_sword.json`）。每个自定义物品获得一个映射到其模型的 `custom_model_data` 值。

</details>

### pack 文件夹

此文件夹（`./plugins/Oraxen/pack`）包含你的资源包。它的工作方式类似于普通的 Minecraft 纹理包，但更简单。你可以将纹理拖入 textures 文件夹，将模型拖入 models 文件夹。你也可以在这些文件夹内创建子文件夹以使其更整洁，但这不是必须的。当插件生成资源包时，它会以 pack.zip 的名称出现在此文件夹中。

### 创建简单的 2D 物品

将你需要的纹理放入 pack 文件夹的 textures 目录中。然后你可以让 Oraxen 通过叠加纹理来生成模型：

```yaml
  Pack:
    generate_model: true
    parent_model: "item/handheld"
    textures:
      - example_image1.png #png 扩展名不需要
      - example_image2.png
```

`parent_model` 字段是 Minecraft 所需的。它允许你的物品继承物品模板的渲染属性。常用值包括用于剑等武器的 `item/handheld`，以及用于简单物品或宝石（如紫水晶）的 `item/generated`。

你还可以使用另一种声明纹理的方式，特别是在使用方块父模型时特别方便。
```yaml
Pack:
  generate_model: true
  parent_model: "block/cube"
  textures:
    top: example_image.png
    side: example_image2.png
```

### 使用 JSON 模型

创建 JSON 模型可能很耗时，但它允许你创建非常酷的效果（如 3D 物品）。使用 Oraxen 集成 JSON 模型非常简单：将你的纹理放入 textures 目录，将模型放入 models 目录（在 Oraxen/pack 文件夹内）。然后你可以让 Oraxen 将此模型应用到你的某个物品上：


模型和纹理名称始终使用小写。自 1.11 起，Minecraft 原版不再支持大写（尽管使用 OptiFine 的用户仍然可以使用）。


```yaml
  Pack:
    generate_model: false
    model: example_model.json #json 扩展名不是必须的
```

#### ⚠️ 使用 JSON 模型时的专业提示！

通常你获得的模板会将纹理放在一个文件夹中，为确保无误，打开 JSON 文件查看前几行，你应该会找到类似以下内容：

```json
{
	"__comment": "Designed by HighBridRed for Oraxen",
	"textures": {
		"particle": "custom/bonesword_palette",
		"texture": "custom/bonesword_palette",
		"bonesword_palette": "custom/bonesword_palette"
	},
	...
```

如你所见，纹理的路径是 **custom/bonesword_palette**，这意味着 Minecraft 将在 "custom" 文件夹中查找名为 **bonesword_palette.png** 的纹理，因此你需要在 "Oraxen/pack/textures" 内创建此文件夹。你也可以移除 "custom/" 只保留纹理名称，这样你只需将其拖放到 textures 文件夹中，无需创建子文件夹。

### 使用 blocking JSON 模型（用于盾牌）
如果你想为盾牌使用自定义模型，需要指定当玩家右键使用盾牌时显示的格挡模型，好在使用 Oraxen 这很容易。以下是可能的配置示例：

```yaml
  Pack:
    generate_model: false
    model: example_shield.json #json 扩展名不是必须的
    blocking_model: example_shield_blocking.json #json 扩展名不是必须的
```

### 使用 pulling JSON 模型（用于弓）
如果你想为弓使用自定义模型，需要指定当玩家右键使用弓时显示的拉弦模型，好在使用 Oraxen 这很容易。以下是可能的配置示例：

```yaml
  Pack:
    generate_model: false
    model: default/combat_bow
    pulling_models:
      - default/combat_bow_pulling_0
      - default/combat_bow_pulling_1
      - default/combat_bow_pulling_2
```
如果你只有纹理文件，也可以使用 pulling_textures

### 使用 charged_model JSON 模型（用于弩）

```yml
  Pack:
    generate_model: false
    model: default/custom_bow
    pulling_models:
      - default/custom_bow_pulling_0
      - default/custom_bow_pulling_1
      - default/custom_bow_pulling_2
    charged_model: default/custom_bow_pulling_2
    firework_model: default/custom_bow_charged #不是非常必要
```
如果你只有纹理文件，也可以使用 charged_texture 和 firework_texture

### 使用 cast_model JSON 模型（用于钓鱼竿）

```yml
  Pack:
    generate_model: false
    model: default/fishing_rod
    cast_model: default/fishing_rod_cast
```
如果你只有纹理文件，也可以使用 cast_texture

### 使用 damaged_model JSON 模型（用于不同耐久度等级）
```yml
Pack:
  generate_model: false
  model: default/diamond_sword
  damaged_models:
    - default/diamond_sword_damaged1
    - default/diamond_sword_damaged2
    - default/diamond_sword_damaged3
```
如果你只有纹理文件，也可以使用 damaged_textures

### 使用高级模型属性（Minecraft 1.21.4+）

从 Minecraft 1.21.4 起，你可以自定义额外的物品模型属性：

**仅 GUI 模型（1.21.2+）**
使用 `gui_model` 选项定义一个仅在 GUI/物品栏上下文中显示的单独模型。这使用 Minecraft 的 `display_context` 选择器在手持/装备时与物品栏中显示不同的模型。

```yaml
  Pack:
    generate_model: false
    model: item/held_sword      # 手持或装备时的模型
    gui_model: item/gui_sword   # 物品栏和 GUI 中的模型
```

当玩家手持或穿戴物品时，使用 `model`。在物品栏、工作台或物品展示框中查看时，则显示 `gui_model`。这适用于：
- 在物品栏中比 3D 手持模型更好看的图标
- 复杂 3D 模型的简化 GUI 版本
- 物品的不同视角（例如物品栏中俯视图，手持时侧视图）

**GUI 超大显示**
允许物品在 GUI 中放大时超出格子边界

```yaml
  Pack:
    generate_model: false
    model: item/large_item
    oversized_in_gui: true
```

当与如下缩放显示模型组合使用时，它会创建一个在物品栏格子中非常醒目的物品。

```json
{
	"parent": "item/handheld",
	"textures": {
		"layer0": "default/welcome_disk"
	},
	"display": {
		"gui": {
			"translation": [-2, -2, 0],
			"scale": [2, 2, 2]
		}
	}
}
```
查看超大显示在实际中的效果。
![model-definitions-showcase.png](/assets/model-definitions-showcase.png)

以下是 Wollodriin 提供的一个示例应用场景。
![model-definitions-use-case.png](/assets/model-definitions-use-case.png)

**换手动画**
控制交换物品时是否播放手部动画（仅在从一个物品切换到另一个物品时）

```yaml
  Pack:
    generate_model: false
    model: item/example_item
    hand_animation_on_swap: false
```

**换手动画缩放**
调整交换动画的缩放比例

```yaml
  Pack:
    generate_model: false
    model: item/example_item
    swap_animation_scale: 1.5
```

### 设置特定的自定义模型数据

你可以手动指定自定义模型数据值：

```yaml
my_item:
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - my_texture
    custom_model_data: 452
```

在 1.21.4+ 上，此值在启用 `model_data_float` 时使用（参见上文[外观系统](#外观系统1214)）。这让你可以控制你的物品使用哪个 CMD 值，以便与其他插件兼容。