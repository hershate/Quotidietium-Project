---
description: MMoItems 引入了非常独特的攻击特效
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966832308395049000/unknown.png
coverY: 0
---

# MMOItems

与 MMOItems 的兼容性允许你导入使用此插件创建的物品，并将其用作 Oraxen 物品的基础（你将保留 MmoItems 中配置的所有内容，并添加你自己的机制、纹理、3D 模型等）。

为此，只需在 Oraxen 的物品配置中添加一个 mmoitem 配置段即可。

```yaml
example_mmoitem:
  displayname: "<gradient:#59A7EA:#F1D2FF>Test"

  mmoitem:
    type: SWORD
    id: FALCON_BLADE
    level: 10 # 可选
    tier: RARE # 可选
    match_level: true # 可选
```
