# MiniMessage 格式参考

> MiniMessage 是 Kyori Adventure 库提供的 Minecraft 富文本标记语言，用于聊天、告示牌、物品名称等场景的文本格式化。
>
> 在线测试工具：[MiniMessage Web Viewer](https://webui.advntr.dev)
>
> 原版组件参考：[Minecraft Wiki - Text component format](https://minecraft.wiki/w/Text_component_format)

---

## 基本语法

MiniMessage 使用 **标签（Tag）** 来定义样式。每个标签有开始标签和结束标签（`<reset>` 是例外，它不需要闭合）。

- 开始标签是必须的，结束标签在非 `strict` 模式下可选
- 以下三种写法在视觉上完全等价：

```mm
<yellow>Hello <blue>World<yellow>!
<yellow>Hello <blue>World</blue>!
<yellow>Hello </yellow><blue>World</blue><yellow>!</yellow>
```

### 自闭合标签

无内容的标签可使用自闭合格式 `<tag/>`，即使在 strict 模式下也不需要单独的闭合标签。

### 大小写

所有标签名不区分大小写以降低冲突可能，但建议保持全小写或至少保持风格一致。

### 带参数的标签

格式为 `<tag:argument>stuff</tag>`：

```mm
<hover:show_text:"<red>test:TEST">TEST
<click:run_command:test>TEST
```

参数可以是 MiniMessage 字符串、数字、普通字符串或其他类型。

### 引号

单引号 `'` 和双引号 `"` 可互换使用。为减少转义，某些参数可切换引号类型。

### 转义字符

- 在纯文本中，标签开头的 `<` 可用反斜杠 `\<` 转义
- 在引号字符串中，可转义开引号字符 `\'` 或 `\"`
- 转义字符本身也可转义：`\\` 表示字面量 `\`
- 无引号标签参数不支持转义，以保持简洁
- 不支持转义的位置，字面量反斜杠会直接透传

---

## Strict 模式（严格模式）

默认情况下 MiniMessage 极为宽松，无效标签会被忽略，末尾未闭合的标签会自动闭合。

应用可启用 **strict 模式**：

- 禁止使用 `<reset>`
- 要求所有标签按打开顺序的**逆序**闭合
- 使用 strict 模式的应用应明确告知用户

---

## 标准标签

以下为 MiniMessage 默认包含并启用的标签。特定解析器可能添加自定义标签或限制可用标签子集，请参阅应用文档。

---

### Color — 颜色

为后续文本着色。

**标签：** `<_颜色名_>` 或 `<_#RRGGBB_>`

**别名：** 无

**参数（位置参数）：**

| 参数 | 说明 |
| ---- | ---- |
| `_颜色名_` | Minecraft 颜色常量，支持以下值 |

**可用颜色名：**

| 颜色名 | 中文 | 颜色名 | 中文 |
| ---- | ---- | ---- | ---- |
| `black` | 黑色 | `dark_blue` | 深蓝 |
| `dark_green` | 深绿 | `dark_aqua` | 深青 |
| `dark_red` | 深红 | `dark_purple` | 深紫 |
| `gold` | 金色 | `gray` / `grey` | 灰色 |
| `dark_gray` / `dark_grey` | 深灰 | `blue` | 蓝色 |
| `green` | 绿色 | `aqua` | 青色 |
| `red` | 红色 | `light_purple` | 浅紫 |
| `yellow` | 黄色 | `white` | 白色 |

- `grey` 可作为 `gray` 的替代，`dark_grey` 可作为 `dark_gray` 的替代。
- 支持十六进制颜色，格式为 `#RRGGBB`。

**示例：**
```mm
<yellow>Hello <blue>World</blue>!
<red>This is a <green>test!
<#00ff00>R G B!
```

---

### Color (Verbose) — 颜色（完整写法）

更明确的颜色定义方式。

**标签：** `<color:_颜色名或十六进制_>`

**别名：** `colour`、`c`

**参数：** 与 Color 标签相同（支持颜色名或十六进制颜色）

**示例：**
```mm
<color:yellow>Hello <color:blue>World</color:blue>!
<color:#FF5555>This is a <color:#55FF55>test!
```

---

### Shadow Color — 阴影颜色

为后续文本的阴影着色。

**标签：** `<shadow:_颜色名或十六进制_:[透明度浮点数]>`

**别名：** `<!shadow>` — 禁用阴影，等价于 `<shadow:#00000000>`（全透明）

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `_颜色名或十六进制_` | 命名颜色或十六进制颜色，支持 `#RRGGBB` 或 `#RRGGBBAA` 格式 | 是 |
| `[透明度浮点数]` | 0~1 之间的浮点数，表示阴影透明度。默认 0.25。如果十六进制颜色已包含 Alpha 值，此参数无效 | 否 |

**示例：**
```mm
<shadow:yellow>Hello <shadow:aqua:0.5>World</shadow>!
<shadow:#FF5555>This is a <shadow:#55FF55>test!
<shadow:#000000FF><b>Thicc
```

---

### Decoration — 装饰

为后续文本添加装饰效果。

**标签：** `<_装饰名_[:false]>` 或 `<!_装饰名_>`（反转装饰状态）

**别名：** 见下表

**可用的装饰：**

| 装饰名 | 别名 | 中文说明 |
|--------|------|----------|
| `bold` | `b` | 粗体 |
| `italic` | `em` / `i` | 斜体 |
| `underlined` | `u` | 下划线 |
| `strikethrough` | `st` | 删除线 |
| `obfuscated` | `obf` | 乱码/混淆 |

**示例：**
```mm
<underlined>This is <bold>important</bold>!
```

---

### Reset — 重置

关闭所有当前打开的标签，重置颜色/装饰等。重置标签**不能**被闭合。

> ⚠️ **注意：** 在 strict 模式下禁止使用 `<reset>`。

**标签：** `<reset>`

**参数：** 无

**示例：**
```mm
<yellow><bold>Hello <reset>world!
```

---

### Click — 点击事件

允许点击组件时执行操作。

**标签：** `<click:_操作类型_:_值_>`

**参数：**

| 参数 | 说明 |
|------|------|
| `_操作类型_` | 点击事件类型，参见 [ClickEvent.Action 枚举](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/event/ClickEvent.Action.html#enum.constant.summary) |
| `_值_` | 该事件类型的参数，参见 [Minecraft Wiki](https://minecraft.wiki/w/Text_component_format) |

**常用 Click 操作：**

| 操作类型 | 说明 | 值示例 |
|----------|------|--------|
| `run_command` | 执行命令 | `/seed` |
| `suggest_command` | 建议命令（填入聊天框） | `/tell Player ` |
| `open_url` | 打开链接 | `https://example.com` |
| `copy_to_clipboard` | 复制到剪贴板 | `要复制的文本` |
| `change_page` | 切换书页 | `1` |

**示例：**
```mm
<click:run_command:/seed>Click</click> to show the world seed!
Click <click:copy_to_clipboard:Haha you suck> this </click>to copy your score!
```

> ⚠️ **注意：** 自 1.19.1 引入聊天签名后，客户端不再执行需要签名参数的命令（如 `/say` 或 `/tell`），以防止服务器代表客户端发送签名消息。

---

### Hover — 悬停事件

允许鼠标悬停时显示信息。

**标签：** `<hover:_操作类型_:_值_>`

**参数：**

| 参数 | 说明 |
|------|------|
| `_操作类型_` | 悬停事件类型，参见 [HoverEvent.Action 字段](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/event/HoverEvent.Action.html#field.summary) |
| `_值_` | 各操作类型对应的参数，详见下表 |

**Hover 操作类型详解：**

| 操作类型 | 值的格式 | 说明 |
|----------|----------|------|
| `show_text` | `_文本_` | 一个 MiniMessage 字符串 |
| `show_item` | `_类型_[:_数量_[(:_组件Key_:_组件Value_)...]]` | 物品的类型 Key，可选数量（整数）和[数据组件](https://minecraft.wiki/w/Data_component_format)键值对列表 |
| `show_item`（旧版） | `_类型_[:_数量_[:tag]]` | ⚠️ 旧版格式：物品类型 Key，可选数量和 tag（[SNBT](https://minecraft.wiki/w/NBT_format#SNBT_format) 字符串） |
| `show_entity` | `_类型_:_UUID_[:_名称_]` | 实体类型 Key、实体 UUID 和可选自定义名称 |

> ⚠️ `show_item` 的旧版 `类型[:数量[:tag]]` 格式可能在未来移除，建议使用新版格式。

**示例：**
```mm
<hover:show_text:'<red>test'>TEST
<hover:show_item:diamond_sword:1:enchantments:'{sharpness:3,knockback:2}'>Very sharp sword!</hover>
```

---

### Keybind — 按键绑定

显示操作对应的配置按键。

**标签：** `<key:_按键ID_>`

**参数：**

| 参数 | 说明 |
|------|------|
| `_按键ID_` | 操作的按键绑定标识符 |

**示例：**
```mm
Press <red><key:key.jump> to jump!
```

---

### Translatable — 可翻译文本

根据玩家语言显示 Minecraft 本地化消息。

**标签：** `<lang:_翻译Key_:_值1_:_值2_...>`

**别名：** `tr`、`translate`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `_翻译Key_` | 翻译键（translation key） | 是 |
| `_值X_` | 用于替换翻译键中占位符的值（对应 JSON 中的 `with` 数组） | 否（可变数量） |

**示例：**
```mm
You should get a <lang:block.minecraft.diamond_block>!
<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!
```

---

### Fallback — 带后备的翻译

> ⚠️ 仅限 Minecraft 1.19.4 及以上版本。

根据玩家语言显示消息，若无对应翻译则显示后备文本。

**标签：** `<lang_or:_翻译Key_:_后备文本_:_值1_:_值2_...>`

**别名：** `tr_or`、`translate_or`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `_翻译Key_` | 翻译键 | 是 |
| `_后备文本_` | 无翻译时的后备显示文本 | 是 |
| `_值X_` | 用于替换占位符的值 | 否（可变数量） |

**示例：**
```mm
You should get a <lang_or:block.minecraft.diamond_block:'Dirt Block'>!
```

---

### Insertion — 插入文本

允许通过 Shift+点击将文本插入聊天框。

**标签：** `<insert:_文本_>`

**参数：**

| 参数 | 说明 |
|------|------|
| `_文本_` | 要插入的文本内容 |

**示例：**
```mm
Shift-click <insert:test>this</insert> to insert!
```

---

### Rainbow — 彩虹色

彩虹渐变色文本。

**标签：** `<rainbow:[!][phase]>`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `!` | 字面量 `!`，反转彩虹方向 | 否 |
| `phase` | 相位偏移（整数），调整彩虹起始位置 | 否 |

**示例：**
```mm
<yellow>Woo: <rainbow>||||||||||||||||||||||||</rainbow>!
<yellow>Woo: <rainbow:!>||||||||||||||||||||||||</rainbow>!
<yellow>Woo: <rainbow:2>||||||||||||||||||||||||</rainbow>!
<yellow>Woo: <rainbow:!2>||||||||||||||||||||||||</rainbow>!
```

---

### Gradient — 渐变色

渐变色彩文本。

**标签：** `<gradient:[颜色1]:[颜色...]:[phase]>`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `[颜色1]...[颜色N]` | 1 到 N 个颜色，可以是十六进制或命名颜色（至少 1 个） | 是 |
| `[phase]` | 相位偏移，范围 -1 到 1，可产生动画效果 | 否 |

**示例：**
```mm
<yellow>Woo: <gradient>||||||||||||||||||||||||</gradient>!
<yellow>Woo: <gradient:#5e4fa2:#f79459>||||||||||||||||||||||||</gradient>!
<yellow>Woo: <gradient:#5e4fa2:#f79459:red>||||||||||||||||||||||||</gradient>!
<yellow>Woo: <gradient:green:blue>||||||||||||||||||||||||</gradient>!
```

---

### Transition — 颜色过渡

在多个颜色之间过渡。与 Gradient 类似，但所有文本显示为同一颜色，phase 决定当前颜色。

**标签：** `<transition:[颜色1]:[颜色...]:[phase]>`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `[颜色1]...[颜色N]` | 1 到 N 个颜色 | 是 |
| `[phase]` | 相位偏移，范围 -1 到 1 | 是（用于标记语法位置，运行时可动态替换） |

**示例：**
```mm
<transition:#00ff00:#ff0000:0>|||||||||</transition>
<transition:white:black:red:[phase]>Hello world [phase]</transition>
```

---

### Font — 字体

更改文本的字体。

**标签：** `<font:key>`

**参数：**

| 参数 | 说明 |
|------|------|
| `key` | 字体的命名空间 Key，缺省命名空间为 `minecraft` |

**Minecraft 内置字体：**

| 字体 Key | 说明 |
|----------|------|
| `minecraft:default` | 默认字体 |
| `minecraft:uniform` | 等宽字体 |
| `minecraft:alt` | 替代字体（魔法符文风格） |
| `minecraft:illageralt` | 灾厄村民字体（Illager 符文） |

**示例：**
```mm
Nothing <font:uniform>Uniform <font:alt>Alt  </font> Uniform
<font:myfont:custom_font>Uses a custom font from a resource pack</font>
```

---

### Newline — 换行

插入换行符。

**标签：** `<newline>`

**别名：** `br`

**参数：** 无

**示例：**
```mm
Let me insert a <newline>line break here.
<hover:show_text:'<red>Hover with a<newline><green>line break'>Text with<newline>line break</hover>
```

---

### Selector — 选择器

> 自 v4.11.0 起可用。

插入一个选择器组件，用于显示实体名称。

**标签：** `<selector:_选择器_[:_分隔符_]>`

**别名：** `sel`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `_选择器_` | Minecraft 目标选择器，如 `@s`、`@e[limit=5]`、`@p` 等 | 是 |
| `_分隔符_` | 多个匹配值之间的分隔符 | 否 |

**示例：**
```mm
Hello <selector:@e[limit=5]>, I'm <selector:@s>!
```

---

### Score — 记分板分数

> 自 v4.13.0 起可用。
> ⚠️ 记分板组件需要在**服务端进行渲染**才能被客户端看到，这是平台相关操作。

插入记分板分数组件。

**标签：** `<score:_名称_:_计分项_>`

**参数：**

| 参数 | 说明 |
|------|------|
| `_名称_` | 服务器记分板上分数持有者的名称，或使用接收者上下文中解析的选择器 |
| `_计分项_` | 要获取 `名称` 在哪个计分项（objective）中的分数 |

**示例：**
```mm
You have won <score:rymiel:gamesWon/> games!
```

---

### NBT — NBT 数据

> 自 v4.13.0 起可用。
> ⚠️ NBT 组件需要在**服务端进行渲染**才能被客户端看到，这是平台相关操作。

插入 NBT 数据组件。语法设计上贴近原版 Minecraft `/data` 命令。

**标签：** `<nbt:block|entity|storage:id:路径[:_分隔符_][:interpret]>`

**别名：** `data`

**参数：**

| 参数 | 说明 |
|------|------|
| `block\|entity\|storage` | 数据源类型：方块实体的 `block`、实体的 `entity` 选择器、或持久化命令 `storage` 容器 |
| `_id_` | 方块 NBT 的位置、实体 NBT 的选择器、或 storage NBT 的 key（资源位置） |
| `_路径_` | 从数据源中解析的 NBT 路径 |
| `_分隔符_` | 多个值之间的分隔符（主要用于实体 NBT 返回多个值时） |
| `interpret` | 字面量 `interpret`，如果存在则将结果解析为组件 JSON |

**示例：**
```mm
Your health is <nbt:entity:'@s':Health/>
```

---

### Pride — 骄傲月旗帜

> 自 v4.18.0 起可用。

将标签内文本着色为与骄傲月旗帜（Pride Flag）对应的渐变色。

**标签：** `<pride[:flag|phase]>`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `flag` | 旗帜类型，见下表 | 否 |
| `phase` | 相位偏移，-1 到 1 之间的数字 | 否 |

**支持的旗帜类型：**
`pride`（默认）、`progress`、`trans`、`bi`、`pan`、`nb`、`lesbian`、`ace`、`agender`、`demisexual`、`genderqueer`、`genderfluid`、`intersex`、`aro`、`baker`、`philly`、`queer`、`gay`、`bigender`、`demigender`、`femboy`、`intersex_inclusive`

**示例：**
```mm
Happy <pride>pride month</pride>!
Kyori supports <pride:trans>trans rights</pride>!
```

---

### Sprite — 精灵图

> 自 v4.25.0 起可用。

插入纹理图集中的精灵图。

**标签：** `<sprite[:图集]:精灵图>`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `图集` | 图集（atlas）名称，如 `minecraft:blocks`。缺省命名空间为 `minecraft` | 否 |
| `精灵图` | 精灵图路径，如 `item/emerald` | 是 |

**示例：**
```mm
Look at my <sprite:blocks:block/stone>!
This item costs 10 x <sprite:"minecraft:items":item/porkchop>.
```

---

### Head — 玩家头颅

> 自 v4.25.0 起可用。

插入玩家头像。

**标签：** `<head:名称|UUID|纹理[:外层显示]>`

**参数：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `名称\|UUID\|纹理` | 玩家名称、UUID 或皮肤纹理路径 | 是 |
| `外层显示` | `true` 或 `false`，决定是否绘制外层（帽子层），默认 `true` | 否 |

**示例：**
```mm
My favorite dev is <head:1f085b2d-9548-4159-a8c7-f3ccdf0c2054>.
Do you prefer <head:entity/player/wide/steve> Steve or <head:entity/player/slim/alex> Alex?
Thanks <head:Strokkur24:false> for the docs!
```

---

## 附录 A：颜色速查表

| Minecraft 颜色名 | 十六进制 | 中文 |
| ---- | ---- | ---- |
| `black` | `#000000` | 黑色 |
| `dark_blue` | `#0000AA` | 深蓝 |
| `dark_green` | `#00AA00` | 深绿 |
| `dark_aqua` | `#00AAAA` | 深青 |
| `dark_red` | `#AA0000` | 深红 |
| `dark_purple` | `#AA00AA` | 深紫 |
| `gold` | `#FFAA00` | 金色 |
| `gray` | `#AAAAAA` | 灰色 |
| `dark_gray` | `#555555` | 深灰 |
| `blue` | `#5555FF` | 蓝色 |
| `green` | `#55FF55` | 绿色 |
| `aqua` | `#55FFFF` | 青色 |
| `red` | `#FF5555` | 红色 |
| `light_purple` | `#FF55FF` | 浅紫 |
| `yellow` | `#FFFF55` | 黄色 |
| `white` | `#FFFFFF` | 白色 |

## 附录 B：装饰标签速查表

| 标签 | 别名 | 效果 |
| ---- | ---- | ---- |
| `<bold>` | `<b>` | **粗体** |
| `<italic>` | `<em>`, `<i>` | *斜体* |
| `<underlined>` | `<u>` | <u>下划线</u> |
| `<strikethrough>` | `<st>` | ~~删除线~~ |
| `<obfuscated>` | `<obf>` | 乱码混淆 |
| `<reset>` | — | 重置全部样式 |
| `<newline>` | `<br>` | 换行 |

## 附录 C：Click/Hover 操作速查

| 类别 | 操作类型 | 说明 |
| ---- | ---- | ---- |
| Click | `run_command` | 执行命令 |
| Click | `suggest_command` | 建议命令 |
| Click | `open_url` | 打开 URL |
| Click | `copy_to_clipboard` | 复制文本 |
| Click | `change_page` | 翻书页 |
| Hover | `show_text` | 显示文本（MiniMessage 字符串） |
| Hover | `show_item` | 显示物品 |
| Hover | `show_entity` | 显示实体信息 |

## 附录 D：完整标签索引

| 标签 | 参数 | 别名 | 最低版本 |
| ---- | ---- | ---- | ---- |
| `<colorName>` | 颜色名/十六进制 | — | — |
| `<color:...>` | 颜色名/十六进制 | `colour`, `c` | — |
| `<shadow:...>` | 颜色[:透明度] | `<!shadow>` | — |
| `<bold>`, `<italic>`, 等 | `[:false]` | `b`, `i`/`em`, `u`, `st`, `obf` | — |
| `<reset>` | 无 | — | — |
| `<click:...>` | 操作:值 | — | — |
| `<hover:...>` | 操作:值 | — | — |
| `<key:...>` | 按键ID | — | — |
| `<lang:...>` | key:值1:值2... | `tr`, `translate` | — |
| `<lang_or:...>` | key:后备:值1:值2... | `tr_or`, `translate_or` | MC 1.19.4 |
| `<insert:...>` | 文本 | — | — |
| `<rainbow>` | [!][phase] | — | — |
| `<gradient:...>` | 颜色1:颜色2...[:phase] | — | — |
| `<transition:...>` | 颜色1:颜色2...:phase | — | — |
| `<font:...>` | 字体key | — | — |
| `<newline>` | 无 | `br` | — |
| `<selector:...>` | 选择器[:分隔符] | `sel` | v4.11.0 |
| `<score:...>` | 名称:计分项 | — | v4.13.0 |
| `<nbt:...>` | block\|entity\|storage:id:路径[:分隔符][:interpret] | `data` | v4.13.0 |
| `<pride>` | [:flag\|phase] | — | v4.18.0 |
| `<sprite:...>` | [:图集]:精灵图 | — | v4.25.0 |
| `<head:...>` | 名称\|UUID\|纹理[:外层] | — | v4.25.0 |
