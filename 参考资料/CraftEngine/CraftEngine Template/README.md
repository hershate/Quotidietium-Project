# CraftEngine 模板集

> 由正版ID为 ZTF3 的玩家根据 CraftEngine 官方文档整理制作

本目录包含 CraftEngine 插件的完整 YAML 配置模板。每个 `.yml` 文件均配有可直接复制使用的示例代码，覆盖方块、物品、家具、配方、盔甲等全部可自定义对象。

所有 `<< CHANGE THIS` 标记处需替换为实际值。命名空间建议使用小写英文。

---

## 开源协议

本目录所有内容统一采用 **Apache License 2.0** 协议开源。

### 署名要求（强制）

任何人使用、修改、分发本目录内容，必须在显著位置完整标注以下信息：

- 源码仓库：<https://github.com/hershate/Quotidietium-Project>
- 制作者：ZTF3

"显著位置"包括但不限于：
- 配置文件头部
- 二次分发作品的说明文档首位

不得删除、隐藏、篡改版权与署名信息。

### 允许使用范围

- 可用于任何 Minecraft 服务器（包括商业服务器）
- 可自由修改、适配自己的服务器
- 可在署名前提下免费分享、分发

### 禁止行为

- 禁止将本目录内容单独提取后售卖、倒卖、有偿分享
- 禁止移除版权声明、署名信息
- 禁止冒用作者名义进行宣传

---

## General/ 文件分类索引

General/ 目录共包含 **44 个 YAML 模板文件**，按功能分为以下 19 个类别。

### 一、方块设置与基础

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `基础方块.yml` | 单状态方块（自动状态、加权随机模型）；多状态方块（轴向、含水、透明+实体渲染器、台阶、红石灯、楼梯、门、沙发、旋钮）。共 14 个完整示例。 | `configuration/block.md`、`configuration/block/settings.md`、`configuration/block/states.md`、`configuration/block/states/properties.md` |
| `方块设置.yml` | 方块 settings 完整配置：硬度、爆炸抗性、活塞行为、挖掘工具、音效（简单/高级）、光照系统、红石导体、物理系数（摩擦/弹跳）、地图颜色、熔岩可燃性、流体状态、支撑形状等。含 7 个示例。 | `configuration/block/settings.md` |
| `方块标签.yml` | 方块标签配置：可挖掘标签（斧/锄/镐/锹/剑效率）、可攀爬、信标底座、重置摔落伤害、灵魂火基底、维度无限燃烧、附魔等级提供、树木可替换等。 | `reference/block_tags.md` |
| `方块实体渲染器.yml` | 方块实体渲染器完整配置：物品展示实体、文本展示实体、物品实体、盔甲架；多渲染元素组合；颜色提供器（tint_source）；实体剔除（culling）；渲染条件（conditions）。 | `configuration/block/states/entity_renderer.md` |

### 二、方块行为——变化与生长

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `变化与蔓延.yml` | 随时间变化方块（氧化式）、扩散方块、表面扩散方块（草方块式）、衰变方块（冰到水，计划刻/随机刻两种模式）、草方块（骨粉地物）、树叶方块（距离计算与枯萎）。 | `configuration/block/behaviors/change_over_time_block.md`、`configuration/block/behaviors/spreading_block.md`、`configuration/block/behaviors/surface_spreading_block.md`、`configuration/block/behaviors/decay_block.md`、`configuration/block/behaviors/grass_block.md`、`configuration/block/behaviors/leaves_block.md` |
| `农作物与植物.yml` | 农作物方块（crop_block，仿小麦生长）、茎方块（stem_block，仿西瓜/南瓜）、附着茎方块、灌木方块（黑/白名单+堆叠）、树苗方块（sapling_block + feature）、垂直作物（vertical_crop_block，向上/向下延伸，可组合悬挂行为）。 | `configuration/block/behaviors/crop_block.md`、`configuration/block/behaviors/stem_block.md`、`configuration/block/behaviors/attached_stem_block.md`、`configuration/block/behaviors/bush_block.md`、`configuration/block/behaviors/sapling_block.md`、`configuration/block/behaviors/vertical_crop_block.md` |

