---
name: craftengine-skill
version: 1.4.0
description: >-
  Generate CraftEngine plugin YAML configuration templates based strictly on the
  CraftEngine Wiki and CraftEngine Template content. Analyzes user needs,
  references the correct Wiki sections and Template examples, then generates one
  complete, validated configuration at a time. After generation, validates YAML
  syntax and cross-checks every field against the Wiki to prevent fabricated content.
  Asks the user for any uncertain decisions before proceeding, including whether
  to output the result in chat or save to a file.
  Triggered by: "生成CraftEngine配置", "CE模板生成", "写CraftEngine物品",
  "CraftEngine方块", "CraftEngine家具", "CraftEngine配方", "CraftEngine装备",
  "CE config", "craftengine template", "生成CE物品", "生成CE方块",
  "生成CE家具", "craftengine配置", "写CE配置", "CraftEngine自定义",
  "craftengine item", "craftengine block", "craftengine furniture".
context: fork
agent: general-purpose
allowed-tools: Read Write Glob Grep Bash WebFetch
---

# CraftEngine Skill

## Purpose

根据用户需求，严格基于 Skill 内置的 **CraftEngine Wiki** 和 **CraftEngine Template** 内容，生成符合官方规范的 CraftEngine 插件 YAML 配置模板。每次只生成一个完整的配置（一个物品、一个方块、一个家具等），生成后校验 YAML 语法，并对照 Wiki 验证是否存在虚构内容。

## When to Use

- 用户需要创建 CraftEngine 插件的自定义配置（物品、方块、家具、配方、装备等）
- 用户不熟悉 CraftEngine 配置格式，需要一个模板作为起点
- 用户需要生成一个完整可用的 CraftEngine YAML 配置
- 用户需要校验已有的 CraftEngine 配置是否正确
- 用户需要了解某个 CraftEngine 功能的具体配置方式

## When NOT to Use

- 用户询问 CraftEngine 的概念性问题或插件安装 —— 引导用户阅读 Wiki 或 Template 的 README.md
- 用户需要批量生成多个配置 —— 要求每次只生成一个，多次调用本 Skill
- 用户需要修改项目中已有的配置而非生成新配置
- 需求与 CraftEngine 插件无关（其他 Minecraft 插件如 Oraxen、CustomCrops 等）

## Workflow / Steps

### Step 1: 分析用户需求

解析用户的输入，提取以下关键信息：

1. **配置类型**：用户需要生成什么类型的 CraftEngine 配置？
   - `item` — 物品（武器、工具、食物、消耗品、装饰品、方块物品、家具物品等）
   - `block` — 方块（基础方块、农作物、门、楼梯、存储方块等）
   - `furniture` — 家具（椅子、桌子、灯具、装饰家具等）
   - `recipe` — 配方（有序/无序合成、烧炼、锻造、酿造等）
   - `equipment` — 装备盔甲（组件型/纹饰型）
   - `category` — 物品分类
   - `loot_table` — 战利品表
   - `jukebox_song` — 唱片机曲目
   - `painting` — 画
   - `image` — 图像
   - `emoji` — 表情
   - `sound` — 音效
   - `template` — 模板系统
   - `global_variable` — 全局变量
   - `lang` / `i18n` — 语言/翻译

2. **核心功能**：用户希望这个配置实现什么功能？
   - 例如：可放置的方块、可交互的家具、带特效的武器、可种植的作物等

3. **特殊要求**：是否有版本限制、命名空间要求、材质路径等

4. **不确定之处**：标记所有用户未明确但生成配置所需的信息

如果用户描述模糊，输出你的理解并向用户确认后再继续。

### Step 2: 查阅参考资料

根据 Step 1 判断的配置类型和核心功能，按以下规则查找对应的 Wiki 和 Template 参考文件：

#### Wiki 查阅规则

