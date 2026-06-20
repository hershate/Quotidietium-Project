---
description: 如何向游戏中添加非立方体的装饰性物体
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966828778028417125/unknown.png
coverY: 0
---

import { Callout } from 'nextra/components'

# 家具

Oraxen 允许你创建自定义 3D 家具，如椅子、桌子、灯具和装饰品。家具使用基于实体的渲染来实现方块无法达成的复杂形状。

![示例家具](/assets/image%20(3).png)

## 何时使用家具

| 使用场景 | 家具 | 方块 |
|----------|-----------|--------|
| 复杂 3D 模型 | ✅ 最佳选择 | ❌ 有限 |
| 可坐的椅子 | ✅ 内置支持 | ❌ 不可能 |
| 可旋转物体 | ✅ 任意角度 | ⚠️ 4 个方向 |
| 大型装饰 | ✅ 多方块碰撞箱 | ⚠️ 复杂 |
| 挖掘/破坏 | ⚠️ 瞬间破坏 | ✅ 自然 |
| 大规模性能 | ⚠️ 基于实体 | ✅ 更好 |

<Callout type="info">
使用家具来制作装饰性物体、椅子、桌子以及任何需要复杂 3D 模型的内容。使用[自定义方块](/creating-content/blocks)来制作矿石、建筑材料以及玩家频繁挖掘的物品。
</Callout>

## 核心功能

