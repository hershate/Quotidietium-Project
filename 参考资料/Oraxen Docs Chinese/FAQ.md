---
description: 最常见问题的汇总
icon: question
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966825489098489856/unknown.png
coverY: 0
---

# 常见问题解答

### Oraxen 是 Mod 吗？

不是，Oraxen 不是通常意义上的 mod。它是一个 Minecraft 插件，允许您向游戏中添加物品、方块以及类似的有趣内容——所有这些都通过自动安装的资源包实现。

### Oraxen 支持 Folia 吗？

支持！Oraxen 原生支持 [Folia](https://papermc.io/software/folia)——PaperMC 的多线程服务器分支。Oraxen 会在启动时自动检测 Folia，并使用基于区域和基于实体的调度器来确保所有操作都是线程安全的。无需额外配置。

### Oraxen 使用了自己的资源包，我还能使用我自己的吗？

可以。有关如何操作的更多信息，请参见[此处](https://docs.oraxen.com/plugin-setup/pack-merging)。

### 我使用 Bungee/Velocity，但玩家切换服务器时资源包会重新加载？

这是因为玩家在技术上离开了一个服务器并加入了另一个服务器。因此，Minecraft 会移除并重新发送资源包。
如果您想防止这种情况，可以获取 [BungeePackLayer](https://www.spigotmc.org/resources/%E2%9C%82%EF%B8%8F-bungee-pack-layer-optimize-resource-pack-sending.94978/)。
这是一个 Bungee/Velocity 插件，可防止资源包被重新发送（除非资源包不同）。
如果所有服务器上的配置文件不完全相同，资源包就会不同。

### 我可以禁用 Oraxen 自带的默认资源和配置吗？

完全可以。您的 `settings.yml` 文件包含禁用这两者的选项：

```yaml
Plugin:
  generation:
    default_assets: false  # 禁用默认纹理/模型/音效
    default_configs: false # 禁用默认物品配置
```

**注意：** 即使禁用，必需的文件仍会生成：
- `glyphs/required.yml` - 包含必要的 UI 字形（退出图标等）
- 核心插件配置（settings.yml、mechanics.yml 等）

当 `default_assets: false` 时，Oraxen 将不会生成：
- 13 个默认物品配置文件（盔甲、方块、武器、家具等）
- 资源包中的默认纹理和模型
- 5 个字形文件（emoji、interface、animations、chat_tags）

当 `default_configs: false` 时，仅保留必需的字形文件和核心配置。

### 如何禁用或更改欢迎音效？

很简单，`settings.yml` 包含了在资源包发送给用户时可执行的配置操作，默认包含一个音效。下面的示例展示了您可以在哪里根据需要禁用或更改音效。

要**禁用**音效，请设置 `enabled: false`。要**更改**音效，请修改 `type`、`volume` 或 `pitch` 值。

```yaml
  receive:
    enabled: true
    loaded:
      actions:
        sound:
          # 设置为 false 以禁用欢迎音效
          # 设置为 true 以启用欢迎音效
          enabled: true
          type: minecraft:welcome  # 更改此项以使用不同的音效
          volume: 1.0  # 0.0 到 1.0
          pitch: 1.0   # 0.5 到 2.0
```

### Oraxen 会替换原版物品吗？

Oraxen 的目标是在不丢失功能的情况下向游戏中添加内容，所以简短的答案是不会。然而，Minecraft 有一些限制（例如，您无法真正添加新的方块或盔甲），因此我们不得不做出选择（可以通过禁用相关机制来撤销）：
- 新方块将使用原版未使用的音符盒变体：这可能会在使用这些不寻常变体的建筑中造成问题。

### 当我添加一个物品时，为什么它会破坏其他已创建物品的纹理？

默认情况下（1.21.4 之前），Oraxen 会自动为您的物品选择自定义模型数据值，并以最优化的方式生成它们。
每个不使用完全相同模型的物品都需要有一个不同的自定义模型数据值。当向 Oraxen 添加新物品并手动设置其自定义模型数据值时，您可能会因意外地在两个或更多不同物品上设置相同的值而破坏其他物品。


请勿忘记使用 `/o reload all` 重新加载插件，**并**使用 `/o pack send @a` 重新发送您的资源包（您也可以断开并重新连接到服务器）。


### 为什么我的纹理在使用 Optifine 时可以正常显示，但在原版中却不行？

自 Minecraft 1.11 起，原版资源包不再允许在文件夹、纹理或模型名称中使用大写字母，但 Optifine 仍然支持。请永远不要使用大写字母以避免问题。

### 如何更新 Oraxen？

这里有一个很好的视频可以帮助您：[https://youtu.be/LkansZwVaPY](https://youtu.be/LkansZwVaPY)

### 如何隐藏物品工具提示？

[https://github.com/lolgeny/item-tooltip-remover](https://github.com/lolgeny/item-tooltip-remover)

### 我应该在哪里建议新功能或报告问题？

第一种选择：登录 GitHub 并向官方仓库提交 issue：[git.io/oraxen](https://github.com/Th0rgal/Oraxen)

第二种选择：加入 [Discord](https://discord.gg/2ng6q3JNQ7)，获取您的 Oraxen 已验证身份组，然后前往支持频道，在那里您可以创建工单。

### 如何仅使用 Oraxen 的机制？

前往您的 settings.yml 文件并设置以下选项：

```yaml
  upload:
    enabled: false
Pack:
  generation:
    generate: false
    compression: BEST_COMPRESSION
    protection: false
  dispatch:
    send_pack: false
  enable_configs_updater: false
Misc:
  reset_recipes: false
  auto_update_items: false
```

这些配置不需要按照该确切顺序排列。更改这些行后，删除 /Oraxen/pack、/Oraxen/items 和 /Oraxen/glyphs 路径中的内容并重启服务器。