**物品 (item) 相关：**
- 基本物品配置 → `references/CraftEngine Wiki/configuration/item.md`
- 物品数据（名称/描述/组件/NBT） → `references/CraftEngine Wiki/configuration/item/data.md`
- 物品设置（燃料/标签/装备/弹射物/食物等） → `references/CraftEngine Wiki/configuration/item/settings.md`
- 物品行为（方块物品/家具物品/堆肥/范围挖掘等） → `references/CraftEngine Wiki/configuration/item/behaviors.md` + 对应子页面
- 物品模型（简化/condition/range_dispatch/composite 等 8 种） → `references/CraftEngine Wiki/configuration/item/models.md` + 对应子页面
- 物品更新器 → `references/CraftEngine Wiki/configuration/item/updater.md`

**方块 (block) 相关：**
- 方块基本配置 → `references/CraftEngine Wiki/configuration/block.md`
- 方块状态（单状态/多状态/属性/外观/变体） → `references/CraftEngine Wiki/configuration/block/states.md`
- 方块状态属性类型 → `references/CraftEngine Wiki/configuration/block/states/properties.md`
- 方块实体渲染器 → `references/CraftEngine Wiki/configuration/block/states/entity_renderer.md`
- 方块设置（硬度/音效/光照/工具等） → `references/CraftEngine Wiki/configuration/block/settings.md`
- 方块行为（生长/下落/门/存储/蔓延等） → `references/CraftEngine Wiki/configuration/block/behaviors.md` + 对应子页面
- 方块标签 → `references/CraftEngine Wiki/reference/block_tags.md`

**家具 (furniture) 相关：**
- 家具基本配置 → `references/CraftEngine Wiki/configuration/furniture.md`
- 家具设置（物品/击打次数/音效/挖掘工具） → `references/CraftEngine Wiki/configuration/furniture/settings.md`
- 家具变体（元素/判定箱/座椅/实体剔除） → `references/CraftEngine Wiki/configuration/furniture/variants.md`
- 家具行为（物品展示/发光/存储） → `references/CraftEngine Wiki/configuration/furniture/behaviors.md`

**配方 (recipe) 相关：**
- 配方全部类型（11 种） + 标签/分组/后处理器 → `references/CraftEngine Wiki/configuration/recipe.md`
- 外部物品来源兼容 → `references/CraftEngine Wiki/compatibility/external_item_sources.md`

**其他配置：**
- 装备盔甲 → `references/CraftEngine Wiki/configuration/equipment.md`
- 分类 → `references/CraftEngine Wiki/configuration/category.md`
- 战利品表 → `references/CraftEngine Wiki/reference/loot_table.md`
- 模板系统 → `references/CraftEngine Wiki/reference/template.md`
- 事件系统（46 种函数） → `references/CraftEngine Wiki/reference/events.md`
- 条件系统（27 种条件） → `references/CraftEngine Wiki/reference/conditions.md`
- 文本格式（MiniMessage + 附加标签） → `references/CraftEngine Wiki/reference/text_format.md`
- 数字格式（11 种） → `references/CraftEngine Wiki/reference/number_format.md`
- 链式参数 → `references/CraftEngine Wiki/reference/text_format/chain_arguments.md`
- 全局变量 → `references/CraftEngine Wiki/configuration/global_variable.md`
- 语言/翻译 → `references/CraftEngine Wiki/configuration/lang.md` + `references/CraftEngine Wiki/configuration/i18n.md`
- 图像/表情 → `references/CraftEngine Wiki/configuration/image.md` + `references/CraftEngine Wiki/configuration/emoji.md`
- 唱片/音效 → `references/CraftEngine Wiki/configuration/jukebox_song.md` + `references/CraftEngine Wiki/configuration/sound.md`
- 画 → `references/CraftEngine Wiki/configuration/painting.md`
- 字体 → `references/CraftEngine Wiki/configuration/font.md`
- 文件冲突 → `references/CraftEngine Wiki/reference/file_conflict.md`

