# 占位符任务

此任务类型使 EpicAchievements 能够与几乎所有拥有 [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/) 占位符的其他插件进行集成。 <br/>

## 输出整数的占位符

其配置与其他任务类型基本相同：

配置示例：

### v2.0

```yaml title="achievements/survival/tiered.yml" showLineNumbers
lumberjack:
  type: PLACEHOLDER
  settings:
    # 要测试的占位符：
    placeholder: "%auraskills_foraging%"
  name: "Professional Lumberjack"
  description:
    - "&fCut down trees!"
  tiers:
    1:
      required-amount: 1
      rewards:
        - type: points
          amount: 10
    2:
      required-amount: 2
      rewards:
        - type: points
          amount: 15
    3:
      required-amount: 3
      rewards:
        - type: points
          amount: 20
```

### v1.0

```yaml title="achievements/survival/achievements.yml"
lumberjack:
  type: PLACEHOLDER
  placeholder: "%auraskills_foraging%"
  name: "Professional Lumberjack"
  description:
    - "&fCut down trees!"
  tiers:
    1:
      required-amount: 1
      points: 10
    2:
      required-amount: 2
      points: 15
    3:
      required-amount: 3
      points: 20
```

## 输出文本的占位符

:::warning
这些成就仅限于 **1** 个等级。
:::

您可以使用以下运算符之一来测试占位符：

| 运算符                   | 描述                                                               |
|--------------------------|--------------------------------------------------------------------|
| `EQUALS`                 | 检查输出是否与指定值匹配。                                         |
| `EQUALS_IGNORE_CASE`     | 检查输出是否与指定值匹配，忽略大小写。                             |
| `NOT_EQUALS`             | 检查输出是否与指定值不匹配。                                       |
| `NOT_EQUALS_IGNORE_CASE` | 检查输出是否与指定值不匹配，忽略大小写。                           |
| `CONTAINS`               | 检查输出是否包含指定值作为子字符串。                               |
| `STARTS_WITH`            | 检查输出是否以指定值开头。                                         |
| `ENDS_WITH`              | 检查输出是否以指定值结尾。                                         |
| `REGEX`                  | 检查输出是否与指定的正则表达式匹配。                               |

配置示例：

### v2.0

```yaml title="achievements/survival/challenges.yml" showLineNumbers
first-nap:
  type: PLACEHOLDER
  settings:
    placeholder: "%player_is_sleeping%"
    operator: EQUALS
    value: "yes"
  name: "First Nap"
  description:
    - '&fSleep for the first time!'
  tiers:
    1:
      required-amount: 1
      rewards:
        - type: points
          amount: 10
```

### v1.0

```yaml title="achievements/survival/achievements.yml"
first-nap:
  type: PLACEHOLDER
  placeholder: '%player_is_sleeping%'
  name: "First Nap"
  description:
    - '&fSleep for the first time!'
  tiers:
    1:
      placeholder:
        operator: EQUALS
        value: "yes"
      points: 10
      rewards: []
```
