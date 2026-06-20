---
description: 插件命令的简单说明
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966827022758330398/unknown.png
coverY: 0
---

# 命令

## 一般信息

所有 Oraxen 命令都以相同的标签开头。这个标签 `oraxen` 有几个别名，所以如果您不想每次都输入 `/oraxen`，也可以使用 `/oxn` 甚至 `/o`。

在本教程中，我们将使用 `/o`，因为它是最短的，但如果此命令已被另一个插件使用，或者您因任何原因无法使用它，只需将以 `/o` 开头的命令标签替换为 `/oxn` 或 `/oraxen`。

## 获取物品

### 用于测试

这种方法的主要好处是它允许您同时查看所有物品，因此更加高效（您只需点击一个物品即可使其出现在您的背包中）。但您不能使用它来自动向其他玩家给予物品（例如从商店）。

#### 用法：`/oraxen inventory`

#### 权限：

```yaml
oraxen.command.inventory.view # 允许查看物品可视化界面
oraxen.command.inventory.give# 允许从物品可视化界面获取物品
oraxen.command.inventory.* # 授予您上述两个权限
```

### 用于给予物品

此命令主要用于您想向其他玩家给予物品或需要自动化给予时。如果此命令的目标玩家背包已满，物品堆会掉落在地上。

#### 用法：

```yaml
/oraxen give <player> <item> <amount> # 给予玩家指定数量的物品
```

#### 权限：

```yaml
oraxen.command.give # 允许您使用 /o give
```

## 修复

### 仅修复一个物品

此命令可用于修复您主手中的物品。您可以配置插件仅修复使用 Oraxen 自定义耐久的物品，或同时修复原版耐久的物品。

#### 用法：

```yaml
/oraxen repair hand # 修复您手持的物品
```

#### 权限：

```yaml
oraxen.command.repair # 允许使用 /o repair 命令
```

### 修复背包中的所有物品

此命令可用于修复背包（或盔甲槽）中的每一个物品。您可以配置插件仅修复使用 Oraxen 自定义耐久的物品，或同时修复原版耐久的物品。

#### 用法：

```yaml
/oraxen repair all # 修复您背包中的所有物品
```

#### 权限：

```yaml
oraxen.command.repair # 因此您也能使用 /o repair hand
oraxen.command.repair.all # 允许使用 /o repair all 命令
```

## 管理配方

此命令允许您使用配方构建器直接在游戏中向配置添加新配方。有关如何使用它的更多信息，请参见[配方](recipes)。

![配方展示，使用 /o recipes show all](/assets/recipe_showcase.png)

#### 用法：

```yaml
/oraxen recipes builder <builder> # 创建类型为 <builder> 的配方构建器并打开它
/oraxen recipes save <name> # 以名称 <name> 保存您的配方
/oraxen recipes show all # 显示已加载的配方
/oraxen recipes show <recipe> # 显示一个配方
```

#### 权限：

```yaml
oraxen.command.recipes # 允许您通过 /o recipes 创建新配方
```

## 表情符号

此命令显示可用的表情符号/字形列表。输出取决于 `emoji_list_permission_only` 设置（参见[字形设置](/plugin-setup/plugin-settings#glyphs)）。

#### 用法：

```yaml
/oraxen emojis # 显示可用的表情符号及其权限状态
```

#### 权限：

```yaml
oraxen.command.emojis # 允许您使用 /o emojis
```

## 资源包

此命令允许您与 Oraxen 资源包进行交互：发送配置的消息以从互联网下载，或直接通过游戏加载。

#### 用法：

```yaml
/oraxen pack send <player> # 直接通过游戏将资源包发送给 <player>
/oraxen pack msg <player> # 将配置的消息发送给 <player>
```

#### 权限：

```yaml
oraxen.command.pack # 允许您使用 /o pack
```

## 物品信息

此命令允许您打印物品信息和自定义模型数据 ID。

#### 用法：

```yaml
/oraxen iteminfo <itemname> # 打印请求的物品信息
```

#### 权限：

```yaml
oraxen.command.iteminfo # 允许您使用 /o iteminfo
```

## 重新加载

此命令允许您快速且无错误地重新加载 Oraxen 配置（您不能使用 plugman 重新加载 Oraxen）。但是，需要注意的是，目前无法重新加载使用 Oraxen 创建的自定义合成配方。

#### 用法

```yaml
/oraxen reload all # 重新加载物品配置、重新加载配方配置、重新生成资源包并上传
/oraxen reload items # 重新加载物品配置
/oraxen reload pack # 重新生成资源包并上传
/oraxen reload recipes # 重新加载配方配置
```

#### 权限：

```yaml
oraxen.command.reload # 允许您使用 /o reload
```

## 调试

我希望您永远不需要使用它，但如果您遇到 Oraxen 的问题，我可能会要求您执行此命令以获取有关您安装的更多信息。这将在控制台中显示高级日志。

#### 用法：

这将取决于具体情况，并且可能随着 Oraxen 的更新而变化，我会为您详细解释。

#### 权限：

```yaml
oraxen.command.debug # 允许您使用 /o debug
```