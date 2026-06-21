# 奖励

## 版本 1.0

EpicAchievements 提供了许多内置奖励。 <br/>
以下是它们的列表：

:::tip
您可以在所有奖励中使用 `{player}` 占位符。
:::

| 奖励 | 描述 |
|------|------|
| `BROADCAST` | 向服务器广播消息 |
| `COMMAND` | 执行控制台命令 |
| `EXPERIENCE_LEVELS` | 给予玩家经验等级 |
| `EXPERIENCE` | 给予玩家经验值 |
| `MESSAGE` | 向玩家发送消息 |
| `VAULT` | 给予玩家金钱 |
| `PLAYER_POINTS` | 给予玩家金钱 |

### 奖励等级系统

玩家可以使用完成成就获得的点数来解锁奖励。 <br/>
以下是一个配置示例：

:::tip
您可以使用 `{level}` 占位符来获取当前等级。 <br/>
支持数学表达式和函数！
:::

```yaml title="rewards.yml"
rewards:
  # 等级范围
  1-100:
    # 解锁奖励所需的点数。支持数学表达式！
    required-points: "{level} * 100"
    # 奖励列表
    rewards:
      - "VAULT:{level} * 10"
    # 奖励锁定状态时显示的物品
    locked-item:
      material: "COAL"
      name: "&cAchievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Reward:"
        - "{rewards}"
        - ""
        - "{status}"
    # 奖励已领取时显示的物品
    claimed-item:
      material: "GOLD_NUGGET"
      name: "&aAchievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&aYou have already claimed this reward!"
    # 奖励未领取时显示的物品
    not-claimed-item:
      material: "GOLD_NUGGET"
      name: "&eAchievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&eClick to claim this reward!"
      glow: true
  # 可以在下方添加其他等级
```

EpicAchievements 提供了许多内置奖励类型：

:::tip
您可以在所有奖励中使用 `{player}` 和 `{uuid}` 占位符。
:::

| 奖励                | 描述                                                                          | 必需参数                 |
|---------------------|-------------------------------------------------------------------------------|--------------------------|
| `points`            | 给予玩家成就点数 <br/> **点数用于解锁奖励！**                                 | `amount`                 |
| `action_bar`        | 发送动作栏消息                                                                | `message`                |
| `broadcast`         | 向服务器广播消息                                                              | `message`                |
| `command`           | 执行控制台命令                                                                | `command`                |
| `experience_levels` | 给予玩家经验等级                                                              | `amount`                 |
| `experience`        | 给予玩家经验值                                                                | `amount`                 |
| `item`              | 给予玩家物品                                                                  | [`item`](../../item-format) |
| `message`           | 向玩家发送消息                                                                | `message`                |
| `title`             | 向玩家发送标题                                                                | `title` `subtitle`       |

### 插件钩子

| 插件                                                      | 奖励            | 描述                   | 必需参数              |
|-----------------------------------------------------------|-----------------|------------------------|-----------------------|
| [Vault](https://www.spigotmc.org/resources/34315/)        | `vault`         | 给予玩家金钱           | `amount`              |
| [PlayerPoints](https://www.spigotmc.org/resources/80745/) | `player_points` | 给予玩家点数           | `amount`              |
| [EcoBits](https://www.spigotmc.org/resources/109967/)     | `ecobits`       | 给予玩家特定货币       | `currency` `amount`   |

---

## 可选字段

### `description`
用于自定义奖励描述，覆盖在 `rewards.yml` 中定义的默认描述。 <br/>
`{amount}` 占位符可用。

```yaml
description: "&8+ &7{amount} &eCoins"
```

### `permission`
领取奖励所需的权限。没有此权限的玩家不会在列表中看到该奖励。 <br/>
**默认值：** `None`
```yaml
permission: "group.vip"
```

## 配置示例

```yaml
rewards:
  - type: points
    amount: 10
    description: "&8+ &7A nice gift!"
    permission: "group.vip"
```

---

## 奖励等级系统

玩家可以使用完成成就获得的点数来解锁奖励。 <br/>
可以定义多种奖励类型：下面的示例包含了 `normal` 和 `special` 两种奖励。 <br/>

![rewards](https://imgur.com/rqs7ypW.png)

:::tip
您可以使用 `{level}` 占位符来获取当前等级。 <br/>
支持数学表达式和函数！
:::

```yaml title="rewards.yml" showLineNumbers
# 在下方定义每个等级的奖励。
rewards:
  normal:
    levels:
      from: 1
      to: 48
      # (可选) 定义等级之间的增量。默认值为 1。
      # step: 1
    # 领取奖励所需的点数。
    required-points: "{level} * 100"
    # (可选) 如果同一等级定义了多个奖励，将使用权重最高的那个。
    # weight: 1
    # 奖励列表。
    rewards:
      - type: vault
        amount: "{level} * 10"
    locked:
      material: "COAL"
      name: "&cNormal Achievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&cYou can't claim this yet!"
    claimed:
      material: "GOLD_NUGGET"
      name: "&aNormal Achievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&aYou have already claimed this reward!"
    unclaimed:
      material: "GOLD_NUGGET"
      name: "&eNormal Achievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&eClick to claim this reward!"
      glow: true

  special:
    levels:
      from: 5
      to: 48
      step: 5
    required-points: "{level} * 100"
    weight: 2
    rewards:
      - type: vault
        amount: "{level} * 20"
    locked:
      material: "COAL_BLOCK"
      name: "&cSpecial Achievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&cYou can't claim this yet!"
    claimed:
      material: "GOLD_BLOCK"
      name: "&aSpecial Achievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&aYou have already claimed this reward!"
    unclaimed:
      material: "GOLD_BLOCK"
      name: "&eSpecial Achievement Reward"
      lore:
        - "&8Level {level}"
        - "&7Required Points: &e{points}"
        - ""
        - "&7Rewards:"
        - "{rewards}"
        - ""
        - "&eClick to claim this reward!"
      glow: true
```
