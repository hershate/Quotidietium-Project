# 条件

条件用于设置完成成就所需满足的要求。<br/>
以下是内置条件的列表：

:::info
默认情况下，所有实体、物品等列表均被视为**白名单**。<br/>
若要将其设为**黑名单**，请添加 `blacklist: true`。

黑名单示例：
```yaml
conditions:
  - type: items
    items:
      - "NETHERITE_INGOT"
    blacklist: true
```
:::
:::tip
大多数条件类型支持**通配符**：
```yaml
conditions:
  - type: items
    items:
      - "*_PICKAXE" # 匹配所有类型的镐
```
:::

## 版本 1.0

### 全局条件
适用于所有类型的成就。

| 条件 | 描述 | 示例 |
|------|------|------|
| `game-modes` | 允许的游戏模式 | `- SURVIVAL` |
| `worlds` | 允许的世界 | `- "world"` |
| `item-in-hand` | 要求玩家手中持有物品 | `- <material>` |
| `item-equipped` | 要求玩家装备了物品 | `- <material>` |
| `riding-entity` | 要求玩家骑乘实体 | `- ALL`<br/>`- <entity>` |
| `regions` | [WorldGuard](https://dev.bukkit.org/projects/worldguard) 区域列表 | `- <region-id>` |
| `is-sneaking` | 要求玩家处于潜行状态 | `true` `false` |
| `is-sprinting` | 要求玩家处于疾跑状态 | `true` `false` |
| `is-flying` | 要求玩家处于飞行状态 | `true` `false` |
| `has-open-inventory` | 检查玩家是否打开了某个界面。<br/>无法检查玩家是否打开了自身的物品栏。 | `true` `false` |

### 任务特定条件
仅适用于某些类型的成就。

| 条件 | 描述 | 示例 |
|------|------|------|
| `entities` | 实体列表 | `- CHICKEN`<br/>`- mythicmobs:<mob-id>`<br/>`- mm:<mob-id>` |
| `items` | 物品列表 | `- <material>` |
| `blocks` | 方块列表 | `- <material>` |
| `potion-effects` | [药水类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionType.html)列表 | `- SWIFTNESS` |
| `crop-age` | 指定作物生长阶段 | `MAX` `<age>` |

### 全局条件
适用于所有类型的成就。

| 条件 | 描述 | 必要参数 |
|------|------|------|
| `game_modes` | 允许的游戏模式 | `game-modes` |
| `worlds` | 允许的世界 | `worlds` |
| `biomes` | 允许的生物群系 | `biomes` |
| `has_item` | 要求玩家物品栏中有某物品 | `items` |
| `has_held` | 要求玩家手中持有物品 | `items` |
| `has_equipped` | 要求玩家装备了物品 | `items` |
| `riding_entity` | 要求玩家骑乘实体 | `entities` |
| `is_sneaking` | 要求玩家处于潜行状态 | `value` (true/false) |
| `is_sprinting` | 要求玩家处于疾跑状态 | `value` (true/false) |
| `is_flying` | 要求玩家处于飞行状态 | `value` (true/false) |
| `has_inventory_open` | 检查玩家是否打开了某个界面。<br/>无法检查玩家是否打开了自身的物品栏。 | `value` (true/false) |

### 插件钩子

| 插件 | 条件 | 描述 | 必要参数 |
|------|------|------|------|
| [WorldGuard](https://dev.bukkit.org/projects/worldguard) | `regions` | 检查玩家是否位于某个区域内 | `regions` |
| [Vault](https://www.spigotmc.org/resources/34315/) | `vault` | 检查玩家是否拥有指定数量的金钱 | `balance` |
| [PlaceholderAPI](https://www.spigotmc.org/resources/6245/) | `placeholder` | 评估 PAPI 占位符 | [`placeholder` `value` `operator`](./tasks/placeholder#placeholders-that-output-text) |
| [CustomFishing](https://polymart.org/resource/customfishing.2723) | `custom_fishing_loot` | 战利品 ID 列表 | `loot` |

### 其他条件
仅适用于某些类型的成就：请参阅[任务](./tasks)文档。

| 条件 | 描述 | 必要参数 |
|------|------|------|
| `entities` | 实体列表<br/>支持 **MythicMobs**：`mythicmobs:<id>` 或 `mm:<id>` | `entities` |
| `is_hostile` | 检查实体是否为敌对 | `value` (true/false) |
| `items` | 物品列表 | `items` |
| `blocks` | 方块列表 | `blocks` |
| `potion_types` | [药水类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionType.html)列表 | `types` |
| `crop_age` | 指定作物生长阶段 | `age` (生长阶段/`MAX`) |
| `damage_causes` | [伤害原因](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)列表 | `causes` |
