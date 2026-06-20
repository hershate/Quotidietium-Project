---
description: >-
  当玩家点击方块或家具时运行命令、播放声音或发送消息。
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966825489098489856/unknown.png
coverY: 0
---

# ClickAction 机制

## 说明

`clickAction` 机制允许你在玩家点击家具或方块时运行命令、播放声音或发送消息。

### 配置

要开始使用，首先创建一个基础的[方块](/creating-content/blocks/noteblock)或[家具](/creating-content/furniture)。

接下来，在 mechanics 部分下，你可以将默认的 clickAction 机制添加到任何音符盒机制、家具机制或绊线钩方块机制物品下。

```yaml
Mechanics:      
  noteblock/furniture/stringblock:
    clickActions:
      - conditions:
          - '#player.hasPermission("test.permission")'
        actions:
          - '[console] say <player> hello <player>!'
```

通过此设置，玩家只有在拥有 `test.permission` 权限时才会触发控制台命令 `say hello <player>` 动作。

如果你不使用条件，需要在其所在位置放置括号：

```yaml
Mechanics:
  noteblock/furniture/stringblock:
    clickActions:
      - conditions: []
        actions:
          - '[console] say <player> hello <player>!'
```


此机制不支持没有碰撞箱的家具。



### 条件

条件是高度可配置的。你可以使用 Player 或 Server 的任何 "get" 方法。有关所有方法，请参见 Spigot Javadocs。




提示！按 "CTRL + F" 搜索 "get" 来查找有效的方法。

此外，Spring 文档是理解如何使用条件表达式的好资源。



#### 条件示例

`#server.getOnlinePlayers().size() > 10`

`#server.getAllowEnd()`

`#server.getDefaultGameMode()`

`#player.world.name == 'world'`

`#player.hasPermission("test.permission")`

`#player.gamemode.name() == 'ADVENTURE'`

### 动作

`[console] <command>`

`[player] <command>`

`[message] <message>`

`[actionbar] <message>`

`{source=SOURCE volume=VOLUME pitch=PITCH} [sound] <sound name>`

#### 动作示例

`[console] say hello`

`[player] say hello`

`[message] <blue>Hello!`

`[actionbar] <gray>Hello from the actionbar!`

`{source=AMBIENT volume=0.1 pitch=1} [sound] minecraft:block.shulker_box.close`