#### Template 查阅规则

根据配置类型查找对应的 Template 参考：

**General 目录（完整模板参考，优先使用）：**
- 物品类：
  - `基础物品.yml` — 装饰物品/工具/燃料/方块物品
  - `物品设置.yml` — 全部 settings 选项
  - `物品行为.yml` — 全部 behavior 类型
  - `物品模型类型.yml` — 全部 8 种模型
  - `物品数据组件.yml` — 全部 data 组件
  - `武器.yml` — 剑/弓/弩/三叉戟
  - `工具.yml` — 范围挖掘/弹射物
  - `食物.yml` — 食物/消耗品
  - `消耗品与药水.yml` — 药水/消耗品
  - `音乐唱片.yml` — 唱片机物品
- 方块类：
  - `基础方块.yml` — 14 种方块示例
  - `方块设置.yml` — settings 完整
  - `方块标签.yml` — 标签配置
  - `方块实体渲染器.yml` — entity_renderer
  - `变化与蔓延.yml` — 氧化/扩散/衰变
  - `农作物与植物.yml` — 作物/茎/灌木/树苗
  - `物理机制方块.yml` — 下落/混凝土粉末/弹跳
  - `特殊机制方块.yml` — 可剥离/稳固基底/母岩
  - `展示与粒子效果.yml` — 展示/粒子
  - `朝向与液体交互.yml` — 定向/悬挂/液体
  - `门与红石方块.yml` — 门/活板门/栅栏/按钮
  - `楼梯台阶与多层方块.yml` — 楼梯/台阶/多层
  - `存储与座椅.yml` — 存储/抽屉/座椅
  - `灯与钟.yml` — 灯/可切换灯/震响
- 家具类：
  - `基础家具.yml` — 3 个完整家具示例
  - `家具行为.yml` — display_item/glowing/storage
- 配方类：
  - `配方.yml` — 全部 11 种配方+后处理器
- 装备类：
  - `盔甲套装.yml` — 组件型/纹饰型/3D 头盔
- 其他：
  - `分类配置.yml` — 分类菜单
  - `战利品表.yml` — 战利品表
  - `模板系统.yml` — template/config_factory
  - `事件与条件.yml` — 事件+条件
  - `语言配置.yml` — lang/i18n
  - `图像配置.yml` — image
  - `表情配置.yml` — emoji
  - `文本格式.yml` — MiniMessage 标签
  - `数字格式.yml` — 数字格式
  - `链式参数.yml` — chain arguments
  - `全局变量.yml` — global_variable
  - `物品更新器.yml` — updater
  - `文件冲突配置.yml` — file_conflict
  - `画配置.yml` — painting
  - `字体配置.yml` — font
  - `音乐唱片.yml` — jukebox_song（sound 配置参考 Wiki `configuration/sound.md`）

**Example 目录（可直接使用的完整示例）：**
- `物品/1. 基础材料与宝石.yml` 到 `物品/10. 物品行为完整示例.yml`
- `方块/1. 基础方块.yml` 到 `方块/9. 方块实体渲染器.yml`
- `家具/1. 基础家具.yml` + `家具/2. 家具行为.yml`
- `配方/1. 全部配方类型.yml`
- `装备/1. 盔甲套装.yml`
- `事件与条件/1. 事件函数完整示例.yml` + `2. 条件完整示例.yml`
- `其他配置/1. 图像与表情.yml` 到 `7. 文件冲突与字体与更新器.yml`

使用 `Read` 工具读取对应的 Wiki 页面和 Template 文件，将关键配置结构加载到上下文中。

#### 参考来源优先级规则

生成配置时，严格按照以下优先级使用参考来源：

