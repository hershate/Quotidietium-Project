---
description: 武器和法术的战斗机制
---

import { Callout } from 'nextra/components'

# 战斗机制

<Callout type="info">
所有基于法术的战斗机制（雷神、能量冲击波、凋零骷髅头、火球）都支持 `charges` 选项，该选项限制物品在消耗前的使用次数。设置为 `-1` 或不设置以允许无限使用。
</Callout>

### 长矛突刺

<Callout type="info">
需要 Minecraft 1.21.4+ 以在蓄力动画期间进行模型交换。
</Callout>

一种蓄力攻击机制，可将你的武器转变为毁灭性的突刺。按住右键蓄力，然后松开或左键向前突刺，对路径上的敌人造成伤害。

#### 特性

- **模型动画**：武器模型在蓄力期间视觉上会过渡（需要 1.21.4+）
- **流畅动画**：可选的中间帧用于流畅的蓄力动画
- **多目标**：具有可配置穿透能力的突刺路径，可命中多个敌人
- **移动减速**：可配置蓄力时的速度降低
- **完全自定义**：粒子、声音、伤害、范围和击退均可配置

#### 每个物品的配置

```yaml
my_spear:
  material: IRON_SWORD
  displayname: "<gradient:#gold:#yellow>Battle Spear"
  Pack:
    generate_model: false
    model: default/spear_inactive  # 基础模型（待机位置）
  Mechanics:
    spear_lunge:
      active_model: default/spear_active  # 完全蓄力时的模型（突刺位置）
      intermediate_models:                 # 蓄力期间的可选动画帧
        - default/spear_frame0
        - default/spear_frame1
      smooth_frames: 2          # 使用的中间帧数量
      charge_ticks: 20          # 蓄满力需要的刻数（20 = 1 秒）
      lunge_velocity: 0.8       # 突刺释放时的向前速度
      max_range: 5.0            # 命中检测范围（以方块计）
      damage: 10.0              # 满蓄力时的伤害
      min_damage: 2.0           # 最低蓄力时的最小伤害
      knockback: 0.8            # 对目标施加的击退
      hitbox_radius: 0.5        # 命中检测的射线追踪宽度
      min_charge_percent: 0.25  # 攻击所需的最小蓄力百分比（25%）
      charge_slowdown: 0.5      # 蓄力时的移动减速（0.0-1.0）
      max_hold_ticks: 60        # 自动取消前的最大保持时间（刻）
      max_targets: 3            # 每次突刺命中的最大敌人数
      particles:
        enabled: true
        charge: CRIT            # 蓄力期间的粒子
        lunge: SWEEP_ATTACK     # 突刺时的粒子
        hit: DAMAGE_INDICATOR   # 命中敌人时的粒子
      sounds:
        enabled: true
        charge: ITEM_TRIDENT_RIPTIDE_1
        lunge: ENTITY_PLAYER_ATTACK_SWEEP
        hit: ENTITY_PLAYER_ATTACK_STRONG
```

#### 配置选项

| 选项 | 默认值 | 描述 |
|--------|---------|-------------|
| `active_model` | - | 完全蓄力时的模型路径（动画所需） |
| `intermediate_models` | - | 流畅蓄力动画的模型路径列表 |
| `smooth_frames` | 0 | 蓄力期间使用的动画帧数 |
| `charge_ticks` | 12 | 达到满蓄力所需的刻数（20 刻 = 1 秒） |
| `lunge_velocity` | 0.6 | 突刺时的向前速度倍率 |
| `max_range` | 3.5 | 最大命中检测范围（以方块计） |
| `damage` | 6.0 | 满蓄力时的基础伤害 |
| `min_damage` | 0.0 | 最低有效蓄力时的最小伤害（按比例从 `min_damage` 到满蓄力的 `damage`） |
| `knockback` | 0.5 | 对目标施加的击退强度 |
| `hitbox_radius` | 0.5 | 命中检测的射线追踪宽度（更高 = 更容易命中偏离中心的目标，最大 5.0） |
| `min_charge_percent` | 0.3 | 攻击所需的最小蓄力百分比（0.0-1.0） |
| `charge_slowdown` | 0.4 | 蓄力时的移动速度降低（0.0 = 无，1.0 = 冻结） |
| `max_hold_ticks` | 60 | 自动取消前保持蓄力的最大刻数 |
| `max_targets` | 1 | 每次突刺命中的最大敌人数 |

