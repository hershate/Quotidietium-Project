---
description: Crucible 是 MythicMobs 的一个附加组件
cover: >-
    https://git.mythiccraft.io/uploads/-/system/project/avatar/51/unknown.png?width=64
coverY: 0
---

# Crucible

与 Crucible 的兼容性允许你导入使用 MythicMobs 和 Crucible 创建的物品，并将其用作 Oraxen 物品的基础（你将保留 Crucible 中配置的所有内容，并添加你自己的机制、纹理、3D 模型等）。

为此，只需在 Oraxen 中添加一个 crucible 配置段并指定 itemID 即可。

```yaml
example_crucible:
  displayname: "<gradient:#59A7EA:#F1D2FF>Test"
  crucible:
    id: my_crucible_itemid
```
