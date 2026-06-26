# Oraxen Configuration Skill

## 简介

根据用户需求，严格基于项目中已有的 **Oraxen Docs Origin（Wiki）** 和 **Oraxen Template（预制配置）** 内容，生成符合官方规范的 Oraxen 插件 YAML 配置模板。

每次只生成一个完整的配置（一个物品、一个方块、一个家具等），生成后校验 YAML 语法，并对照 Wiki 验证是否存在虚构内容。

## 目录结构

```
Oraxen Skill/                  # Skill 主目录
├── SKILL.md                   # 技能主文件（注册到 Claude Code 使用）
├── README.md                  # 本文件
└── references/
    └── wiki-index.md          # Wiki 索引导航（快速查找对应配置类型的 Wiki 页面）

项目中的参考资源（Skill 运行时读取）：
参考资料/Oraxen/Oraxen Docs Origin/    # Oraxen 官方 Wiki（英文）
参考资料/Oraxen/Oraxen Docs Chinese/    # Oraxen 官方 Wiki（中文）
参考资料/Oraxen_food_template.md        # 食物配置模板速查
Oraxen/items/                            # Oraxen 预制配置模板
```

## 安装方式

1. 将 `Oraxen Skill/` 目录复制到项目 `.claude/skills/oraxen-skill/` 下
2. 重新启动 Claude Code
3. 使用 `/oraxen-skill` 或触发关键词激活

## 使用方式

### 斜杠命令

`/oraxen-skill <需求描述>` — 生成指定类型的 Oraxen 配置

**示例：**
- `/oraxen-skill 生成一个吃了获得急迫效果的矿工三明治`
- `/oraxen-skill 生成一个紫水晶矿石方块`
- `/oraxen-skill 生成一把带雷击效果的剑`
- `/oraxen-skill 生成一个有座椅的双人椅子家具`

### 自动触发

当用户输入以下关键词时自动激活：
- "生成Oraxen配置"、"Oraxen模板生成"
- "写Oraxen物品"、"Oraxen方块"、"Oraxen家具"
- "Oraxen盔甲"、"Oraxen食物"、"Oraxen武器"、"Oraxen工具"
- "oraxen config"、"oraxen item"、"oraxen block"
- "生成Oraxen物品"、"生成Oraxen家具"、"生成Oraxen盔甲"

## Workflow 说明

1. **分析需求** — 解析用户输入，确定配置类型（物品/方块/家具/盔甲/食物等）
2. **查阅参考** — 根据配置类型读取对应的 Wiki 页面和模板文件，交叉验证
3. **确认不确定项** — 向用户提问所有必需的但未明确的信息（ID、名称、材质、版本等）
4. **生成配置** — 基于 Wiki 和模板生成完整的 YAML 配置，附带详细注释
5. **校验** — 检查 YAML 语法，对照 Wiki 逐字段验证
6. **输出结果** — 以对话展示或保存文件的方式交付

## 技术细节

### 强大的参考体系

Skill 内置了对 Oraxen Docs Origin（Wiki）和 Oraxen Template 的完整引用映射，能够根据用户需求精准定位对应的 Wiki 页面和模板示例：

- **物品类**：参考 `Items/Getting Started.md`、`Items/Components.md`、`Items/Appearance & Models.md`
- **方块类**：参考 `Blocks/Overview.md`、`Blocks/NoteBlock.md` 等
- **家具类**：参考 `Furniture/Overview.md`、`Furniture/Display Entities.md` 等
- **盔甲类**：参考 `Armors/Overview.md`、`Armors/Components(1.21.2+).md` 等
- **Mechanics（机制）**：参考 `Items/Item Abilities/` 系列文档

### 支持的配置类型

| 类型 | 核心字段 | 版本要求 |
|------|---------|---------|
| 基础物品 | itemname + material + Pack.textures | 无 |
| 武器 | + AttributeModifiers + Mechanics | 无 |
| 工具 | + Components.tool + Mechanics（bigmining 等） | 无 |
| 食物 | Components.food + Components.consumable | 1.20.5+（最新）或 Mechanics.food（旧版） |
| 方块（NoteBlock） | Mechanics.noteblock + custom_variation | 无 |
| 方块（StringBlock） | Mechanics.stringblock | 无 |
| 方块（ChorusBlock） | Mechanics.chorusblock | 无 |
| 方块（ShapedBlock） | Mechanics.shapedblock | 无 |
| 方块（FarmBlock） | Mechanics.noteblock.farmblock | 无 |
| 家具（DISPLAY_ENTITY） | Mechanics.furniture + type:DISPLAY_ENTITY | 1.19.4+ |
| 家具（ITEM_FRAME） | Mechanics.furniture + type:ITEM_FRAME | 无 |
| 盔甲 | Components.equippable + AttributeModifiers | 1.21.2+（Components 法） |
| 唱片 | Components.jukebox_playable | 1.21+ |
| 背包 | Mechanics.backpack | 无 |
| 作物/植物 | Mechanics.furniture + stages/evolution | 无 |

### Mechanics 支持

Skill 支持基于 Wiki 生成以下 Mechanics：

**战斗类：** thor（雷击）、lifeleech（生命偷取）、bleeding（流血）、energyblast（能量爆破）、witherskull（凋零头颅）、fireball（火球）、knockback_strike（连击击退）、spear_lunge（长矛突刺）

**农耕类：** bigmining（范围挖掘）、smelting（自动熔炼）、harvesting（自动收割）、watering（浇水）、bedrockbreak（破基岩）、bottledexp（经验瓶）

**杂项类：** food（食物）、durability（耐久）、efficiency（效率/急迫）、backpack（背包）、repair（修复）、commands（命令）、armor_effects（盔甲效果）、hat（帽子）、aura（光环）、soulbound（灵魂绑定）、skinnable/skin（皮肤）、toggle_light（切换光照）

### 版本差异处理

Skill 会自动根据用户提供的 Minecraft 版本选择正确的配置格式：

- **1.21.2+**：使用 Components 系统（food + consumable 分离、equippable 等）
- **1.20.5-1.21**：使用旧版 Components（food 合并所有消耗属性）
- **1.20.5 以下**：使用 Mechanics 方式（Mechanics.food、Mechanics.durability 等）

## 注意事项

- **配置准确性优先**：Skill 严格遵守 Wiki 内容，不会编造未记载的功能
- **一次只生成一个配置**：如需多个配置，需多次调用
- **用户确认不可跳过**：对于不确定的字段，必须询问用户
- **纹理文件需自行准备**：生成的配置引用纹理路径，但实际的 `.png` 文件需要用户自行添加到 `Oraxen/pack/textures/` 目录
- **custom_variation 冲突**：NoteBlock/StringBlock 的 `custom_variation` 值必须在整个项目中唯一
- **版本问题**：生成配置前确保告知 Skill 你的 Minecraft 服务器版本，以使用正确的配置格式
- **Oraxen Docs Origin（Wiki）和 Oraxen Template（预制配置）** 必须存在于项目中，Skill 才能正常工作
- **在线文档使用规则**：官方在线文档（<https://docs.oraxen.com/>）**仅在用户明确要求时才能使用**。不可擅自访问。由于网络环境差异，在线文档可能无法访问，尝试后如不可用会向用户报告。
