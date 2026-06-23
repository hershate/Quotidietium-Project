# CraftEngine 配置模板库

> 基于 CraftEngine 官方文档穷举的配置模板，严格遵循文档中的配置项。
> 每个模板均对照文档验证，**未出现于文档中的配置项不会使用**。

## 📁 目录结构

```
CraftEngine Template/
├── README.md                     # 本文件
├── 物品/
│   ├── 基础材料与宝石.yml         # 基础物品、材料、宝石模板
│   ├── 武器.yml                   # 剑、弓、弩等武器模板
│   ├── 工具.yml                   # 镐、斧、锹、锄等工具模板
│   ├── 食物.yml                   # 食物、消耗品模板
│   ├── 消耗品与药水.yml           # 药水、特殊消耗品模板
│   └── 音乐唱片.yml               # 自定义音乐唱片模板
├── 方块/
│   ├── 基础方块.yml               # 基础方块、多状态方块模板
│   ├── 农作物.yml                 # 农作物、树苗、藤蔓等生长方块模板
│   ├── 功能方块.yml               # 门、活板门、按钮、灯等交互方块模板
│   └── 物理机制方块.yml           # 下落、蔓延、液体等物理效果方块模板
├── 家具/
│   └── 基础家具.yml               # 展示实体家具、座椅、存储家具模板
├── 装备/
│   └── 盔甲套装.yml               # 基于组件/纹饰的自定义盔甲模板
├── 配方/
│   └── 全部配方类型.yml           # 有序/无序合成、烧炼、锻造、酿造等配方模板
└── 其他配置/
    ├── 事件与函数参考.yml          # 全部事件触发器、函数类型、条件类型参考
    ├── 图像配置.yml                # 单字符/多字符位图、图像引用模板
    ├── 表情配置.yml                # 聊天表情、关键词、场景覆盖模板
    ├── 音效配置.yml                # 自定义音效事件、加权多音效模板
    ├── 画配置.yml                  # 自定义画作及物品绑定模板
    ├── 分类配置.yml                # 物品浏览器分类、子分类、嵌套分类模板
    ├── 全局变量.yml                # 全局变量定义与使用模板
    ├── 模板系统.yml                # 模板定义、参数、覆写、合并、配置工厂参考
    ├── 战利品表参考.yml            # 战利品表、掉落函数、公式参考
    ├── 语言配置.yml                # lang/i18n/l10n 多语言配置模板
    ├── 数字格式.yml                # 常量、随机数、分布函数等数字格式参考
    ├── 文本格式.yml                # MiniMessage 标签及附加标签参考
    └── 方块标签.yml                # 可挖掘标签、特殊机制标签参考
```

## 🚀 快速开始

### 第一步：创建你的第一个物品

参考 [`物品/基础材料与宝石.yml`](物品/基础材料与宝石.yml) 模板，创建一个最简单的自定义物品。

### 第二步：添加模型和纹理

参考 [`物品/基础材料与宝石.yml`](物品/基础材料与宝石.yml) 中的 `model` 配置部分。

### 第三步：创建自定义方块

参考 [`方块/基础方块.yml`](方块/基础方块.yml) 模板。

### 第四步：添加配方

参考 [`配方/全部配方类型.yml`](配方/全部配方类型.yml) 为你的物品/方块添加合成配方。

### 第五步：添加交互事件

参考 [`其他配置/事件与函数参考.yml`](其他配置/事件与函数参考.yml) 为物品/方块添加右键、破坏等交互逻辑。

## 📋 配置总览

| 配置区域 | 根键 | 文档来源 |
|---------|------|---------|
| 物品 | `items:` | configuration/item.md |
| 方块 | `blocks:` | configuration/block.md |
| 家具 | `furniture:` | configuration/furniture.md |
| 装备 | `equipments:` | configuration/equipment.md |
| 配方 | `recipes:` | configuration/recipe.md |
| 战利品 | `loot:` | reference/loot_table.md |
| 事件 | `events:` | reference/events.md |
| 条件 | `conditions:` | reference/conditions.md |
| 分类 | `categories:` | configuration/category.md |
| 图像 | `images:` | configuration/image.md |
| 表情 | `emoji:` | configuration/emoji.md |
| 音效 | `sounds:` | configuration/sound.md |
| 画 | `paintings:` | configuration/painting.md |
| 全局变量 | `global_variables:` | configuration/global_variable.md |
| 模板 | `templates:` | reference/template.md |
| 语言 | `lang:` / `translations:` | configuration/lang.md / configuration/i18n.md |

## ⚠️ 注意事项

1. **仅使用文档中出现的配置项** — 本模板库严格遵循 CraftEngine 文档，未出现在文档中的功能/参数不会被使用
2. **命名空间ID格式** — 全部使用小写字母加下划线，格式: `命名空间:路径`
3. **物品材质 (material)** — 使用 Minecraft 原版 Bukkit Material 名 (小写)
4. **付费版功能** — 标记为"付费版专属"的功能需要购买付费版 CraftEngine
5. **验证来源** — 所有模板基于 `CraftEngine Wiki` 目录中的原始文档创建

## 📚 参考文档

CraftEngine 原始文档位于同级目录: [`CraftEngine Wiki/`](../CraftEngine%20Wiki/)
