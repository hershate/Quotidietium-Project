---
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966825489098489856/unknown.png
coverY: 0
---

# 家具位置

如果你的服务器使用 1.19.4 或以上版本，有一种称为展示实体的新实体类型。
这些实体有一些与家具位置相关的额外属性需要设置。
其中最主要是 `display_transform`，它决定了应该使用何种变换来显示你的物品。
你可以在[这里](/creating-content/furniture/display-entities#display-entity-properties)获得更好的解释。
以下是一个家具的示例，其 `type` 设置为 `ITEM_FRAME`，或者 `DISPLAY_ENTITY` 的 `display_transform` 设置为 `FIXED`。

要开始使用家具而不让它看起来不好，你需要调整它的位置。假设你使用 BlockBench 创建了物品，然后进入
![](https://hibiscuscreative.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc051221b-af62-46a7-a988-c9fdaf3d9c47%2FUntitled.png?table=block&id=bb951dcd-f5c4-4a1d-a73b-a7cdb36d18f0&spaceId=d94d82a0-f00a-4f51-82f0-03722550c74d&width=1340&userId=&cache=v2)

大多数情况下，家具使用隐形物品展示框来实现。所以，你需要修改"Frame"的平移设置。

![](https://hibiscuscreative.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F451c946e-fb1b-45c5-9738-be49b3fd4a5e%2FUntitled.png?table=block&id=07248014-959d-40c7-b9bd-74a038a3c361&spaceId=d94d82a0-f00a-4f51-82f0-03722550c74d&width=1440&userId=&cache=v2)

这样就完成了！