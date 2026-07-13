# Oraxen GUI 物品实战示例

> GUI 物品是专门为自定义菜单界面设计的 Oraxen 自定义物品。它们通常搭配 DeluxeMenus、TrMenu、ChestCommands 等菜单插件使用，作为导航按钮（翻页、退出、返回）或隐形点击区域。GUI 物品与普通自定义物品的区别在于：它们通常被隐藏（不通过 `/oraxen give` 直接获得），仅通过菜单插件引用。
>
> **本文件基于项目实际配置：** `Oraxen/items/guis.yml`

---

## 一、项目真实配置 — 三种基础 GUI 物品

来自项目 `Oraxen/items/guis.yml` 的完整配置（当前为注释状态）：

```yaml
# ============================================================
# 文件: plugins/Oraxen/items/guis.yml
# 用途: 自定义 GUI 界面使用的图标/按钮物品
# ============================================================

# Material 列表参考:
#   https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html
# EntityType 列表参考:
#   https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html
# Attribute 列表参考:
#   https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html
# 药水效果列表参考:
#   https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html
# 随机 UUID 生成器:
#   https://www.uuidgenerator.net/
# 颜色代码参考:
#   https://docs.adventure.kyori.net/minimessage.html#format

# --- 下页箭头按钮 ---
arrow_next_icon:                            # 【必填】物品 ID，全局唯一
                                            #         在其他插件中引用: oraxen:arrow_next_icon
  displayname: <#D5D6D8>Next page              # 【必填】物品显示名称
                                            #         可使用 MiniMessage 颜色标签
                                            #         <#D5D6D8> = 十六进制颜色（浅灰白）
  material: PAPER                           # 【必填】Minecraft 基础物品材质
                                            #         PAPER 是轻量选择，纹理可完全覆盖外观
                                            #         常用的材质: PAPER, IRON_NUGGET, STICK
  excludeFromInventory: true                # 【关键】将此物品从 /oraxen inventory 中隐藏
                                            #        true = 玩家无法通过 /oraxen give 直接获取
                                            #        用于纯 GUI 物品，防止玩家刷出
  Pack:                                     # 【必填】资源包配置
    generate_model: true                    # 【必填】自动生成物品模型 JSON 文件
                                            #         false 仅当你有手动编写的模型文件时使用
    parent_model: "item/generated"          # 【必填】父模型路径
                                            #         item/generated = 标准 2D 物品模型
                                            #         item/handheld   = 手持工具模型（适合剑/工具）
    textures:                               # 【必填】纹理列表
      - required/arrow_next_icon.png        #         纹理路径，相对于 pack/textures/
                                            #         注意此处的路径包含 .png 扩展名！
                                            #         与字形配置不同，Pack 纹理路径需要扩展名
                                            #         实际文件: pack/textures/required/arrow_next_icon.png

# --- 上页箭头按钮 ---
arrow_previous_icon:                        # 上一页箭头，与下页成对使用
  displayname: <#D5D6D8>Previous page
  material: PAPER
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - required/arrow_previous_icon.png    # 纹理: pack/textures/required/arrow_previous_icon.png

# --- 退出/返回主菜单按钮 ---
exit_icon:                                  # 退出按钮，通常放在菜单右下角
  displayname: <gradient:#FA7CBB:#F14658>Back to main menu
                                            # 渐变色名称: 粉色 → 红色
                                            # <gradient:起始色:结束色>文字</gradient>
  material: PAPER
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - required/exit_icon.png              # 纹理: pack/textures/required/exit_icon.png
                                            # 注意: 此纹理与 required.yml 中的字形
                                            # texture: required/exit_icon 对应的
                                            # 是同一个 PNG 文件!
```

---

## 二、excludeFromInventory 详解

```
excludeFromInventory: true 的作用和原理:

1. 功能:
   - 从 /oraxen inventory 命令的 GUI 列表中隐藏此物品
   - 从 /oraxen give 命令的 Tab 补全中移除
   - 玩家无法通过任何 Oraxen 命令直接获取此物品

2. 为什么需要它:
   - GUI 按钮物品不应该被玩家放入背包
   - 这些物品在菜单插件中被直接引用，不需要物理存在
   - 防止玩家使用 /oraxen give arrow_next_icon 刷出箭头物品

3. 工作原理:
   - Oraxen 仍会为物品生成资源包模型和纹理
   - 物品在 Minecraft 中技术上"存在"（资源包已包含其模型）
   - 但 Oraxen 的命令系统拒绝提供此物品给玩家
   - 菜单插件通过物品 ID 引用它时，使用的是 NBT 标签匹配

4. 什么时候设为 false（或不设置）:
   - 物品同时作为 GUI 按钮和实际可收集物品
   - 例如: 一个特殊货币图标既在商店 GUI 中使用，也作为掉落物

5. 重要:
   - excludeFromInventory 只影响 Oraxen 命令系统
   - 具有 OP 权限的玩家仍可通过 /give 命令获取（如果你给他们物品的完整命名空间 ID）
   - 如果想要完全阻止获取，需要配合权限插件
```

