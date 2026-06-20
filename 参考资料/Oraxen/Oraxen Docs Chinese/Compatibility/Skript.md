---
description: Skript 集成允许你在 Skript 脚本中使用 Oraxen 物品、方块和家具
---

import { Callout, Tabs, Tab, Steps } from 'nextra/components'

# Skript 集成

Oraxen 包含内置的 Skript 兼容性，当服务器上存在 [Skript](https://github.com/SkriptLang/Skript) 时会自动加载。这允许你直接在脚本中使用 Oraxen 物品、自定义方块和家具。

<Callout type="info">
  建议使用 Skript 2.9+ 以获得完整的兼容性。
</Callout>

## 入门

无需配置！只需在服务器上同时安装 Oraxen 和 Skript。Oraxen 将自动检测 Skript 并注册所有语法元素。

加载时你将在控制台中看到此消息：
```
[Oraxen] Skript compatibility enabled - Oraxen syntax registered
```

## 可用语法

### 表达式

#### 获取 Oraxen 物品

从 Oraxen 物品 ID 获取 ItemStack。

```
oraxen item %string%
oraxen item from id %string%
```

**示例：**
```vb
give player oraxen item "ruby_sword"
set {_item} to oraxen item "emerald_pickaxe"
drop oraxen item "custom_helmet" at player's location
```

#### 获取 Oraxen ID

从 ItemStack、方块、实体或位置获取 Oraxen ID。

```
oraxen id of %itemstack/block/entity/location%
%itemstack/block/entity/location%'s oraxen id
```

**示例：**
```vb
set {_id} to oraxen id of player's tool
broadcast "方块 ID：%oraxen id of clicked block%"
if oraxen id of target entity is "treasure_chest":
    # 执行某些操作
```

#### 获取 Oraxen 方块

获取位置或方块上的 Oraxen 方块 ID。

```
oraxen block at %location/block%
%location/block%'s oraxen block
```

**示例：**
```vb
set {_blockId} to oraxen block at player's location
if oraxen block at clicked block exists:
    broadcast "这是一个 Oraxen 方块！"
```

#### 获取 Oraxen 家具

从位置、方块或实体获取 Oraxen 家具 ID。

```
oraxen furniture at %location/block/entity%
%location/block/entity%'s oraxen furniture
```

**示例：**
```vb
set {_furnitureId} to oraxen furniture at target entity
if oraxen furniture at clicked entity is "wooden_chair":
    make player sit
```

---

### 条件

#### 是否为 Oraxen 物品

检查一个物品是否为 Oraxen 物品。

```
%itemstack% is [an] oraxen item
%itemstack% is oraxen item %string%
%itemstack% is not [an] oraxen item
```

**示例：**
```vb
if player's tool is an oraxen item:
    broadcast "你正手持一个自定义物品！"

if player's tool is oraxen item "ruby_sword":
    broadcast "你拥有红宝石之剑！"
```

#### 是否为 Oraxen 方块

检查一个方块是否为 Oraxen 自定义方块。

```
%block/location% is [an] oraxen block
%block/location% is oraxen block %string%
%block/location% is not [an] oraxen block
```

**示例：**
```vb
if clicked block is an oraxen block:
    cancel event

if block at player's location is oraxen block "ruby_ore":
    broadcast "你发现了红宝石矿石！"
```

#### 是否为 Oraxen 家具

检查一个实体、方块或位置是否为 Oraxen 家具。

```
%entity/block/location% is [an] oraxen furniture
%entity/block/location% is oraxen furniture %string%
%entity/block/location% is not [an] oraxen furniture
```

**示例：**
```vb
if target entity is oraxen furniture:
    broadcast "你正在看一件家具！"

if clicked entity is oraxen furniture "wooden_chair":
    # 处理椅子交互
```

---

### 事件

所有事件都支持使用 `of "item_id"` 过滤特定的 Oraxen 物品 ID。

#### Oraxen 方块破坏事件

当玩家破坏 Oraxen 自定义方块（NoteBlock 或 StringBlock）时调用。

```
on oraxen block break [of %string%]
```

**事件值：** `event-player`、`event-block`、`event-string`（Oraxen ID）

**示例：**
```vb
on oraxen block break:
    broadcast "%player% 破坏了一个 Oraxen 方块：%event-string%"

on oraxen block break of "ruby_ore":
    cancel event
    send "你需要一把特殊的镐子来开采这个！" to player
```

#### Oraxen 方块放置事件

当玩家放置 Oraxen 自定义方块时调用。

```
on oraxen block place [of %string%]
```

**事件值：** `event-player`、`event-block`、`event-item`、`event-string`

**示例：**
```vb
on oraxen block place:
    broadcast "%player% 放置了一个 Oraxen 方块！"

on oraxen block place of "tnt_block":
    cancel event
    send "TNT 方块已被禁用！" to player
```

#### Oraxen 方块交互事件

当玩家与 Oraxen 自定义方块交互时调用。

```
on oraxen block interact [of %string%]
```

**事件值：** `event-player`、`event-block`、`event-item`、`event-string`

**示例：**
```vb
on oraxen block interact of "magic_chest":
    open virtual chest inventory to player
```

#### Oraxen 家具破坏事件

当玩家破坏 Oraxen 家具时调用。

```
on oraxen furniture break [of %string%]
```

**事件值：** `event-player`、`event-block`、`event-entity`、`event-string`

**示例：**
```vb
on oraxen furniture break:
    broadcast "%player% 破坏了家具：%event-string%"

on oraxen furniture break of "expensive_chair":
    cancel event
    send "你不能破坏这个！" to player
```

#### Oraxen 家具放置事件

当玩家放置 Oraxen 家具时调用。

```
on oraxen furniture place [of %string%]
```

**事件值：** `event-player`、`event-block`、`event-entity`、`event-item`、`event-string`

**示例：**
```vb
on oraxen furniture place of "lamp":
    broadcast "一盏灯被放置了！"
```

#### Oraxen 家具交互事件

当玩家与 Oraxen 家具交互时调用。

```
on oraxen furniture interact [of %string%]
```

**事件值：** `event-player`、`event-block`、`event-entity`、`event-item`、`event-string`

**示例：**
```vb
on oraxen furniture interact:
    broadcast "%player% 与家具进行了交互！"

on oraxen furniture interact of "treasure_chest":
    give player diamond
    send "你找到了宝藏！" to player
```

---

### 效果

#### 放置 Oraxen 方块

在指定位置放置一个 Oraxen 自定义方块。

```
place oraxen block %string% at %locations%
set oraxen block at %locations% to %string%
```

**示例：**
```vb
place oraxen block "ruby_ore" at player's location
place oraxen block "custom_stone" at {_locations::*}
```

#### 放置 Oraxen 家具

在指定位置放置 Oraxen 家具。

```
place oraxen furniture %string% at %locations%
spawn oraxen furniture %string% at %locations%
```

**示例：**
```vb
place oraxen furniture "wooden_chair" at player's location
spawn oraxen furniture "lamp" at {_location}
```

#### 移除 Oraxen 方块

移除位置上的 Oraxen 方块（不掉落物品）。

```
remove oraxen block at %locations/blocks%
delete oraxen block at %locations/blocks%
```

**示例：**
```vb
remove oraxen block at player's location
remove oraxen block at clicked block
```

#### 移除 Oraxen 家具

移除位置或实体上的 Oraxen 家具（不掉落物品）。

```
remove oraxen furniture at %locations/entities%
delete oraxen furniture at %locations/entities%
```

**示例：**
```vb
remove oraxen furniture at target entity
remove oraxen furniture at player's location
```

---

## 完整示例脚本

以下是一个完整的示例脚本，演示了各种 Oraxen 功能：

```vb
# 用自定义物品欢迎玩家
on join:
    give player oraxen item "welcome_gift"
    send "&a欢迎！你收到了一份自定义礼物！"

# 自定义法杖效果
on right click:
    if player's tool is oraxen item "magic_wand":
        strike lightning at target block
        send "&e噼啪！" to player

# 保护特殊方块
on oraxen block break of "admin_block":
    if player does not have permission "oraxen.admin":
        cancel event
        send "&c你没有权限破坏这个！" to player

# 自定义家具商店
on oraxen furniture interact of "shop_counter":
    open virtual chest inventory with 3 rows named "&6商店" to player
    # 添加商店物品...

# 放置特殊物品时生成家具
on place of diamond block:
    if player's tool is oraxen item "furniture_spawner":
        cancel event
        place oraxen furniture "diamond_statue" at event-block's location
        remove 1 of player's tool from player

# 自定义矿石开采
on oraxen block break of "ruby_ore":
    if player's tool is oraxen item "ruby_pickaxe":
        give player oraxen item "ruby" with amount 3
    else:
        cancel event
        send "&c你需要一把红宝石镐来开采这个！" to player

# 放置家具的命令
command /placefurniture <text>:
    permission: oraxen.placefurniture
    trigger:
        place oraxen furniture arg-1 at player's target block
        send "&a已放置 %arg-1%！" to player
```

## 故障排除

<Callout type="warning">
  如果 Skript 语法不生效，请确保：
  - Skript 已正确安装并启用
  - 你在控制台中看到了 "Skript compatibility enabled" 消息
  - 你正在使用 Skript 2.9 或更新版本
</Callout>

### 常见问题

**语法未被识别：**
- 使用 `/skript reload all` 重新加载 Skript
- 检查控制台中的解析错误
- 验证 Oraxen 是否加载成功

**物品 ID 未找到：**
- 确保 Oraxen 物品在你的配置中存在
- 检查物品 ID 是否有拼写错误
- 物品 ID 区分大小写

**事件未触发：**
- 验证特定事件是否存在（并非所有原版事件都会触发 Oraxen 事件）
- 检查方块/家具是否确实来自 Oraxen
