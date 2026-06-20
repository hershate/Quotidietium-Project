---
description: 如何自定义 Oraxen 品牌标识、插件消息和语言文件
---

# 品牌与自定义

了解如何自定义 Oraxen 的品牌标识、更改插件消息、更新前缀以及修改语言文件以匹配您服务器的风格。

## 更改插件前缀

插件前缀出现在聊天中所有 Oraxen 消息之前。要自定义它：

**位置:** `plugins/Oraxen/languages/<language>.yml`

对于英文，编辑 `plugins/Oraxen/languages/english.yml`：

```yaml
general:
  prefix: "<gradient:#9055FF:#13E2DA>Oraxen <gray>| "
```

### 示例

**简单的彩色前缀：**
```yaml
prefix: "<gold>[MyServer] "
```

**带自定义颜色的渐变：**
```yaml
prefix: "<gradient:#FF6B6B:#4ECDC4>MyServer <dark_gray>» "
```

**多色阶渐变：**
```yaml
prefix: "<gradient:#667eea:#764ba2:#f093fb>✦ MyPlugin <gray>| "
```

更改前缀后，使用 `/oraxen reload all` 重载。

## 自定义插件消息

所有插件消息存储在语言文件中。Oraxen 支持 9 种语言：

- `english.yml`（默认）
- `french.yml`
- `german.yml`
- `czech.yml`
- `spanish.yml`
- `korean.yml`
- `japanese.yml`
- `chinese-simplified.yml`（zh-CN）
- `chinese-traditional.yml`（zh-TW）
- `russian.yml`（ru-RU）
- `portuguese-brazil.yml`（pt-BR）

### 更改语言

在 `settings.yml` 中：

```yaml
Plugin:
  language: "english"  # 更改为: french, german, czech, korean, jpn_JP, ru-RU, zh-CN, zh-TW, pt-BR
```

### 编辑消息

**位置:** `plugins/Oraxen/languages/<language>.yml`

`english.yml` 中的自定义示例：

```yaml
general:
  prefix: "<gradient:#9055FF:#13E2DA>Oraxen <gray>| "
  no_permission: "<prefix><#fa4943>您缺少权限 <b><permission></b> 来执行此操作！"
  reload: "<prefix><#55ffa4>成功重载"

  # 自定义为您服务器的风格：
  reload: "<prefix><green>✓ 配置已重载！"
  no_permission: "<prefix><red>⚠ 缺少权限: <yellow><permission>"
```

### 消息格式化