#### 工作原理

1. **开始蓄力**：手持长矛按住右键开始蓄力
2. **视觉反馈**：武器模型在帧之间动画过渡，生成粒子，你的移动速度变慢
3. **攻击**：蓄力后松开右键或左键向前突刺
4. **伤害**：你前方射线上的敌人受到按蓄力百分比缩放（从 `min_damage` 到 `damage`）的伤害
5. **冷却时间**：攻击后，有一个短暂的冷却时间才能再次蓄力

<Callout type="warning">
如果你蓄力太久（超过 `max_hold_ticks`），攻击将自动取消并恢复到非活动模型，不会造成伤害。这可以防止玩家无限期地带着蓄力武器四处走动。
</Callout>

### 雷神（Thor）

你是否曾梦想过能够投掷闪电？这就是为你准备的。

#### 每个物品的配置

```yaml
Mechanics:
  thor:
    lightning_bolts_amount: 5
    random_location_variation: 1.5
    delay: 20000 # 以毫秒为单位（20000ms = 20s）
    charges: -1 # 可选：物品消耗前的使用次数（-1 为无限）
```

* **lightning_bolts_amount**：将生成多少道闪电？
* **random_location_variation**：闪电之间的随机变化范围（以方块计）
* **delay**：使用之间的延迟（毫秒）（1000ms = 1s）

### 生命吸取（Lifeleech）

想要在击中对手时窃取他们的生命值吗？

#### 每个物品的配置

```yaml
Mechanics:
  lifeleech:
    amount: 2 # 从对手那里窃取的半颗心数量
```

### 流血（Bleeding）

让你的敌人流血持续特定时间。

#### 每个物品的配置

```yaml
Mechanics:
  bleeding:
    chance: 0.3 # 30% 概率在命中时施加流血
    duration: 100 # 流血持续 100 刻（5 秒）
    damage_per_interval: 0.5 # 每个间隔造成 0.5 伤害（1/4 心）
    interval: 20 # 每 20 刻（1 秒）施加一次伤害
```

* **chance**：命中时施加流血的概率
* **duration**：流血的持续时间（刻）（20 刻 = 1 秒）
* **damage_per_interval**：每个间隔造成的伤害
* **interval**：伤害之间的间隔（刻）（20 刻 = 1 秒）

### 能量冲击波（EnergyBlast）

能量冲击波是一个非常酷的机制，它创建一个粒子锥形区域来攻击实体。

#### 每个物品的配置

```yaml
Mechanics:
  energyblast:
    delay: 20000
    length: 5
    damage: 10.0
    charges: -1 # 可选：物品消耗前的使用次数（-1 为无限）
    particle:
      type: REDSTONE # 只有 REDSTONE 粒子可以改变大小和颜色
      size: 1
      color:
        red: 0
        green: 255
        blue: 255
```

### 凋零骷髅头（Witherskull）

右键时发射凋零骷髅头！

#### 每个物品的配置

```yaml
Mechanics:
  witherskull:
    charged: false # 充能的骷髅头可以破坏方块
    delay: 3000 # 以毫秒为单位（3000ms = 3s）
    charges: -1 # 可选：物品消耗前的使用次数（-1 为无限）
```

### 火球（Fireball）

右键时发射火球！火球在撞击时爆炸。

#### 每个物品的配置

