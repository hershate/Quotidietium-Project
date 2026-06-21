# 进度任务

此任务在玩家完成一个进度时触发。 <br/>

:::warning
这些成就仅限于 **1** 个等级。
:::

### v2.0

如果未指定命名空间，则默认使用 `minecraft`。 <br/>
您可以在[此处](https://minecraft.fandom.com/wiki/Advancements#List_of_advancements)找到有效的进度 ID 列表。ID 可在 `Resource location` 列中找到。

示例配置：

```yaml title="achievements/survival/challenges.yml" showLineNumbers
birdwatcher:
  type: ADVANCEMENT
  settings:
    # 您也可以指定自定义命名空间
    # <namespace>:<resource-location>
    advancement: "adventure/spyglass_at_parrot"
  name: "Birdwatcher"
  description:
    - "&fWatch a parrot through a spyglass!"
  tiers:
    1:
      required-amount: 1
      rewards:
        - type: points
          amount: 10
```

### v1.0

必须设置 `advancement` 属性。

如果未指定命名空间，则默认使用 `minecraft`。 <br/>
您可以在[此处](https://minecraft.fandom.com/wiki/Advancements#List_of_advancements)找到有效的进度列表。ID 可在 `Resource location` 列中找到。

示例配置：

```yaml title="achievements/survival/achievements.yml"
birdwatcher:
  type: ADVANCEMENT
  # 您也可以指定自定义命名空间
  # <namespace>:<resource-location>
  advancement: "adventure/spyglass_at_parrot"
  name: "Birdwatcher"
  description:
    - "&fWatch a parrot through a spyglass!"
  tiers:
    1:
      required-amount: 1
      points: 10
```
