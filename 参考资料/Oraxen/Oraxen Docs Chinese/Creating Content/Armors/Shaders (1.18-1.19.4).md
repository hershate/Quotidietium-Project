# 基于着色器的盔甲 (1.18-1.19.4)

Oraxen 通过使用染色皮革盔甲和着色器来修改这第二层纹理。
盔甲就像每个物品一样，在物品栏和手中有一个纹理，但它还有在穿戴在身体上时的第二层纹理。
这第二种外观有一些限制，需要一些练习。我们将使用一个关于皮革盔甲和颜色的技巧。


如果你通过 Optifine 或 Iris 模组使用着色器，你需要一些额外的步骤。
对于 Optifine，一切都会自动处理。
对于 Iris，你还需要 [CIT Resewn](https://modrinth.com/mod/cit-resewn)，其他一切都会为你处理。


![A: 物品外观    B: 身体外观](/assets/stuff.png)


在命名你的盔甲时必须小心，以确保纹理被正确检测。

如果你想创建一个 **amethyst** 盔甲套装，那么你的物品条目必须是：
\- **amethyst**_helmet
\- **amethyst**_chestplate
\- **amethyst**_leggings
\- **amethyst**_boots

然后在[步骤2](./#2-name-your-textures-correctly)中，你将能够创建纹理：
\- **amethyst**_armor_layer_1.png
\- **amethyst**_armor_layer_2.png


#### 如何配置你的盔甲？

为此，我们将使用以下配置示例作为参考：
```yaml
ruby_helmet:
  displayname: "<gradient:#FA7CBB:#F14658>Ruby Helmet"
  material: LEATHER_HELMET
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - default/armors/ruby_helmet
      - default/armors/ruby_helmet
```

确保物品的 ID，即上面示例的第一行，遵循 `armorname_armortype` 的模式。
对于上述套装中的其余部分，应为 `ruby_chestplate`、`ruby_leggings` 和 `ruby_boots`。



这也是为什么皮革是唯一可以使用的材质。
自定义盔甲不能使用钻石作为基础材质。
要获得自定义盔甲数值，只需添加属性修改器。


### 如何更改穿戴外观？

现在有趣的部分开始了。我们将使用原版着色器将盔甲样式与特定的颜色关联。
感谢 [Ancientkingg](https://twitter.com/ancientkingg) 开发了 Oraxen 使用的着色器。

### 1) 创建你的纹理

你需要为你的盔甲创建两个纹理。你可以在这里下载红宝石示例：
[https://oraxen.com/resources/armor_rest.png](https://media.discordapp.net/attachments/758785982005903431/1009559045893537802/ruby_armor_layer_1.png)
[https://oraxen.com/resources/armor_leggings.png](https://media.discordapp.net/attachments/758785982005903431/1009559063815786626/ruby_armor_layer_2.png)


确保你的盔甲分辨率符合 settings.yml 中设置的值。
默认情况下，armor_resolution 设为 16。这意味着你的纹理必须是 64x32 像素。
如果你想使用更高的分辨率，你需要更改 settings.yml 中的值。
例如，128x64 像素的 armor_layer 文件必须在 settings.yml 中将分辨率设为 32。
你不能某些是 64x32 而另一些是 128x64，只能是统一的。

还要确保你纹理的位深度是 32 位。
其他任何位深度意味着不完全透明，着色器使用的像素将是黑色的。
这不会破坏 Optifine/Iris 版本，但会破坏所有原版版本。


![](/assets/leggings.png)


![](/assets/armor.png)


你可以通过添加另一个以 **_e.png** 结尾的同名文件来使你的纹理**发光**（无需 Optifine）。例如 `ruby_armor_layer_1_e.png`
此纹理将被视为发光度贴图，其中像素的透明度将被视为发光程度。


### 2) 正确命名你的纹理

为了让你的纹理被正确注册，它们的名称需要包含 `armor_layer_X`。
例如：
`ruby_armor_layer_1.png` 和 `ruby_armor_layer_2.png`
你可以将它们放在资源包纹理的任何文件夹中，建议放在 `~/textures/default/armors`。