| 功能 | 描述 |
|---------|-------------|
| [展示实体](/creating-content/furniture/display-entities) | 具有变换和动画的现代渲染方式 |
| [屏障与碰撞箱](/creating-content/furniture/display-entities#hitbox) | 碰撞和交互区域 |
| [座位](#seats) | 让玩家坐在家具上 |
| [存储](#storage) | 自定义容器和箱子 |
| [发光](#light) | 会发光的家具 |
| [进化](#evolution) | 随时间生长的作物和植物 |
| [ModelEngine](/compatibility/modelengine-custom-mobs) | 使用 Blockbench 制作的动画模型 |

## 基础配置

```yaml
table:
  displayname: "<gray>Table"
  material: DIAMOND
  Pack:
    generate_model: false
    model: default/table
  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      barrier: true
      drop:
        silktouch: false
        loots:
          - { oraxen_item: table, probability: 1.0 }
```

## 文本显示

家具可以为基础家具实体附加仅数据包层面的文本显示。这些文本显示仅发送给客户端；它们不会保存为真实的服务器实体，也不会增加碰撞或实体 AI 开销。它们需要服务器版本支持展示实体。

使用 `text_entity` 设置单个标签：

```yaml
table:
  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      text_entity:
        text:
          - "<gold>Workshop Table"
          - "<gray>%player_name%"
        offset: { x: 0.0, y: 1.2, z: 0.0 }
        scale: { x: 1.0, y: 1.0, z: 1.0 }
        billboard: CENTER
        alignment: CENTER
        shadow: true
        see_through: false
        background_color: "#40000000"
        text_opacity: -1
        line_width: 200
        view_range: 32
        refresh_ticks: 20
```

使用 `text_entities` 设置多个标签：

```yaml
Mechanics:
  furniture:
    text_entities:
      - text: "<green>Open"
        offset: { x: 0.0, y: 1.1, z: 0.0 }
      - text: "<red>Closed"
        offset: { x: 0.0, y: 0.8, z: 0.0 }
        scale: [0.75, 0.75, 0.75]
```

| 属性 | 默认值 | 描述 |
|----------|---------|-------------|
| `text` | 空 | 字符串或字符串列表。列表渲染为独立行。支持 MiniMessage。 |
| `offset` | `{ x: 0.0, y: 0.6, z: 0.0 }` | 相对于家具基础实体的位置。X/Z 偏移会随家具旋转。也可以使用 `[x, y, z]`。 |
| `scale` | `{ x: 1.0, y: 1.0, z: 1.0 }` | 文本显示缩放。也可以使用 `[x, y, z]`。 |
| `billboard` | `CENTER` | `FIXED`、`VERTICAL`、`HORIZONTAL` 或 `CENTER`。 |
| `alignment` | `CENTER` | `LEFT`、`CENTER` 或 `RIGHT`。 |
| `shadow` | `false` | 添加原版文本阴影。 |
| `see_through` | `false` | 透过方块渲染文本。 |
| `default_background` | `false` | 使用客户端的默认文本显示背景。 |
| `background_color` | `#40000000` | ARGB 十六进制颜色。六位 RGB 值使用 alpha `40`。 |
| `text_opacity` | `-1` | 原版文本不透明度值，范围 `-1` 到 `127`。 |
| `line_width` | `200` | 换行前的最大文本行宽度。 |
| `view_range` | `32` | 最大可视距离（以方块计）。 |
| `refresh_ticks` | `0` | 元数据刷新间隔。当此项未设置时，包含占位符的文本会自动刷新。 |

当 `refresh_ticks` 大于 `0` 时，文本针对每个观察者刷新，因此 PlaceholderAPI 占位符可以为每个玩家解析出不同的结果。如果 `refresh_ticks` 为 `0` 且文本中没有占位符，则文本在家具进入玩家视野时发送。

## 自定义音效
家具和自定义方块一样，可以拥有自定义音效。
目前可用的选项有放置/破坏/击打/行走/摔落。
```yaml
Mechanics:
  furniture:
    block_sounds:
      place_sound: block.stone.place
      break_sound: block.stone.break
      hit_sound: my.custom.hitsound     # 在 Oraxen/sound.yml 中定义的自定义音效
      step_sound: my.custom.stepsound   # 还需要在 Oraxen/pack-folder 中有对应的音效文件
      fall_sound: my.custom.fallsound
```
所有音量和音调值都设置为 Minecraft 正常对方块使用的值。
如果你想更改音量或音调，可以使用以下格式。
请注意这两种格式可以互相兼容。
我们建议直接使用默认格式，但如果你想更改，这个选项是可用的。
```yaml
Mechanics:
  furniture:
    block_sounds:
      place:
        sound: block.stone.place
        volume: 1.0
        pitch: 0.2
      break_sound: block.stone.break
      hit_sound: my.custom.hitsound     # 在 Oraxen/sound.yml 中定义的自定义音效
      step_sound: my.custom.stepsound   # 还需要在 Oraxen/pack-folder 中有对应的音效文件
      fall_sound: my.custom.fallsound
```

## 可旋转
要使家具可旋转，只需在你的物品配置中添加以下内容。
```yaml
Mechanics:
  furniture:
    rotatable: true
```

## ModelEngine 家具
要将 ModelEngine 模型用作家具，只需在你的物品配置中添加以下内容：
```yaml
Mechanics:
  furniture:
    modelengine_id: name_of_your_bbmodel_file
```

## 唱片机
允许此家具接受音乐唱片和自定义音乐唱片并播放。
你可以调整唱片机的 `volume`（音量）和 `pitch`（音调）。
还有一个 `permission` 字段，如果你想仅允许特定玩家从唱片机播放音乐，可以使用它。
默认情况下权限为空，意味着任何人都可以从唱片机播放音乐。

你还可以指定 `active_model` 来在唱片播放时更改家具的外观：
```yaml
turntable:
  Mechanics:
    furniture:
      jukebox:
        active_model: opened  # 引用 Pack.models 中的键名
        volume: 1.0
        pitch: 1.0
        permission: "oraxen.jukebox.play"
  Pack:
    model: default/turntable_closed
    models:
      opened: default/turntable_opened  # 播放时显示的模型
```

`active_model` 引用 `Pack.models` 中定义的键名。更多详情请参见 [Pack.models](#packmodels)。

## 屏障

屏障是随你的家具放置的隐形方块，使其拥有逼真的碰撞箱。你可以放置单个屏障，也可以放置一个相对于放置玩家位置的列表。

注意：对于展示实体（Display Entity）家具，你可以使用 `hitbox` 代替屏障来简化配置。屏障对于较大的家具或需要碰撞的情况仍然有用。

### 单个屏障：

```yaml
Mechanics:
  furniture:
    barrier: true
```

### 多个屏障：

```yaml
Mechanics:
  furniture:
      barriers:
        - origin # { x: 0, y: 0, z: 0 } 的简写
        - z: 1 # 如果未指定，坐标默认为 0 -> { x: 0, y: 0, z: 1 }
        - z: 2
        - x: 1
        - { x: 1, z: 1 }
        - x: 1
          z: 2
```

# 座位
<b>座位仅在启用屏障时可用。</b>
目前如果有多个屏障，它也会为每个屏障生成一个座位。
你可以通过以下配置调整座位的高度偏移：

```yaml
Mechanics:
  furniture:
    seat: { height: 0.5 }
```
如果需要，你也可以通过添加 yaw 部分来调整旋转角度。
请记住，建议不要设置此项
```yaml
Mechanics:
  furniture:
    seat: { height: -0.5, yaw: 90 }
```

# 限制旋转
你可以使用 `restricted_rotation` 来限制家具的旋转方向数量。
可以设置为 STRICT 或 VERY_STRICT，分别对应 8 个和 4 个朝向。
```yaml
chair:
  Mechanics:
    furniture:
      restricted_rotation: VERY_STRICT # 如果未指定，默认是 STRICT
```

# 有限放置
你可以使用 `limited_placing` 子部分来自定义自定义方块/家具可以放置在什么方块上。
你可以使用 `roof`、`floor` 和 `wall` 选项来指定方块可以放置的位置。默认情况下，所有选项都设置为 `true`。
`type` 指定是仅允许还是仅禁止放置在特定方块上。
如果 type 是 `ALLOW`，则该方块只能放置在给定的方块上。
如果 type 是 `DENY`，则可以放置在与给定方块不匹配的所有方块上。
还有一个 `radius_limitation` 选项，允许你限制在特定半径内某种家具的数量。
```yaml
chair:
  Mechanics:
    furniture:
      limited_placing:
        radius_limitation:
          radius: 20
          amount: 10
        roof: false
        floor: true
        wall: false
        type: ALLOW
        block_types:
          - GRASS_BLOCK
          - DIRT
        block_tags:
          - base_stone_nether
        oraxen_blocks:
          - chair
          - ruby_ore
```

`block_tags` 可以在[这个页面](https://minecraft.fandom.com/wiki/Tag#Block_tags)找到。在你想允许/禁止一组方块时很有用。
`block_types` 是材质。在你想允许/禁止特定的方块列表时很有用。
`oraxen_blocks` 是在 Oraxen 配置中定义的方块。
这允许所有自定义方块和家具，但家具需要屏障碰撞箱。

# 存储
这是家具和音符盒机制的子机制，允许你制作自定义存储容器。
本质上就是一个箱子、衣柜或任何你想要的。

有几种不同的类型：_STORAGE、PERSONAL、ENDERCHEST 和 DISPOSAL_。
**STORAGE** 类似于普通箱子。任何人都可以打开它并查看其中的内容。
**PERSONAL** 本质上是自定义的末影箱，允许你编辑行数等。
**ENDERCHEST** 就是字面意义上的末影箱物品栏，但允许你制作自定义方块/家具来访问它。
**DISPOSAL** 是一个自定义垃圾桶，允许你向其中投入物品，关闭时物品将被删除。

```yaml
Mechanics:
  furniture:
    barrier: true
    storage:
      type: STORAGE
      rows: 5                             # 默认: 6
      title: "<red>My Storage"            # 默认: "Storage"
      open_sound: entity.shulker.open     # 默认: entity.chest.open
      close_sound: entity.shulker.close   # 默认: entity.chest.close
```

此机制如果与家具一起使用，需要屏障！


## 发光

你可以配置你的家具使其发光。此选项对应光照强度，必须在 1 到 15 之间。

```yaml
Mechanics:
  furniture:
    barrier: true
    light: 5
    drop:
      silktouch: false
      loots:
        - { oraxen_item: table, probability: 1.0 }
```

## BlockLocker
你可以使用此项通过 [BlockLocker](https://www.spigotmc.org/resources/blocklocker.3268/) 来允许保护
有效的 protectionTypes 为 CONTAINER、DOOR、ATTACHABLE
```yaml
Mechanics:
  furniture:
    blocklocker:
      can_protect: true
      protection_type: CONTAINER
```

## 硬度
你可以为你的家具设置自定义硬度，这会影响破坏它所需的时间。
```yaml
Mechanics:
  furniture:
    hardness: 5 # 默认: 1
```

## 替代显示物品
在家具放置时使用不同 Oraxen 物品的模型。适用于库存图标与放置后外观不同的情况。
```yaml
Mechanics:
  furniture:
    item: different_item_id # 放置时显示的物品模型
```

## 放置要求
要求家具必须放置在耕地或自定义 Oraxen 耕地方块上。
```yaml
Mechanics:
  furniture:
    farmland_required: true # 需要原版耕地
    # 或者
    farmblock_required: true # 需要 Oraxen 自定义耕地方块
```

## 进化
让家具随时间进化成不同的阶段，像作物生长一样。适用于自定义植物。
```yaml
Mechanics:
  furniture:
    evolution:
      delay: 6000 # 进化检查之间的间隔刻数
      next_stage: my_plant_stage2 # 要进化成的物品 ID
      probability: 0.5 # 进化几率 (0.0 到 1.0)
      light_boost: # 可选：在光照下加速
        minimum_light_level: 9
        boost_tick: 2000 # 光照充足时每次检查增加的刻数
      rain_boost: # 可选：在下雨时加速
        boost_tick: 1500
      bone_meal: # 可选：允许骨粉推进生长
        chance: 30 # 使用骨粉时推进生长的百分比几率
```

## 点击动作
当玩家点击家具时运行命令、播放音效或发送消息。
详细配置请参见 [clickAction 机制](/creating-content/items/abilities/clickaction)。

## Pack.models

使用 `Pack.models` 为单个物品定义多个模型。这样在需要不同视觉状态时就不需要创建虚假的辅助物品了。

```yaml
my_furniture:
  Pack:
    model: default/my_furniture        # 基础模型
    models:
      active: default/my_furniture_active    # 额外模型
      broken: default/my_furniture_broken    # 另一个模型
```

这些模型会自动注册为：
- `oraxen:my_furniture` → 基础模型
- `oraxen:my_furniture/active` → active 变体
- `oraxen:my_furniture/broken` → broken 变体

### 使用案例

**带播放状态的唱片机：**
```yaml
turntable:
  Mechanics:
    furniture:
      jukebox:
        active_model: opened  # 播放时切换到此模型
  Pack:
    model: default/turntable_closed
    models:
      opened: default/turntable_opened
```

**带生长阶段的植物：**
```yaml
seed:
  Mechanics:
    furniture:
      stages:
        - model: stage0
          evolution: { delay: 10000 }
        - model: stage1
          # ...
  Pack:
    models:
      stage0: default/plant/stage0
      stage1: default/plant/stage1
```

详见[农耕机制](/creating-content/furniture/farming)了解详细的植物/进化配置。

## 下一步

- [展示实体](/creating-content/furniture/display-entities) - 现代家具渲染和碰撞箱
- [农耕机制](/creating-content/furniture/farming) - 自定义作物和植物
- [创建你的第一个物品](/creating-content/items) - 首先学习物品基础知识