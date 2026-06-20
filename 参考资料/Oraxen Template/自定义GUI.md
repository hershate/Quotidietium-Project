# Oraxen 自定义 GUI 配置模板

> 使用 Oraxen 字形可以创建自定义带纹理的 GUI（图形用户界面）。
> 纹理作为库存背景，配合隐形物品实现可点击的交互按钮。
>
> **GUI 纹理的实质：** 一个高 height 值的字形，覆盖整个库存界面作为背景图层。
>
> **配置文件位置：**
> - GUI 纹理字形: `plugins/Oraxen/glyphs/` 目录下的任意 `.yml` 文件
> - 隐形物品: `plugins/Oraxen/items/` 目录下的任意 `.yml` 文件

---

## 一、GUI 纹理字形配置

> GUI 纹理实质上是一个大尺寸的字形。纹理分辨率不能超过 256x256 像素，
> 纹理文件名必须全小写、不含空格（符合资源包文件规范）。

```yaml
# ============================================================
# 文件: plugins/Oraxen/glyphs/gui.yml （或其他任意名称的 .yml 文件）
# ============================================================

# --- 基础 GUI 背景纹理 ---
customshop:                             # 【必填】字形 ID（同时也是 GUI 标识）
  texture: custom/gui/shop_bg           # 【必填】纹理路径，相对于 pack/textures/（不加 .png）
  ascent: 13                            # 【必填】垂直偏移，控制纹理在库存中的上下位置
  height: 256                           # 【必填】显示高度，通常设为 256 以填满库存高度
  # 纹理尺寸建议:
  #   宽度: 根据 GUI 列数（通常 9 格 ≈ 176 像素内容区）
  #   高度: 库存总高约 166 像素（6 行），设为 256 可通过 ascent 微调

# --- 另一个 GUI 纹理示例 ---
quest_menu:
  texture: custom/gui/quest_bg
  ascent: 10
  height: 256
```

---

## 二、水平位置调整

> 使用 MiniMessage 的 `<shift:N>` 标签调整纹理/字形在库存中的水平位置。

```
<shift:-8>      向后（左）移动 8 像素
<shift:211>     向前（右）移动 211 像素
<shift:100>     向右移动 100 像素
```

### GUI 标题中使用字形和位移

> 在任何支持 MiniMessage 的插件（如 DeluxeMenus、TrMenu 等）中，
> 将 GUI 标题设置为包含字形的文本即可显示纹理背景。

```
# 示例: GUI 标题配置（配合菜单插件使用）
title: "<shift:0><glyph:customshop>"

# 调整水平位置的示例:
title: "<shift:50><glyph:customshop>"

# 组合多个字形:
title: "<shift:0><glyph:gui_left><shift:100><glyph:gui_right>"
```

---

## 三、隐形物品（可点击按钮）

> 隐形物品是制作可点击按钮的关键。创建一个透明纹理的物品，
> 放在 GUI 中即可作为玩家看不到但能点击的交互按钮。

```yaml
# ============================================================
# 文件: plugins/Oraxen/items/invisible_items.yml
# ============================================================

# --- 基础隐形物品 ---
invisible_item:                         # 【必填】物品 ID
  displayname: "<white>"                # 【必填】显示名称（设为空白或透明色）
  material: PAPER                       # 【必填】Minecraft 物品材质（PAPER 轻量推荐）
  Pack:                                 # 【必填】资源包配置
    generate_model: true                # 【必填】自动生成物品模型
    parent_model: "item/generated"      # 【必填】父模型
    textures:
      - required/particle               # 【必填】透明纹理路径

# --- 带自定义模型的隐形按钮 ---
invisible_button:
  displayname: "<white>"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - required/particle
  # 可以通过 Mechanics 给按钮添加点击功能（见下方）

# --- 使用自定义模型遮挡 (Custom Model Data) ---
# 如果不想用透明纹理，也可以让物品使用一个极小的模型
invisible_clickable:
  displayname: " "
  material: IRON_NUGGET
  Pack:
    generate_model: false               # 使用手动模型时不自动生成
    custom_model_data: 99999            # 自定义模型数据 ID
```

