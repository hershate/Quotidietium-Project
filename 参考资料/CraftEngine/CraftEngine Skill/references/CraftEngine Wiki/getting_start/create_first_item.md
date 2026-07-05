# 💎 首个物品

## 您的第一大步

感谢您选择 CraftEngine —— 这是一个您不会后悔的明智决定！欢迎体验 CraftEngine 的首个教程！我猜您已经迫不及待想创建您的首个物品了。但在开始之前，让我先带您了解 CraftEngine 的 **配置文件夹** 是如何组织的。

:::tip

您可以点击这些文件夹，也别错过每个文件旁边的"?"——它也是可点击的！

:::

```
📁 cache
📁 generated
│   └── 📄 resource_pack.zip
📁 libs
📁 resources
│   └── 📁 tutorial
│       ├── 📁 configuration
│       │   └── 📄 first_item.yml
│       ├── 📁 resourcepack
│       │   └── 📁 assets
│       └── 📄 pack.yml
📁 translations
│   ├── 📄 en.yml
│   └── 📄 zh_cn.yml
📄 commands.yml
📄 config.yml
```

### 建立文件夹结构

请在上面的文件夹中找到我们的 **first_item.yml**，然后创建相同的目录结构。注意——在本教程中您无需创建 pack.yml 文件。

<details>
  <summary>小提示</summary>

1️⃣ 创建一个名为 `tutorial` 的文件夹（在 resources 目录下）  
2️⃣ 在其中新建一个 `configuration` 文件夹  
3️⃣ 在该文件夹内添加一个名为 `first_item.yml` 的新文件

</details>

### 创建您的首个物品配置

现在将此配置复制到您的 YML 文件中。保存后，运行 `/ce reload` 命令，然后在游戏中通过 `/ce item get tutorial:diamond` 获取您的物品。

```yaml
items:
  tutorial:diamond:
    material: diamond
```

### 添加物品基础信息

现在它只是一个普通的钻石——让我们给它加点料！我们将给它一个自定义的名称和描述。试试这段配置：

```yaml
items:
  tutorial:diamond:
    material: diamond
    data:
      item_name: "<blue>闪瞎24K狗眼的钻石"
      lore:
        - "<!i><red>史诗物品"
```

![](/img/i18n/zh-Hans/first_item.png)


:::tip

别忘了**重新加载**您的配置文件！\
（使用 `/ce reload` 应用更改）

关于 `<!i>`：它会移除斜体格式（默认情况下，物品提示框中所显示的描述信息为紫色且斜体）。

需要文本格式帮助？  
查看 [**MiniMessage**](https://docs.papermc.io/adventure/minimessage/format/) 来学习如何自定义样式！✨

:::

### 动态物品渲染

**付费版专属**

如何更新物品提示框中所显示的描述信息？只需使用 CraftEngine 的特殊客户端侧数据功能！与常规数据不同，这种数据仅对玩家可见——服务器甚至不会知道它的存在。

```yaml
items:
  tutorial:diamond:
    material: diamond
    client_bound_data:
      item_name: "<blue>闪瞎24K狗眼的钻石"
      lore:
        - "<!i><red>史诗物品"
```

如果你手上还有刚刚创建的那个钻石，试试客户端侧数据吧！只需触发一次服务端的物品更新 —— 比如丢弃它或在容器中移动它 —— 然后立刻就能看到焕然一新的外观。如果没有更新，试试切换到生存模式。

:::caution

`client_bound_data` 意味着服务器不会拥有真实数据。如果将其用于 `item_name`，任何服务端的名称检查都将失败。请根据您的服务器需求谨慎使用。

像 `max_damage` 和 `attribute_modifiers` 这样的数据组件不应使用 `client_bound_data`。它们会改变真实的服务器游戏体验，否则会导致奇怪的视觉同步问题。

译者注：不恰当的使用很有可能导致反作弊的误判

:::
