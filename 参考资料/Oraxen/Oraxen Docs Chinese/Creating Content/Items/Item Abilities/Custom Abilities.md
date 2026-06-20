---
description: >-
  这个机制允许你在无需编程的情况下实现极其可自定义的机制
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966825489098489856/unknown.png
coverY: 0
---

# 自定义机制

## 它是如何工作的？

此机制仅适用于物品，不适用于方块/家具。对于方块/家具，请查看 [clickAction 机制](/creating-content/items/abilities/clickaction)。这些机制让你可以创建由 3 个部分组成的小节：

* **事件**：此机制何时触发？例如当你右键点击方块时
* **条件**：一组必须满足的条件。例如拥有某个权限
* **动作**：一组要执行的动作。例如发送命令或消息


一个名为 oneUsage 的可选设置允许你模拟物品的一次性使用。


## 一个综合示例

```yaml
Mechanics:
  custom:
    test:
      one_usage: false
      event: "CLICK:right:all"
      conditions:
        - "HAS_PERMISSION:example.permission"
      actions:
        - "[console] give <player> cooked_beef 1"
```

在此示例中，小节 `test` 定义了一个自定义机制，当某人右键点击（在方块上或在空中）时触发。如果该玩家拥有 `example.permission` 权限，控制台将执行 give 命令并将 \<player> 替换为玩家名称。物品不会被消耗（oneUsage: false）。

## 可用事件

### CLICK:mouse_click_type:target_type

当你点击物品时调用。

**mouse_click_type**: `[ right, left, all ]`
**target_type**: `[ block, air, all ]`

### DROP

当你丢弃物品时调用。

### PICKUP

当你拾取物品时调用。

### BREAK

当玩家物品损坏时调用。

### EQUIP

当玩家装备物品时调用。

### UNEQUIP

当玩家卸下物品时调用。

### INV_CLICK

当玩家在物品栏中点击物品时调用。

### DEATH

当玩家死亡并且通常会掉落该物品时调用。

## 可用条件

### HAS_PERMISSION:the.permission

**the.permission**: `使用物品的玩家所需的权限`

## 可用动作

### COMMAND:sender:command

**sender**: `[ console, player ]`
**command**: `要执行的命令。可以使用占位符 <player>。`

### MESSAGE:content

**content**: `要发送的消息内容（支持 minimessage 格式）`

### ACTIONBAR:content

**content**: `要发送的消息内容（支持 minimessage 格式）`