### 三、方块行为——物理与机制

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `物理机制方块.yml` | 可下落方块（falling_block，仿沙子/沙砾，可配置伤害与音效）、混凝土粉末方块（遇水硬化）、弹跳方块（bouncing_block，配置弹力系数、摔伤减免、客户端同步）。 | `configuration/block/behaviors/falling_block.md`、`configuration/block/behaviors/concrete_powder_block.md`、`configuration/block/behaviors/bouncing_block.md` |
| `特殊机制方块.yml` | 可剥离方块（strippable_block，斧右键剥离+属性继承控制）、稳固基底方块（sturdy_base_block，需支撑面+可堆叠）、母岩方块（budding_block，紫水晶式催生）、覆雪方块（snowy_block）、掉落经验方块（drop_exp_block，可加附魔条件）。 | `configuration/block/behaviors/strippable_block.md`、`configuration/block/behaviors/sturdy_base_block.md`、`configuration/block/behaviors/budding_block.md`、`configuration/block/behaviors/snowy_block.md`、`configuration/block/behaviors/drop_experience_block.md` |
| `展示与粒子效果.yml` | 物品展示方块（display_item_block）、物品展示框方块（item_frame_block，可发光/隐形）、简单粒子方块（simple_particle_block，含物品粒子/方块粒子/粉尘/振动/轨迹等 10 种粒子类型）、墙上火把粒子方块（wall_torch_particle_block，粒子位置随朝向旋转）、颜色提供器方块（tint_source_block）。 | `configuration/block/behaviors/display_item_block.md`、`configuration/block/behaviors/item_frame_block.md`、`configuration/block/behaviors/simple_particle_block.md`、`configuration/block/behaviors/wall_torch_particle_block.md`、`configuration/block/behaviors/tint_source_block.md` |

### 四、方块行为——朝向与液体交互

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `朝向与液体交互.yml` | 定向附着方块（墙上火把式）、水平面定向附着方块（按钮/拉杆式）、可悬挂方块（灯笼式）、悬挂方块（钟乳石式）；流体推动方块（可替换）、邻液方块（火焰藤式，需附近有液体）、液面方块（睡莲式）。 | `configuration/block/behaviors/directional_attached_block.md`、`configuration/block/behaviors/face_attached_horizontal_directional_block.md`、`configuration/block/behaviors/hangable_block.md`、`configuration/block/behaviors/hanging_block.md`、`configuration/block/behaviors/liquid_flowable_block.md`、`configuration/block/behaviors/near_liquid_block.md`、`configuration/block/behaviors/on_liquid_block.md` |

### 五、方块行为——建筑组件

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `门与红石方块.yml` | 门、活板门、栅栏、栅栏门、按钮（组合 face_attached_horizontal_directional_block）、压力板。每种均包含自定义音效与行为参数。 | `configuration/block/behaviors/door_block.md`、`configuration/block/behaviors/trapdoor_block.md`、`configuration/block/behaviors/fence_block.md`、`configuration/block/behaviors/fence_gate_block.md`、`configuration/block/behaviors/button_block.md`、`configuration/block/behaviors/pressure_plate_block.md` |
| `楼梯台阶与多层方块.yml` | 楼梯方块（stairs_block，原版兼容连接逻辑）、台阶方块（slab_block，支持双层合并）、双层方块（double_high_block，两格高连锁破坏）、多层方块（multi_high_block，自定义 int 属性层数控制，3层/5层/2层示例）。 | `configuration/block/behaviors/stairs_block.md`、`configuration/block/behaviors/slab_block.md`、`configuration/block/behaviors/double_high_block.md`、`configuration/block/behaviors/multi_high_block.md` |

