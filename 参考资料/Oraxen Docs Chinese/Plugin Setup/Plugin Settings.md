---
description: 影响插件整体行为的各种选项
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966825582216237126/unknown.png
coverY: 0
---

# 插件设置

## Plugin

```yaml
Plugin:
  commands:
    repair:
      oraxen_durability_only: false # 设为 true 将不修复原版物品
```

插件相关选项。您可以在此配置某些功能的运作方式。修复功能是否应该只修复具有 Oraxen 耐久度的 Oraxen 物品？

## Plugin 选项

```yaml
Plugin:
  language: english # 要使用的语言文件
  debug: false # 启用详细日志记录（NMS 检测、资源包生成、HUD 加载等）
  auto_update_paper_config: true # 自动更新 paper-global.yml 以适配自定义方块
  generation:
    default_assets: true # 首次运行时生成默认纹理/模型
    default_configs: true # 首次运行时生成默认物品配置
  formatting: # 在各种上下文中启用 MiniMessage 格式化
    inventory_titles: true
    titles: true
    subtitles: true
    action_bar: true
    anvil: false
    signs: false
    chat: false
    books: false
```

### 调试模式

当启用 `debug: true` 时，Oraxen 会向控制台输出额外的信息消息，包括：
- NMS 版本检测
- 数据包适配器选择
- 资源包生成进度
- HUD 加载详情
- Shift 字体生成消息

这些消息默认隐藏，以保持控制台输出整洁。

### 自动更新 Paper 配置

当 `auto_update_paper_config: true`（默认）时，Oraxen 会自动更新您的 `paper-global.yml`，以禁用会干扰自定义方块的方块更新：
- `disable-noteblock-updates: true`
- `disable-tripwire-updates: true`
- `disable-chorus-plant-updates: true`

如果您希望手动管理这些设置，请设为 `false`。您也可以使用 JVM 参数 `-Doraxen.autoUpdatePaperConfig=false` 覆盖此项。

## Item 配置

### Oraxen 配置如何工作？

首先，Oraxen 有几个文件夹，其中 3 个用于配置内容。第一个是 `Oraxen/glyphs/`，用于配置自定义字体或字形；其次是 `Oraxen/items/`，用于配置和创建您自己的配置 yaml；最后是 `Oraxen/pack/`，所有文件（如纹理和模型）的目标生成位置。

## Pack

### Generation

```yaml
  generation:
    generate: true
    compression: BEST_COMPRESSION # 参见 Deflater.class
    # protection 将使用多种方法使您的资源包无法通过常规工具
    # （原生 Windows 解压、7zip、winrar 等）提取，而不改变其完整性。
    # 如果启用此选项，请小心不要尝试提取资源包，否则可能会占满您的磁盘。
    protection: true
    comment: "此纹理包的内容
     \n属于 Oraxen 插件的所有者，
     \n任何全部或部分使用
     \n必须遵守 Oraxen 的
     \n条款与条件。"
    appearance:
      item_properties: true        # 使用 item_model 组件
      model_data_ids: false        # 使用 custom_model_data.strings 配合 select
      model_data_float: false      # 使用 custom_model_data.floats 配合 range_dispatch
      generate_predicates: false   # 生成旧版 predicate（在 1.21.4+ 上不需要）
```

此部分允许您配置资源包的**生成**。**compression** 默认配置为生成尽可能小的 zip。您可以更改 **comment**，这基本上是您 zip 内部的水印。

#### 外观系统（1.21.4+）

`appearance` 部分控制物品纹理的应用方式。**多个系统可以同时启用**以获得最大兼容性：

| 设置 | 资源包输出 | 物品组件 | 描述 |
|---------|-------------|----------------|-------------|
| `item_properties` | `assets/oraxen/items/<id>.json` | `item_model` 组件 | **默认。** 使用带有 Oraxen ID（`oraxen:<item_id>`）的物品模型定义。 |
| `model_data_ids` | `assets/minecraft/items/<material>.json` | `custom_model_data.strings[0]` | 使用 `minecraft:select` 分派器配合字符串 ID（`oraxen:<item_id>`）。 |
| `model_data_float` | `assets/minecraft/items/<material>.json` | `custom_model_data.floats[0]` | 使用 `minecraft:range_dispatch` 配合数字阈值。 |
| `generate_predicates` | `assets/minecraft/models/item/<material>.json` | — | 生成旧版 predicate 覆盖。**在 1.21.4+ 上不需要。** |

