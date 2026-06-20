---
cover: >-
  https://images-ext-2.discordapp.net/external/lXJpPHHy3JFqjn9qU_JpNHjaP2edFMFvnQjuYvTghYE/https/mcmodels.net/wp-content/uploads/2022/01/image-1.png
coverY: 0
---

# 自定义 GUI

使用 Oraxen 字形，你可以创建自定义带纹理的 GUI。下面是一个示例：

```yaml
customshop:
  texture: custom/default/custom/gui_tienda.png
  ascent: 13
  height: 256
```

纹理的分辨率不能高于 256x256，纹理名称必须全部小写且不含空格，与所有资源包文件一样。
要调整纹理/字形在库存中的水平位置，使用 shift 标签。`<shift:-8>` 用于向后移动 8 像素，`<shift:211>` 用于向前移动 211 像素。

![](https://images-ext-2.discordapp.net/external/lXJpPHHy3JFqjn9qU_JpNHjaP2edFMFvnQjuYvTghYE/https/mcmodels.net/wp-content/uploads/2022/01/image-1.png)

### 如何获取字形的 unicode？
这实际上不是必需的，因为 Oraxen 会在任何库存/标题中处理 `<glyph:glyph_id>` 标签。
所以要在任何其他插件中添加此字形，只需将标题设置为 `<glyph:glyph_id>`。
如果你仍然想要原始 unicode，可以在你的字形配置中找到它。

### 如何创建隐形物品？


隐形元素非常适合制作可点击的按钮。要创建隐形元素，你需要制作一个具有透明纹理的元素。示例如下


```yaml
invisible_item:
  displayname: "<white>"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
    - required/particle
```