### 六、方块行为——交互

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `存储与座椅.yml` | 简单存储方块（simple_storage_block，自定义行数/比较器/音效）、抽屉方块（drawer_block，单物品大储量+展示物品位置）、座椅方块（seat_block，多座位+偏航锁定）、沙发方块（sofa_block，PP 更新自动连接）、可堆叠方块（stackable_block，仿海泡菜/蜡烛）。 | `configuration/block/behaviors/simple_storage_block.md`、`configuration/block/behaviors/drawer_block.md`、`configuration/block/behaviors/seat_block.md`、`configuration/block/behaviors/sofa_block.md`、`configuration/block/behaviors/stackable_block.md` |
| `灯与钟.yml` | 灯方块（lamp_block，红石控制亮灭）、可切换灯方块（toggleable_lamp_block，红石翻转/手动交互/浸水）、震响方块（chime_block，弹射物击中音效）。 | `configuration/block/behaviors/lamp_block.md`、`configuration/block/behaviors/toggleable_lamp_block.md`、`configuration/block/behaviors/chime_block.md` |

### 七、物品基础配置

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `基础物品.yml` | 装饰物品、工具（数据组件全套）、燃料/堆肥/染色物品（settings 完整）、方块物品（block_state/attribute_modifiers/food/trim/PDC/jukebox）、完整复杂物品（付费版功能：client_bound_data、conditional、equippable、projectile）。共 5 个示例。 | `configuration/item.md`、`configuration/item/data.md`、`configuration/item/settings.md` |
| `物品设置.yml` | 物品 settings 全部选项：燃料时间、标签、装备绑定、可修复性、铁砧材料、可重命名、弹射物（含音效/射击参数）、可染色、食物、消耗替代品、合成剩余物、免疫伤害类型、死亡保留/损毁概率、掉落物显示格式、发光颜色等。 | `configuration/item/settings.md` |
| `物品模型类型.yml` | 全部 8 种物品模型类型完整覆盖：简化模型（texture/textures/models 快捷写法）、minecraft:model（含 generation/tints/transformation）、minecraft:condition（9 种布尔谓词）、minecraft:range_dispatch（12 种数值属性）、minecraft:composite（组合渲染）、minecraft:select（10 种枚举属性）、minecraft:special（15 种特殊模型渲染器）、legacy_model（旧版兼容）。 | `configuration/item/models.md`、`configuration/item/models/model.md`、`configuration/item/models/condition.md`、`configuration/item/models/range_dispatch.md`、`configuration/item/models/composite.md`、`configuration/item/models/select.md`、`configuration/item/models/special.md` |
| `物品数据组件.yml` | 物品 data 全部组件分类：名称相关（item_name/custom_name/overwritable_item_name）、Lore（简单/高级格式/插入/移除/覆写）、基础属性（unbreakable/max_damage/dyed_color/hide_tooltip）、功能组件（enchantment/block_state/attribute_modifiers/food/jukebox_playable/trim/equippable/painting_variant）、持久化数据（PDC/profile/external）、条件数据（付费）、自定义组件（NBT/components/remove_components）、客户端侧数据（付费）。 | `configuration/item/data.md` |
| `物品行为.yml` | 所有物品行为的完整覆盖：block_item（标准/内联）、ceiling/wall/ground_block_item（定向放置）、double_high/multi_high_block_item（多格放置）、liquid_collision_block_item（液面放置）、furniture_item（家具物品+放置规则）、liquid_collision_furniture_item（液面家具）、compostable_item（堆肥）、range_mining_item（范围挖掘，十字/3x3 两种模式）。 | `configuration/item/behaviors/block_item.md`、`configuration/item/behaviors/ceiling_block_item.md`、`configuration/item/behaviors/wall_block_item.md`、`configuration/item/behaviors/ground_block_item.md`、`configuration/item/behaviors/double_high_block_item.md`、`configuration/item/behaviors/multi_high_block_item.md`、`configuration/item/behaviors/liquid_collision_block_item.md`、`configuration/item/behaviors/furniture_item.md`、`configuration/item/behaviors/liquid_collision_furniture_item.md`、`configuration/item/behaviors/compostable_item.md`、`configuration/item/behaviors/range_mining_item.md` |