1. **本地 CraftEngine Wiki**（`references/CraftEngine Wiki/`）— 最优先，默认使用
2. **本地 CraftEngine Template**（`references/CraftEngine Template/`）— 辅助参考
3. **官方在线文档**（[https://ce.gtemc.cn/zh-Hans/](https://ce.gtemc.cn/zh-Hans/)）— **仅在用户明确要求时才使用**

#### 在线文档使用规则

- **在用户明确说明要使用官方在线文档之前，绝对不要使用在线文档。** 始终优先使用本地文档。
- 如果遇到本地 Wiki 和 Template 中均未记载的功能或字段，且你觉得有必要查阅在线文档，**必须先向用户确认**是否搜索在线文档。
- 向用户确认时，必须说明：**在线文档可能因网络原因无法访问**。
- 如果用户同意使用在线文档，使用 `WebFetch` 或 `WebSearch` 工具获取在线文档内容。
- 如果在线文档无法访问（网络超时、404 等），**必须告知用户无法访问**，并询问用户是否仍要继续生成（此时告知用户缺少参考依据，配置可能有风险），或中止当前操作。

#### 验证规则

- 必须实际读取文件内容，不得仅凭文件名推断
- 同一功能同时读取 Wiki 和对应 Template 进行交叉验证
- 如果 Wiki 和 Template 对同一字段描述不一致，**以 Wiki 为准**
- 对于不确定的字段用法，查看 Wiki 中的具体示例确认
- 记录读取了哪些参考文件，供 Step 5 校验使用

### Step 3: 向用户确认不确定项

在生成配置之前，列出所有无法确定的信息并向用户提问。包括但不限于：

- **命名空间**（默认 namespace，建议用户提供）
- **物品/方块 ID**（需用户指定）
- **材质/模型路径**（需用户指定）
- **显示名称和描述文本**（需用户提供）
- **具体数值**（如耐久度、伤害值、烧炼时间等）—— 如果用户未指定，使用合理的默认值并标注
- **行为参数**（如方块行为的具体类型参数）
- **版本要求**（针对哪个 Minecraft 版本？默认使用最新）
- **付费版功能**：如果用户所需功能仅付费版支持，明确告知用户
- **在线文档查询**：如果本地 Wiki 和 Template 均无法满足需求，**向用户询问**是否尝试查阅官方在线文档（`https://ce.gtemc.cn/zh-Hans/`），同时说明在线文档可能因网络原因无法访问

#### 输出方式询问（新增）

**如果用户没有明确说明输出方式，必须向用户询问：**
- **对话中返回** — 配置以 YAML 代码块形式直接展示在对话中
- **输出到文件** — 使用 `Write` 工具将配置保存到项目目录下的指定位置

询问格式示例：
> 输出方式：你希望生成的配置以什么形式交付？
> 1. **对话中返回** — 直接展示 YAML 代码块，方便复制
> 2. **输出到文件** — 保存到项目目录，方便后续管理

如果用户选择了"输出到文件"，继续询问：
- 保存路径（默认：`plugins/CraftEngine/<对应子目录>/<id>.yml`）
- 文件名

**判断规则：**
- 用户说"保存""生成到""写到文件""输出到"等 → 视为选择"输出到文件"
- 用户说"展示""显示""看看""给我看"等 → 视为选择"对话中返回"
- 用户没有明确倾向 → 默认选择"输出到文件"并询问路径

提问格式示例：
> 我将为你生成一个 [配置类型]，需要以下信息：
> 1. 命名空间（如 `my_namespace`）：？
> 2. 物品 ID（如 `my_sword`）：？
> 3. 材质路径（如 `minecraft:item/custom/my_sword`）：？
> 4. 显示名称：？
> 5. ...其他问题

除非用户明确说"你自己决定"，否则不得跳过此步骤擅自假设。

### Step 4: 生成配置模板

根据 Wiki 和 Template 参考内容，严格按照以下规范生成配置：

#### 通用规范

1. **文件结构**：
   ```yaml
   # =============================================================================
   # CraftEngine [配置类型] 配置 — [配置名称]
   # =============================================================================
   # Wiki 参考路径:
   #   - references/CraftEngine Wiki/[对应Wiki路径]
   # Template 参考:
   #   - references/CraftEngine Template/[对应Template路径]
   # =============================================================================

   [根键]:
     [命名空间]:[ID]:
       # 配置内容
   ```

2. **命名空间格式**：使用 `小写英文:小写英文_id` 格式（如 `default:topaz_sword`）

3. **必填字段**必须标注（来源：[Wiki 页面名]）
4. **可选字段**标注默认值（来源：[Wiki 页面名]）
5. **付费版功能**标注 `# 付费版专属`
6. **版本要求**标注 `# 需要 1.21.2+` 等
7. **<< CHANGE THIS** 标记所有需要用户自行修改的值

#### 配置类型规范

**物品 (items) 生成规范：**
```yaml
items:
  namespace:item_id:
    material: paper          # 必填。基础材质
    custom_model_data: 1001  # 可选。正整数，同材质物品不同值
    item_model: "namespace:item_id"  # 可选。1.21.2+
    # data:
    #   item_name: "<!i><颜色>名称"
    #   lore: [...]
    #   components: {...}
    # settings: {...}
    # behavior:
    #   type: block_item / furniture_item / ...
    # model: {...}
    # events: [...]
    # category: namespace:category_id
```

**方块 (blocks) 生成规范：**
```yaml
blocks:
  namespace:block_id:
    state:
      auto_state: note_block
      model:
        texture: "minecraft:block/custom/..."  # 单张纹理
    settings:
      hardness: 2.0
      # ...
    # behavior:
    #   type: ...
    # loot: {...}
    # events: [...]
```

**家具 (furniture) 生成规范：**
```yaml
furniture:
  namespace:furniture_id:
    settings:
      item: namespace:furniture_item_id
      hit_times: 3
      sounds: {...}
    variants:
      ground:
        elements:
          - type: item_display
            item: namespace:furniture_item_id
            # ...
        hitboxes:
          - type: shulker / interaction / ...
            # ...
```

**配方 (recipes) 生成规范：**
```yaml
recipes:
  namespace:recipe_id:
    type: shaped / shapeless / smelting / ...
    pattern: [...]
    ingredients: {...}
    result:
      id: namespace:item_id
      count: 1
```

#### 关键约束

- **绝对不要使用 Wiki 中没有提到的字段、参数或功能。** 如果你不确定某字段是否存在，查找 Wiki 确认。Wiki 中找不到的，不使用。
- **绝对不要假设 Template 中的示例包含所有可能字段。** Template 只是示例，完整字段列表以 Wiki 为准。
- **YAML 格式必须正确。** 注意缩进（2 空格）、冒号后的空格、列表的连字符格式。
- **注释中使用参考来源。** 每个主要配置块旁标注对应的 Wiki 页面路径。
- **使用 "<!i>" 前缀** 确保物品名称在 1.20.4 及以下版本正确显示（来源：Wiki data.md item_name 节）。
- **使用 MiniMessage 格式** 进行文本格式化（来源：Wiki reference/text_format.md）。
- **可选字段注释掉** 而非删除，方便用户按需启用。

### Step 5: 校验生成的配置

生成配置后，执行以下校验步骤：

#### 5a. YAML 语法校验

运行以下命令验证 YAML 是否合法：

```bash
python -c "import yaml; yaml.safe_load(open('配置路径', 'r', encoding='utf-8'))" 2>&1
```

如果 Python 不可用，手动逐行检查：
- 缩进是否一致（统一 2 空格）
- 冒号后是否有空格
- 列表项 `- ` 格式是否正确
- 字符串引号是否匹配
- 多行字符串格式是否正确

#### 5b. Wiki 对照校验

逐字段检查生成的配置，确保：

1. **所有字段名都存在于 Wiki 中** — 对照 Step 2 中读取的 Wiki 页面，逐一确认每个键名
2. **所有字段类型正确** — Wiki 中定义为字符串的不写为数字，列表不写为映射
3. **所有字段值范围正确** — 如 boolean 只用 `true`/`false`，方向值用 `north`/`south`/`east`/`west`/`up`/`down`
4. **没有虚构功能** — 不要假设 CraftEngine 支持某个 Wiki 未记载的功能
5. **auto_state 组名** — 必须使用 Wiki states.md 表格中列出的组名（如 `solid`、`note_block`、`leaves` 等）
6. **属性类型** — 必须使用 Wiki properties.md 中定义的 11 种类型之一

#### 5c. 不确定项标记检查

检查所有不确定的值是否已使用 `<< CHANGE THIS` 标记，以便用户知晓需要修改。

#### 5d. 修复并重校验

如果发现问题，立即修正配置，然后重新执行 Step 5a-5c 直到全部通过。

### Step 6: 输出结果

根据 Step 3 确认的输出方式，按对应格式输出：

#### 6a. 对话中返回

以 Markdown 代码块形式展示完整的 YAML 配置，包含：

1. **生成的配置内容** — 以 YAML 代码块展示完整的配置
2. **参考来源** — 列出参考的 Wiki 页面和 Template 文件
3. **需修改项** — 列出所有标记了 `<< CHANGE THIS` 的项
4. **注意事项** — 版本要求、付费版限制、已知限制等
5. **保存建议** — 建议将配置保存到 `plugins/CraftEngine/` 的哪个子目录

#### 6b. 输出到文件

使用 `Write` 工具将配置保存到指定路径：

1. **确定保存路径** — 使用 Step 3 中用户确认的路径，默认为：
   - `items:` → `plugins/CraftEngine/items/<id>.yml`
   - `blocks:` → `plugins/CraftEngine/blocks/<id>.yml`
   - `furniture:` → `plugins/CraftEngine/furniture/<id>.yml`
   - `recipes:` → `plugins/CraftEngine/recipes/<id>.yml`
   - `equipments:` → `plugins/CraftEngine/equipments/<id>.yml`
   - 以此类推，子目录名与 YAML 根键名一致
2. **检查目录是否存在** — 如果目标目录不存在，先向用户确认是否创建
3. **写入文件** — 使用 `Write` 工具保存配置，包含完整的文件头注释（Wiki 参考路径、Template 参考路径、使用说明）
4. **输出报告** — 向用户报告文件已保存的路径、文件内容概要、需修改项列表、注意事项

#### 判断规则

- 如果 Step 3 未确定输出方式，**不得默认使用"对话中返回"**，必须回到 Step 3 询问用户
- 使用 `Write` 工具前，先确认目标目录所在的项目路径是否存在

## Constraints

- **Always** 在生成任何配置前，先读取对应的 Wiki 页面和 Template 文件，确保准确理解配置结构
- **Always** 严格遵守 Wiki 内容 — Wiki 中没有的功能/字段绝对不使用
- **Always** 以 Wiki 为准 — 如果 Template 与 Wiki 描述不一致，以 Wiki 为准
- **Always** 一次只生成一个配置（一个物品、一个方块、一个家具等），不要一次性生成多个
- **Always** 生成完成后执行 YAML 语法校验和 Wiki 对照校验
- **Always** 对任何不确定的配置项向用户提问，除非用户明确授权你自行决定
- **Always** 使用 `<< CHANGE THIS` 标记所有需要用户修改的值
- **Always** 在配置注释中标注参考来源（Wiki 页面路径）
- **Always** 在配置中标注字段的必填/可选状态和默认值
- **Always** 标注付费版专属功能和版本要求
- **Always** 如果用户没有明确说明输出方式（对话中返回 / 输出到文件），必须向用户询问后再输出
- **Never** 在用户未明确输出方式的情况下默认使用"对话中返回"进行交付
- **Always** 优先使用本地 CraftEngine Wiki 和 Template，**绝不**在用户未明确要求时擅自使用在线文档
- **Always** 如果觉得有必要查阅在线文档，必须先向用户确认，并说明在线文档可能因网络原因无法访问
- **Always** 尝试在线文档后若无法访问，必须告知用户，并询问是否继续或中止
- **Never** 在本地文档完全满足需求时向用户提出使用在线文档
- **Never** 使用推测或假设的功能 — 只使用 Wiki 中明确记载的
- **Never** 同时生成多个配置 — 用户需要多个配置时，分别调用
- **Never** 在配置中存在语法错误时交付
- **Never** 使用 `is:` 键（CraftEngine 不使用此键）
- **Never** 假设 Template 文件中的占位符 namespace（如 `my:`、`custom:`）是正确的 — 提示用户替换
- **Never** 在 YAML 中使用 Tab 缩进 — 只使用 2 空格缩进

## Examples

### ✅ Do This

**用户输入：**
```
生成一个可放置的家具椅子，双人座，带座椅功能
```

**正确做法：**

Step 1 分析：
- 配置类型：furniture（家具）
- 核心功能：双人座椅子，带座椅（两个座位）
- 参考：furniture.md + furniture/variants.md（seats 配置）

Step 2 查阅：
- Read `references/CraftEngine Wiki/configuration/furniture.md` — 了解家具整体结构
- Read `references/CraftEngine Wiki/configuration/furniture/settings.md` — 了解 settings 选项
- Read `references/CraftEngine Wiki/configuration/furniture/variants.md` — 了解 elements、hitboxes、seats 配置
- Read `references/CraftEngine Template/General/基础家具.yml` — 参考椅子示例

Step 3 向用户确认：
> 需要以下信息：
> 1. 命名空间：？
> 2. 家具 ID（如 `double_chair`）：？
> 3. 物品 ID（如 `double_chair_item`）：？
> 4. 显示名称：？
> 5. 材质路径：？
> 6. 输出方式：你希望生成的配置以什么形式交付？
>    a) **对话中返回** — 直接展示 YAML 代码块
>    b) **输出到文件** — 保存到项目目录

