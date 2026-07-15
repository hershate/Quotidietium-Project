# oraxen-skill — Oraxen 配置生成器

## 简介

根据用户需求，严格基于 Skill 内置的 **Oraxen Docs Origin（Wiki）** 和 **Oraxen Template（预制配置模板）** 内容，生成符合官方规范的 Oraxen 插件 YAML 配置模板。

每次只生成一个完整的配置（一个物品、一个方块、一个家具等），生成后校验 YAML 语法，并对照 Wiki 验证是否存在虚构内容。

本项目使用 [Meta-skill](https://github.com/hershate/Meta-skill) 项目构建。

## 作者信息

本 Skill 由 **正版 ID 为 `ZTF3` 的玩家** 根据 Oraxen Docs Origin 和 Oraxen Template 的内容整理和撰写。

- 所有内置的 Wiki 文档和配置模板均来自开源或授权渠道
- Skill 本身采用 Apache License 2.0 协议开源

## 目录结构

```
oraxen-skill/                  # Skill 主目录（完全自包含，可直接复制使用）
├── SKILL.md                   # 技能主文件（注册到 Claude Code 使用）
├── README.md                  # 本文件
└── references/
    ├── wiki-index.md          # Wiki 索引导航（快速查找对应配置类型的页面）
    ├── Oraxen Docs Origin/    # Oraxen 官方 Wiki（68 个文档，自包含）
    ├── Oraxen Template/       # Oraxen 配置模板（68 个文件，自包含）
    │   ├── General/           # 通用配置参考文档（34 个）
    │   └── Example/           # 完整配置示例（34 个）
    └── Oraxen_food_template.md # 食物配置模板速查
```

## 安装方式

1. 将 `oraxen-skill/` 整个目录复制到项目 `.claude/skills/oraxen-skill/` 下
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
5. **校验** — 检查 YAML 语法，对照 Wiki 逐字段验证，禁止虚构内容
6. **输出结果** — 以对话展示或保存文件的方式交付

## 技术细节

### 强大的参考体系

Skill 内置了完整的 Oraxen Docs Origin（Wiki）和 Oraxen Template，所有资料均位于 `references/` 目录下，完全自包含，无需依赖项目中其他文件。

- **Wiki 参考**：`references/Oraxen Docs Origin/`（68 个文档，涵盖物品/方块/家具/盔甲/Mechanics/配方等）
- **模板参考**：`references/Oraxen Template/General/`（34 个通用参考）+ `Example/`（34 个完整示例）
- **食物速查**：`references/Oraxen_food_template.md`

### 支持的配置类型

| 类型 | 核心字段 | 版本要求 |
|------|---------|---------|
| 基础物品 | displayname + material + Pack.textures | 无 |
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

Skill 会根据用户提供的 Minecraft 版本选择正确的配置格式：

- **1.21.2+**：使用 Components 系统（food + consumable 分离、equippable 等）
- **1.20.5-1.21**：使用旧版 Components（food 合并所有消耗属性）
- **1.20.5 以下**：使用 Mechanics 方式（Mechanics.food、Mechanics.durability 等）

## 注意事项

- **配置准确性优先**：Skill 严格遵守 Wiki 内容，不会编造未记载的功能
- **Wiki 对照校验**：每次生成后自动逐字段对照 Wiki 验证，杜绝虚构内容
- **一次只生成一个配置**：如需多个配置，需多次调用
- **用户确认不可跳过**：对于不确定的字段（ID、名称、数值等），必须询问用户
- **纹理文件需自行准备**：生成的配置引用纹理路径，但实际的 `.png` 文件需要用户自行添加到 `Oraxen/pack/textures/` 目录
- **custom_variation 冲突**：NoteBlock/StringBlock 的 `custom_variation` 值必须在整个项目中唯一
- **版本问题**：生成配置前确保告知 Skill 你的 Minecraft 服务器版本
- **Skill 完全自包含**：所有 Wiki 文档和模板示例已内置在 `references/` 目录中，可直接复制到任何项目使用
- **在线文档使用规则**：官方在线文档（<https://docs.oraxen.com/>）**仅在用户明确要求时才能使用**，不可擅自访问

## 许可

- Skill 内容（SKILL.md、README.md）采用 Apache License 2.0
- 内置的 Oraxen Docs Origin（Wiki）遵循其原始许可协议
- 内置的 Oraxen Template 来自开源/授权渠道
