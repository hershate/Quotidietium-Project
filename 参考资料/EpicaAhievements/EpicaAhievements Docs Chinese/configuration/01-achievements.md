# 成就

## 版本 1.0

### 交互式设置

创建和编辑成就最简单的方法是使用游戏内编辑器。 <br/>
> 您可以通过输入 `/achievements editor` 来打开它。

### 手动编辑配置

如果您是高级用户，可以手动编辑成就的配置文件。

:::note
成就文件位于 `plugins/EpicAchievements/achievements/<category>` 文件夹中。 <br/>
每个分类中可以放置任意数量的成就文件。 <br/>
默认情况下，如果不存在该文件，游戏内编辑器将在名为 `achievements.yml` 的文件中创建新成就。
:::

以下是一个成就配置示例：

```yaml title="achievements/survival/achievements.yml"
# 唯一标识符。请勿修改，否则玩家将丢失进度！
builder:
# 任务类型：参见 https://wiki.pixelstudios.dev/epicachievements/configuration/tasks
type: PLACE
# 用于消息和菜单中的名称
name: "Builder"
# 成就的描述
description:
- "&fPlace blocks."
# （可选）在该成就中取得进展所需的权限
permission: achievements.builder
# 在该成就中取得进展所需的前置成就
required-achievements:
- miner
- farmer
# 条件：参见 https://wiki.pixelstudios.dev/epicachievements/configuration/conditions
blocks:
- STONE_BRICKS
- BRICKS
worlds:
- world
- resource_world
game-modes:
- SURVIVAL
# 等级列表。至少需要一个等级
tiers:
1:
# 完成该等级所需的进度值
required-amount: 10
# 完成该等级后获得的点数
points: 25
# 奖励列表。参见 https://wiki.pixelstudios.dev/epicachievements/configuration/rewards
# 格式：REWARD_TYPE:VALUE
rewards:
- "VAULT:100"
- "COMMAND:say {player} has completed the Builder achievement!"
# 可在下方添加其他等级
```

:::info
成就分为两种类型：
- `CHALLENGE`：单等级
- `TIERED`：多等级

类型会根据等级数量自动确定。
:::

:::note
成就文件位于 `plugins/EpicAchievements/achievements/<category>` 文件夹中。 <br/>
每个分类中可以放置任意数量的成就文件。
:::

## 必填字段

### `type`
您可以[在此](./tasks)查看所有可用的任务类型。
```yaml
type: FISH
```

### `name`
成就的名称，显示在消息和菜单中。
```yaml
name: "Lucky Catch"
```

### `description`
成就的描述，显示在消息和菜单中。
```yaml
description:
  - "&fCatch an enchanted book"
  - "&fwhile fishing."
```

### `tiers`
等级列表，每个等级由唯一编号标识。 <br/>
**至少需要一个等级。**

- `required-amount`：完成该等级所需的进度值。
- `rewards`：完成该等级后的奖励列表。[点击此处](./rewards)了解更多信息。
```yaml
tiers:
  1:
    required-amount: 1
    rewards:
      - type: points
        amount: 5
  2:
    required-amount: 5
    rewards:
      - type: points
        amount: 10
```

## 可选字段

### `weight`
成就的权重，用于确定菜单中的默认排序顺序。 <br/>
**默认值：** `1`
```yaml
weight: 5
```

### `permission`
访问该成就所需的权限。 <br/>
**默认值：** `None`
```yaml
permission: "achievements.lucky-catch"
```

### `hidden`
如果设置为 true，该成就将从菜单中隐藏并保持*秘密*状态。 <br/>
**默认值：** `false`
```yaml
hidden: true
```

### `requirements`
玩家必须先完成这些成就，才能访问该成就。 <br/>
**默认值：** `None` <br/>

有效格式：
- `<id>` - 需要完成该成就的**所有等级**。
- `<id>:<tier>` - 需要完成该成就的指定等级。
```yaml
requirements:
  - "miner"
  - "farmer:3"
```

### `conditions`
必须满足才能完成该成就的条件列表。 <br/>
[点击此处](./conditions)了解更多信息。
```yaml
conditions:
  - type: game_modes
    game-modes:
      - SURVIVAL
  - type: items
    items:
      - ENCHANTED_BOOK
```

### `settings`
成就的附加设置。

`toast-message`：覆盖 `config.yml` 中设置的默认弹出消息（需要 **[CrazyAdvancementsAPI](https://www.spigotmc.org/resources/51741/)**）
  - `icon`：弹出消息中显示的图标。
  - `message`：弹出消息中显示的文字。
  - `type`：您可以选择 `CHALLENGE`、`TASK` 或 `GOAL`。
```yaml
settings:
  toast-message:
    icon: ENCHANTED_BOOK
    message: "Custom toast message!"
    type: CHALLENGE
```

## 配置示例

```yaml title="achievements/survival/challenges.yml" showLineNumbers=true"
# 唯一标识符。请勿修改，否则玩家将丢失进度！
lucky-catch:
  type: FISH
  name: "Lucky Catch"
  description:
    - "&fCatch an enchanted book"
    - "&fwhile fishing."
  settings:
    toast-message:
      icon: ENCHANTED_BOOK
      message: "Custom toast message!"
      type: CHALLENGE
  conditions:
    - type: game_modes
      game-modes:
        - SURVIVAL
    - type: items
      items:
        - ENCHANTED_BOOK
  tiers:
    1:
      required-amount: 1
      rewards:
        - type: points
          amount: 5
```