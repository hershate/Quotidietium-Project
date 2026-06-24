# ㊙️ 字体

:::info

这个过程极其简单，无需插件端配置。只需按照下面的教程操作即可。

:::

## TTF

[TrueType矢量字体](https://zh.minecraft.wiki/w/自定义字体#ttf)

对于 TTF 字体，你需要在以下路径中创建一个 `default.json` 文件。如果你已经有一个 `default.json` 文件，只需将你的字体 JSON 追加到现有 JSON 文件的末尾即可。

![](/img/font_1.png)

```json
{
    "providers": [
        {
            "type": "ttf",
            "file": "minecraft:custom_font.ttf",
            "oversample": 10,
            "size": 11
        }
    ]
}
```

![](/img/font_2.png)

## 位图

[位图字体](https://zh.minecraft.wiki/w/自定义字体#bitmap)

如果你希望替换原版字符图片，只需将以下 PNG 文件放置在指定路径中，如下所示。

![](/img/font_3.png)

## Unihex

要配置 Minecraft 中的 unihex 字体（这种字体相对不常见且很少使用），你可以参考 Minecraft Wiki 获取详细说明。

[Unihex 字体](https://zh.minecraft.wiki/w/自定义字体#unihex)