### 八、物品——武器/工具与消耗品

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `武器.yml` | 剑（minecraft:model + handheld + attribute_modifiers 全套）、弓（minecraft:condition + pulling 模型 + enchantment.merge）、弩（minecraft:range_dispatch + charge 分档 + custom components）、三叉戟（minecraft:condition + throwing 模型）、投射物箭（minecraft:model + generated + use_remainder）。共 5 个大型示例。 | `configuration/item.md`、`configuration/item/data.md`、`configuration/item/models.md` |
| `工具.yml` | 范围挖掘工具：镐（3x3 完整面）、斧（水平 3x1 砍树）、锹（3x3 水平平面）、锄（十字形）。弹射物完整配置（含自定义音效/方块类型覆盖/穿透/重力/伤害）。铁砧修复材料配置。 | `configuration/item/behaviors/range_mining_item.md`、`configuration/item/settings.md` |
| `食物.yml` | 基础食物（food 硬编码）、食物+consumable 组件（含音效/粒子/动画/耗时）、食物+on_consume_effects（apply_effects 状态效果）、完整功能食物（全字段组合）、版本条件食物（$$>=1.21.2 区分高/低版本组件）、消耗替代品（consume_replacement）。共 7 个示例。 | `configuration/item/data.md`（food 节与 components 节）、`configuration.md`（minecraft:consumable 组件示例） |
| `消耗品与药水.yml` | 魔力药水（drink 动画+apply_effects+冷却）、狂战士酿造（多重 on_consume_effects+粒子+动作栏+治疗）、天使恩典（clear_all_effects+teleport_randomly+apply_effects+remove_effects+标题+图腾动画）、经验药剂（set_food+set_saturation+set_exp）。共 4 个完整药水示例。 | `configuration/item/data.md`、`configuration/item/settings.md`、`reference/events.md`、`reference/conditions.md` |

### 九、家具配置

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `基础家具.yml` | 基础椅子（单元素 item_display + 潜影贝判定箱 + 座位）、带标牌桌子（双元素 item_display+text_display + 交互判定箱 + 完整实体剔除）、吊灯与墙壁开关（多变体 ceiling+wall + 盔甲架+物品展示 + 混合判定箱 custom+shulker+interaction）、外部模型蓝图引用（BetterModel/ModelEngine）。共 3 个大型示例。 | `configuration/furniture.md`、`configuration/furniture/settings.md`、`configuration/furniture/variants.md`、`reference/loot_table.md`、`reference/events.md`、`configuration/item/behaviors/furniture_item.md`、`configuration/item/behaviors/liquid_collision_furniture_item.md` |
| `家具行为.yml` | 物品展示家具（display_item_furniture，多变体物品位置）、发光家具（glowing_furniture，统一/按变体两种配置）、简单存储家具（simple_storage_furniture，容器+标题+行数+音效）。 | `configuration/furniture/behaviors/display_item_furniture.md`、`configuration/furniture/behaviors/glowing_furniture.md`、`configuration/furniture/behaviors/simple_storage_furniture.md` |

### 十、盔甲

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `盔甲套装.yml` | 组件型盔甲（1.21.2+，简单字符串/块配置/多纹理列表/花环/全预设模型）、纹饰型盔甲（type: trim，1.20+）。含头盔/胸甲/护腿/靴子完整物品绑定、可染色盔甲、3D 头盔（禁用盔甲渲染器两种方案）。全部预设模型类型速查表。 | `configuration/equipment.md`、`configuration/item/settings.md` |

### 十一、配方

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `配方.yml` | 有序合成（shaped，含自动附魔后处理器/原料批量消耗）、无序合成（shapeless，含标签引用/嵌套列表）、烧炼（smelting/blasting/smoking/campfire_cooking）、切石机（stonecutting）、锻造升级（smithing_transform + transform_processors 可继承组件）、有序合成转化（shaped_transform）、盔甲纹饰（smithing_trim）、酿造（brewing）、付费版（visual_result/functions/conditions）。含外部插件兼容配置参考。 | `configuration/recipe.md`、`configuration/items.md`、`compatibility/external_item_sources.md` |

### 十二、战利品

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `战利品表.yml` | 标准战利品表：单物品掉落、多条目权重随机、家具物品掉落、经验值掉落、alternatives 条件分支（精准采集 vs 矿物+时运+经验）、完整函数组合（apply_bonus/apply_data/set_count/explosion_decay/drop_exp/limit_count）。原版战利品覆盖（vanilla_loots）：方块单体/多目标、实体战利品。 | `reference/loot_table.md`、`configuration/vanilla_loot.md` |