---

## 四、完整 GUI 示例

> 以下示例展示如何创建一个简单的自定义商店 GUI：
> 一个带纹理背景的 3 行库存界面，包含 3 个可点击按钮。

### 第一步：创建 GUI 背景字形

```yaml
# ============================================================
# 文件: plugins/Oraxen/glyphs/gui.yml
# ============================================================

shop_gui:
  texture: custom/gui/shop_background
  ascent: 8
  height: 256
```

### 第二步：创建隐形按钮物品

```yaml
# ============================================================
# 文件: plugins/Oraxen/items/buttons.yml
# ============================================================

shop_button:
  displayname: "<white>"
  material: PAPER
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - required/particle
```

### 第三步：创建交互物品（带名称和图标的可点击物品）

```yaml
# ============================================================
# 文件: plugins/Oraxen/items/shop_items.yml
# ============================================================

diamond_pack:
  displayname: "<gradient:#00FFFF:#0088FF>钻石礼包</gradient>"
  material: DIAMOND
  lore:
    - "<gray>包含 64 颗钻石"
    - "<green>点击购买 <yellow>100 金币"
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - custom/items/diamond_pack
  Mechanics:
    custom:
      purchase:                         # Mechanics 配置
        event: CLICK:left:all           # 左键点击触发
        actions:
          # 在此定义购买逻辑（需配合其他插件或脚本）
          # 例如: console_command: "eco take %player% 100"
          #       give_item: "diamond 64"

iron_pack:
  displayname: "<gradient:#DDDDDD:#888888>铁锭礼包</gradient>"
  material: IRON_INGOT
  lore:
    - "<gray>包含 64 个铁锭"
    - "<green>点击购买 <yellow>50 金币"
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - custom/items/iron_pack

close_button:
  displayname: "<red>关闭</red>"
  material: BARRIER
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - custom/items/close_btn
```

### 第四步：在菜单插件中使用（以 DeluxeMenus 为例）

```yaml
# ============================================================
# 文件: plugins/DeluxeMenus/gui_menus/shop.yml
# （此文件格式取决于你使用的菜单插件）
# ============================================================

menu_title: "<shift:0><glyph:shop_gui>"      # 使用字形作为背景

size: 27                                      # 3 行库存

items:
  # 背景装饰层 — 使用隐形物品覆盖不需要交互的格子
  background:
    material: "oraxen:shop_button"
    slot: 0-26                                # 铺满所有槽位
    display_name: " "                         # 空白名称

  # 实际交互物品 — 覆盖在隐形物品之上
  diamond_button:
    material: "oraxen:diamond_pack"
    slot: 11                                  # 放在第 2 行第 3 列
    display_name: "<glyph:diamond_icon> <gradient:#00FFFF:#0088FF>钻石礼包"

  iron_button:
    material: "oraxen:iron_pack"
    slot: 13                                  # 放在第 2 行第 5 列
    display_name: "<glyph:iron_icon> <gradient:#DDDDDD:#888888>铁锭礼包"

  close_button:
    material: "oraxen:close_button"
    slot: 15                                  # 放在第 2 行第 7 列
```

---

## 五、GUI 设计要点总结

| 要素 | 说明 |
|------|------|
| **GUI 纹理** | 一个 height=256 的字形，通过 GUI 标题中的 `<glyph:ID>` 标签显示 |
| **纹理限制** | 分辨率不超过 256x256 像素，文件名全小写无空格 |
| **水平定位** | 使用 `<shift:N>` 标签调整纹理的水平位置 |
| **隐形物品** | 透明纹理的物品，作为背景层填充不需要交互的槽位 |
| **交互物品** | 普通 Oraxen 自定义物品，放在隐形物品之上提供可点击的图标 |
| **库存大小** | 通过菜单插件的 `size`/`rows` 配置控制 |
| **物品排列** | 槽位编号从 0 开始（0-8 第 1 行，9-17 第 2 行，以此类推） |
