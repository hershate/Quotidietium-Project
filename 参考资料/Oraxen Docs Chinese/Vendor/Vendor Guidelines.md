---
description: 供应商在为 Oraxen 创建资源包时应遵循的指南。
---

# 供应商指南

## 简介

Oraxen 提供了多种方式让你将 MCModels 资源包与其集成。
本指南将介绍你可以实现这一目标的不同方法。
根据资源包的类型，无论是家具、自定义方块还是自定义物品，你需要使用略有不同的配置。
在你提供的可下载资源包中，建议为 Oraxen 配置和其他文件设立一个专门的文件夹。
这使得用户可以轻松地将文件拖放到他们的 Oraxen 文件夹中。

## 通用资源包结构指南

`model` 和 `textures` 属性都是相对于 `plugins/Oraxen/pack/models(or textures)/` 的路径。
因此，上面的模型文件将位于 `plugins/Oraxen/pack/models/packname_or_something/model_file.json`。
如果你希望使用其他命名空间，你应该将文件放入 `plugins/Oraxen/pack/assets/NAMESPACE/models(or textures)/`。
然后在配置中，`model` 和 `textures` 的格式为 `NAMESPACE:filepath`。

任何模型、纹理或文件路径在任何情况下都不应包含大写字母或空格。
这是 1.13 之后资源包不支持的格式（尽管 Optifine 支持）。

1. `assets/namespace/models/SOMETHING/my model.json` X
2. `assets/namespace/models/something/my model.json` X
3. `assets/namespace/models/something/my_model.json` √

纹理的大小也应最大为 256x256 像素。
这些都是基础的资源包知识，但因为出现问题的情况足够多，我觉得有必要指出。

只要可能，建议不要导入 paper.json 和其他基础材质文件。
这些是支持中的头号问题，可以通过制作非常基础的 OraxenItem 配置来避免。
本质上，如果一个或多个 OraxenItem 配置使用了该材质，Oraxen 会将这些文件生成到最终的资源包中。
这样将更容易正确处理 CustomModelData，并减少大多数与此相关的支持问题。

## 通用配置属性

CustomModelData 是资源包冲突中最常见的陷阱。
多个资源包往往会使用相同的材质和相同的 CustomModelData 值。
Oraxen 有几种处理此问题的方法。

1. 如果配置中没有指定 Pack.custom_model_data，Oraxen 将根据 `material` 和 `model` 分配最高的未使用值
   1. 该值始终会保存到配置中，除非 `disable_automatic_model_data` 设置为 true
   2. 供应商应将此设置设为 `true`，且不在配置中指定 CustomModelData 的值，让 Oraxen 分配一个未使用的值
2. 对于 Glyphs 也是类似的情况。它有一个 `code` 属性，Oraxen 会分配最高的未使用值
   1. 该值始终会保存到配置中，除非 `disable_automatic_glyph_code` 设置为 true
   2. 供应商应将此设置设为 `true`，且不在配置中指定 Glyph 代码的值，让 Oraxen 分配一个未使用的值
3. 由于 ModelEngine 使用 `LEATHER_HORSE_ARMOR` 作为其默认属性，建议不要在配置中使用此材质
   1. 使用其他可染色物品，如 `TIPPED_ARROW`、`POTION` 或 `SPLASH_POTION` 以获得最佳兼容性
4. 如果你在制作自定义盔甲，请注意不同分辨率无法组合使用
   1. 这意味着任何添加 128x64 盔甲的资源包将无法与 64x32 盔甲配合使用
   2. 还应告知用户，他们需要更改 `armor_resolution` 设置以匹配他们正在使用的资源包
   3. 此项应设置为 armor_layer 文件的高度像素数除以 2（128x64 = 32，64x32 = 16（默认值））
   4. 盔甲的格式要求非常严格，建议你确保遵循[盔甲](/creating-content/armors)章节中的指南。

## 自定义物品

自定义物品是最常见的资源包类型，也是最容易与 Oraxen 集成的。
你真正需要的只是一个物品的配置文件，以及一个存放所有资源包文件的文件夹。
配置文件应放在 Oraxen/items 中，文件名可以任意命名。
为了清晰起见，建议将其命名为与你的资源包相同的名称。
配置文件应如下所示：

```yaml
my_example_item:
  displayname: "<red>My Example Item"
  material: PAPER
  Pack:
    generate_model: false
    model: packname_or_something/model_file
```

这是最基本的示例。
如果你使用 2D 物品，你的 `Pack` 配置节应改为如下所示：

```yaml
Pack:
  generate_model: true
  parent_model: "item/generated"
  textures:
    - packname_or_something/texture_file
```

可选地，textures 属性可以接受特定的基础名称：

```yaml
Pack:
  generate_model: true
  parent_model: "item/generated"
  textures:
    top: packname_or_something/top
    bottom: packname_or_something/bottom
    side: packname_or_something/side
```

主要用于有方向的自定义方块，因为你可以更轻松地指定侧面、顶部、底部的纹理。
基本上这依赖于 `parent_model`，所以如果你在那里有自定义条目，你也可以使用这个。`parent_model` 遵循与 `model` 和 `textures` 相同的结构，因此如果需要，你也可以使用 `NAMESPACE:filepath`。