（用户选择"对话中返回"）

Step 4 生成配置（示例输出）：
```yaml
# =============================================================================
# CraftEngine 家具配置 — 双人座椅
# =============================================================================
# Wiki 参考:
#   - references/CraftEngine Wiki/configuration/furniture.md
#   - references/CraftEngine Wiki/configuration/furniture/settings.md
#   - references/CraftEngine Wiki/configuration/furniture/variants.md
# Template 参考:
#   - references/CraftEngine Template/General/基础家具.yml (示例 1: 基础椅子)
# =============================================================================

furniture:
  namespace:double_chair:              # << CHANGE THIS: 家具ID
    settings:
      item: namespace:double_chair     # << CHANGE THIS: 对应物品ID
      hit_times: 3                     # 击打次数 (可选, 默认值: 未定义)
      sounds:
        break: minecraft:block.bamboo_wood.break   # << CHANGE THIS
        place: minecraft:block.bamboo_wood.place   # << CHANGE THIS
        hit: minecraft:block.bamboo_wood.hit       # << CHANGE THIS
      adventure_mode_breaking: false   # 冒险模式破坏 (可选)
      correct_tools:                   # 合适挖掘工具 (可选)
        - "#minecraft:axes"
    variants:
      ground:
        loot_spawn_offset: 0.5,0.5,0   # 掉落物偏移 (可选)
        elements:
          - type: item_display         # 物品展示实体
            item: namespace:double_chair_item  # << CHANGE THIS
            display_transform: none
            billboard: fixed
            position: 0.5,0,0
            translation: 0,0.5,0
            scale: 1
        hitboxes:
          - type: shulker              # 潜影贝判定箱 (硬碰撞)
            can_use_item_on: true
            blocks_building: true
            position: 0,0,0
            scale: 1
            peek: 0
            direction: east
            interaction_entity: true
            interactive: true
            seats:                     # 双人座位
              - 0,0,-0.1 0             # 第一个座位
              - 1,0,-0.1 0             # 第二个座位 (来源: Wiki furniture/variants.md seats)
```

