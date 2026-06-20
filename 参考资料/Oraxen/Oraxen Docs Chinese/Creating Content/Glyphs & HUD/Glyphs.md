---
description: 如何添加自定义字形、表情符号和 HUD 元素
cover: https://i.imgur.com/T76ianD.png
coverY: 0
---

import { Callout } from 'nextra/components'

# 字形与 HUD 元素

Oraxen 允许你创建自定义字形——可以在聊天、物品名称、描述、计分板等位置出现的带纹理的 Unicode 符号。

## 你可以创建的内容

| 类型 | 使用场景 | 示例 |
|------|----------|---------|
| 表情符号 | 聊天表情 | ❤️ 聊天中的 :heart: |
| 图标 | 物品描述、等级 | 等级徽章、稀有度图标 |
| HUD 元素 | 自定义 UI | 血条、小地图 |
| GUI 纹理 | 自定义菜单 | 库存背景 |
| 大型图片 | 横幅、标志 | 服务器品牌 |

## 字形功能

| 功能 | 描述 |
|---------|-------------|
| [基础字形](#如何添加字形) | 简单的表情风格图标 |
| [多点阵图](#多点阵图字形) | 从一张图片中提取多个字形 |
| [网格字形](#基于网格的字形) | 跨多个字符的大型图片 |
| [动画字形](#动画字形) | 移动/动画图标 |
| [引用字形](#引用字形) | 指向现有字形的别名 |
| [位移](#位移不再需要-shiftsyml) | 像素级精确定位 |

<Callout type="info">
字形在任何显示文本的地方都可以使用：聊天、物品名称、描述、计分板、Boss 栏、操作栏等。
</Callout>

---

## 什么是字形？

字形是一个带纹理的 Unicode 符号。它可以用于任何文本中（聊天、物品名称、描述等）。它们可以用来做非常非常强大的事情（自定义库存、额外栏位），但最简单的用途是作为表情符号。

## 如何添加字形？

你首先需要创建一个 png 纹理。例如包含在 `default/chat` 中的 heart.png 文件。

![heart.png](/assets/heart%20(1).png)

然后你可以将你的部分添加到 glyphs 目录中的任何 yaml 文件中。每个字形的代码必须不同。这是与将要使用的 Unicode 字符编号对应的数字。texture 是纹理文件的路径和名称。height 允许你设置显示的字符缩放，而 ascent 定义显示结果的垂直偏移。

```yaml
heart:
  texture: default/chat/heart
  ascent: 8
  height: 8
```

## 我的字形不工作？

这很可能是由于字形配置错误。
请检查你的控制台是否有任何错误，因为它应该准确地告诉你哪个字形配置错误以及如何错误。
![](https://user-images.githubusercontent.com/62521371/185404681-e0c1a881-e30b-446a-9f33-20dd88bae27c.png)

## 多点阵图字形
如果你的 png 由多个表情组成，你可以将其设置为多点阵图。
这意味着你可以将多个字形绑定到一张图片上。然而，这需要一些额外的配置才能工作。
在 fonts.yml 中有一个 `bitmaps` 部分。
在这里你需要指定一个 `id`，你将在字形配置中使用它。
你还需要指定纹理的路径，以及位图有多少行和列。
以下是 `fonts.yml` 中的一个条目示例：

```yaml
bitmaps:
  example_bitmap:
    texture: example/example_bitmap
    rows: 4
    columns: 9
    ascent: 8
    height: 8
```
![](/assets/example_bitmap.png)

如你所见，上面显示的图片有 4 行和 9 列。
ascent 和 height 属性将用于所有绑定到此位图的字形。
现在你有了配置好的位图，你可以将字形链接到它。
在你的字形配置中，你需要指定位图 id，以及你想要使用的字形所在的行和列。
以下是使用上述位图的字形配置示例。

```yaml
example_glyph:
  texture: default/chat/example_glyph
  bitmap:
    id: example_bitmap
    row: 1
    column: 1
  #ascent: 8 # 不需要，因为位图已指定
  #height: 8 # 不需要，因为位图已指定
```

这会将字形链接到上图中第一行的第一个表情。

## 表情列表
要使字形出现在 `/oraxen emojis` 下，你需要像下面这样指定它是一个表情。
如果未指定，此项默认值为 `false`
```yaml
heart:
  texture: default/chat/heart
  is_emoji: true
```
默认情况下，它也会只显示玩家有权限使用的表情。
在 `settings.yml` 中你可以切换 `only_show_emojis_with_permission` 设置。
这将会向每个玩家显示所有表情，并添加一个悬停消息指示他们是否有权限。
![img](https://cdn.discordapp.com/attachments/758785982005903431/1002564595099111474/unknown.png)
## 如何在聊天中使用它？

你需要在你的字形部分中添加一个 chat 子部分：

```yaml
chat:
  placeholders:
    - "<3"
  permission: "oraxen.emoji.heart"
```

拥有所需权限的玩家可以在聊天中使用这些占位符（如果指定了权限，则权限不是强制性的）。

## 如何让字形支持 Tab 补全？
只需在 chat 部分中设置 `tabcomplete: true`。
如果未指定，此项默认值为 `false`
Tab 补全目前仅适用于 1.19.3 及以上版本的服务器。
```yaml
chat:
  tabcomplete: true
  placeholders:
    - "<3"
  permission: "oraxen.emoji.heart"
```


## 基于网格的字形

<Callout type="info">
基于网格的字形允许你使用跨越多个 Unicode 字符的单个大型纹理，非常适合大型图片、详细图标或精灵表。
</Callout>

如果你的纹理大于 256x256 像素，或者想在聊天/描述中显示大型图片，你可以使用 `grid` 配置将其分割到多个字符上。

```yaml
large_banner:
  texture: custom/large_banner
  ascent: 8
  height: 128
  grid:
    rows: 2      # 图片跨越 2 行
    columns: 3   # 图片跨越 3 列
```

插件将自动为该字形分配所需的 Unicode 字符（行 x 列）。在上面的例子中，将分配 6 个字符来显示完整的图片。

在 MiniMessage 标签中使用网格字形时，你可以选择特定部分：
- `<glyph:large_banner>` - 显示所有字符，行之间用换行分隔
- `<glyph:large_banner:1>` - 仅显示第 1 个字符
- `<glyph:large_banner:1..4>` - 显示第 1 到第 4 个字符

## 外观配置

字形支持 `appearance` 部分用于高级样式选项：

```yaml
custom_icon:
  texture: icons/custom
  ascent: 8
  height: 8
  appearance:
    font: "minecraft:default"   # 自定义字体（默认: minecraft:default）
    shadow_color: "#80000000"   # ARGB 十六进制格式的阴影颜色 (1.21.4+)
```

### 阴影颜色 (1.21.4+)

在 Minecraft 1.21.4 及以上版本，你可以为字形自定义文本阴影颜色。阴影颜色使用 ARGB 十六进制格式：
- `#AARRGGBB` - 带 alpha、红、绿、蓝的完整格式
- `#RRGGBB` - RGB 格式（假定 FF alpha）
- `#RGB` - 短格式（扩展为 #FFRRGGBB）

示例：`#80000000` 创建半透明的黑色阴影。

<Callout type="info">
如果字形配置了 `shadow_color`，使用字形标签时阴影会**自动应用**——无需额外的标志。你只需要在想要用不同颜色覆盖时使用 `:s:#color` 语法。
</Callout>

## 字形标签选项

在 MiniMessage 格式中使用字形时，你可以添加修饰符：

```
<glyph:heart>              基本用法（自动应用配置的 shadow_color）
<g:heart>                  简写语法
<glyph:heart:c>            可着色 - 继承周围文本的颜色
<glyph:heart:colorable>    同上（完整名称）
<glyph:heart:s:#FF0000>    用自定义颜色（红色）覆盖阴影
<glyph:heart:shadow:#FF0000>  同上（完整名称）
<glyph:grid_icon:2>        选择特定字符索引（从 1 开始）
<glyph:grid_icon:1..4>     选择字符范围
```

多个选项可以组合：
```
<glyph:heart:c:s:#80FF0000>  可着色，并使用自定义半透明红色阴影
```

### 可着色字形

默认情况下，字形以白色渲染以显示其原始纹理颜色。使用 `:c` 或 `:colorable` 修饰符允许字形从周围文本继承颜色：

```
<red>I <glyph:heart:c> Oraxen</red>  // 心形将为红色
```

## 位移（不再需要 shifts.yml）

Oraxen 不再依赖生成的 `glyphs/shifts.yml` 文件。位移现在是**内置的**，使用在资源包生成过程中自动注入到默认字体中的空格字体提供器。

- 如果你仍然有 `plugins/Oraxen/glyphs/shifts.yml`，它已**弃用**，可以安全删除。
- 位移标签仍然有效（例如 `<shift:8>`），但它们现在由**空格提供器**支持，而不是"虚假字形纹理"。

<Callout type="info">
如果你之前自定义了 `shifts.yml`，你应该将该逻辑迁移到普通字形或布局逻辑。位移现在被视为基础设施，会自动生成。
</Callout>

## 引用字形

引用字形允许你**别名现有字形的一部分**（例如：网格字形的一个子集），而无需生成新的提供器/纹理。这使得资源包更小，并使大型 GUI 字形更易于重用。

示例：

```yaml
gui_header:
  reference:
    glyph: full_gui      # 源字形 ID
    index: 1..3          # 要包含的字符（从 1 开始索引）
  chat:
    placeholders: [":header:"]
    permission: "gui.header"
```

## 动画字形

动画字形从 **PNG 精灵表**（帧垂直堆叠）渲染帧。动画由 Oraxen 在资源包生成期间生成的着色器处理。

示例：

```yaml
loading:
  texture: animations/loading # plugins/Oraxen/pack/textures 下的路径（png 扩展名可选）
  animation:
    frames: 12                # 精灵表中的帧数（最大: 16）
    fps: 12                   # 1-127（默认: 10）
    loop: true                # 默认: true
    offset: 0                 # 可选的像素水平偏移
  ascent: 8
  height: 16
  chat:
    placeholders: [":loading:"]
```

<Callout type="info">
**限制：** 动画字形每个动画最多支持 **16 帧**。非循环动画（`loop: false`）与服务器时间同步播放，意味着同一动画的所有实例将保持同步。
</Callout>

<Callout type="warning">
动画字形需要启用 Oraxen 的资源包生成功能，并且可能与其他替换 Minecraft 文本着色器的资源包冲突。如果你使用多个编辑着色器的资源包，请使用资源包合并系统并确保着色器文件被有意合并。
</Callout>

<Callout type="info">
在寻找彩虹、波浪、抖动或脉冲等文字特效吗？请参见[文字特效](/creating-content/text-effects)文档。
</Callout>

## PlaceholderAPI

### 我的字形占位符是什么？
部分名称就是字形 id。在这个例子中字形 id 是 `heart`，占位符是 `%oraxen_glyphid%`，所以在这个例子中：`%oraxen_heart%`
Glyph-ID 是任何字形配置中的第一行，它不是纹理名称或占位符。

### 位移占位符

Oraxen 为像素位移提供了 PlaceholderAPI 占位符，当你需要在兼容的插件中偏移文本或字形时很有用：

| 占位符 | 描述 |
|-------------|-------------|
| `%oraxen_shift_N%` | 向右移动 N 像素（正向） |
| `%oraxen_neg_shift_N%` | 向左移动 N 像素（负向） |

**示例：**
- `%oraxen_shift_8%` - 向右移动 8 像素
- `%oraxen_shift_16%` - 向右移动 16 像素
- `%oraxen_neg_shift_8%` - 向左移动 8 像素
- `%oraxen_neg_shift_100%` - 向左移动 100 像素

这些是 `<shift:N>` MiniMessage 标签的 PlaceholderAPI 等价物。

### 如何在前缀 / Luckperms 中使用它
要将字形添加到 LuckPerms 前缀中（通常用于显示等级），只需将 `%oraxen_glyphid%` 添加到你选择的前缀方案中。
例如，如果使用 LuckPerms，你可以使用命令：`/lp group default meta setprefix %oraxen_glyphid%`，它会用字形替换它。
因为大多数插件只解析一次占位符，`%luckperms_prefix%` 不会被再次解析。
你很可能还需要获取 PlaceholderAPI 的 Utils-Expansion。
要获取它，请访问[这个链接](https://api.extendedclip.com/media/Utils-Expansion-1.0.1.jar)，并将其放入你的 plugins/PlaceholderAPI/expansions 文件夹中。
然后在你选择的插件中使用 `%utils_parse:2_luckperms_prefix%` 来再次解析前缀。
请记住，你的聊天插件必须支持 PlaceholderAPI 才能使其工作。
如果出于某种原因这不工作，你可以始终使用字形配置中 `char` 属性的原始 unicode

### 如何在物品的名称/描述中使用字形？
任何字形都可以在你的物品配置的名称和描述中使用。

```
<glyph:heart>
```

其中 heart 替换为你的字形部分名称。