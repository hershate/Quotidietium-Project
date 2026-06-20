---
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966834695058890772/unknown.png
coverY: 0
---

# 可染色物品

## 介绍

Oraxen 允许你基于 `POTION` 和 `LEATHER_HORSE_ARMOR` 创建可染色物品和家具，所以让我们先看看如何在 BlockBench 中实现！

### 我该如何操作？

#### 第一步 打开你的 Blockbench 模型

![](https://cdn.discordapp.com/attachments/896841738621177896/966749278615764992/IMG_20220421_121428.png)

#### 选择要染色的面

![](https://cdn.discordapp.com/attachments/896841738621177896/966749278850670592/IMG_20220421_121444.png)

#### 激活 `tint` 选项


使用白色可以获得更好的染色效果


![](https://cdn.discordapp.com/attachments/896841738621177896/966749279102308413/IMG_20220421_121505.png)

![](https://cdn.discordapp.com/attachments/896841738621177896/966749279349776424/IMG_20220421_121543.png)

#### 然后选择模型中所有使用该选项的面！



```yaml
clock:
  displayname: "<white>Clock"
  material: LEATHER_HORSE_ARMOR
  color: 255, 255, 255 #rgb
  Mechanics:
    furniture:
      barrier: false
      drop: # 如果不使用 barrier，则无用
        silktouch: false
        loots:
          - { oraxen_item: clock, probability: 1.0 }
  Pack:
    generate_model: false
    model: custom/furniture/clock
```