---

## 三、透明纹理 — 隐形按钮技术

隐形按钮是 GUI 设计中的核心技术。通过使用透明纹理创建一个不可见的物品，放置在 GUI 槽位中作为背景层或不可见点击区域：

```yaml
# ============================================================
# 文件: plugins/Oraxen/items/invisible_items.yml
# 透明纹理的隐形物品配置
# ============================================================

# --- 完全透明的隐形物品 ---
invisible_button:                           # 用于 GUI 背景层的不互动物品
  displayname: " "                             # 空格作为名称（不可见的名称）
  material: PAPER                           # PAPER 是最轻量的基础材质
  excludeFromInventory: true                # 隐藏（玩家不应获取）
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - required/particle                   # 透明纹理！
                                            # 实际文件: pack/textures/required/particle.png
                                            # 这是一个完全透明的 PNG 文件（1x1 像素或全透明）
                                            # 路径不加 .png 是简写（Oraxen 自动补全）

# --- 带半透明边框的隐形物品（调试用）---
debug_button:                               # 调试用，开发时查看按钮位置
  displayname: "<red>[DEV] Button Slot"        # 调试名称
  material: PAPER
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - required/particle_border            # 带半透明边框的纹理
                                            # 开发时方便看到按钮位置
                                            # 上线前切换为完全透明的 particle

# --- 使用 CUSTOM_MODEL_DATA 的替代方案 ---
invisible_clickable_cmd:
  displayname: " "
  material: IRON_NUGGET
  excludeFromInventory: true
  Pack:
    generate_model: false                   # 不自动生成模型
    custom_model_data: 99999                # 使用自定义模型数据
                                            # 配合手动编写的模型 JSON 文件
                                            # 模型文件中的纹理可指向透明纹理
```

### 透明纹理的制作

```
透明 PNG 纹理的技术要点:

1. 最低限度: 1x1 像素全透明 PNG 文件
2. 推荐: 16x16 或 32x32 全透明（避免某些渲染器的边缘问题）
3. 文件位置: pack/textures/required/particle.png
4. 制作方法:
   - 在任何图像编辑软件中创建全透明背景的新文件
   - 导出为 PNG 格式（确保保留 Alpha 通道）
   - 不需要任何可见像素

5. 为什么用 PAPER 材质:
   - PAPER 在 Minecraft 中是一件"扁平"物品
   - 渲染时只有一层纹理（不像方块有 6 个面）
   - 配合 item/generated 父模型，只渲染 texture[0]
   - 是性能最优的隐形物品载体

6. 调试提示:
   - 开发时先用红色半透明纹理（方便看到按钮位置）
   - 确认按钮位置正确后切换为完全透明
   - 可在配置中保留 debug_button 供开发环境使用
```

---

## 四、完整 GUI 物品配置 — 导航按钮套件

以下是一个完整的 GUI 导航按钮套件，包括翻页、关闭、返回、确认等常用按钮：

