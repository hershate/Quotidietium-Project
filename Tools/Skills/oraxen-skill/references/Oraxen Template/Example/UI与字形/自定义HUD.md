# Oraxen 自定义 HUD 实战示例

> HUD（抬头显示，Heads-Up Display）在 Minecraft 中通过操作栏（Action Bar）实现。Oraxen 提供了一套完整的 HUD 系统，允许你在屏幕底部操作栏位置显示自定义的文本、图标、数值等信息。支持 PlaceholderAPI 占位符和 MiniMessage 标签。
>
> **重要：** 任何其他使用操作栏的插件可能与 Oraxen HUD 产生干扰。HUD 通过每 N 个游戏刻重新发送操作栏内容来实现"持续显示"效果。
>
> **配置文件位置：** `plugins/Oraxen/hud.yml`
>
> **本文件基于项目实际配置：** `Oraxen/hud.yml`

---

## 一、HUD 基础结构

来自项目 `Oraxen/hud.yml` 的真实配置：

```yaml
# ============================================================
# 文件: plugins/Oraxen/hud.yml
# ============================================================

# update_time_in_ticks: HUD 刷新间隔（游戏刻）
# 20 刻 = 1 秒
# 设为 0 表示完全禁用自定义 HUD 系统
# 设为 0 时，huds 下面的所有元素都不会显示
update_time_in_ticks: 0         # 当前项目中 HUD 被禁用

# 经验值: 40 刻（每 2 秒）刷新适合余额等变化较慢的数据
# 10 刻（每 0.5 秒）适合生命值/魔力值等需实时更新的数据

huds:                           # HUD 元素定义区域
  # 在此处添加 HUD 元素配置
```

---

## 二、余额显示 HUD — 单元素完整示例

基于项目配置的扩展和注释版：

```yaml
# ============================================================
# 文件: plugins/Oraxen/hud.yml
# ============================================================

update_time_in_ticks: 40        # 每 2 秒刷新一次（经济数据不需要太快的刷新率）

huds:
  # --- 余额显示 HUD ---
  balance:                                          # 【必填】HUD ID，全局唯一标识符
                                                    #         用于 /oraxen hud toggle balance 命令
    permission: "oraxen.hud.balance"                # 【可选】查看此 HUD 需要的权限节点
                                                    #         不设置则所有玩家可见
                                                    #         建议对经济类 HUD 设置权限以控制可见性
    display_text: >-                                # 【必填】操作栏上显示的文本内容
      <shift:100>                                   #         水平位移 100 像素（向右）
                                                    #         HUD 位移使用空白字符偏移实现
      <font:balance_hud>                            #         切换到自定义 HUD 字体
                                                    #         自定义字体控制文字在操作栏中的垂直位置
      %vault_eco_balance%                           #         PlaceholderAPI 占位符 — 玩家余额
                                                    #         需要安装 Vault + 经济插件
      <font:default>                                #         切换回默认字体
      <glyph:coin>                                  #         显示金币图标字形
                                                    #         字形使用方式与聊天中相同
    disabled_whilst_in_water: true                  # 【可选】在水下时隐藏 HUD
                                                    #         设为 true 可避免 HUD 遮挡氧气条
                                                    #         默认: false
    enabled_by_default: true                        # 【可选】玩家首次加入时默认启用
                                                    #         true = 新玩家自动看到此 HUD
                                                    #         默认: false（需要手动 /oraxen hud toggle）
    enable_for_spectator_mode: false                # 【可选】观察者模式下是否显示
                                                    #         默认: false（观察者通常不需要看 HUD）
```

### 配置项完整说明

| 配置项 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `permission` | 字符串 | 否 | 无 | 玩家需要的权限节点。无权限者完全看不见此 HUD |
| `display_text` | 字符串 | **是** | — | 在操作栏上显示的文本。支持 MiniMessage、PAPI 占位符、字形标签 |
| `disabled_whilst_in_water` | 布尔 | 否 | `false` | 在水中时隐藏（防止与氧气条竞争操作栏显示） |
| `enabled_by_default` | 布尔 | 否 | `false` | 新玩家是否默认启用。已有玩家的开关状态保存在 playerdata 中 |
| `enable_for_spectator_mode` | 布尔 | 否 | `false` | 观察者模式下是否显示 |

---

## 三、display_text 中的多标签组合详解

