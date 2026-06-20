---
description: 物品的杂项机制
---

# 杂项机制

### 自定义食物
此机制允许你为任何食物物品设置食物相关属性。  
这意味着你可以创建恢复不同饥饿值和饱和度的食物。  
它还允许你设置食物被消耗后的替换物品。  

以下是自定义食物机制部分的配置示例：


在 1.20.5+ 上，请改用新的 [Food-Component](/creating-content/items/components)


```yaml
Mechanics:
  food:
    hunger: 10
    saturation: 10
    replacement:
      oraxen_item: any_oraxen_itemid      # 也可以是 minecraft_type 或 crucible_item
    effect_probability: 0.35              # 效果应用的概率，默认为 1.0 / 100%
    effects:
      hunger:                             # 必须是有效的药水效果，可在此找到列表 https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html 
        amplifier: 1                      # 如果未设置，默认为 0
        duration: 20                      # 持续时间（秒）。如果未设置，默认为 1 秒
        is_ambient: true                  # 如果未设置，默认为 true
        has_particles: true               # 如果未设置，默认为 true
        has_icon: true                    # 如果未设置，默认为 true
      night_vision:
        duration: 60
```

### 背包
这允许你将任何物品变成一个背包。


此机制可能导致物品复制问题！如果你发现任何问题，请提交 [bug-report](https://github.com/oraxen/oraxen/issues/new?assignees=&labels=bug&template=bug-report.yml&title=%5BBUG%5D+%3Cname+for+bug%3E)，我们将尽快修复！


目前已知存在一个复制漏洞，如果你的背包使用可堆叠的材质（如纸），请确保将该物品指定为不可堆叠，如下所示。

#### 每个物品的配置
```yml
backpack:
  displayname: backpack
  material: PAPER
  unstackable: true # 建议将其设为不可堆叠以避免上述复制漏洞
  Mechanics:
    backpack:
      rows: 4
      title: "<red>Backpack"                      # 可选，默认："Backpack"
      open_sound: "entity.shulker.open"       # 可选，默认："entity.shulker.open"
      close_sound: "entity.shulker.close"     # 可选，默认："entity.shulker.close"
```

### 音乐唱片
这允许你制作带有自定义声音的自定义音乐唱片。要添加声音，只需按照默认示例将其添加到 `Oraxen/sound.yml` 中。

任何立体声声音都不会在特定位置或跟随实体播放。如果你需要此功能，需要确保你的 .ogg 声音文件是单声道音频格式。



在 1.21+ 上，请改用新的 [JukeboxPlayable-Component](/creating-content/items/components)


`song` 是你在 `sound.yml` 中定义的 namespace:sound.name。如果你的 sound.yml 条目如下所示：
```yml
sounds:
  my_music_disc_song.mysong:
    category: record
    sound: mysong.ogg
```
这意味着你的 .ogg 文件位于路径 `Oraxen/sounds/mysong.ogg`，你的声音 ID 是命名空间为 minecraft 的 `my_music_disc_song.mysong`。如果你将 sounds.json 导入到另一个命名空间，那么该命名空间自然不是 minecraft。
```yml
Mechanics:
  music_disc:
    song: "minecraft:my_music_disc_song.mysong"
```

### 耐久度

这允许你更改使用 Oraxen 创建的物品的耐久度。Minecraft 原版的系统不适合处理这种修改，这就是为什么此系统不完美。你不会在物品上看到正确的耐久度数值，它将作为百分比工作。这意味着，例如你基于木镐（默认耐久度为 59）创建一个镐子并将其改为 5900，你仍然会在物品上看到 59 的耐久度。但你需要破坏 100 个方块才能消耗 1 点耐久度。一个好处是显示的耐久条会被正确更新。


在 1.20.5+ 上，请改用新的 [Durability-Component](/creating-content/items/components)


#### 每个物品的配置

有两个可用选项：ratio 和 fixed_amount。在同一物品上只能使用这两个选项之一。Ratio 允许你修复物品的百分比（0.15 将修复 15% 的最大耐久度，而 1.0 将修复到 100%）。Fixed amount 修复物品的固定耐久度点数（例如，如果你想为物品添加 10 点耐久度，请设置 10）。

```yaml
Mechanics:
  durability:
    value: 5000 # 钻石剑默认为 1561
```

### 效率

在手持物品时给予玩家挖掘速度加成（急迫效果）。使用负值则变为挖掘疲劳。

#### 每个物品的配置

```yaml
Mechanics:
  efficiency:
    amount: 2 # 急迫等级（使用负值获得挖掘疲劳）
```

### 消耗品

使物品在右键时被消耗。使用时物品数量减少 1。

#### 每个物品的配置

```yaml
Mechanics:
  consumable: {}
```

### 消耗品药水效果

在物品被消耗或使用时应用药水效果。这通常与消耗品机制结合使用。

#### 每个物品的配置

```yaml
Mechanics:
  consumable_potion_effects:
    speed:
      amplifier: 1 # 效果等级（0 = 等级 1）
      duration: 600 # 以刻为单位（600 = 30 秒）
      ambient: false
      particles: true
      icon: true
    regeneration:
      amplifier: 0
      duration: 200
```

### 杂项机制
此机制包含了一系列可对物品进行的小更改。它们各自的作用应该非常一目了然。


在 1.20.5+ 上，请改用新的 [FireResistant-Component](/creating-content/items/components) 替代下面的 burns_in_X
在 1.21.2+ 上，请改用新的 [DamageResistant-Component](/creating-content/items/components) 替代下面的 burns_in_X/breaks_from_cactus


```yaml
Mechanics:
  misc:
    breaks_from_cactus: true
    burns_in_fire: true
    burns_in_lava: true
    disable_vanilla_interactions: false
    can_strip_logs: false
    piglins_ignore_when_equipped: false
    compostable: false
    allow_in_vanilla_recipes: true
```

### 修复

此机制允许你使用一个物品来修复另一个物品（使用原版耐久度或或 Oraxen 自定义耐久度）。默认情况下，此机制绑定到铁、金和钻石齿轮。要使用它们，你只需点击你想要修复的物品。

#### 每个物品的配置

```yaml
Mechanics:
  repair:
    ratio: 0.10 # 10%
    fixed_amount: 10 # 或 10 点耐久度
```

#### 全局配置

如果你启用 oraxen_durability_only，此机制将仅适用于使用 Oraxen 耐久度机制的物品。

```yaml
repair:
  enabled: true
  oraxen_durability_only: false
```

### 命令

这允许你执行命令（作为控制台、玩家或 OP 玩家）。如果这个选项通常不是最优雅的，但它有简化很多事情的优点。你可以创建使用之间的冷却时间，检查玩家是否拥有特定权限，并使用物品（即执行命令时物品数量减少 1）。

#### 每个物品的配置

```yaml
Mechanics:
  commands:
    cooldown: 5 # 冷却时间示例（秒）。此为可选
    permission: "my.awesome.perm" # 所需权限。此为可选
    one_usage: true # 使用时是否减少数量？默认：false
    console:
      # 例如：杀死玩家
      - "kill %p%"
    player:
      # 例如：玩家执行 /spawn
      - "spawn"
    opped_player:
      # 例如：玩家给自己一把钻石剑
      - "give diamond_sword 1"
```

### 护甲效果

这允许你将药水效果绑定到护甲（或帽子）上，这样当你装备它时，就会获得该效果。

#### 每个物品的配置

[这里](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html)是所有可用药水效果类型的列表。

```yaml
Mechanics:
  armor_effects:
    night_vision: # 药水效果类型
      duration: 10
      amplifier: 0
      ambient: true # 使药水效果产生更多半透明的粒子。
      particles: true # 此效果是否有粒子
      icon: true # 此效果是否有图标
```

你也可以设置仅在穿戴完整套装时应用效果。
```yaml
Mechanics:
  armor_effects:
    night_vision:
      requires_full_set: true
      ...
```

### 方块和音符盒

这些机制允许你将物品用作方块。由于这些是相当特殊的机制，它们有[专门的教程页面](/creating-content/blocks/noteblock)。

### clickAction

此机制允许你在玩家点击方块或家具时运行各种事件。它非常可自定义，因此也有[专门的教程页面](/creating-content/items/abilities/clickaction)。

### 光环（Aura）

你想在玩家手持你的物品时显示酷炫的粒子效果吗？光环机制就是你的选择。你可以在此处找到可用粒子列表：[https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)

#### 每个物品的配置（简单）

```yaml
Mechanics:
  aura:
    type: simple # 可用类型：[ simple, ring, helix ]
    particle: PORTAL
```

### 帽子

你想创建一个帽子吗？使用此机制，你将能够将任何物品放在你的头上。

#### 每个物品的配置（简单）

```yaml
Mechanics:
  hat:
    enabled: true
```

### 可换肤（Skinnable）

使用此机制，你可以通过使用带有皮肤（Skin）机制的物品来改变物品的纹理。

#### 每个物品的配置

```yaml
Mechanics:
  skinnable: {}
```

### ItemType

使用此机制，你可以更改 OraxenBlocks 检测到的物品类型。请确保使用[在方块机制内部声明](/creating-content/blocks/noteblock#global-configuration)的类型。

#### 每个物品的配置

```yaml
Mechanics:
  itemtype:
    value: SUPER_MATERIAL # 你的 itemType
```

### 灵魂绑定（Soulbound）

使用此机制，你可以防止玩家在死亡时丢失他们的物品。

#### 每个物品的配置

```yaml
Mechanics:
  soulbound:
    lose_chance: 0  # 0-1，死亡时丢失物品的概率（0 = 永不丢失，1 = 总是丢失）
```

### 切换灯光（Toggle-Light）

使用此机制，你可以为家具、音符盒和绊线钩方块创建交互式灯光。玩家可以右键点击这些物品，在基础亮度和切换亮度之间切换其灯光等级，从而允许他们打开和关闭灯光。

- 自定义物品的交互式灯光控制
- 支持静态基础灯光和可切换灯光
- 状态在服务器重启后持久化
- 与现有家具机制无缝集成（屏障、存储、座位、旋转）

**重要提示**
- 对于带屏障的家具：灯光会在家具结构中的所有屏障方块之间切换
- 灯光状态在服务器加载/重载时自动刷新

#### 每个物品的配置

```yaml
Mechanics:
  toggle_light:
    light: 5          # 基础灯光等级（0-15），始终激活
    toggle_light: 15  # 切换灯光等级（0-15），交互时激活
```

- `light`：始终激活的基础灯光等级（0-15）。这是默认状态。
- `toggle_light`：玩家与物品交互时激活的切换灯光等级（0-15）。设置此项以启用可切换灯光。

### 自定义机制

此机制允许你自定义事件、条件和动作。由于这是一个相当特殊的机制，它有[专门的教程页面](/creating-content/items/abilities/custom-ability)。

### 皮肤（Skin）

此机制将允许该物品成为可换肤（Skinnable）机制的皮肤，皮肤和可换肤物品必须具有相同的材质才能应用纹理。

#### 每个物品的配置

```yaml
Mechanics:
  skin: 
    consume: true #消耗 1 个皮肤物品
```