```yaml
# ============================================================
# 文件: plugins/Oraxen/items/gui_buttons.yml
# 完整的 GUI 导航按钮套件
# ============================================================

# -------------------- 翻页系统 --------------------
next_page:
  displayname: "<#D5D6D8>下一页 →"
  material: PAPER
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/arrow_next.png                  # 纹理: pack/textures/gui/arrow_next.png
  lore:
    - "<gray>点击查看下一页</gray>"

previous_page:
  displayname: "<#D5D6D8>← 上一页"
  material: PAPER
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/arrow_previous.png              # 纹理: pack/textures/gui/arrow_previous.png
  lore:
    - "<gray>点击查看上一页</gray>"

# -------------------- 导航按钮 --------------------
back_button:
  displayname: "<gradient:#FA7CBB:#F14658>← 返回主菜单</gradient>"
  material: PAPER
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/back_button.png
  lore:
    - "<gray>返回到主菜单</gray>"

close_button:
  displayname: "<red>✕ 关闭</red>"
  material: BARRIER                         # BARRIER 材质自带禁止符号外观
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/close_button.png
  lore:
    - "<gray>关闭当前菜单</gray>"

# -------------------- 确认/取消按钮 --------------------
confirm_button:
  displayname: "<green>✓ 确认</green>"
  material: LIME_DYE                        # 绿色染料（天然绿色图标）
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/confirm_button.png
  lore:
    - "<gray>确认操作</gray>"

cancel_button:
  displayname: "<red>✕ 取消</red>"
  material: RED_DYE                         # 红色染料（天然红色图标）
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/cancel_button.png
  lore:
    - "<gray>取消操作</gray>"

# -------------------- 特殊功能按钮 --------------------
info_button:
  displayname: "<yellow>ℹ 信息</yellow>"
  material: BOOK                            # 书本材质（天然信息图标）
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/info_button.png
  lore:
    - "<gray>查看详细信息</gray>"

settings_button:
  displayname: "<gray>⚙ 设置</gray>"
  material: COMPARATOR                      # 比较器材质（天然设置/齿轮感）
  excludeFromInventory: true
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - gui/settings_button.png
  lore:
    - "<gray>打开设置菜单</gray>"

# -------------------- 空白填充按钮 --------------------
filler_pane:
  displayname: " "
  material: GRAY_STAINED_GLASS_PANE         # 灰色染色玻璃板（半透明背景感）
  excludeFromInventory: true
  Pack:
    generate_model: false                   # 使用原版材质，无需自定义纹理
    # 不设置 textures — 自动使用原版玻璃板纹理
```

---

## 五、GUI 物品与菜单插件的配合使用

### 5.1 在 DeluxeMenus 中使用 Oraxen GUI 物品

```yaml
# ============================================================
# 文件: plugins/DeluxeMenus/gui_menus/example_shop.yml
# DeluxeMenus 配合 Oraxen GUI 物品的完整示例
# ============================================================

menu_title: "<shift:0><glyph:shop_banner>"

size: 54                                     # 6 行库存 (9x6)

items:
  # 背景填充 — 使用透明物品覆盖所有槽位
  background:
    material: "oraxen:invisible_button"      # 引用 Oraxen 物品
    slot: 0-53                               # 覆盖整个库存
    display_name: " "                        # 覆盖为空白名称

  # 装饰性玻璃板边框
  border_top:
    material: "oraxen:filler_pane"
    slot: 0,1,2,3,4,5,6,7,8                # 顶行
    display_name: " "

  border_bottom:
    material: "oraxen:filler_pane"
    slot: 45,46,47,48,49,50,51,52,53        # 底行
    display_name: " "

  # 翻页按钮
  next_page_button:
    material: "oraxen:next_page"             # 引用 Oraxen 下页按钮
    slot: 50                                 # 第 6 行第 6 列（从 0 开始）
    # display_name 自动从 items/guis.yml 的 displayname 继承
    # 如需覆盖:
    # display_name: "自定义名称"
    left_click_commands:
      - "[openguimenu] shop_page_2"         # 打开下一页菜单

  previous_page_button:
    material: "oraxen:previous_page"
    slot: 48                                 # 第 6 行第 4 列
    left_click_commands:
      - "[openguimenu] shop_page_1"

  # 退出按钮
  close_button:
    material: "oraxen:exit_icon"
    slot: 49                                 # 第 6 行第 5 列
    left_click_commands:
      - "[openguimenu] main_menu"

  # 实际商品 — 也可以是 Oraxen 物品
  diamond_offer:
    material: "oraxen:diamond_pack"          # 引用商品物品
    slot: 22                                 # 第 3 行第 5 列
    left_click_commands:
      - "[console] eco take %player_name% 100"
      - "[console] give %player_name% diamond 64"
      - "[message] <green>购买成功! 消费 100 金币</green>"
```

### 5.2 在 TrMenu 中使用

```yaml
# TrMenu 配置示例
title: "<shift:0><glyph:menu_banner>"

layout:
  - "#########"
  - "#  A B #"
  - "#  C D #"
  - "#########"

icons:
  A:
    material: "oraxen:next_page"
    click:
      - condition: 'perm *'
        actions:
          - 'opengui: shop_page_2'

  B:
    material: "oraxen:exit_icon"
    click:
      - condition: 'perm *'
        actions:
          - 'opengui: main_menu'
```

### 5.3 物品槽位布局参考

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 第 0 行 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--:|
| 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 第 1 行 |
| 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 第 2 行 |
| 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 第 3 行 |
| 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 第 4 行 |
| 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 第 5 行 |

