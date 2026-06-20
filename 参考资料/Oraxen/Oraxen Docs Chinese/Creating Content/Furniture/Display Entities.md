# 展示实体家具

本页面仅适用于服务器版本 1.19.4 及以上。
展示实体家具仅对 1.19.4 及以上版本的玩家可见。
ViaVersion 无法解决此问题。
Oraxen 版本也必须为 1.154.0 或以上



请注意，更改旧的家具配置不是一个好主意。
已经放置的、使用物品展示框的家具不会自动更新，如果配置更改可能会损坏。
如果你想更改配置，你应该移除家具然后重新放置。
未来，我们可能会制作一个命令、系统或插件扩展来将旧家具迁移到展示实体/新配置。


展示实体是 1.19.4 中引入的一种新实体类型。
它包含几种不同的类型：物品、方块和交互。
Oraxen 的家具机制使用了物品展示实体和交互实体。
有了它，你可以配置许多以前无法配置的内容。
除了更多的选项外，它也不会被剔除，这意味着它不会在某些角度取消渲染。
这可能导致一些玩家的 FPS 降低，但家具不会消失。

以下是这种配置的一个示例：
```yml
cart:
  displayname: "<gray>Cart"
  material: PAPER
  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      hitbox:
        width: 0.4
        height: 0.3
      display_entity_properties:
        display_transform: NONE
        brightness:
          block_light: 15
          sky_light: 0
      barrier: true
  Pack:
    generate_model: false
    model: default/cart
```

### 家具类型
首先，`type` 是 Oraxen 1.154.0 中新增的属性。
它允许你指定是想使用旧的物品展示框类型，还是新的展示实体类型。
如果你的服务器允许低于 1.19.4 版本的玩家进入，我们建议坚持使用物品展示框，因为另一种类型对这些玩家不可见。
如果未指定此属性，在支持的服务器（1.19.4+）上默认为 `DISPLAY_ENTITY`，否则为 `ITEM_FRAME`。
可用选项有：`DISPLAY_ENTITY`、`ITEM_FRAME`、`GLOW_ITEM_FRAME` 和 `ARMOR_STAND`

### 碰撞箱
碰撞箱也是 Oraxen 1.154.0 的新属性。
这是关于新的交互实体类型的。
这个实体是完全隐形的，没有碰撞，仅充当碰撞箱使用。
它可以与旧的屏障机制一起使用。
它有 `width` 和 `height` 属性来定义碰撞箱。
![](https://media.discordapp.net/attachments/743544047733440582/1085341928004005918/image.png?width=998&height=910)

### 展示实体属性
本节将详细说明这种新实体类型添加的众多选项。
其中一些比其他的更有用，但我已经添加了几乎所有的选项。
在 `display_entity_properties` 下你可以定义这些设置：
`display_transform`、`tracking_rotation`、`brightness`、`view_range`、`shadow_radius`、`shadow_strength`、`scale`

`display_transform` 决定了模型如何显示。
默认设置为 `NONE`，会按照你在 BlockBench 中打开模型时的样子显示。
因为其他一些插件可能使用盔甲架并将家具放在其头部，你可以将此选项设置为 `HEAD` 来获得相同的效果。
还有以下选项：`FIRSTPERSON_LEFTHAND`、`FIRSTPERSON_RIGHTHAND`、`FIXED`、`GROUND`、`GUI`、`THIRDPERSON_LEFTHAND`、`THIRDPERSON_RIGHTHAND`。
所有这些在游戏中的显示效果都与 BlockBench 显示选项卡中指定类型下的显示效果相同。
查看[家具位置](position)了解 FIXED（物品展示框位置）的示例

`tracking_rotation` 属性定义你希望家具是否"跟踪"玩家。
这主要用于公告板和你想让玩家看到的排行榜，而不是普通家具。
选项有：
`FIXED` - 无旋转
`VERTICAL` - 绕垂直轴旋转
`HORIZONTAL` - 绕水平轴旋转
`CENTER` - 绕中心点旋转

`brightness` 属性是让你的家具发光的一种方式。
它有 `block_light` 和 `sky_light` 属性，对应 Minecraft 的两种不同光照类型。
配置应该像这样：
```yaml
display_entity_properties:
  brightness:
    block_light: 15
    sky_light: 0
```

`scale` 属性是缩放家具的一种方式。
它有 `x`、`y` 和 `z` 属性，用于在每个轴上进行缩放。
配置应该像这样：
```yaml
display_entity_properties:
  scale:
    x: 1
    y: 1
    z: 1
```

`translation` 属性允许你偏移家具相对于其放置方块的位置。
这对于在不更改放置坐标的情况下微调模型的精确位置非常有用。
数值以方块为单位指定（0.1 = 方块的 1/10）。
它有 `x`、`y` 和 `z` 属性，用于在每个轴上进行偏移。
配置应该像这样：
```yaml
display_entity_properties:
  translation:
    x: 0.0
    y: 0.1  # 将家具稍微抬离地面
    z: 0.0
```

这在以下情况特别有用：
- 居中稍微偏离中心的模型
- 无需在 BlockBench 中修改模型即可调整垂直位置
- 微调放置在表面上的家具（桌子、椅子等）


`view_range` 控制家具在多远（以方块计）可以被看见。

`shadow_radius` 和 `shadow_strength` 控制家具投射的阴影。

### 动画属性

`interpolation_duration` 设置变换（缩放/旋转变化）完成所需的刻数。适用于平滑动画。

`interpolation_delay` 设置变换开始前的延迟刻数。

```yaml
display_entity_properties:
  interpolation_duration: 10 # 10 刻用于平滑过渡
  interpolation_delay: 0
```

### 显示尺寸

`displayWidth` 和 `displayHeight` 控制用于剔除（当家具不在视野中时隐藏）的包围盒尺寸。

```yaml
display_entity_properties:
  displayWidth: 1.0
  displayHeight: 1.0
```