# 实战示例

> 本目录包含从 Quotidietium 项目实际 Oraxen 配置中提取的实战示例。
> 每个文件都是**可直接复制修改使用的完整 YAML 配置**，配有详尽的中文行内注释。
>
> 所有示例严格遵循 [Oraxen 官方文档](https://docs.oraxen.com/)（Oraxen 1.216.0），并基于项目 `Oraxen/items/` 目录下的实际配置。

该示例由正版ID为 **ZTF3** 的玩家整理与编写。
如有不当请指正qw

## 示例索引（34 个文件）

### 物品（9 个）

| # | 文件 | 核心示例 |
|:-:|:----:|:---------|
| 1 | [基础材料与宝石](物品/1.%20基础材料与宝石.md) | Ruby、Onyx、Amethyst — 最简物品配置 |
| 2 | [武器](物品/2.%20武器.md) | 玻璃剑、雷神之剑、吸血之剑、战斗弓、武士刀 |
| 3 | [工具](物品/3.%20工具.md) | 基岩镐、火焰锤、范围挖掘锤、修理齿轮、收割镰刀 |
| 4 | [食物](物品/4.%20食物.md) | 生培根/生鸡腿、熟食、啤酒/葡萄酒、饮料 — 含新旧系统对比 |
| 5 | [消耗品与药水](物品/5.%20消耗品与药水.md) | 喷溅型凋零药水、多效果消耗品 — Components vs Mechanics |
| 6 | [音乐唱片](物品/6.%20音乐唱片.md) | Welcome Disk — jukebox_playable 组件 + sound.yml 歌曲配置 |
| 7 | [背包](物品/7.%20背包.md) | Leather Backpack — backpack 存储 + backpack_cosmetic 装饰 |
| 8 | [皮肤系统](物品/8.%20皮肤系统.md) | skinnable 接收方 + skin 消耗方 — 完整工作流 |
| 9 | [帽子与头部装备](物品/9.%20帽子与头部装备.md) | Crown、Anubis Head(夜视)、Witch Hat — equippable + armor_effects |

### 方块（5 个）

| # | 文件 | 核心示例 |
|:-:|:----:|:---------|
| 1 | [音符盒矿石](方块/音符盒矿石.md) | 紫水晶/红宝石/黑曜石/Orax 矿石 — NoteBlock ~800 变体 |
| 2 | [绊线花朵与植物](方块/绊线花朵与植物.md) | brunnera/daffodil/dailily — StringBlock 127 变体 |
| 3 | [紫颂透明方块](方块/紫颂透明方块.md) | 自定义树叶、玻璃、带座椅方块 — ChorusBlock 63 变体 |
| 4 | [形状方块](方块/形状方块.md) | 楼梯/台阶/门/活板门/格栅/灯泡 — ShapedBlock |
| 5 | [农场方块与种植盆](方块/农场方块与种植盆.md) | 通用农场方块示例 — FarmBlock 双方块互链 |

### 家具（4 个）

| # | 文件 | 核心示例 |
|:-:|:----:|:---------|
| 1 | [基础家具](家具/基础家具.md) | table(桌子)、shelf(书架)、cart(手推车) — ITEM_FRAME/DISPLAY_ENTITY |
| 2 | [座椅与大型家具](家具/座椅与大型家具.md) | chair(椅子)、coach(长沙发) — seat + 多 barriers |
| 3 | [唱片机](家具/唱片机.md) | turntable — jukebox + Pack.models 双状态模型 |
| 4 | [进化植物](家具/进化植物.md) | weed(大麻5阶段)、grape(葡萄6阶段) — inline stages 新系统 |

### 盔甲（4 个）

| # | 文件 | 核心示例 |
|:-:|:----:|:---------|
| 1 | [绿宝石套装](盔甲/完整盔甲套装_绿宝石.md) | 4件套 + HP加成 + ARMOR_TOUGHNESS — 均衡型设计 |
| 2 | [黑曜石套装](盔甲/完整盔甲套装_黑曜石.md) | 4件套 + 10倍耐久 — 纯防御型的耐久之王 |
| 3 | [头盔与药水效果](盔甲/头盔与药水效果.md) | Anubis Head(夜视) + 4种装饰头盔 — armor_effects 详解 |
| 4 | [自定义鞘翅](盔甲/自定义鞘翅.md) | magic_elytra、phoenix_elytra — `_elytra` 命名约定 |

### UI 与字形（5 个）

| # | 文件 | 核心示例 |
|:-:|:----:|:---------|
| 1 | [表情字形](UI与字形/表情字形.md) | heart(爱心) — chat.placeholders + permission + 18个表情清单 |
| 2 | [界面字形](UI与字形/界面字形.md) | logo、menu_banner、menu_items — 大型界面字形 |
| 3 | [自定义HUD](UI与字形/自定义HUD.md) | 余额显示 + 血条/魔力条/金币/坐标四栏 HUD |
| 4 | [GUI物品](UI与字形/GUI物品.md) | 翻页箭头、退出按钮 — excludeFromInventory + 10个导航按钮套件 |
| 5 | [文字特效](UI与字形/文字特效.md) | rainbow/wave/shake/pulse + 8个自定义 GLSL 特效 |

### 其他配置（7 个）

| # | 文件 | 核心内容 |
|:-:|:----:|:---------|
| 1 | [配方](其他配置/配方.md) | 有序/无序合成、熔炉/锻造台、禁用配方 — 从项目实际 recipes 提取 |
| 2 | [自定义音效](其他配置/自定义音效.md) | sound.yml、唱片机歌曲、原版音效替换、OGG 格式要求 |
| 3 | [战斗机制参考](其他配置/战斗机制完整参考.md) | 8 种战斗机制完整参数表（spear_lunge/thor/bleeding 等） |
| 4 | [农耕机制参考](其他配置/农耕机制完整参考.md) | 6 种农耕机制完整参数表（harvesting/bigmining/bedrockbreak 等） |
| 5 | [杂项机制参考](其他配置/杂项机制完整参考.md) | 17 种杂项机制完整参数表（durability/repair/backpack 等） |
| 6 | [自定义能力与点击动作](其他配置/自定义能力_点击动作.md) | Custom 机制 8 种事件 + ClickAction SpEL 条件/动作系统 |
| 7 | [综合配置示例](其他配置/综合配置示例.md) | 节日食物、多功能武器、终极套装 — 多机制组合实战 |

## 与 General 模板的关系

| 维度 | General（通用模板） | Example（实战示例） |
|:----:|:----:|:----:|
| 来源 | Oraxen 官方文档翻译 | 项目 `Oraxen/items/` 实际配置 |
| 定位 | 参数速查、全字段列举 | 可直接复制使用的真实配置 |
| 注释 | "这个字段是什么" | "为什么这样写、为什么选这个值" |
| 内容 | 1个文件覆盖1种类型 | 1个文件含多个变体对比 |

**建议先看 Example 理解实际用法，再查 General 获取完整字段列表。**

## 使用说明

1. 找到对应类型的示例文件
2. 复制其中的 YAML 配置块
3. 修改物品 ID（`my_` 前缀 → 你的唯一 ID）
4. 修改纹理路径（`default/xxx.png` → 你的纹理路径）
5. 调整参数值（耐久度、伤害、概率等）
6. 将纹理文件放入 `plugins/Oraxen/pack/textures/` 对应路径
7. 执行 `/oraxen reload all` 重载
8. 执行 `/oraxen pack send @a` 推送资源包

## 许可

该文件夹内容和仓库中其他内容一样，统一采用 Apache License 2.0 协议开源。

尊重整理劳动——如需二次分发或修改，请在显著位置标注整理者信息（ZTF3）及本仓库来源。