典型按钮位置:
  - 翻页按钮: 槽位 48 (上页) 和 50 (下页) — 底行左右
  - 退出按钮: 槽位 49 — 底行正中央
  - 返回按钮: 槽位 45 或 53 — 底行角落
  - 确认按钮: 槽位 47~48 — 底行偏左
  - 取消按钮: 槽位 50~51 — 底行偏右

布局原则:
  - 翻页按钮放在底部中央两侧
  - 导航按钮（返回/关闭）放在右下角
  - 功能按钮（确认/取消）放在底部中央
  - 装饰品放在顶部一行和底部一行
  - 商品/内容放在中间行 (槽位 10~43)

---

## 六、Pack 纹理路径约定

```
Pack 纹理路径与字形纹理路径的区别:

字形配置 (glyphs/*.yml):
  texture: required/exit_icon           ← 不加 .png 扩展名
  texture: default/chat/heart           ← 路径相对于 pack/textures/

物品配置 (items/*.yml):
  Pack:
    textures:
      - required/exit_icon.png          ← 必须加 .png 扩展名！
      - required/arrow_next_icon.png    ← 路径同样相对于 pack/textures/

为什么不一样:
  - 字形系统内部有自己的路径处理逻辑，自动补全 .png
  - 物品 Pack 系统直接使用 Minecraft 资源包模型系统的路径约定
  - 资源包模型 JSON 中的纹理引用必须包含文件扩展名

同名纹理共享:
  - required.yml 中的字形: texture: required/exit_icon
  - guis.yml 中的物品: textures: - required/exit_icon.png
  - 两者指向同一个文件: pack/textures/required/exit_icon.png
  - 这是常见做法: 一个纹理同时作为字形图标和物品图标

推荐目录结构:
  pack/textures/
  ├── required/                      # 插件必需/核心文件
  │   ├── exit_icon.png             # 退出按钮（字形 + 物品共用）
  │   ├── arrow_next_icon.png       # 下页箭头（物品专用）
  │   ├── arrow_previous_icon.png   # 上页箭头（物品专用）
  │   └── particle.png              # 透明纹理（隐形物品用）
  ├── gui/                           # GUI 专用纹理
  │   ├── next_page.png
  │   ├── back_button.png
  │   ├── close_button.png
  │   └── confirm_button.png
  └── default/chat/                  # 聊天/表情纹理
      ├── heart.png
      └── ...
```

---

## 七、物品模型系统简述

```
parent_model 选项:

item/generated:
  - 标准 2D 物品模型（扁平的物品图标）
  - 适用于: 纸张、图标、按钮、大多数 GUI 物品
  - 只渲染 1 层纹理

item/handheld:
  - 手持工具模型（有厚度感，适合武器/工具）
  - 适用于: 剑、斧头、法杖类物品
  - 在 GUI 中与 item/generated 外观相同

block/block:
  - 方块模型（3D 渲染）
  - 适用于: 自定义家具、装饰性方块
  - 在 GUI 中使用需谨慎（渲染不同）

generate_model: true vs false:

true (自动生成):
  - Oraxen 根据 textures 列表自动创建 model JSON
  - 适合: 简单的单纹理物品

false (手动模型):
  - 你需要自己提供模型 JSON 文件
  - 适合: 复杂的多层模型，或使用 custom_model_data
  - 需要使用 custom_model_data 指定模型 ID
```

---

## 八、常见问题排查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| GUI 物品显示为紫黑方块 | 纹理 PNG 文件缺失 | 确认 `pack/textures/xxx.png` 文件存在且路径正确 |
| excludeFromInventory 无效 | 缓存问题 | 执行 `/oraxen reload all` 刷新配置 |
| 材质不是预期的颜色 | parent_model 使用了原版材质 | 确认 `generate_model: true` 且 textures 路径正确 |
| 透明物品仍可见 | 纹理不是真正的全透明 | 用图像编辑器确认 PNG 的 Alpha 通道是全透明的 |
| 物品在菜单中显示为原版物品 | Oraxen 物品 ID 拼写错误 | 确认菜单插件中使用的是 `oraxen:item_id` |
| 纹理路径错误导致加载失败 | Pack textures 路径缺少 .png | 在物品 Pack 配置中务必包含 .png 扩展名 |
| 物品可以被 /oraxen give 获取 | excludeFromInventory 未设置 | 添加 `excludeFromInventory: true` |
| 翻页按钮尺寸与其他物品不一致 | model 不同 | 确认所有按钮使用相同的 parent_model |