## 自定义方块

自定义方块本质上就是自定义物品，只是添加了一种方块机制。
这意味着你可以使用与上面相同的配置，但需要额外添加 `Mechanics` 配置节。
有两种类型的方块机制：`noteblock` 和 `stringblock`。
`noteblock` 基本上用于任何应该作为普通方块的东西，如石头、木头、泥土等。
`stringblock` 主要针对植物、花卉和其他装饰物，因为它们没有碰撞体积。

### NoteBlock

`noteblock` 机制是最常见的，用于大多数方块。
其配置应如下所示：

```yaml
my_example_block:
  displayname: "<red>My Example Block"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "block/cube_all"
    textures:
      - something/texture_file
  Mechanics:
    noteblock:
      custom_variation: 1
      model: something/model_file
```

`custom_variation` 属性用于区分所有自定义方块，并且必须是唯一的。
与 `custom_model_data` 不同，它不会自动分配，你必须自行指定。
这样做的考虑是，由于它是放置在游戏世界中的，用户应该对其拥有控制权。
也许将来它会自动分配。如果你包含一个 README 文件，你应该对此进行说明。

`model` 属性与 `Pack` 配置节中的相同，并遵循相同的规则。
如果你启用了 `generate_model` 并指定了纹理，则模型名称将使用你的物品 ID，即 `my_example_block`。
还有额外的子机制，如自定义音效、硬度等。
你可以在 [NoteBlock 机制](/creating-content/blocks/noteblock)及其相关页面中了解更多信息。

### StringBlock

`stringblock` 机制用于不应有碰撞体积的方块。
这主要用于植物、花卉和其他装饰物。
其配置应如下所示：

```yaml
my_example_block:
  displayname: "<red>My Example Block"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "block/cross"
    textures:
        - something/texture_file
  Mechanics:
    stringblock:
      custom_variation: 1
      model: something/model_file
```

如你所见，它与 `noteblock` 机制非常相似。
子机制可以在 [StringBlock 机制](/creating-content/blocks/stringblock)及其相关页面中找到。

## 自定义家具

家具主要用于制作 3D 模型物品，如椅子、桌子等。
其配置应如下所示：

```yaml
my_example_furniture:
  displayname: "<red>My Example Furniture"
  material: PAPER
  Pack:
    generate_model: false
    model: packname_or_something/model_file
  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      hitbox:
        width: 1.0
        height: 1.0
      display_entity_properties:
        display_transform: FIXED
      barrier: true
```

如你所见，这里有一些额外的属性。
`type` 属性用于指定家具的类型。
可选项有 `DISPLAY_ENTITY`、`ITEM_FRAME` 和 `GLOW_ITEM_FRAME`。
`DISPLAY_ENTITY` 是 1.19.4 新增的类型，仅在 1.19.4 及更高版本的服务器上可用。
建议无论如何都将其设置为此选项，因为在旧版本上它会自动转换为 `ITEM_FRAME`。
此类型拥有更多属性，并允许更好的碰撞箱和性能表现。

`hitbox` 属性用于指定家具的碰撞箱。
它仅在 1.19.4+ 服务器上有用，会生成一个称为交互实体（Interaction Entity）的东西。
你可以把它想象成一个碰撞箱，用于检测对家具的击打和交互。
但它本身没有碰撞体积，为此你需要 `barrier` 属性。

`display_entity_properties` 属性用于指定 `DISPLAY_ENTITY` 的属性。
`display_transform` 属性用于指定物品的变换。
可选项有 `FIXED`、`HEAD`、`BODY`、`LEFT_ARM`、`RIGHT_ARM`、`LEFT_LEG`、`RIGHT_LEG` 和 `GROUND`。
这基本上就是 BlockBench 中 `Display` 选项卡的所有选项。
如果你想要 ITEM_FRAME 和 DISPLAY_ENTITY 之间的兼容性，你应该使用 `FIXED`。
ItemsAdder 相当于使用 `HEAD`，因为 ArmorStand 是其首选的实体类型。
你可以在[显示实体属性](/creating-content/furniture/display-entities)中找到其余选项。

`barrier` 属性用于指定家具是否应有碰撞体积。
这将在家具的原点放置一个普通的屏障方块。
你可以按照以下格式放置多个屏障：

```yaml
Mechanics:
  furniture:
    barriers:
        - { x: 0, y: 0, z: 0 }
        - { x: 0, y: 1, z: 0 }
```

## 自定义音效

某些资源包可能包含用于环境音、生物或其他用途的自定义音效。
在可能的情况下，建议为此使用另一个命名空间。
这是因为 Oraxen 默认基于 `sound.yml` 文件创建 sounds.json，而这可能会导致冲突。
如果使用场景允许使用自定义命名空间，只需将你的 sounds.json 添加到 `Oraxen/pack/assets/namespace/` 并将音效文件添加到 `Oraxen/pack/assets/namespace/sounds` 文件夹。

如果使用场景需要放在普通的 minecraft 命名空间中，你不应包含 sounds.json。
而是将条目添加到 Oraxen 的 sound.yml 文件中以获得最佳兼容性。
然后只需将音效文件添加到 `Oraxen/pack/assets/minecraft/sounds` 文件夹中。