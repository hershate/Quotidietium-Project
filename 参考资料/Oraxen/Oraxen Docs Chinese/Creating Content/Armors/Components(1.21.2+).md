# 基于组件的盔甲 (1.21.2+)

如果使用 COMPONENTS 作为自定义盔甲类型，你不会像 TRIMS 和 SHADER 那样受到任何限制。
与 SHADER 不同，此方法不会在着色器模组下失效，并且不限于 LEATHER_ARMOR 物品。
另一个好处是它根本不需要基于盔甲物品，如果你愿意，可以使用 PAPER。
早期方法的每一个缺点现在都已消除，没有任何限制。

## 如何配置你的盔甲？


确保你的 OraxenItem 的 itemID 遵循 `armorname_armortype` 的模式。
对于上述套装中的其余部分，应为 `ruby_chestplate`、`ruby_leggings` 和 `ruby_boots`。

确保你的盔甲层文件遵循 **armorname**_armor_layer_1/2.png 的格式。
在下面的例子中，我们需要 **ruby**_armor_layer_1.png 和 **ruby**_armor_layer_2.png


只需设置你想要的材质，无需指定两次纹理图标：

```yaml
ruby_helmet:
  displayname: "<gradient:#FA7CBB:#F14658>Ruby Helmet"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - default/armors/ruby_helmet
```

要使盔甲正确显示，还需要一个可装备组件 (Equippable-Component)。
如果未手动指定，Oraxen 将自动分配它。
如果需要，你也可以选择手动分配该组件。
值应为 `oraxen:armorname`，在我们的例子中：

```yaml
ruby_helmet:
  Components:
    equippable:
      slot: HEAD
      model: oraxen:ruby
```

## 自定义鞘翅

你可以使用组件盔甲系统创建具有独特纹理的自定义鞘翅。将你的物品 ID 命名为带有 `_elytra` 后缀（例如 `magic_elytra`），并提供名为 `armorprefix_elytra.png` 的匹配纹理文件。

```yaml
magic_elytra:
  displayname: "<gradient:#FA7CBB:#F14658>Magic Elytra"
  material: ELYTRA
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - default/armors/magic_elytra
  Components:
    equippable:
      slot: CHEST
      model: oraxen:magic_elytra
```

将你的鞘翅纹理文件以 `magic_elytra.png` 的形式放置在盔甲层纹理所在的同一文件夹中。Oraxen 将自动生成带有 `wings` 图层的装备模型。

鞘翅物品通过物品 ID 中的 `_elytra` 后缀、`ELYTRA` 材质或 `isGlider()` 物品元标记来检测。