Oraxen 使用 [MiniMessage](https://docs.advntr.dev/minimessage/format.html) 格式化：

**颜色：**
- `<red>`、`<green>`、`<blue>` 等。
- `<#HEX>` 用于自定义颜色：`<#FF5733>`
- `<gradient:#start:#end>文本</gradient>`

**格式：**
- `<bold>`、`<italic>`、`<underlined>`
- `<strikethrough>`、`<obfuscated>`

**占位符：**
- `<prefix>` - 插件前缀
- `<permission>` - 所需权限
- `<player>` - 玩家名称
- `<item>` - 物品名称
- `<amount>` - 数量

示例：
```yaml
updated_items: "<prefix><gradient:#00FF00:#00AA00>✓ 为 <player> 更新了 <amount> 个物品！"
```

## 自定义欢迎消息

### 加入消息（文本）

玩家加入时发送的文本消息（与欢迎音效分开）：

**位置:** `settings.yml`

```yaml
Pack:
  dispatch:
    join_message:
      enabled: false  # 设为 true 启用
      delay: -1       # 延迟（刻）（-1 = 立即，20 = 1秒）
```

消息内容在 `languages/<language>.yml` 中定义：

```yaml
command:
  join: |-
    <dark_gray><st>                           </st><dark_gray>{<aqua><bold>资源包</bold><dark_gray>}<dark_gray><st>                        </st>
    <gray><bold>要看到新物品，您需要使用一个特殊的资源包（但别担心，这不会阻止您同时使用自己的资源包）。</bold>
    <dark_gray>»<gray> 要尝试直接从游戏中加载它，<click:run_command:"oraxen pack send @p"><hover:show_text:"<red>! 从游戏中加载资源包可能会导致卡顿"><red><bold>点击此处</bold></hover></click>
```

### 欢迎音效

**位置:** `settings.yml`

```yaml
Pack:
  receive:
    loaded:
      actions:
        sound:
          enabled: true           # 设为 false 禁用
          type: minecraft:welcome # 更改为您自定义的音效
          volume: 1.0
          pitch: 1.0
```

要使用自定义音效，您必须先在 `sound.yml` 中注册它。详情请参阅 [sound.yml 文档](./sound-yml)。

## 自定义资源包提示

当玩家加入时，他们会看到接受资源包的提示：

**位置:** `settings.yml`

```yaml
Pack:
  dispatch:
    prompt: "<#fa4943>接受资源包以获得完整的 <b><gradient:#9055FF:#13E2DA>Oraxen</b><#fa4943> 体验"
```

### 示例

**简单提示：**
```yaml
prompt: "<gold>请接受资源包以查看自定义物品！"
```

**品牌化提示：**
```yaml
prompt: "<gradient:#FF6B6B:#4ECDC4>MyServer <white>需要此资源包以获得完整体验！"
```

**带表情符号：**
```yaml
prompt: "✨ <yellow>接受我们的自定义资源包以获得 <gold><bold>超棒的物品</bold><yellow>！ ✨"
```

## 自定义资源包注释（水印）

在资源包 ZIP 文件中添加自定义水印：

**位置:** `settings.yml`

```yaml
Pack:
  generation:
    comment: "此纹理包的内容
      \n属于 Oraxen 插件的所有者，
      \n任何全部或部分使用
      \n必须遵守 Oraxen 的
      \n条款与条件。"
```

将其更改为您服务器的版权声明或品牌信息。

## 创建自定义语言文件

要创建自定义语言文件（例如，用于尚未支持的语言）：

1. 复制 `plugins/Oraxen/languages/english.yml` 为您想要的语言名称
2. 在保持相同结构的情况下翻译所有消息
3. 更新 `settings.yml`：

```yaml
Plugin:
  language: "custom"  # 您的新语言文件名称（不含 .yml）
```

## 常见自定义示例

### 极简/简洁风格

```yaml
general:
  prefix: "<dark_gray>[<aqua>O<dark_gray>] "
  reload: "<prefix><green>已重载。"
  no_permission: "<prefix><red>无权限。"
```

### 奢华/高级风格

```yaml
general:
  prefix: "<gradient:#FFD700:#FFA500>⚜ ORAXEN <gray>» "
  reload: "<prefix><gradient:#00FF00:#00AA00>✓ 已成功重载所有配置！"
  no_permission: "<prefix><gradient:#FF0000:#AA0000>⚠ 访问被拒绝 <dark_gray>| <gray>缺少: <yellow><permission>"
```

### 角色扮演/奇幻风格

```yaml
general:
  prefix: "<gradient:#8B4513:#D2691E>⚔ Oraxen Magic <gray>~ "
  reload: "<prefix><#90EE90>古老的卷轴已刷新！"
  no_permission: "<prefix><#FF6347>奥术之力拒绝您的访问！(<italic><permission></italic>)"
```

## 故障排除

### 消息没有颜色显示

确保在 `settings.yml` 中启用了 MiniMessage 格式化：

```yaml
Plugin:
  formatting:
    chat: true
```

### 前缀没有变化

1. 确保编辑了正确的语言文件（检查 settings.yml 中的 `Plugin.language`）
2. 使用 `/oraxen reload all` 应用更改
3. 验证您使用的是 MiniMessage 格式，而非旧版颜色代码（`&c`、`§c` 将不起作用）

### 自定义语言文件未加载

1. 确保文件名完全匹配（区分大小写）
2. 使用在线验证器检查 YAML 语法错误
3. 验证文件位于 `plugins/Oraxen/languages/`
4. 重启服务器（某些语言更改需要重启）

## 另请参阅

- [sound.yml 配置](./sound-yml) - 自定义音效
- [插件设置](../plugin-setup/plugin-settings) - 通用插件配置
- [MiniMessage 文档](https://docs.advntr.dev/minimessage/format.html) - 完整格式化指南