# 任务

EpicAchievements 提供了多种内置任务类型。<br/>
您可以在下表中找到它们：

### v2.0
| 任务 | 描述 | [支持的条件](/epicachievements/configuration/conditions) | 最低 Minecraft 版本 | 需要 Paper |
|------|------|-------|------------|------|
| `ADVANCEMENT` | 完成一个进度<br/>需要[额外设置](tasks/advancement) | | 1.12 | |
| `BREAK` | 破坏一个方块 | `blocks` `crop_age` | 1.8 | |
| `BREED` | 繁殖一个实体 | `entities` `is_hostile` | 1.10 | |
| `BREW` | 酿造一个物品 | `items` `potion_types` | 1.18 | |
| `CHAT` | 发送一条聊天消息 | | 1.8 | |
| `COMMAND` | 执行一条命令<br/>需要[额外设置](tasks/command) | | 1.8 | |
| `CONSUME` | 消耗一个物品 | `items` | 1.8 | |
| `CRAFT` | 合成一个物品 | `items` | 1.8 | |
| `DAMAGE` | 对实体造成伤害 | `entities` `is_hostile` `damage_causes` | 1.8 | |
| `DEATH` | 死亡 | `damage_causes` | 1.8 | |
| `DROP` | 丢弃一个物品 | `items` | 1.8 | |
| `ENCHANT` | 附魔一个物品 | `items` | 1.8 | |
| `ENTER_VEHICLE` | 进入载具 | `entities` `is_hostile` | 1.8 | |
| `EXIT_VEHICLE` | 离开载具 | `entities` `is_hostile` | 1.8 | |
| `EXPERIENCE` | 获得经验等级 | | 1.8 | |
| `HARVEST` | 收获一个方块 | `blocks` `crop_age` | 1.16 | |
| `FISH` | 钓鱼时获得物品 | `items` | 1.8 | |
| `INTERACT` | 右键点击方块 | `blocks` | 1.8 | |
| `JUMP` | 跳跃 | | 1.12 | **是** |
| `KILL` | 击杀一个实体 | `entities` `is_hostile` | 1.8 | |
| `KILL_TOTEM` | 击杀持有不死图腾的玩家 | | 1.11 | |
| `MILK` | 给实体挤奶 | | 1.8 | |
| `PICKUP` | 拾取一个物品 | `items` | 1.8 | |
| `PLACE` | 放置一个方块 | `blocks` `crop_age` | 1.8 | |
| `PLAYTIME` | 游玩一定时长（以**秒**为单位） | | 1.8 | |
| `RAID` | 赢得一次袭击 | | 1.14 | |
| `RESURRECT` | 使用不死图腾复活 | | 1.11 | |
| `SHEAR` | 给实体剪毛 | `entities` `is_hostile` | 1.8 | |
| `SHOOT` | 使用弓/弩射出弹射物 | | 1.8 | |
| `SLEEP` | 上床睡觉 | | 1.14 | |
| `SMELT` | 烧炼一个物品 | `items` | 1.8 | |
| `TAME` | 驯服一个实体 | `entities` `is_hostile` | 1.8 | |
| `TRADE` | 与村民交易 | `items` | 1.16 | **是** |
| `WALK` | 行走一定数量方块 | | 1.8 | |
| `NONE` | 不与任何游戏内动作关联。只能通过[管理员命令](../commands-and-permissions#admin-commands)进行进度推进。 | | 1.8 | |

### 插件集成
| 插件 | 任务 | 描述 | 支持的条件 |
|------|------|------|------|
| [PlaceholderAPI](https://www.spigotmc.org/resources/6245/) | `PLACEHOLDER` | 评估一个占位符。需要[额外设置](tasks/placeholder) | |
| [CustomFishing](https://polymart.org/resource/2723/) | `CUSTOM_FISHING` | 捕获 CustomFishing 的战利品 | `custom_fishing_loot` |
| [EconomyShopGUI](https://www.spigotmc.org/resources/economyshopgui.69927/) | `ECONOMY_SHOP_GUI:BUY` | 购买物品 | `items` |
| | `ECONOMY_SHOP_GUI:SELL` | 出售物品 | `items` |

### v1.0
| 任务 | 描述 | [支持的条件](/epicachievements/configuration/conditions) | 最低 Minecraft 版本 |
|------|------|-------|------------|
| `ADVANCEMENT` | 完成一个进度<br/>需要[额外设置](tasks/advancement) | | 1.12 |
| `BREAK` | 破坏一个方块 | `blocks` `crop-age` | 1.8 |
| `BREED` | 繁殖一个实体 | `entities` | 1.10 |
| `BREW` | 酿造一个物品 | `items`<br/>`potion-effects` | 1.18 |
| `COMMAND` | 执行一条命令<br/>需要[额外设置](tasks/command) | | 1.8 |
| `CONSUME` | 消耗一个物品 | `items` | 1.8 |
| `CRAFT` | 合成一个物品 | `items` | 1.8 |
| `DAMAGE` | 对实体造成伤害 | `entities` | 1.8 |
| `DEATH` | 死亡 | | 1.8 |
| `DROP` | 丢弃一个物品 | `items` | 1.8 |
| `ENCHANT` | 附魔一个物品 | `items` | 1.8 |
| `EXPERIENCE` | 获得经验点数 | | 1.8 |
| `FARM` | 收获一个方块 | `blocks` `crop-age` | 1.16 |
| `FISH` | 钓鱼时获得物品 | `items` | 1.8 |
| `KILL` | 击杀一个实体 | `entities` | 1.8 |
| `MILK` | 给实体挤奶 | | 1.8 |
| `PICKUP` | 拾取一个物品 | `items` | 1.8 |
| `PLACE` | 放置一个方块 | `blocks` `crop-age` | 1.8 |
| `PLACEHOLDER` | 检查 PlaceholderAPI 占位符<br/>需要[额外设置](tasks/placeholder) | | 1.8 |
| `PLAYTIME` | 游玩一定时长<br/>时长必须以 `seconds` 为单位 | | 1.8 |
| `SHEAR` | 给实体剪毛 | `entities` | 1.8 |
| `SMELT` | 烧炼一个物品 | `items` | 1.8 |
| `TAME` | 驯服一个实体 | `entities` | 1.8 |
| `TRADE` | 与村民交易 | `items` | 1.16（**需要 Paper**） |
| `WALK` | 行走一定数量方块 | | 1.8 |