```yaml
Mechanics:
  fireball:
    delay: 3000 # 以毫秒为单位（3000ms = 3s）
    yield: 2.0 # 爆炸威力
    speed: 1.0 # 弹射物速度
    charges: 5 # 可选：物品消耗前的使用次数（-1 为无限）
```

### 击退连击（Knockback Strike）

一种基于连击的击退机制，在命中一定次数的连续攻击后触发。非常适合奖励持续战斗参与的武器。

#### 特性

- **命中追踪**：计数连续命中次数，达到阈值时触发击退
- **可自定义击退**：配置水平和垂直击退力度
- **粒子效果**：击退触发时显示粒子
- **声音效果**：击退激活时播放声音
- **自动重置**：命中计数器在可配置的超时后重置
- **线程安全**：兼容 Folia 的多线程服务器实现

#### 每个物品的配置

```yaml
legendary_hammer:
  displayname: "<gradient:#F06966:#FAD6A6>Legendary Hammer"
  material: DIAMOND_PICKAXE
  lore:
    - "<#ff455b>» <#D5D6D8>Strike your enemies with a devastating blow"
    - "<#ff455b>» <#D5D6D8>On the 15th hit, the player is launched forward"
  Mechanics:
    knockback_strike:
      required_hits: 15              # 触发击退所需的命中次数
      knockback_horizontal: 2.0      # 水平力度（向后推）
      knockback_vertical: 1.2        # 垂直力度（向上击飞）
      reset_time: 80                 # 命中计数器重置前的刻数（20 = 1 秒）
      play_sound: true               # 击退触发时播放声音
      sound_type: ENTITY_ENDER_DRAGON_HURT  # 播放的声音
      sound_volume: 1.5              # 声音音量（0.0-2.0）
      sound_pitch: 0.8               # 声音音调（0.5-2.0，更低 = 更深沉）
      particle:
        type: DUST                   # 生成的粒子类型
        count: 200                   # 粒子数量
        spread: 0.5                  # 粒子扩散半径（以方块计）
```

#### 配置选项

| 选项 | 默认值 | 描述 |
|--------|---------|-------------|
| `required_hits` | 3 | 触发击退所需的连续命中次数（1-20） |
| `knockback_horizontal` | 2.0 | 将目标向后推的水平击退力度（0.0-10.0） |
| `knockback_vertical` | 0.5 | 将目标向上击飞的垂直击退力度（0.0-5.0） |
| `reset_time` | 60 | 未命中后命中计数器重置前的刻数（20-200） |
| `play_sound` | true | 击退触发时是否播放声音 |
| `sound_type` | ENTITY_PLAYER_ATTACK_KNOCKBACK | 击退时播放的声音 |
| `sound_volume` | 1.0 | 声音音量（0.0-2.0） |
| `sound_pitch` | 1.0 | 声音音调（0.5-2.0） |
| `particle.type` | CRIT | 显示的粒子类型 |
| `particle.count` | 20 | 生成的粒子数量（1-100） |
| `particle.spread` | 0.5 | 粒子扩散半径（以方块计）（0.0-5.0） |

#### 支持的粒子类型

常见粒子类型包括：`CRIT`、`EXPLOSION_NORMAL`、`FLAME`、`SPELL_WITCH`、`DUST`（彩色）、`CLOUD`、`DRAGON_BREATH`、`SWEEP_ATTACK` 等等。`DUST` 粒子类型显示为红色粉尘。

#### 工作原理

1. **命中追踪**：每次你用武器命中实体时，计数器递增
2. **超时重置**：如果你在 `reset_time` 刻内没有命中另一次，计数器重置为零
3. **击退触发**：当命中次数达到 `required_hits` 时，对目标施加击退
4. **效果**：粒子在目标位置生成，声音播放（如果启用）
5. **计数器重置**：触发后，计数器重置，循环重新开始

<Callout type="info">
此机制通过 ProtectionLib 尊重保护插件。击退不会在 PvP 被禁用的受保护区域触发。
</Callout>