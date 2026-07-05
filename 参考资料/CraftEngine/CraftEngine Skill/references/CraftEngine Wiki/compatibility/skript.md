# 🔮 Skript

:::tip
对于高级 Skript 用户，请使用反射来实现更高级的功能。如果您在使用 CraftEngine 提供的 Skript 功能时遇到问题，请及时向我们[反馈](https://github.com/Xiao-MoMi/craft-engine/issues/new)。如果您想要请求新的 Skript 功能并且您了解 Java，请考虑通过拉取请求贡献您的代码！
:::

:::warning
请注意，如果您在服务器加载插件时遇到错误，这可能是因为 Skript 脚本在 CraftEngine 之前加载。目前无法修复此问题，只能通过重新加载来解决。

你需要安装 [Skript](https://modrinth.com/plugin/skript) 2.15.0 或更高版本。
:::

## 事件

### 放置或破坏 CraftEngine 方块事件

**类型:** Event  
**描述:** 当放置和破坏 CraftEngine 方块时触发

**语法格式:**
```
[on] (break[ing]|1¦min(e|ing)) of (custom|ce|craft-engine) block[s] [[of] %-unsafeblockstatematchers%]
[on] (plac(e|ing)|build[ing]) of (custom|ce|craft-engine) block[s] [[of] %-unsafeblockstatematchers%]
```

**事件字段:**
- event-block - 事件方块
- event-location - 事件位置
- event-player - 事件玩家
- event-world - 事件世界

**示例:**
```
on break of ce block default:palm_log[axis=y]:
  send "你破坏了自定义方块！" to event-player
```

---

### 放置或破坏 CraftEngine 家具事件

**类型:** Event  
**描述:** 当放置和破坏 CraftEngine 家具时触发

**语法格式:**
```
[on] (break[ing]) of [(custom|ce|craft-engine)] furniture[s] [[of] %-strings%]
[on] (plac(e|ing)|build[ing]) of [(custom|ce|craft-engine)] furniture[s] [[of] %-strings%]
```

**事件字段:**
- event-entity - 事件实体
- event-location - 事件位置
- event-player - 事件玩家
- event-world - 事件世界

**示例:**
```
on place of custom furniture default:chinese_lantern:
  send "你放置了自定义家具！" to event-player
```

---

### 点击 CraftEngine 方块或家具事件

**类型:** Event  
**描述:** 当点击 CraftEngine 方块和家具时触发

**语法格式:**
```
[on] [(right|left)(| |-)][mouse(| |-)]click[ing] of (ce|craft-engine) [on %-unsafeblockstatematchers/strings%] [(with|using|holding) %-itemtype%]
[on] [(right|left)(| |-)][mouse(| |-)]click[ing] of (ce|craft-engine) (with|using|holding) %itemtype% on %unsafeblockstatematchers/strings%
```

**事件字段:**
- event-block - 事件方块
- event-entity - 事件实体
- event-location - 事件位置
- event-player - 事件玩家
- event-world - 事件世界

**示例:**
```
on right-click of craft-engine on default:chinese_lantern:
   send "你点击了自定义方块！" to event-player
```

---

### CraftEngine 重新加载事件

**类型:** Event  
**描述:** 当 CraftEngine 加载时触发

**语法格式:**
```
[on] (ce|craft(engine|-engine)) [first] (load[ed]|reload)
```

**示例:**
```
on craft-engine loaded:
  send "嘿，CraftEngine 已加载，现在可以获取 CE 物品了！" to console
```
```
on craft-engine first loaded:
  send "嘿，CraftEngine 已在服务器启用时加载，脚本现在将初始化一些内容！" to console
```

---

## 条件

### CraftEngine 是否已加载

**类型:** Condition  
**描述:** 检查 CraftEngine 是否已加载

**语法格式:**
```
(ce|craft[-]engine) (has been|is) load[ed]
(ce|craft[-]engine) (has not been|is not) load[ed] [yet]
(ce|craft[-]engine) (hasn't been|isn't) load[ed] [yet]
```

**示例:**
```
on script load:
  stop if craft-engine has not been loaded yet
  send "脚本初始化一些内容！" to console
```

---

### 是自定义物品

**类型:** Condition  
**描述:** 检查物品是否为来自 CraftEngine 的自定义物品

**语法格式:**
```
%itemstack/itemtype/slot% (is [a[n]]|are) (custom|ce|craft-engine) item[s]
%itemstack/itemtype/slot% (isn't|is not|aren't|are not) [a[n]] (custom|ce|craft-engine) item[s]
```

**示例:**
```
on mine:
  if event-player's tool is a custom item:
    send "你正在使用自定义物品挖掘" to event-player
```

---

### 是自定义方块

**类型:** Condition  
**描述:** 检查方块是否为来自 CraftEngine 的自定义方块

**语法格式:**
```
%blocks% (is|are) [a[n]] (custom|ce|craft-engine) block[s]
%blocks% (is|are) (n't| not) [a[n]] (custom|ce|craft-engine) block[s]
```

**示例:**
```
on mine:
  if event-block is custom block:
    send "你破坏了一个自定义方块" to event-player
```

---

### 是自定义家具

**类型:** Condition  
**描述:** 检查实体是否为来自 CraftEngine 的自定义家具

**语法格式:**
```
%entities% (is|are) [a[n]] [(custom|ce|craft-engine)] furniture[s]
%entities% (is|are) (n't| not) [a[n]] [(custom|ce|craft-engine)] furniture[s]
```

**示例:**
```
on click:
  set {_entity} to nearest pig
  if {_entity} is a ce furniture:
    send "我在做什么？" to event-player
```

---

## 表达式

### 自定义物品

**类型:** Expression  
**描述:** 通过命名空间ID获取自定义物品

**语法格式:**
```
[(the|a)] (custom|ce|craft-engine) item [with [namespace] id] %strings%
```

**示例:**
```
set {_item} to custom item with namespace id "default:topaz"
```

---

### 自定义物品命名空间ID

**类型:** Expression  
**描述:** 获取自定义物品的命名空间ID

**语法格式:**
```
(custom|ce|craft-engine) item [namespace] id of %itemstack/itemtype/slot%
%itemstack/itemtype/slot%'[s] (custom|ce|craft-engine) item [namespace] id
```

**示例:**
```
set {_itemId} to craft-engine item id of player's tool
```

---

### 自定义方块命名空间ID

**类型:** Expression  
**描述:** 获取自定义方块的命名空间ID

**语法格式:**
```
%blocks/blockdata/customblockstates%'s (custom|ce|craft-engine) block [namespace] id
(custom|ce|craft-engine) block [namespace] id of %blocks/blockdata/customblockstates%
```

**示例:**
```
on mine:
  if event-block's ce block id is "default:chinese_lantern":
    send "破坏了一个中式灯笼方块" to event-player
```

---

### 自定义方块状态

**类型:** Expression  
**描述:** 获取自定义方块的方块状态

**语法格式:**
```
%blocks/blockdata/customblockstates%'s (custom|ce|craft-engine) block[ ]state
(custom|ce|craft-engine) block[ ]state of %blocks/blockdata/customblockstates%
```

**示例:**
```
on mine:
  send event-block's ce block state to event-player
```

---

### 家具命名空间ID

**类型:** Expression  
**描述:** 从实体获取家具的命名空间ID

**语法格式:**
```
%entities%'s [(custom|ce|craft-engine)] furniture [namespace] id
```

**示例:**
```
set {_furnitureId} to {_entity}'s craft-engine furniture id
```

---

## 效果

### 放置自定义方块

**类型:** Effect  
**描述:** 放置一个自定义方块

**语法格式:**
```
place (custom|ce|craft-engine) block %customblockstates% [at] [%directions% %locations%]
```

**示例:**
```
place custom block default:palm_log[axis=x] at location of the player
```

---

### 放置家具

**类型:** Effect  
**描述:** 放置一个家具

**语法格式:**
```
place [(custom|ce|craft-engine)] furniture[s] %strings% [at] [%directions% %locations%]
```

**示例:**
```
place furniture "default:bench" at location of player
```

---

### 移除家具

**类型:** Effect  
**描述:** 移除一个家具

**语法格式:**
```
remove [(custom|ce|craft-engine)] furniture %entities%
```

**示例:**
```
remove craft-engine furniture target entity
```