Step 5 校验：
- YAML 语法校验通过
- Wiki 对照：seats 格式 `x,y,z yaw` 来自 Wiki variants.md；所有字段名均存在于 Wiki

### ❌ Not This

**错误做法 — 生成配置时包含 Wiki 未记载的功能：**
```yaml
# ❌ Wiki 中不存在 "auto_rotate" 字段
variants:
  ground:
    auto_rotate: true
    elements:
      - ...
```

**错误做法 — 不查阅 Wiki 直接凭记忆生成：**
```yaml
# ❌ 假设所有物品都需要 "display_name" 字段（Wiki 中不存在此字段）
items:
  my:item:
    display_name: "My Item"  # ❌ Wiki 中使用 data.item_name
```

**错误做法 — 一次生成多个配置：**
> 用户说要一个椅子，一次性生成了椅子+桌子+灯具+配方共 4 个配置

**错误做法 — 不向用户确认不确定项：**
> 用户说"生成个剑"，直接假设了命名空间为 `default`、伤害值为 10、材质路径等

**错误做法 — 用户未指定输出方式时自行假设：**
> 用户说"生成一个铁剑的 CraftEngine 配置"，没有说明要保存还是展示
> ❌ 直接以代码块输出到对话中，未询问用户是否需要保存到文件
> ✅ 应先询问：你希望生成的配置以什么形式交付？（对话中返回 / 输出到文件）

