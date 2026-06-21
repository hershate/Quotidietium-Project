# 命令任务

此任务在玩家执行命令时触发。 <br/>

:::warning
这些成就仅限于 **1** 个等级。
:::

### v2.0

支持[正则表达式](https://regex101.com/)。示例配置：

```yaml title="achievements/survival/challenges.yml" showLineNumbers
mayor:
  type: COMMAND
  settings:
    # 匹配任何城镇名称
    command: "^town create .+$"
  name: "Mayor"
  description:
    - "&fCreate your own town!"
  tiers:
    1:
      required-amount: 1
      rewards:
        - type: points
          amount: 10
```

### v1.0

必须设置 `command` 属性。支持[正则表达式](https://regex101.com/)。

示例配置：

```yaml title="achievements/survival/achievements.yml"
mayor:
  type: COMMAND
  # 匹配任何城镇名称
  command: "^town create .+$"
  name: "Mayor"
  description:
    - "&fCreate your own town!"
  tiers:
    1:
      required-amount: 1
      points: 10
```
