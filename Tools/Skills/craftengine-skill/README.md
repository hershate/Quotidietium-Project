# CraftEngine Skill

> 由正版 ID 为 **ZTF3** 的玩家根据 CraftEngine 官方文档整理和撰写。

## 简介

一个严格基于 Skill **内置的 CraftEngine Wiki 和 CraftEngine Template** 内容，自动生成 CraftEngine 插件 YAML 配置模板的 Claude Code Skill。

每次只生成一个完整的配置（物品/方块/家具/配方等），生成后校验 YAML 语法，并对照 Wiki 验证是否存在虚构内容。对于不确定的配置项会主动向用户提问，不会擅自假设。

## 目录结构

```
craftengine-skill/
├── SKILL.md                              # 技能主文件
├── README.md                             # 本文件
├── references/
│   ├── CraftEngine Wiki/                 # 本地 Wiki 副本（145 个 .md 文件）
│   └── CraftEngine Template/             # 本地 Template 副本（76 个 .yml/.md 文件）
└── scripts/                              # (预留) 辅助脚本
```

## 安装方式

将本 Skill 整体复制到 `.claude/skills/craftengine-skill/` 目录下，重启 Claude Code 即可使用。

> 本 Skill 已自包含所有 Wiki 和 Template 参考文件（位于 `references/` 目录），无需额外配置或依赖项目中的原始文件。

## 使用方式

### 斜杠命令

`/craftengine-skill <需求描述>` — 根据描述生成对应的 CraftEngine 配置模板

### 自动触发

当用户输入以下关键词时自动激活：

- "生成CraftEngine配置"、"CE模板生成"
- "写CraftEngine物品"、"CraftEngine方块"、"CraftEngine家具"、"CraftEngine配方"
- "craftengine template"、"CE config"
- "生成CE物品"、"生成CE方块"、"生成CE家具"
- "craftengine配置"、"写CE配置"

## Workflow 说明

1. **需求分析** — 解析用户需求，确定配置类型和核心功能
2. **查阅参考资料** — 读取 Skill 内置的 Wiki 和 Template 对应页面
3. **确认不确定项** — 向用户询问缺失信息（含输出方式选择）
4. **生成配置模板** — 严格依据 Wiki 内容生成 YAML 配置
5. **校验** — YAML 语法校验 + Wiki 逐字段对照校验
6. **交付** — 按用户选择的输出方式交付（对话返回 / 保存文件）

## 支持的全部配置类型

| 类型 | 说明 | 参考 Wiki 页面数 |
|------|------|-----------------|
| `items` | 物品（武器/工具/食物/消耗品/方块物品/家具物品等） | 10+ |
| `blocks` | 方块（基础/农作物/门/楼梯/存储/红石等 60+ 行为） | 70+ |
| `furniture` | 家具（椅子/桌子/灯具/装饰/存储家具等） | 8 |
| `recipes` | 配方（11 种类型：有序/无序/烧炼/锻造/酿造等） | 2 |
| `equipment` | 装备盔甲（组件型 1.21.2+ / 纹饰型 1.20+） | 2 |
| `category` | 物品分类菜单（多级嵌套） | 1 |
| `loot_table` | 战利品表（条目/函数/公式） | 1 |
| `jukebox_song` | 唱片机曲目 | 1 |
| `painting` | 画 | 1 |
| `image` / `emoji` | 图像/表情 | 2 |
| `sound` | 音效 | 1 |
| `template` | 模板系统（含配置工厂） | 1 |
| `lang` / `i18n` | 语言/翻译 | 2 |
| `global_variable` | 全局变量 | 1 |

## 核心原则

### 严格遵循 Wiki

**Wiki 中没有的功能，绝不使用。** 如果用户要求的功能在 Wiki 中没有记载，Skill 会明确告知用户该功能不可用或未记载，而不是自行推测配置方式。

### Template 为辅助，Wiki 为准

Template 文件提供了便捷的参考示例，但如果 Template 与 Wiki 对同一字段的描述有差异，**以 Wiki 为准**。

### 一次一个配置

每次调用只生成一个配置，确保配置质量和可维护性。如需多个配置请多次调用。

### 不确定就问

对于任何无法从用户描述中确定的配置项（命名空间、ID、数值、路径、输出方式等），Skill 会主动提问确认，绝不擅自假设。

### 本地文档优先

Skill **始终优先使用内置的本地文档**。官方在线文档（[https://ce.gtemc.cn/zh-Hans/](https://ce.gtemc.cn/zh-Hans/)）仅当用户**明确要求**时才会尝试访问，且会提前说明网络不可用的风险。

## 技术细节

### 依赖

- **Python 3**（可选） — 用于自动 YAML 语法校验（`pip install pyyaml`）。未安装时使用手动校验。
- **Skill 内置的 CraftEngine Wiki 和 CraftEngine Template** — 位于 `references/` 目录下，安装即用。

### 使用的工具

- `Read` — 读取内置 Wiki 和 Template 参考文件
- `Write` — 保存生成的配置到文件
- `Glob` — 搜索对应的参考文件
- `Grep` — 在 Wiki 中搜索特定字段确认用法
- `Bash` — 运行 YAML 语法校验命令
- `WebFetch` — 用户明确要求时访问官方在线文档

### 输出说明

- 支持两种输出方式：
  - **对话中返回**：配置以 YAML 代码块形式直接展示，适合快速复制
  - **输出到文件**：使用 `Write` 工具保存到指定路径，适合后续管理
- 如果用户未指定输出方式，Skill 会主动询问
- 配置中所有需要用户修改的值使用 `<< CHANGE THIS` 标记

## 注意事项

- **PyYAML 依赖**：如需自动 YAML 语法校验，需安装 PyYAML（`pip install pyyaml`）。未安装时使用手动校验。
- **CraftEngine 版本**：内置 Wiki 基于官方文档仓库 [Xiao-MoMi/craft-engine-wiki](https://github.com/Xiao-MoMi/craft-engine-wiki) 在 **2026 年 6 月 23 日**的内容，可能落后于 CraftEngine 最新版本。如需查阅最新内容，可告知 Skill 尝试访问官方在线文档（[https://ce.gtemc.cn/zh-Hans/](https://ce.gtemc.cn/zh-Hans/)），但需注意在线文档可能因网络原因无法访问。
- **内容准确性**：本 Skill 的 Wiki 和 Template 内容均整理自上述官方仓库。**如有错误欢迎指正。**
- **付费版功能标注**：配置中所有付费版功能（`client_bound_data`、`visual_result` 等）都会标注 `# 付费版专属`，方便用户区分。
- **版本兼容性**：配置中会标注需要的最低 Minecraft 版本（如 `# 需要 1.21.2+`）。
- **文件存放**：生成的配置文件应根据根键放入 `plugins/CraftEngine/` 下对应子目录（根键名即子目录名）。

## 版权与许可

本 Skill 所有内容（包括 SKILL.md、README.md 及 references/ 目录下的所有文件）统一采用 **Apache License 2.0** 协议开源。

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

## 参考

- [CraftEngine Wiki (Skill 内置)](./references/CraftEngine Wiki/)
- [CraftEngine Template (Skill 内置)](./references/CraftEngine Template/)
- [CraftEngine 官方在线文档](https://ce.gtemc.cn/zh-Hans/)
- [Quotidietium-Project 仓库](https://github.com/hershate/Quotidietium-Project)