### 十三、音乐

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `音乐唱片.yml` | 唱片机曲目定义（jukebox_songs，时长/比较器输出/范围）、可播放唱片物品（items + jukebox_playable 组件，标准唱片材质/自定义材质）、自定义音效定义（sounds，简单/复杂/权重随机/覆盖原版）。 | `configuration/jukebox_song.md`、`configuration/sound.md` |

### 十四、画

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `画配置.yml` | 画注册（painting variant：完整/最小/自定义尺寸/管理员标签/自定义标题作者）+ 物品绑定（material: painting + data.painting_variant）。 | `configuration/painting.md` |

### 十五、图像与字体

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `图像配置.yml` | 全局图像设置（config.yml 拦截包配置）、images 配置块（单字符位图/多字符精灵图/引用别名/默认字体覆盖）。含 MiniMessage/MineDown/PlaceholderAPI 调用参考。 | `configuration/image.md`、`reference/text_format.md`、`compatibility/placeholderapi.md` |
| `字体配置.yml` | TTF 矢量字体提供器配置（type: ttf，含 oversample/size）。位图字体与 Unihex 字体参考说明。资源包目录结构总览。 | `configuration/font.md` |

### 十六、文本格式

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `文本格式.yml` | MiniMessage 标签完整示例：shift（偏移）、papi（PlaceholderAPI）、image（图像引用）、i18n/l10n（翻译）、expr（数学运算+DecimalFormat）、global（全局变量）。高级用法：viewer_arg/viewer_papi（多上下文主体）、bubble/nameplate/background（CustomNameplates 集成）、关系型 PAPI。 | `reference/text_format.md` |
| `数字格式.yml` | 全部 11 种数字格式：常量、均匀随机、表达式、二项分布、加权列表、高斯/正态分布、偏态分布、对数正态分布、三角分布、贝塔分布、指数分布。每种包含完整参数+简写形式。嵌套用法示例。 | `reference/number_format.md` |
| `链式参数.yml` | 链式参数完整参考：player（坐标/身份/状态/手持物品/世界/位置）、block（坐标/方块状态/世界/位置）、world、entity（含掉落物物品子对象）、position、item、furniture。含 6 个实际配置场景示例。 | `reference/text_format/chain_arguments.md` |

### 十七、本地化

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `语言配置.yml` | lang 系统（客户端资源包驱动，en_us/zh_cn/all 覆盖）；translations 系统（i18n 服务端替换 / l10n 客户端替换，支持通用语言回退）。含 item_name 中 `<lang:>` / `<i18n:>` / `<l10n:>` 标签使用参考。 | `configuration/lang.md`、`configuration/i18n.md` |
| `表情配置.yml` | 基础表情（权限+图像+关键词）、带 Hover 提示的复杂表情（MiniMessage 丰富格式+PlaceholderAPI）、多行格式表情、场景内容覆盖（content_overrides：chat/book/anvil/sign/command 五种场景分别定义）、多场景+多行混合模板。 | `configuration/emoji.md`（另参考 `configuration/image.md` 图像配置前置依赖） |

### 十八、事件与条件

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `事件与条件.yml` | 事件触发器（物品/方块/家具的 break/right_click/left_click/consume/pick_up/attack 等）。46 种函数类型完整覆盖：命令/消息/标题/动作栏/粒子/音效/冷却/伤害/治疗/经验/传送/弹窗/图腾动画/家具操作（生成/移除/替换/旋转）/条件分支（if_else/when）/循环方块属性/村民交易等。27 种条件类型完整覆盖：权限/随机/表达式/字符串匹配/正则/冷却/物品栏检测/WorldGuard 区域/距离/魔咒/时运概率表/摔落方块检测等。含完整综合示例。 | `reference/events.md`、`reference/conditions.md` |

### 十九、其他配置