```
display_text 解析为: "<shift:100><font:balance_hud>%vault_eco_balance%<font:default><glyph:coin>"

逐标签分解:

<shift:100>
  └─ 向右移动 100 像素。正值右移，负值左移。
     典型值: -150（屏幕左） ~ 0（中央） ~ 150（屏幕右）

<font:balance_hud>
  └─ 切换到名为 "balance_hud" 的自定义字体。
     此字体需要在 fonts.yml 或资源包中预先定义。
     字体的 ascent 值控制 HUD 文本的垂直位置。

%vault_eco_balance%
  └─ PlaceholderAPI 占位符，实时显示玩家金币数量。
     例如显示: "1234.56"

<font:default>
  └─ 切换回 Minecraft 默认字体。
     重要: 使用自定义字体后务必切换回 default，
     否则后续文本和字形的渲染位置会受影响。

<glyph:coin>
  └─ 显示金币图标字形（需在 glyphs/ 中预先定义）。
     使用 :c 后缀可让字形继承 <font:default> 的颜色。
```

---

## 四、HUD 的 Shift 位移系统说明

```
HUD 中的 <shift:N> 与聊天/GUI 中的 <shift:N> 的区别:

聊天/GUI 中的 shift:
  - 使用 Oraxen 内建的空格字体提供器实现
  - 基于资源包中的 ascii_offset 字体
  - 精度: 1 像素精度

HUD 中的 shift:
  - 使用操作栏的空白字符偏移实现
  - 基于 Minecraft 操作栏自身的字符间距
  - 精度: 同样是 1 像素精度

两者使用相同的 MiniMessage 语法: <shift:N>

屏幕水平位置参考:
  <shift:-170>      ┌─────────────┐
    (最左)          │             │
  <shift:-80>   左  │  HUD 文字   │  右  <shift:80>
                    │  [金币100]  │
  <shift:0>     中  │             │     <shift:170>
                    └─────────────┘        (最右)

经验值:
  -160 ~ -120      屏幕左侧边缘区域
   -80 ~  -40      屏幕左侧内容区
   -20 ~   20      屏幕中央区域
    40 ~   80      屏幕右侧内容区
   120 ~  160      屏幕右侧边缘区域
```

---

## 五、HUD 中使用的自定义字体

### 5.1 字体在 HUD 中的作用

```
自定义字体通过控制文本的 ascent（垂直偏移）来实现文本在操作栏中的精确定位。

操作栏的默认布局中，文本位于屏幕底部偏上的固定位置。
通过自定义字体，你可以:
  - 让文本在操作栏中更高/更低
  - 创建一个统一的 HUD 显示层
  - 隔离字形渲染（避免字形与聊天文本冲突）
```

### 5.2 fonts.yml 中定义 HUD 字体

```yaml
# ============================================================
# 文件: plugins/Oraxen/fonts.yml
# HUD 相关的字体配置
# ============================================================

# 方式一: 使用 TTF 字体（1.21.4+）
# ⚠️ docs（Glyphs.md）仅记载 fonts.yml 的 bitmaps 段；以下 TTF 字体段为 Minecraft 1.21.4+ 原生功能，Oraxen 应支持但 docs 未详述，使用前请按实际版本验证。
fonts:
  balance_hud:                          # 字体 ID（在 display_text 中引用）
    type: "ttf"                         # TrueType 字体类型
    file: "minecraft:PPP.ttf"           # TTF 字体文件路径
                                        # 相对于资源包 assets/ 目录
    shift_x: 0.0                        # 水平平移（像素）
    shift_y: 1.6                        # 垂直平移（像素），
                                        # 正数 = 下移，负数 = 上移
    size: 8.0                           # 字体大小（像素）
    oversample: 10.0                    # 采样精度（越高质量越好但生成越慢）

  # 更多 HUD 字体示例
  mana_hud:
    type: "ttf"
    file: "minecraft:PPP.ttf"           # 可以复用同一字体文件
    shift_x: 0.0
    shift_y: 2.0                        # 不同垂直位置
    size: 9.0                           # 更大的字号

# 方式二: 使用位图字体 — 通过 JSON 字体提供器
# 位图字体需要你在资源包中手动创建 JSON 文件:
# assets/<namespace>/font/<font_name>.json
```

### 5.3 HUD 字体 JSON 示例