## Notes

- **项目中 Skill 内置的 Wiki 和 Template 路径**：所有 Wiki 文件位于 `references/CraftEngine Wiki/`，Template 文件位于 `references/CraftEngine Template/`。
- **官方在线文档地址**：[https://ce.gtemc.cn/zh-Hans/](https://ce.gtemc.cn/zh-Hans/) — 仅当用户明确要求时使用，不可擅自访问。由于网络环境差异，在线文档可能无法访问，尝试后如不可用应向用户报告。
- **命名空间规范**：CraftEngine 使用 `命名空间:路径` 格式（如 `default:topaz_sword`），命名空间建议使用小写英文。
- **版本差异**：CraftEngine 的部分功能依赖 Minecraft 版本。1.20.5+ 使用组件系统，旧版本使用 NBT。生成配置时注意版本标注。
- **付费版功能**：`client_bound_data`、`client_bound_material`、`visual_result`、`functions`、`conditions`（配方级）、`conditional`（条件数据）等为付费版专属，生成时需要标注。
- **auto_state 组**：方块状态使用 `auto_state` 时，组名必须来自 Wiki states.md 列的表格（如 `solid`、`note_block`、`leaves` 等）。
- **YAML 格式**：CraftEngine 支持 `.yml` 和 `.yaml` 扩展名，配置文件应使用 UTF-8 编码。
- **区块标识符**：当单个 YAML 文件中出现多个同一根键的配置块时，使用 `items#0:`、`items#1:` 格式（来源：Wiki configuration.md）。
- **Template 优势**：CraftEngine 的模板系统（`templates` + `arguments`）可以大幅减少重复配置，适合批量生成类似物品。
- **文件存放位置**：生成的配置文件应根据根键放入 CraftEngine 的对应子目录（如 `items:` → `items/` 目录，`blocks:` → `blocks/` 目录，`recipes:` → `recipes/` 目录等）。
- **输出方式选择**：两种输出方式各有适用场景。"对话中返回"适合快速查看和复制配置片段；"输出到文件"适合生成完整配置后直接使用。如果用户不确定选择哪个，推荐"输出到文件"以便后续管理。
