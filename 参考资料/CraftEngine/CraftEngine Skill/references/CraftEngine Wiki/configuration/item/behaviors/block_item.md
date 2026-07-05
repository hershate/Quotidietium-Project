# 🧱 方块物品

## 简介

**方块物品** 是绑定到方块的物品。你可以在这里配置其对应的**方块命名空间ID**，甚至**完整的方块配置**。当我们将这种行为绑定到一个物品时，可以通过**右键点击**来放置它。

```yaml
items:
  default:palm_sapling:
    behavior:
      type: block_item
      block: default:palm_sapling

blocks:
  default:palm_sapling:
    behavior: ...
    settings: ...
    states: ...
    loot: ...
    events: ...
```

或

```yaml
items:
  default:palm_sapling:
    behavior:
      type: block_item
      block: # 译者注：我不是很推荐这种方式，这不太符合 Minecraft 的方块和物品区分的设计
        behavior: ...
        settings: ...
        states: ...
        loot: ...
        events: ...
```

:::tip
其他基于**方块物品**的变体行为也可以用这种格式配置。
:::

![](/img/block_item_1.png)