**版本行为：**
- **1.21.4 之前**: 始终使用旧版 predicate 覆盖（无论设置如何）
- **1.21.4+**: 使用启用的系统

**常见配置：**
- 仅 `item_properties: true` — 现代 1.21.4+ 设置（默认）
- `item_properties: true` + `model_data_ids: true` — 混合方案，适用于读取 CMD 字符串的插件
- `model_data_float: true` + `generate_predicates: true` — 完整的旧版兼容性

<Callout type="warning">
`model_data_ids` 和 `model_data_float` 不能同时启用——它们写入相同的资源包文件路径。如果两者都启用，`model_data_ids` 优先。
</Callout>

<Callout type="info">
**generate_predicates** 仅在外部工具需要读取旧版 predicate JSON 文件时才需要。在 1.21.4+ 上，Minecraft 使用新的物品定义系统，因此游戏客户端不需要 predicate。
</Callout>

关于详细文档和每个物品的选项，请参阅[物品外观](/creating-content/items/appearance#appearance-systems-1214)。

#### 多版本资源包

如果您的服务器使用 ViaVersion 或 ProtocolSupport 来接受不同 Minecraft 版本的玩家，您可以启用多版本资源包生成。Oraxen 将为每个版本范围生成一个单独的资源包，使用正确的 `pack_format`，并在玩家加入时将正确的资源包发送给每个玩家。

```yaml
Pack:
  generation:
    multi_version_packs: false
```

启用时，Oraxen 为以下版本范围生成资源包：

| 版本范围 | 资源包格式 |
|---------------|-------------|
| 1.20-1.20.1 | 15 |
| 1.20.2 | 18 |
| 1.20.3-1.20.4 | 22 |
| 1.20.5-1.20.6 | 32 |
| 1.21-1.21.1 | 34 |
| 1.21.2-1.21.3 | 42 |
| 1.21.4 | 46 |
| 1.21.5 | 55 |
| 1.21.6 | 63 |
| 1.21.7-1.21.8 | 64 |
| 1.21.9-1.21.10 | 69 |
| 1.21.11 | 75 |
| 26.1.x | 84 |

**要求：**
- 安装了 **ViaVersion** 或 **ProtocolSupport** 插件（用于客户端版本检测）
- 上传类型必须是 `polymath` 或 `external`（不能是 `self-host`，它只能提供一个文件）
- 必须启用资源包上传（`Pack.upload.enabled: true`）

如果没有版本检测插件，所有玩家将收到服务器自身版本的资源包作为回退。

<Callout type="info">
当启用多版本资源包时，始终会生成旧版 predicate 覆盖，因为旧客户端（1.21.4 之前）无法使用物品定义。
</Callout>

<Callout type="info">
**26.1.x 和 `pack.mcmeta` 变更：** 从 Minecraft 1.21.9（资源包格式 69）开始，资源包元数据使用顶层 `min_format` 和 `max_format` 字段，而非旧版的 `supported_formats` 对象。Oraxen 会自动处理这一点。面向 1.21.9+ 的资源包使用新字段，面向 1.20.2 至 1.21.8 的资源包使用 `supported_formats`，而更旧的目标（如 1.20-1.20.1）仅使用 `pack_format`。
</Callout>

<Callout type="info">
**跨版本着色器叠加：** 当启用多版本资源包时，Oraxen 会为每个支持的格式组（1.20.2、1.21.4、1.21.6、26.x）生成着色器叠加层，作为发送给每个客户端的版本特定资源包的一部分。在 26.x 上，不再生成 `rendertype_text*.json` 着色器定义文件，因为引擎自动管理管线元数据，并且光照贴图采样使用 `sample_lightmap()` 而非 `texelFetch()`。
</Callout>

#### 保护

保护功能可防止玩家轻易盗取您的纹理。这不会使您的资源包变得更重，但如果启用了此功能，您**切勿**尝试提取生成的 zip，否则可能会损坏您的磁盘。

![1 EB = 1000000000 GB](/assets/size.png)

![您的操作系统应阻止提取以保护您的磁盘完整性](/assets/extraction.png)

### Import

`import` 部分控制 Oraxen 如何合并外部资源包和处理重复资源。

```yaml
Pack:
  import:
    merge_duplicate_fonts: true      # 合并重复的字体文件（例如 default.json）
    merge_duplicates: true            # 启用通用重复处理
    retain_custom_model_data: true   # 保留导入资源包中的 CustomModelData
    merge_item_base_models: false    # 合并基础模型 JSON（paper.json 等）
```

#### 导入设置说明

| 设置 | 默认值 | 描述 |
|---------|---------|-------------|
| `merge_duplicate_fonts` | `true` | 将重复的字体文件（最常见的是 `default.json`）合并为单个文件。原始文件从最终资源包中排除，优先使用合并版本。 |
| `merge_duplicates` | `true` | 启用 Oraxen 的重复资源处理程序。当多个资源包包含相同资源时，Oraxen 会智能地合并它们。 |
| `retain_custom_model_data` | `true` | 导入外部资源包时，保留其原始的 `custom_model_data` 值。**警告：** 如果它们使用相同的 CMD 值，可能会覆盖您的 Oraxen 物品。设为 `false` 让 Oraxen 自动重新分配值。 |
| `merge_item_base_models` | `false` | 尝试合并导入资源包中的基础模型 JSON 文件（例如 `paper.json`、`diamond_sword.json`）。不如字体合并可靠，但对复杂的资源包组合有用。不论此设置如何，CustomModelData 冲突仍可能发生。 |

#### 何时使用这些设置

**`retain_custom_model_data: true`** - 使用场景：
- 您需要导入的物品保持其精确的 CMD 值以与其他插件兼容
- 您正在导入一个需要特定 CMD 映射的第三方资源包

**`retain_custom_model_data: false`** - 使用场景：
- 您希望 Oraxen 自动处理所有 CMD 分配
- 您遇到导入物品和 Oraxen 物品之间的 CMD 冲突

**`merge_item_base_models: true`** - 使用场景：
- 导入多个修改相同原版物品的资源包
- 您需要外部资源包的 predicate 与 Oraxen 的 predicate 共存

### Upload

```yaml
    enabled: true
    type: polymath #transfer.sh 或 polymath
    polymath:
      server: atlas.oraxen.com # 您也可以托管自己的 polymath 实例
```

Oraxen 集成了 Polymath（一个用 Python 编写的自定义网页服务器，专门设计为兼容）。您可以从[此处](https://github.com/Th0rgal/Polymath/)下载源代码并自行托管，或使用提供的实例（atlas）。您也可以集成[您自己的自定义托管服务](../developers/custom-hosting-service)。

### Dispatch

此部分允许您根据玩家的资源包状态轻松执行操作。

您可以发送消息（通过 KICK、聊天、操作栏或标题），并指定延迟和周期（如果您使用操作栏或标题的多个消息之间）。

#### 分发模式（1.212.0+）

```yaml
Pack:
  dispatch:
    send_pre_join: false  # 在配置阶段发送资源包（仅 Paper 1.21.7+）
    send_on_join: true    # 在玩家加入后发送资源包（默认行为）
```

| 设置 | 默认值 | 描述 |
|---------|---------|-------------|
| `send_on_join` | `true` | 在玩家完全加入服务器后发送资源包。这是标准行为，适用于所有服务器版本。 |
| `send_pre_join` | `false` | 在配置阶段发送资源包，在玩家看到世界之前。需要 **Paper 1.21.7+**。当启用且受支持时，优先于 `send_on_join`。 |

<Callout type="info">
`send_pre_join` 使用 Paper 在 1.21.7 中引入的 `PlayerConfigurationConnection` API。在不支持此 API 的服务器上，Oraxen 会自动回退到 `send_on_join`，无论您的设置如何。
</Callout>

<Callout type="warning">
`send_pre_join` 是实验性的，默认禁用。仅在您希望玩家在看到世界中的任何方块或物品之前收到资源包时才启用它。
</Callout>

#### 资源包分层（1.20.3+）

```yaml
Pack:
  dispatch:
    layer: ""  # 设置为任意值（例如 "bungee"）进行分层，或留空进行替换
```

`layer` 选项控制 Minecraft 1.20.3+ 服务器上的资源包分层：

**空字符串 `""`（默认）：** 传统行为
- 使用 `setResourcePack()`，它**替换**任何现有的资源包
- 最适合独立服务器
- 玩家只能看到 Oraxen 的资源包

**非空值（例如 `"bungee"`、`"proxy"`、`"layer"`）：** 分层模式
- 使用 `addResourcePack()`，它**叠加**资源包
- 保留 BungeeCord/Velocity 代理分发的资源包
- 旧的 Oraxen 资源包会在添加新资源包之前自动移除
- 多个资源包可以共存
- 需要 Minecraft 1.20.3+ 客户端

**使用分层模式的场景：**
- 在具有代理分发资源包的 BungeeCord/Velocity 网络上运行
- 需要 Oraxen 与其他发送资源包的插件共存
- 希望玩家同时使用多个资源包

**使用替换模式（空字符串）的场景：**
- 运行独立服务器
- Oraxen 是唯一的资源包来源
- 需要与较旧客户端的最大兼容性

#### 加载期间的玩家保护

Oraxen 可以在玩家下载和加载资源包期间保护他们。这可以防止玩家在屏幕可能冻结或无法正常看到的情况下被杀死或移动到危险区域。

```yaml
Pack:
  dispatch:
    disable_movement_on_load: true  # 在资源包加载期间冻结玩家
    disable_damage_on_load: true    # 在资源包加载期间使玩家无敌
```

| 设置 | 默认值 | 描述 |
|---------|---------|-------------|
| `disable_movement_on_load` | `true` | 从玩家接受资源包到加载完成期间阻止玩家移动 |
| `disable_damage_on_load` | `true` | 在资源包加载期间防止玩家受到任何伤害 |

两种保护会在资源包成功加载、被拒绝或下载失败后自动移除。玩家断开连接时也会从受保护状态中移除。

#### 状态操作

Oraxen 允许您根据每个玩家客户端报告的资源包状态触发操作。

**可用状态：**

| 状态 | Minecraft 版本 | 描述 |
|--------|-------------------|-------------|
| `loaded` | 所有版本 | 资源包成功加载并应用 |
| `accepted` | 所有版本 | 玩家在资源包提示上点击了"是" |
| `denied` | 所有版本 | 玩家在资源包提示上点击了"否" |
| `failed_download` | 所有版本 | 下载失败（网络错误、超时等） |
| `downloaded` | 仅 1.20.3+ | 资源包已下载但尚未应用 |
| `failed_reload` | 仅 1.20.3+ | 重新加载资源包失败 |
| `invalid_url` | 仅 1.20.3+ | 资源包 URL 无效或不可达 |
| `discarded` | 仅 1.20.3+ | 资源包被客户端丢弃 |

```yaml
receive:
  enabled: true

  loaded:
    actions:
      message:
        enabled: true
        # KICK / CHAT / ACTION_BAR / TITLE
        type: ACTION_BAR
        # 第一条消息出现之前的延迟，单位为秒
        delay: 0
        # 仅当您发送多条 ACTION_BAR 或 TITLE 类型的消息时才需要周期
        period: -1
        # 点击和悬停元素仅在使用 CHAT 类型时可用
        messages:
          - "<green><bold>资源包已成功加载！"

      # 如果您需要发送命令
      commands:
        console: []
        player: []
        opped_player: []

  accepted:
    actions:
      message:
        enabled: true
        # KICK / CHAT / ACTION_BAR / TITLE
        type: TITLE
        # 第一条消息出现之前的延迟，单位为秒
        delay: 0
        # 仅当您发送多条 ACTION_BAR 或 TITLE 类型的消息时才需要周期
        period: 3
        # 点击和悬停元素仅在使用 CHAT 类型时可用
        messages:
          - "<green><bold>资源包已接受！"
          - "谢谢您"
      # 如果您需要发送命令
      commands:
        console: []
        player: []
        opped_player: []

  denied:
    actions:
      message:
        enabled: true
        # KICK / CHAT / ACTION_BAR / TITLE
        type: CHAT
        # 第一条消息出现之前的延迟，单位为秒
        delay: 0
        # 您可以在此处放任何值，因为这是 CHAT 消息
        period: -1
        # 点击和悬停元素仅在使用 CHAT 类型时可用
        messages:
          - "<red>您拒绝了资源包，但您需要它才能看到新物品。请 </red><click:run_command:/oraxen pack><hover:show_text:\"<green>显示更多信息\"><green><bold>点击此处</bold></hover></click> <red>或输入 <bold>/o pack"
      # 如果您需要发送命令
      commands:
        console: []
        player: []
        opped_player: []

  failed_download:
    actions:
      message:
        enabled: true
        # KICK / CHAT / ACTION_BAR / TITLE
        type: CHAT
        # 第一条消息出现之前的延迟，单位为秒
        delay: 0
        # 您可以在此处放任何值，因为这是 CHAT 消息
        period: -1
        # 点击和悬停元素仅在使用 CHAT 类型时可用
        messages:
          - "<red>您下载资源包失败，但您需要它才能看到新物品。请 </red><click:run_command:/oraxen pack getpack><hover:show_text:\"<red>/!\\ 从游戏内加载资源包可能会导致卡顿\"><red><bold>点击此处</bold></hover></click> <red>重试或输入 <bold>/o pack</bold> 并从互联网下载"
      # 如果您需要发送命令
      commands:
        console: []
        player: []
        opped_player: []

  # Minecraft 1.20.3+ 额外状态
  # 这些状态仅在 Minecraft 1.20.3 及以上版本可用

  downloaded:  # 仅 1.20.3+ - 资源包已下载但尚未应用
    actions:
      commands:
        console: []
        player: []
        opped_player: []

  failed_reload:  # 仅 1.20.3+ - 资源包重新加载失败（更换资源包时）
    actions:
      commands:
        console: []
        player: []
        opped_player: []

  invalid_url:  # 仅 1.20.3+ - 资源包 URL 无效或不可达
    actions:
      commands:
        console: []
        player: []
        opped_player: []

  discarded:  # 仅 1.20.3+ - 资源包被客户端丢弃
    actions:
      commands:
        console: []
        player: []
        opped_player: []
```

## ConfigTools

```yaml
ConfigsTools:
  enable_configs_updater: true
  disable_automatic_model_data: false
  disable_automatic_glyph_code: false
  error_item:
    material: PODZOL
    excludeFromInventory: false # 设为 true 如果您不想在背包中显示它
    injectID: false
```

| 设置 | 描述 |
|---------|-------------|
| `enable_configs_updater` | 当添加新选项时自动更新配置文件 |
| `disable_automatic_model_data` | 阻止 Oraxen 自动分配 `custom_model_data` 值 |
| `disable_automatic_glyph_code` | 阻止 Oraxen 自动为字形分配 Unicode 字符 |

import { Callout } from 'nextra/components'

<Callout type="warning">
**网格字形警告：** 如果您启用 `disable_automatic_glyph_code`，您**必须**为任何[基于网格的字形](/creating-content/glyphs-hud#grid-based-glyphs)手动定义 `chars` 列表。没有手动字符分配，网格字形将在每次重启服务器时获得新的 Unicode 字符，从而破坏已保存的引用。单个字符字形将重用其现有的 `char` 值，但网格字形没有这样的回退。
</Callout>

## CustomArmor

```yaml
CustomArmor:
  disable_leather_repair: true
```

此选项允许您禁用皮革修复自定义盔甲。
这意味着修复自定义盔甲套装的唯一方式是使用该盔甲套装的其他副本。

## Misc

### hide_scoreboard_numbers

此选项允许您隐藏红色的记分板数字。

```yaml
  hide_scoreboard_numbers: true
```

<Callout type="warning">
在 Minecraft 26.x+ 上，基于着色器的记分板数字隐藏**不受支持**，因为渲染引擎现在自动管理管线元数据。在 Paper 1.20.3+ 上，请改用数据包适配器（ProtocolLib 或 PacketEvents）——如果可用，Oraxen 会自动执行此操作。
</Callout>

**之前：**
![](https://media.discordapp.net/attachments/758785982005903431/1043486669371887616/image.png)
**之后：**
![](https://media.discordapp.net/attachments/758785982005903431/1043486615655432193/image.png)

### hide_scoreboard_background

此选项允许您隐藏记分板背景。

```yaml
  hide_scoreboard_background: true
```

### hide_tablist_background

```yaml
  hide_tablist_background: true
```

此选项允许您隐藏玩家列表背景（仅 1.21+）。

### reset_recipes

```yaml
reset_recipes: true
```

此选项可能与其他配方插件产生 bug。如果您在重载 Oraxen 时发现与配方插件的 bug，可以禁用此选项。如果这样做，您将需要重启服务器以刷新 Oraxen 配方。

## Glyphs

```yaml
Glyphs:
  glyph_handler: vanilla # 或 nms - 推荐 vanilla
  emoji_list_permission_only: false # 按权限过滤表情列表
  unicode_completions: true # 为 Unicode 字符启用 Tab 补全
  chat_hover_text: true # 在聊天中悬停时显示字形名称
```

| 设置 | 默认值 | 描述 |
|---------|---------|-------------|
| `glyph_handler` | `vanilla` | 字形渲染处理程序（推荐 `vanilla`，可用 `nms`） |
| `emoji_list_permission_only` | `false` | 控制 `/oraxen emojis` 输出（见下文） |
| `unicode_completions` | `true` | 在聊天中启用 Unicode 字符的 Tab 补全 |
| `chat_hover_text` | `true` | 在聊天中悬停表情时显示字形名称 |

### 表情列表权限

`emoji_list_permission_only` 设置控制 `/oraxen emojis` 命令如何显示表情：

- **`false`（默认）**：显示所有表情。悬停文本用颜色指示权限状态：
  - <span style={{color: 'green'}}>绿色</span> = 玩家有权限
  - <span style={{color: 'red'}}>红色</span> = 无权限
- **`true`**：仅显示玩家有权限使用的表情

## Chat

```yaml
Chat:
  chat_handler: vanilla # 或 nms
```

## WorldEdit

启用/禁用自定义方块的 WorldEdit 集成。

```yaml
WorldEdit:
  noteblock_mechanic: true
  stringblock_mechanic: true
  furniture_mechanic: true
```

## ItemUpdater

控制 Oraxen 在配置更改时如何更新现有物品。

```yaml
ItemUpdater:
  update_items: true # 自动更新背包中的物品
  update_items_on_reload: true # 在 /o reload 时更新
  override_renamed_items: false # 即使玩家重命名了物品也更新
  override_item_lore: true # 覆盖描述更改
```

## FurnitureUpdater

控制 Oraxen 如何更新已放置的家具。

```yaml
FurnitureUpdater:
  update_furniture: true
  update_on_reload: true
  update_on_load: true
  experimental_furniture_type_update: false # 在配置更改时更新家具实体类型
  experimental_fix_broken_furniture: false # 尝试修复损坏的家具
```

## CustomBlocks

```yaml
CustomBlocks:
  block_correction: true # 自动修正方块状态
  use_legacy_noteblocks: false # 使用旧的音符盒系统（不推荐）
```

## Oraxen 背包

```yaml
oraxen_inventory:
  main_menu_title: "<shift:-18><glyph:menu_items><shift:-193>"
  menu_rows: 6
  menu_layout:
    armors:
      slot: 1
      icon: emerald_chestplate
      title: "<main_menu_title><#362753><glyph:menu_items_overlay:colorable>"
    blocks:
      slot: 2
      icon: orax_ore
      title: "<main_menu_title><#EDCDEB><glyph:menu_items_overlay:colorable>"
    furniture:
      slot: 3
      icon: chair
      title: "<main_menu_title><#F2F2F2><glyph:menu_items_overlay:colorable>"
    flowers:
      slot: 4
      icon: dailily
      title: "<main_menu_title><#bf332c><glyph:menu_items_overlay:colorable>"
    hats:
      slot: 5
      icon: crown
      title: "<main_menu_title><#81B125><glyph:menu_items_overlay:colorable>"
    items:
      slot: 6
      icon: ruby
      title: "<main_menu_title><#DA2E45><glyph:menu_items_overlay:colorable>"
    mystical:
      slot: 7
      icon: legendary_hammer
      title: "<main_menu_title><#9AB2E4><glyph:menu_items_overlay:colorable>"
    plants:
      slot: 8
      icon: weed_leaf
      title: "<main_menu_title><#44C886><glyph:menu_items_overlay:colorable>"
    skins:
      slot: 9
      icon: wood_sword
      title: "<main_menu_title><#C48E40><glyph:menu_items_overlay:colorable>"
    tools:
      slot: 10
      icon: iron_serpe
      title: "<main_menu_title><#FFFFFF><glyph:menu_items_overlay:colorable>"
    weapons:
      slot: 11
      icon: energy_crystal_sword
      title: "<main_menu_title><#2FB6FF><glyph:menu_items_overlay:colorable>"
```

这允许您为 Oraxen 背包的每个分类配置一个图标。您可以使用 Oraxen ID 或 Minecraft 材料。