| 文件名 | 模板内容 | 覆盖的本地 Wiki 文件 |
|--------|----------|---------------------|
| `分类配置.yml` | 物品分类菜单配置：基础分类（独立显示）、无条件公开分类、all_items 自动汇总、多级分类（父分类+子分类嵌套 `#` 引用）、三级及以上深度嵌套。物品级分类指定（category 字段/多分类列表）。条件（permission/world/biome）配置参考。 | `configuration/category.md`、`reference/conditions.md` |
| `全局变量.yml` | 全局变量定义与引用：纯文本+格式码、带参数传值（`<arg:0>` / `<arg:1>` 占位符）、图像/材质标签、组合用法（格式码+参数+图像）。跨插件调用参考示例。 | `configuration/global_variable.md` |
| `模板系统.yml` | 模板定义（基本/带参数/带默认值/自动命名空间/多模板组合/链式引用）、模板调用（单模板/多模板/合并/覆写/参数顺序应用）、扩展参数类型（列表/映射/__skip_template_argument__/condition/when/大小写转换/自增整数/数学表达式）、配置工厂（blueprint + instances 批量生成）。 | `reference/template.md` |
| `文件冲突配置.yml` | 资源包文件冲突处理规则：通用匹配（all_of/any_of/inverted/filename/exact/parent_path_prefix/parent_path_suffix/contains/pattern）、冲突解决方案（merge_json/retain_matching/conditional/merge_pack_mcmeta/merge_atlas/merge_font）。含完整 config.yml 配置示例。 | `reference/file_conflict.md` |
| `物品更新器.yml` | 物品更新器配置：触发器配置（点击/丢弃/拾取）、单步更新（apply_data）、多步更新（apply_data + transmute 组合）、reset 更新器（保留指定组件/NBT 重置为最新定义）、综合多步更新示例。更新器类型速查。 | `configuration/item/updater.md`、`configuration/item/data.md` |
| `高级配置特性.yml` | 高级配置系统特性：Section Identifiers（节标识符 `items#0` 语法）、Section Separators（`::` 双冒号键折叠）、Version-Based Configuration（`$$>=1.21.2` 版本条件选择与合并）、Extended Value Types（`!!long`、`!!float` 等 YAML 类型标签）、Subpacks（`pack.yml` 子包配置）。 | `configuration.md` |

---

## 目录结构

```
CraftEngine Template/
├── General/                ← 通用配置模板（44 个 .yml 文件，覆盖全部功能类别）
├── Example/                ← 完整示例包（32 个 .yml 文件，分类编排，可直接使用）
│   ├── 物品/               ← 10 个示例（基础材料、武器、工具、食物、消耗品、唱片、数据组件、设置、模型、行为）
│   ├── 方块/               ← 9 个示例（基础、农作物、功能、物理、存储、装饰、朝向、特殊、实体渲染器）
│   ├── 家具/               ← 2 个示例（基础家具、家具行为）
│   ├── 装备/               ← 1 个示例（盔甲套装）
│   ├── 配方/               ← 1 个示例（全部配方类型）
│   ├── 事件与条件/          ← 2 个示例（事件函数、条件）
│   └── 其他配置/            ← 7 个示例（图像与表情、画与分类、模板、语言、数字格式、战利品、文件冲突）
└── 完整产业链/             ← 21 个端到端应用模板（采矿、农业、装饰、魔法装备、钓鱼、红石机械、远程武器、存储物流、粒子特效、经济交易、音乐音效、世界生成、盔甲特效、战利品宝藏、模板系统、农耕扩展、附魔升级、便携工具、酿造饮品、季节活动、画作装饰）
```

## 使用方式

1. 将 `General/` 或 `Example/` 中的 `.yml` 文件放入 `plugins/CraftEngine/` 对应目录下（根据 YAML 顶级键决定：`blocks:` 放入 blocks 目录，`items:` 放入 items 目录，以此类推）。
2. 全局替换文件中所有示例命名空间（如 `my:`、`custom:`、`your_namespace:`）为你的实际命名空间。
3. 搜索 `<< CHANGE THIS` 标记，将每个标记值替换为实际配置值。
4. 删除不需要的示例区块。
5. 重载配置（`/ce reload`）或重启服务器。

---

> **文件位置:** `./General/`
> **Wiki 位置:** `../CraftEngine Wiki/`
> **最后更新:** 2026-07-09