```json
// ============================================================
// 文件: assets/minecraft/font/balance_hud.json
// （此文件由 Oraxen 或资源包创建）
// ============================================================
{
  "providers": [
    {
      "type": "bitmap",
      "file": "minecraft:required/ascii_offset.png",
      "ascent": -13,                    // 负值 = 文本上移
                                        // 更负的 ascent 使文本在操作栏中更高
      "height": 8,                      // 字符高度
      "chars": [
        "                ",
        "                ",
        " !\"#$%&'()*+,-./",
        "0123456789:;<=>?",
        "@ABCDEFGHIJKLMNO",
        "PQRSTUVWXYZ[\\]^_",
        "`abcdefghijklmno",
        "pqrstuvwxyz{|}~ ",
        "                "
      ]
    }
  ]
}
```

---

## 六、在 HUD 中使用字形

```yaml
# 两种方式在 HUD 的 display_text 中嵌入字形:

# 方式一: 使用 MiniMessage 字形标签（推荐，清晰直观）
display_text: "<shift:100>金币: %vault_eco_balance% <glyph:coin:c>"

# 方式二: 使用 PlaceholderAPI 字形占位符（兼容旧版）
display_text: "<shift:100>金币: %vault_eco_balance% %oraxen_coin%"

# :c 后缀 = colorable（可着色）
# 让字形继承所在文本的颜色，适用于 HUD 中保持一致的颜色风格

# 组合使用多种字形
display_text: "<shift:-150><glyph:health_icon:c> %player_health% <shift:200><glyph:coin:c> %vault_eco_balance%"
```

---

## 七、完整 HUD 示例：血条与魔力条双显示

基于项目配置的扩展实战示例：

```yaml
# ============================================================
# 文件: plugins/Oraxen/hud.yml
# 完整双 HUD 示例 — 血条（左） + 魔力条（右）
# ============================================================

update_time_in_ticks: 10             # 每 0.5 秒刷新（生命值需快速更新）

huds:
  # --- 自定义生命值显示（左侧）---
  health_display:
    enabled_by_default: true         # 新玩家默认可见
    enable_for_spectator_mode: false # 观察者不显示
    disabled_whilst_in_water: false  # 水下不隐藏（血量信息很重要）
    # 不需要 permission — 所有玩家可见
    display_text: >-
      <shift:-160>
      <font:health_hud>
      <red>❤ %player_health_rounded% / %player_max_health_rounded%</red>
      <font:default>

  # --- 自定义魔力值显示（右侧）---
  mana_display:
    permission: "oraxen.hud.mana"    # 只有拥有魔力系统的玩家才看到
    enabled_by_default: true
    enable_for_spectator_mode: false
    disabled_whilst_in_water: false
    display_text: >-
      <shift:160>
      <font:mana_hud>
      <blue>✦ %oraxen_mana% / %oraxen_max_mana%</blue>
      <font:default>

  # --- 金币显示（右下角）---
  coin_display:
    permission: "oraxen.hud.coin"
    enabled_by_default: true
    display_text: >-
      <shift:170>
      <font:coin_hud>
      <gold>%vault_eco_balance%</gold> <glyph:coin:c>
      <font:default>

  # --- 坐标显示（左上角）---
  coord_display:
    enabled_by_default: true
    display_text: >-
      <shift:-170>
      <font:coord_hud>
      <gray>XYZ: %player_x% %player_y% %player_z%</gray>
      <font:default>
```

---

## 八、使用字形进度条的高级 HUD

结合字形系统创建视觉化的进度条 HUD：

```yaml
# ============================================================
# 文件: plugins/Oraxen/hud.yml
# 进度条式 HUD 的两种实现方式
# ============================================================

update_time_in_ticks: 20             # 每秒更新

huds:
  # --- 方式一: 使用 PlaceholderAPI 数值 + 字形图标 ---
  health_bar_icon:
    enabled_by_default: true
    display_text: >-
      <shift:-100>
      <font:hud_font>
      <glyph:heart_full:c> <red>%player_health_rounded%</red> / <dark_red>%player_max_health_rounded%</dark_red>
      <font:default>

  # --- 方式二: 使用自定义进度条字形（需预先创建 bar_full / bar_empty 字形）---
  # 注意: 这种方式需要 PlaceholderAPI 扩展支持条件判断，
  #       或配合 JavaScript 占位符使用
  health_bar_visual:
    enabled_by_default: true
    display_text: >-
      <shift:-80>
      <font:hud_font>
      %oraxen_health_bar%              # 自定义占位符，动态返回条形字符串
      <font:default>
      %player_health% / %player_max_health%

  # --- 使用 CustomCrops 风格的进度条字形 ---
  # 参考 Oraxen/glyphs/customcrops/images.yml 中的 bars_* 字形
  crops_growth_bar:
    permission: "oraxen.hud.crops"
    enabled_by_default: false
    display_text: >-
      <shift:0>
      <font:customcrops>
      <glyph:bars_left>               # 进度条左端
      <glyph:bars_full>               # 实心段
      <glyph:bars_empty>              # 空心段
      <glyph:bars_right>              # 进度条右端
      <font:default>
