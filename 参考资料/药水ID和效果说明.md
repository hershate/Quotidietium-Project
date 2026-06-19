# 药水ID和效果说明

> 数据来源：Minecraft 中文 Wiki · 版本：Java版 1.21+ / 基岩版 1.21+
> 最后更新：2025-06-19
> 用途：Oraxen 自定义药水 / 服务器插件开发参考

---

## 目录

1. [状态效果 ID 总表](#1-状态效果-id-总表)
2. [药水数据总表](#2-药水数据总表)
3. [药水时长与效果值速查](#3-药水时长与效果值速查)
4. [Oraxen 配置参考](#4-oraxen-配置参考)
5. [参考资料](#5-参考资料)

---

## 1. 状态效果 ID 总表

| 数字ID | 命名空间ID | 中文名称 | 英文名称 | 颗粒颜色 | 类型 | 效果说明 |
|:-----:|:-----------|:--------|:---------|:--------:|:----:|:---------|
| 1 | `minecraft:speed` | 速度 | Speed | `#7CAFC6` | ✅ 正面 | 行走速度 +20%/级 |
| 2 | `minecraft:slowness` | 缓慢 | Slowness | `#5A6C81` | ❌ 负面 | 行走速度 -15%/级 |
| 3 | `minecraft:haste` | 急迫 | Haste | `#D9C043` | ✅ 正面 | 挖掘/攻击速度 +20%/级 |
| 4 | `minecraft:mining_fatigue` | 挖掘疲劳 | Mining Fatigue | `#4A4217` | ❌ 负面 | 挖掘/攻击速度降低 |
| 5 | `minecraft:strength` | 力量 | Strength | `#932423` | ✅ 正面 | 近战伤害 +3/级 |
| 6 | `minecraft:instant_health` | 瞬间治疗 | Instant Health | `#F82423` | ✅ 正面 | 立即治疗，对亡灵生物造成伤害 |
| 7 | `minecraft:instant_damage` | 瞬间伤害 | Instant Damage | `#430A09` | ❌ 负面 | 立即伤害，治疗亡灵生物 |
| 8 | `minecraft:jump_boost` | 跳跃提升 | Jump Boost | `#22FF4C` | ✅ 正面 | 跳跃高度提升，减免摔落伤害 |
| 9 | `minecraft:nausea` | 反胃 | Nausea | `#551D4A` | ❌ 负面 | 视野晃动扭曲 |
| 10 | `minecraft:regeneration` | 生命恢复 | Regeneration | `#CD5CAB` | ✅ 正面 | 每 2.5 秒恢复 1❤️（II 级加快） |
| 11 | `minecraft:resistance` | 抗性提升 | Resistance | `#99453A` | ✅ 正面 | 减免 20% 伤害/级 |
| 12 | `minecraft:fire_resistance` | 防火 | Fire Resistance | `#E49A3A` | ✅ 正面 | 免疫火、岩浆伤害 |
| 13 | `minecraft:water_breathing` | 水下呼吸 | Water Breathing | `#2E5299` | ✅ 正面 | 氧气条不消耗 |
| 14 | `minecraft:invisibility` | 隐身 | Invisibility | `#7F8392` | ✅ 正面 | 实体模型消失（装备仍可见） |
| 15 | `minecraft:blindness` | 失明 | Blindness | `#1F1F23` | ❌ 负面 | 视野黑雾，禁止疾跑 |
| 16 | `minecraft:night_vision` | 夜视 | Night Vision | `#1F1FA1` | ✅ 正面 | 全亮度提升至 15 级 |
| 17 | `minecraft:hunger` | 饥饿 | Hunger | `#587653` | ❌ 负面 | 加快饥饿值消耗（每级 × 食物 exhaustion） |
| 18 | `minecraft:weakness` | 虚弱 | Weakness | `#484D48` | ❌ 负面 | 近战伤害 -4/级 |
| 19 | `minecraft:poison` | 中毒 | Poison | `#4E9331` | ❌ 负面 | 持续伤害（最低保留 1❤️，不致死） |
| 20 | `minecraft:wither` | 凋零 | Wither | `#352A27` | ❌ 负面 | 持续伤害（可致死） |
| 21 | `minecraft:health_boost` | 生命提升 | Health Boost | `#F87D23` | ✅ 正面 | +4❤️ 生命上限/级 |
| 22 | `minecraft:absorption` | 伤害吸收 | Absorption | `#2552A5` | ✅ 正面 | +4❤️ 吸收生命/级 |
| 23 | `minecraft:saturation` | 饱和 | Saturation | `#F82423` | ✅ 正面 | 恢复饥饿值与饱和度 |
| 24 | `minecraft:glowing` | 发光 | Glowing | `#94A061` | ⚪ 中性 | 高亮实体轮廓线（透视） |
| 25 | `minecraft:levitation` | 飘浮 | Levitation | `#CEFFFF` | ⚪ 中性 | 向上飘浮移动 |
| 26 | `minecraft:luck` | 幸运 | Luck | `#339900` | ✅ 正面 | 提升高品质战利品概率 |
| 27 | `minecraft:unluck` | 霉运 | Bad Luck | `#C0A44D` | ❌ 负面 | 降低高品质战利品概率 |
| 28 | `minecraft:slow_falling` | 缓降 | Slow Falling | `#FFEFD1` | ✅ 正面 | 缓降速度，免疫摔落伤害 |
| 29 | `minecraft:conduit_power` | 潮涌能量 | Conduit Power | `#1DC2D1` | ✅ 正面 | 水下视野/挖掘速度提升，免溺水 |
| 30 | `minecraft:dolphins_grace` | 海豚的恩惠 | Dolphin's Grace | `#88AABB` | ✅ 正面 | 游泳速度提升 |
| 31 | `minecraft:bad_omen` | 不祥之兆 | Bad Omen | `#B8B5AB` | ❌ 负面 | 进入村庄触发袭击 |
| 32 | `minecraft:hero_of_the_village` | 村庄英雄 | Hero of the Village | `#44FF44` | ✅ 正面 | 与村民交易降价 |
| — | `minecraft:darkness` | 黑暗 | Darkness | `#222222` | ❌ 负面 | 视野周期性变暗（1.19+） |
| — | `minecraft:wind_charged` | 蓄风 | Wind Charged | `#BDC9FF` | ⚪ 中性 | 被击中时产生风弹（1.21+） |
| — | `minecraft:weaving` | 盘丝 | Weaving | `#78695A` | ❌ 负面 | 死亡后生成蜘蛛网（1.21+） |
| — | `minecraft:oozing` | 渗浆 | Oozing | `#99FFA3` | ⚪ 中性 | 死亡后生成史莱姆（1.21+） |
| — | `minecraft:infested` | 寄生 | Infested | `#8C9B8C` | ❌ 负面 | 受伤时生成蠹虫（1.21+） |
| — | `minecraft:raid_omen` | 袭击之兆 | Raid Omen | `#C04C4C` | ❌ 负面 | 进入村庄触发不祥袭击（1.21+） |
| — | `minecraft:trial_omen` | 试炼之兆 | Trial Omen | `#1F1F8F` | ❌ 负面 | 触发试炼刷怪笼升级（1.21+） |

> 💡 **提示**：数字 ID 在 Java 版 1.13 扁平化后已弃用，新版本请使用命名空间 ID（`minecraft:xxx`）。

---

## 2. 药水数据总表

### 2.1 无效果药水（基底）

| 药水名称 | 命名空间ID | 基岩版数字ID | 颜色 | 备注 |
|:--------|:-----------|:----------:|:----:|:----|
| 水瓶 | `water` | 0 | `#385DC6` | — |
| 平凡的药水 | `mundane` | 1 | `#385DC6` | — |
| 长久平凡药水 | `long_mundane` | 2 | `#385DC6` | 仅基岩版 |
| 浓稠的药水 | `thick` | 3 | `#385DC6` | — |
| 粗制的药水 | `awkward` | 4 | `#385DC6` | 大多数药水的酿造基底 |

### 2.2 有效果药水

> ⏱️ 时间格式为 `分:秒`（如 3:00 = 3 分钟）
>
> 药水 → 喷溅型 → 滞留型 → 药箭分别对应四个时长值

| 药水名称 | 命名空间ID | BE数字ID | 药水颜色 | 效果 | 药水 | 喷溅型 | 滞留型 | 药箭 |
|:--------|:-----------|:-------:|:--------:|:-----|:----:|:------:|:------:|:----:|
| **夜视药水** | `night_vision` | 5 | `#C2FF66` | 夜视 | 3:00 | 3:00 | 0:45 | 0:22 |
| | `long_night_vision` | 6 | `#C2FF66` | 夜视 | 8:00 | 8:00 | 2:00 | 1:00 |
| **隐身药水** | `invisibility` | 7 | `#F6F6F6` | 隐身 | 3:00 | 3:00 | 0:45 | 0:22 |
| | `long_invisibility` | 8 | `#F6F6F6` | 隐身 | 8:00 | 8:00 | 2:00 | 1:00 |
| **跳跃药水** | `leaping` | 9 | `#FDFF84` | 跳跃提升 I | 3:00 | 3:00 | 0:45 | 0:22 |
| | `long_leaping` | 10 | `#FDFF84` | 跳跃提升 I | 8:00 | 8:00 | 2:00 | 1:00 |
| | `strong_leaping` | 11 | `#FDFF84` | 跳跃提升 II | 1:30 | 1:30 | 0:22 | 0:11 |
| **抗火药水** | `fire_resistance` | 12 | `#FF9900` | 防火 | 3:00 | 3:00 | 0:45 | 0:22 |
| | `long_fire_resistance` | 13 | `#FF9900` | 防火 | 8:00 | 8:00 | 2:00 | 1:00 |
| **迅捷药水** | `swiftness` | 14 | `#33EBFF` | 速度 I (+20%) | 3:00 | 3:00 | 0:45 | 0:22 |
| | `long_swiftness` | 15 | `#33EBFF` | 速度 I (+20%) | 8:00 | 8:00 | 2:00 | 1:00 |
| | `strong_swiftness` | 16 | `#33EBFF` | 速度 II (+40%) | 1:30 | 1:30 | 0:22 | 0:11 |
| **迟缓药水** | `slowness` | 17 | `#8BAFE0` | 缓慢 I (-15%) | 1:30 | 1:30 | 0:22 | 0:11 |
| | `long_slowness` | 18 | `#8BAFE0` | 缓慢 I (-15%) | 4:00 | 4:00 | 1:00 | 0:30 |
| | `strong_slowness` | 42 | `#8BAFE0` | 缓慢 IV (-60%) | 0:20 | 0:20 | 0:05 | 0:02 |
| **水肺药水** | `water_breathing` | 19 | `#98DAC0` | 水下呼吸 | 3:00 | 3:00 | 0:45 | 0:22 |
| | `long_water_breathing` | 20 | `#98DAC0` | 水下呼吸 | 8:00 | 8:00 | 2:00 | 1:00 |
| **治疗药水** | `healing` | 21 | `#F82423` | 瞬间治疗 | 即时 | 即时 | 即时 | 即时 |
| | `strong_healing` | 22 | `#F82423` | 瞬间治疗 II | 即时 | 即时 | 即时 | 即时 |
| **伤害药水** | `harming` | 23 | `#A9656A` | 瞬间伤害 | 即时 | 即时 | 即时 | 即时 |
| | `strong_harming` | 24 | `#A9656A` | 瞬间伤害 II | 即时 | 即时 | 即时 | 即时 |
| **剧毒药水** | `poison` | 25 | `#87A363` | 中毒 | 0:45 | 0:45 | 0:11 | 0:05 |
| | `long_poison` | 26 | `#87A363` | 中毒 | 1:30 | 1:30 | 0:22 | 0:11 |
| | `strong_poison` | 27 | `#87A363` | 中毒 II | 0:21 | 0:21 | 0:05 | 0:02 |
| **再生药水** | `regeneration` | 28 | `#CD5CAB` | 生命恢复 | 0:45 | 0:45 | 0:11 | 0:05 |
| | `long_regeneration` | 29 | `#CD5CAB` | 生命恢复 | 1:30 | 1:30 | 0:22 | 0:11 |
| | `strong_regeneration` | 30 | `#CD5CAB` | 生命恢复 II | 0:22 | 0:22 | 0:05 | 0:02 |
| **力量药水** | `strength` | 31 | `#FFC700` | 力量 I (+3 攻击) | 3:00 | 3:00 | 0:45 | 0:22 |
| | `long_strength` | 32 | `#FFC700` | 力量 I (+3 攻击) | 8:00 | 8:00 | 2:00 | 1:00 |
| | `strong_strength` | 33 | `#FFC700` | 力量 II (+6 攻击) | 1:30 | 1:30 | 0:22 | 0:11 |
| **虚弱药水** | `weakness` | 34 | `#484D48` | 虚弱 (-4 攻击) | 1:30 | 1:30 | 0:22 | 0:11 |
| | `long_weakness` | 35 | `#484D48` | 虚弱 (-4 攻击) | 4:00 | 4:00 | 1:00 | 0:30 |
| **幸运药水** | `luck` | — | `#59C106` | 幸运 (+1 幸运值) | 5:00 | 5:00 | 1:15 | 0:37 |
| | | | | | ⚠️ 仅 Java 版 | | | |
| **衰变药水** | `wither` | 36 | `#736156` | 凋零 II | 0:40 | 0:40 | — | — |
| | | | | | ⚠️ 仅基岩版 | | | |
| **神龟药水** | `turtle_master` | 37 | `#8B80E3` | 缓慢 IV + 抗性提升 III | 0:20 | 0:20 | 0:05 | 0:02 |
| | `long_turtle_master` | 38 | `#8B80E3` | 缓慢 IV + 抗性提升 III | 0:40 | 0:40 | 0:10 | 0:05 |
| | `strong_turtle_master` | 39 | `#8D85E6` | 缓慢 VI + 抗性提升 IV | 0:20 | 0:20 | 0:05 | 0:02 |
| **缓降药水** | `slow_falling` | 40 | `#FFEFD1` | 缓降 | 1:30 | 1:30 | 0:22 | 0:11 |
| | `long_slow_falling` | 41 | `#FFEFD1` | 缓降 | 4:00 | 4:00 | 1:00 | 0:30 |
| **蓄风药水** | `wind_charged` | 43 | `#BDC9FF` | 蓄风 | 3:00 | 3:00 | 0:45 | 0:22 |
| **盘丝药水** | `weaving` | 44 | `#78695A` | 盘丝 | 3:00 | 3:00 | 0:45 | 0:22 |
| **渗浆药水** | `oozing` | 45 | `#99FFA3` | 渗浆 | 3:00 | 3:00 | 0:45 | 0:22 |
| **虫蚀药水** | `infested` | 46 | `#8C9B8C` | 寄生 | 3:00 | 3:00 | 0:45 | 0:22 |

> 🔴 **注意**：1.21+ 新增药水（蓄风/盘丝/渗浆/虫蚀）目前 **不可酿造**，仅可通过 `/effect` 命令或试炼密室获取。

---

## 3. 药水时长与效果值速查

### 3.1 时长倍率关系

| 药水类型 | 相对于普通药水的时长倍率 |
|:--------|:---------------------:|
| 普通药水（饮用） | 1×（基准） |
| 喷溅型药水 | 1×（与普通相同） |
| 滞留型药水 | 0.25×（1/4） |
| 药箭 | 0.125×（1/8） |

### 3.2 不同等级前缀的命名约定

| 前缀 | 含义 | 等级倍率（amplifier） | 示例 |
|:----|:----|:-------------------:|:-----|
| `long_` | 延长版（时长增加） | 不变（amplifier = 0） | `long_swiftness` → 速度 8:00 |
| `strong_` | 强化版（等级+1） | 时长减半 | `strong_swiftness` → 速度 II 1:30 |

### 3.3 瞬间效果的特殊说明

| 效果 | 等级 I 治疗/伤害量 | 等级 II 治疗/伤害量 | 对亡灵生物 |
|:----|:----------------:|:-----------------:|:----------|
| 瞬间治疗 | 恢复 4❤️（2 点） | 恢复 8❤️（4 点） | ❌ 造成伤害 |
| 瞬间伤害 | 造成 6❤️（3 点） | 造成 12❤️（6 点） | ✅ 治疗 |

### 3.4 神龟药水组合效果

| 变体 | 速度效果 | 抗性效果 |
|:----|:---------|:---------|
| `turtle_master` | 缓慢 IV（-60% 速度） | 抗性提升 III（-60% 伤害） |
| `long_turtle_master` | 缓慢 IV（-60% 速度） | 抗性提升 III（-60% 伤害） |
| `strong_turtle_master` | 缓慢 VI（-90% 速度） | 抗性提升 IV（-80% 伤害） |

---

## 4. Oraxen 食物配置参考

> 📌 本节配置格式严格参考同目录下的 [Oraxen_food_template.md](Oraxen_food_template.md) 模板文件。
>
> Oraxen 使用 Components 系统（1.21+ 组件格式），**不再使用**旧版 `Effects:` 数组。

### 4.1 食物模板格式

```yaml
<食物ID>:
  itemname: <显示名称>                        # 支持渐变颜色 <gradient:#c1:#c2>
  material: PAPER                             # 基础材质（建议使用 PAPER 自定义模型）
  Components:
    food:                                     # 食物组件
      nutrition: <数值>                        # 饱食度恢复量
      saturation: <数值>                       # 饱和度附加（通常 = nutrition × 1.6）
      can_always_eat: <true/false>             # 是否可在饱腹时继续吃
    consumable:                               # 食用组件
      consume_seconds: <秒数>                   # 食用所需时间（秒）
      animation: <EAT/DRINK>                   # 食用动画（EAT=吃, DRINK=喝）
      sound: <声音ID>                          # 食用音效（如 entity.generic.eat）
      has_consume_particles: <true/false>      # 是否显示食用颗粒
      on_consume_effects:                      # 食用后效果列表
        - type: apply_effects                  # 效果类型：应用状态效果
          effects:
            minecraft:<效果ID>:                 # 使用命名空间ID（见 §1 总表）
              duration: <刻数>                  # 持续时间（20刻=1秒）
              amplifier: <数值>                 # 等级-1（0=I级, 1=II级, 2=III级）
              ambient: <true/false>             # 是否来自环境（影响颗粒透明度）
              show_particles: <true/false>      # 是否显示效果颗粒
              show_icon: <true/false>           # 是否显示效果图标
          probability: <0.0~1.0>               # 触发概率（1.0 = 100%）
  Pack:
    generate_model: true                       # 自动生成模型
    parent_model: item/generated               # 父模型
    textures:
      - <材质路径.png>                          # 材质文件路径
```

### 4.2 示例（来自模板文件）

```yaml
miner_sandwich:
  itemname: <gradient:#F69D84:#FAD98D>Miner's Sandwich
  material: PAPER
  Components:
    food:
      nutrition: 8
      saturation: 12.8
      can_always_eat: true
    consumable:
      consume_seconds: 5
      animation: EAT
      sound: entity.generic.eat
      has_consume_particles: true
      on_consume_effects:
        - type: apply_effects
          effects:
            minecraft:haste:
              duration: 3600
              amplifier: 0
              ambient: true
              show_particles: true
              show_icon: true
          probability: 1.0
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - default/sandwich.png
```

### 4.3 字段详解

| 字段 | 说明 | 建议值 |
|:----|:----|:-------|
| `nutrition` | 恢复的饱食度（鸡腿数 × 2） | 普通食物 4~8，高级食物 8~12 |
| `saturation` | 附加饱和度（先消耗这个） | 通常 = nutrition × 1.2~1.6 |
| `can_always_eat` | 能否在满饱时吃 | 恢复类食物建议 `true` |
| `consume_seconds` | 吃/喝耗时（秒） | 普通 1.6s，大餐 3~5s |
| `animation` | 动画类型 | 固体食物用 `EAT`，液体用 `DRINK` |
| `sound` | 音效 | 吃: `entity.generic.eat`，喝: `entity.generic.drink` |
| `probability` | 效果触发概率 | 必触发用 `1.0`，概率触发用 `0.3`~`0.5` |
| `amplifier` | 效果等级 | 0=I级, 1=II级, 2=III级... |

### 4.4 时长换算参考

| 游戏内时间 | 刻（tick） | 秒 | 适用场景 |
|:----------|:----------:|:--:|:--------|
| 2 秒 | 40 | 2s | 瞬时/短效 |
| 5 秒 | 100 | 5s | 药箭等级II |
| 11 秒 | 220 | 11s | 药箭等级I |
| 22 秒 | 450 | 22s | 滞留II / 药箭延长 |
| 30 秒 | 600 | 30s | 短时增益 |
| 45 秒 | 900 | 45s | 滞留型药水 |
| 1:00 | 1200 | 60s | 药箭延长版 |
| 1:30 | 1800 | 90s | 普通II/缓降 |
| 2:00 | 2400 | 120s | 滞留延长 |
| 3:00 | 3600 | 180s | 普通药水 / 常用食物效果 |
| 5:00 | 6000 | 300s | 幸运药水 / 长时食物效果 |
| 8:00 | 9600 | 480s | 延长版药水 |
| 10:00 | 12000 | 600s | 自定义长时间增益 |
| 30:00 | 36000 | 1800s | 信标范围效果 |

### 4.5 多种效果配置示例

```yaml
# 同时应用多个状态效果
festive_feast:
  itemname: <gradient:#FF6B6B:#FFE66D>Festive Feast
  material: PAPER
  Components:
    food:
      nutrition: 10
      saturation: 16
      can_always_eat: true
    consumable:
      consume_seconds: 4
      animation: EAT
      sound: entity.generic.eat
      has_consume_particles: true
      on_consume_effects:
        - type: apply_effects
          effects:
            minecraft:strength:
              duration: 3600
              amplifier: 0
              ambient: true
              show_particles: true
              show_icon: true
            minecraft:resistance:
              duration: 3600
              amplifier: 0
              ambient: true
              show_particles: true
              show_icon: true
            minecraft:regeneration:
              duration: 1800
              amplifier: 0
              ambient: true
              show_particles: true
              show_icon: true
          probability: 1.0
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - default/feast.png

# 概率触发效果（30% 几率获得速度 II）
lucky_cookie:
  itemname: <gradient:#F6D365:#FDA085>Lucky Cookie
  material: PAPER
  Components:
    food:
      nutrition: 2
      saturation: 0.4
      can_always_eat: true
    consumable:
      consume_seconds: 1
      animation: EAT
      sound: entity.generic.eat
      has_consume_particles: false
      on_consume_effects:
        - type: apply_effects
          effects:
            minecraft:speed:
              duration: 1200
              amplifier: 1
              ambient: false
              show_particles: false
              show_icon: true
          probability: 0.3
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - default/cookie.png
```

### 4.6 常用效果ID索引（对应 §1 总表）

| 用途 | 效果ID (minecraft:xxx) | amplifier | duration(刻) | 效果简述 |
|:----|:----------------------|:---------:|:------------:|:---------|
| 加速挖掘 | `haste` | 0~1 | 3600~7200 | 挖掘速度 +20%/级 |
| 增加伤害 | `strength` | 0~1 | 3600 | 近战伤害 +3/级 |
| 快速回血 | `regeneration` | 0~2 | 600~1800 | 每 2.5 秒回血 |
| 减免伤害 | `resistance` | 0~3 | 3600 | 减伤 20%/级 |
| 加速移动 | `speed` | 0~2 | 1800~3600 | 移速 +20%/级 |
| 跳跃提升 | `jump_boost` | 0~1 | 3600 | 跳得更高 |
| 防火 | `fire_resistance` | 0 | 3600~9600 | 免疫火伤 |
| 夜视 | `night_vision` | 0 | 3600~9600 | 全亮度 |
| 水下呼吸 | `water_breathing` | 0 | 3600~9600 | 氧气不耗 |
| 伤害吸收 | `absorption` | 0~4 | 1200~3600 | +4❤️吸收/级 |
| 饱和 | `saturation` | 0 | 1 | 瞬间恢复饱食度 |

### 4.7 常用指令

```mcfunction
# 给予普通速度效果（I级，30秒）
/effect give @s minecraft:speed 30 0

# 给予速度 II（30秒）
/effect give @s minecraft:speed 30 1

# 清除所有效果
/effect clear @s

# 清除指定效果
/effect clear @s minecraft:speed

# Oraxen 获取自定义食物物品
# 使用 Oraxen 的 give 命令
# /oraxen give <玩家> <食物ID>

---

## 5. 参考资料

- [Minecraft 中文 Wiki - 药水效果](https://zh.minecraft.wiki/w/%E8%8D%AF%E6%B0%B4%E6%95%88%E6%9E%9C?variant=zh-cn)
- [Minecraft 中文 Wiki - 状态效果](https://zh.minecraft.wiki/w/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C)
- [Minecraft 中文 Wiki - 药水](https://zh.minecraft.wiki/w/%E8%8D%AF%E6%B0%B4)
- [Minecraft 中文 Wiki - Java版数据值](https://zh.minecraft.wiki/w/Java%E7%89%88%E6%95%B0%E6%8D%AE%E5%80%BC?variant=zh-cn)
- [Minecraft Wiki - Potion (English)](https://minecraft.wiki/w/Potion)
- [百度百科 - 药水效果](https://baike.baidu.com/item/%E8%8D%AF%E6%B0%B4%E6%95%88%E6%9E%9C/19372833)

---

> 📝 **维护说明**：本文档基于 Minecraft 1.21 版本数据整理。每次大版本更新后，请检查是否有新药水效果加入，并及时更新表格。