```

---

## 九、HUD 命令参考

```
HUD 玩家命令:
  /oraxen hud toggle <hud_id>     切换指定 HUD 的显示/隐藏状态
  /oraxen hud toggle balance      示例: 切换余额 HUD
  /oraxen hud toggle mana         示例: 切换魔力 HUD

HUD 权限:
  oraxen.hud.<hud_id>            查看某个 HUD 的权限
  oraxen.command.hud             使用 /oraxen hud 命令的权限

HUD 管理员命令:
  /oraxen reload all             完全重载 Oraxen（包括 HUD；docs 仅记载 all/items/pack/recipes 子命令，无独立 reload hud）
  /oraxen reload all             完全重载 Oraxen（包括 HUD）

注意事项:
  - HUD toggle 的开关状态保存在玩家的 playerdata 中
  - 首次加入的玩家根据 enabled_by_default 决定初始状态
  - update_time_in_ticks: 0 时所有 HUD 不可见，/oraxen hud toggle 无效果
```

---

## 十、HUD 最佳实践

```
设计原则:

1. 刷新频率选择
   - 经济数据（余额/积分）:  40~80 刻（2~4 秒），降低服务器负担
   - 生命值/魔力值:         10~20 刻（0.5~1 秒），实时反馈
   - 坐标/朝向:             20~40 刻（1~2 秒）
   - 静态信息:              100~200 刻（5~10 秒），如在线人数

2. 字体管理
   - 为每种 HUD 创建独立字体（便于独立调整垂直位置）
   - 在 display_text 末尾务必 <font:default> 恢复默认字体
   - 字体文件名使用小写 + 下划线（如 health_hud, mana_hud）

3. 性能注意事项
   - HUD 在客户端操作栏中渲染，对服务器性能影响极小
   - 但 PAPI 占位符的解析在服务端进行，复杂占位符可能带来开销
   - 避免在 HUD 中使用大量嵌套占位符

4. 兼容性
   - 任何使用操作栏的插件（BossBar 插件、技能提示等）都可能与 HUD 冲突
   - 测试环境中先禁用其他可能使用操作栏的插件
   - 考虑使用 BossBar 替代操作栏（某些场景下更不易冲突）

5. 用户体验
   - 不要同时启用超过 3-4 个 HUD 元素（操作栏只有一行）
   - 左右对称布局（如血量在左，魔力在右）
   - 给每个 HUD 设置明确的位置，避免重叠
   - 在水中/骑乘时隐藏非必要 HUD（减少视觉干扰）
```

---

## 十一、常见问题排查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| HUD 完全不显示 | update_time_in_ticks 为 0 | 将值设为正数（如 20） |
| 特定 HUD 不显示 | 玩家无权限 | 检查 permission 配置，确保玩家有对应权限 |
| HUD 文字位置不对 | shift 值不合适 or 字体未定义 | 调整 shift 值，检查字体 JSON 文件是否存在 |
| 字形在 HUD 中不显示 | 字形未加载 or 字体不匹配 | 确认字形已定义，使用 `<font:default>` 切换回默认字体 |
| HUD 闪烁/跳动 | 刷新频率过高 or 与其他插件冲突 | 降低 update_time_in_ticks 的值（增大间隔） |
| PAPI 占位符不解析 | 对应扩展未安装 | 安装需要的 PAPI 扩展（如 Vault、Player 等） |
| HUD 在水下消失 | disabled_whilst_in_water 为 true | 改为 false 或确认这是你想要的行为 |
| HUD 与其他操作栏消息冲突 | 操作栏只能同时显示一条消息 | 使用 BossBar 替代，或协调其他插件不使用操作栏 |
| 新玩家看不到 HUD | enabled_by_default 为 false | 设为 true，或让玩家手动 `/oraxen hud toggle` |
