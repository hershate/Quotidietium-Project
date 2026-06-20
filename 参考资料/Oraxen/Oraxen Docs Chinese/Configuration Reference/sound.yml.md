---
description: sound.yml 自定义音效配置完整指南
---

# sound.yml 配置

了解如何在 Oraxen 中注册自定义音效、配置唱片机歌曲以及替换原版音效。

## 概述

`sound.yml` 文件允许您：
- 注册自定义音效文件（.ogg 格式）
- 配置带有元数据的唱片机歌曲
- 替换原版 Minecraft 音效
- 定义音效类别和字幕
- 添加自定义方块破坏/放置音效

**位置:** `plugins/Oraxen/sound.yml`

## 文件结构

```yaml
settings:
  automatically_generate: true  # 自动为资源包生成 sounds.json

sounds:
  sound_id:
    category: records           # 音效类别
    sound: filename.ogg         # 音效文件（扩展名可选）
    stream: true                # 是否流式播放（推荐用于音乐）
    subtitle: "字幕文本"         # 游戏中显示的字幕
    replace: false              # 是否替换原版音效
    jukebox_song:               # （可选）唱片机歌曲元数据
      description: "歌曲描述"
      length_in_seconds: 120
      comparator_output: 15
```

## 基础音效注册

### 添加自定义音效

1. **将您的 .ogg 文件** 放入 `plugins/Oraxen/pack/sounds/`（如需可创建子目录）

2. **在 sound.yml 中注册：**

```yaml
sounds:
  my_custom_sound:
    category: block
    sound: custom/my_sound.ogg
    subtitle: "自定义音效"
```

3. **重载 Oraxen：** `/oraxen reload all`

4. **在游戏中使用：** 通过 `/playsound oraxen:my_custom_sound` 播放

### 音效类别

有效的类别：
- `master` - 主音量滑块
- `music` - 音乐和唱片机音量
- `record` - music 的别名（用于唱片机歌曲）
- `weather` - 天气音效
- `block` - 方块破坏/放置音效
- `hostile` - 敌对生物音效
- `neutral` - 中立生物音效
- `player` - 玩家音效（脚步声、受伤等）
- `ambient` - 环境音效
- `voice` - 语音/说话音效

## 唱片机歌曲

创建在唱片机中播放自定义歌曲的音乐唱片。

### 配置

```yaml
sounds:
  welcome:
    category: records
    sound: welcome.ogg
    stream: true  # 音乐始终使用流式播放
    subtitle: "欢迎曲"
    jukebox_song:
      description:
        - text: "Oraxen - 欢迎"
          color: "gray"
          italic: false
      length_in_seconds: 180
      comparator_output: 15
```

### 唱片机歌曲属性

**`description`** - 物品提示中显示的歌曲标题：
```yaml
jukebox_song:
  description:
    - text: "艺术家 - 歌曲名称"
      color: "aqua"
      italic: true
    - text: "专辑名称"
      color: "gray"
```

**`length_in_seconds`** - 歌曲持续时间（用于停止播放）

**`comparator_output`** - 播放时的红石比较器信号强度（1-15）

### 创建音乐唱片物品

在您的物品配置中（例如，`items/items.yml`）：

```yaml
welcome_disk:
  displayname: "<gradient:#9055FF:#13E2DA>Welcome Disk"
  material: MUSIC_DISC_13  # 或任何音乐唱片材料
  ItemFlags:
    - HIDE_ADDITIONAL_TOOLTIP
  Components:
    jukebox_playable:
      show_in_tooltip: true
      song_key: "oraxen:welcome"  # 必须与音效 ID 匹配
  Pack:
    generate_model: true
    parent_model: "item/handheld"
    textures:
      - default/welcome_disk.png
```

## 替换原版音效

用自定义音效覆盖 Minecraft 的默认音效。

### 示例：自定义方块破坏音效

```yaml
sounds:
  custom_stone_break:
    category: block
    sound: blocks/custom_stone.ogg
    replace: true
    subtitle: "方块被破坏"
```

要将其应用于自定义方块，请在方块的配置中引用它。

### 常见的原版音效替换

```yaml
sounds:
  # 自定义木头音效
  wood_break:
    category: block
    sound: blocks/wood/break.ogg
    replace: true
    subtitle: "方块被破坏"

  wood_step:
    category: block
    sound: blocks/wood/step.ogg
    replace: true

  wood_place:
    category: block
    sound: blocks/wood/place.ogg
    replace: true
    subtitle: "方块被放置"

  # 自定义石头音效
  stone_break:
    category: block
    sound: blocks/stone/break.ogg
    replace: true
    subtitle: "方块被破坏"

  stone_step:
    category: block
    sound: blocks/stone/step.ogg
    replace: true
```

## 方块音效集成

### 将音效应用于自定义方块

在您的方块配置中：

```yaml
my_custom_block:
  # ... 其他方块属性 ...
  sounds:
    break: oraxen:custom_stone_break
    place: oraxen:wood_place
    step: oraxen:wood_step
    hit: oraxen:custom_stone_break
    fall: oraxen:wood_step
```

### 必需音效模式

对于应使用原版音效组（木材、石头等）的方块：

```yaml
sounds:
  required.wood.break:
    category: block
    sound: block/wood/break.ogg
    replace: true

  required.wood.step:
    category: block
    sound: block/wood/step.ogg
    replace: true

  required.wood.place:
    category: block
    sound: block/wood/place.ogg
    replace: true
```

`required.` 前缀告诉 Oraxen 这些是必需的音效映射。

## 流式播放与非流式播放

### 何时使用流式播放

**使用 `stream: true` 的场景：**
- 音乐唱片（唱片机歌曲）
- 长环境音效（超过10秒）
- 背景音乐
- 旁白/对话

**使用 `stream: false`（或省略）的场景：**
- 短音效（少于5秒）
- 方块破坏/放置音效
- UI 音效
- 频繁播放的音效

### 为什么重要

- **非流式：** 将整个音效加载到内存中（播放速度快，内存使用更高）
- **流式：** 分块加载音效（内存更低，播放开始时略有延迟）

## 音效文件要求

### 格式要求

- **格式：** OGG Vorbis（`.ogg`）
- **声道：** 单声道（立体声会自动转换但浪费空间）
- **采样率：** 推荐 44.1kHz 或 48kHz
- **比特率：** 音乐使用 128-192 kbps，音效使用 64-96 kbps

### 文件放置

将音效文件放入 `plugins/Oraxen/pack/sounds/`：

```
pack/
└── sounds/
    ├── music/
    │   ├── welcome.ogg
    │   └── boss_theme.ogg
    ├── blocks/
    │   ├── wood/
    │   │   ├── break.ogg
    │   │   ├── step.ogg
    │   │   └── place.ogg
    │   └── stone/
    │       └── break.ogg
    └── custom/
        └── my_sound.ogg
```

### 转换音频文件

使用 FFmpeg 将音频转换为 OGG：

```bash
# 将 MP3 转换为 OGG（单声道，128kbps）
ffmpeg -i input.mp3 -ac 1 -b:a 128k output.ogg

# 将 WAV 转换为 OGG（单声道，96kbps 用于音效）
ffmpeg -i input.wav -ac 1 -b:a 96k output.ogg
```

## 完整示例

以下是包含各种音效类型的完整 sound.yml：

```yaml
settings:
  automatically_generate: true

sounds:
  # 音乐唱片
  epic_theme:
    category: records
    sound: music/epic_theme.ogg
    stream: true
    subtitle: "史诗主题曲播放中"
    jukebox_song:
      description:
        - text: "Epic Theme"
          color: "gold"
          italic: false
        - text: "By Composer Name"
          color: "gray"
      length_in_seconds: 240
      comparator_output: 15

  # 方块音效
  crystal_break:
    category: block
    sound: blocks/crystal/break.ogg
    subtitle: "水晶碎裂"

  crystal_step:
    category: block
    sound: blocks/crystal/step.ogg

  # 环境音效
  magical_hum:
    category: ambient
    sound: ambient/magical_hum.ogg
    stream: true
    subtitle: "魔法嗡鸣"

  # UI 音效
  menu_click:
    category: master
    sound: ui/menu_click.ogg

  # 武器音效
  sword_swing:
    category: player
    sound: weapons/sword_swing.ogg
    subtitle: "嗖"
```

## 在物品中使用音效

### 在物品使用时播放音效

在物品配置中：

```yaml
magic_wand:
  # ... 物品属性 ...
  Mechanics:
    custom:
      one_usage:
        event: CLICK:right:all
        actions:
          sound:
            name: oraxen:magical_hum
            volume: 1.0
            pitch: 1.0
```

### 在方块破坏时播放音效

```yaml
my_custom_block:
  # ... 方块属性 ...
  break_sounds:
    - oraxen:crystal_break
```

## 故障排除

### 音效不播放

1. **检查文件格式：** 必须是 `.ogg`（OGG Vorbis）
2. **验证文件路径：** 检查 `plugins/Oraxen/pack/sounds/<path>`
3. **重载 Oraxen：** `/oraxen reload all`
4. **重新发送资源包：** `/oraxen pack send @a`
5. **检查客户端日志：** 按 F3 + T 重新加载资源包

### 音效播放但没有字幕

确保定义了字幕并且游戏中启用了字幕（选项 > 辅助功能 > 字幕）

### 唱片机歌曲不播放

1. 验证 `song_key` 与音效 ID 匹配：`oraxen:<sound_id>`
2. 确保设置了 `stream: true`
3. 检查 `length_in_seconds` 是否准确
4. 确认物品具有 `jukebox_playable` 组件

### 音效文件太大

**对于音乐：**
- 降低比特率：128kbps 通常足够
- 将立体声转换为单声道（文件大小减半）
- 使用流式播放（`stream: true`）

**对于音效：**
- 短音效使用 64-96kbps
- 确保单声道
- 裁剪开头/结尾的静音

### 音效播放音量不正确

调整游戏中的音量滑块：
- 检查音效的 `category` 是否匹配预期的滑块
- `master` - 主音量
- `music` - 音乐/唱片机音量
- `block` - 方块音量
- `ambient` - 环境音量

## 高级：音效事件

### 自定义音效事件

您可以通过插件事件触发音效：

```yaml
Mechanics:
  custom:
    on_kill:
      event: KILL:player
      actions:
        sound:
          name: oraxen:victory_fanfare
          volume: 0.8
          pitch: 1.2
```

### 多个音效

从音效池中随机播放：

```yaml
sounds:
  footstep_1:
    category: player
    sound: footsteps/step1.ogg

  footstep_2:
    category: player
    sound: footsteps/step2.ogg

  footstep_3:
    category: player
    sound: footsteps/step3.ogg
```

然后在机制中或通过插件代码随机引用。

## 另请参阅

- [物品能力](../creating-content/items/abilities/) - 在物品机制中使用音效
- [自定义方块](../creating-content/blocks/) - 向方块添加音效
- [品牌自定义](./branding-customization) - 自定义欢迎音效
- [MiniMessage 格式](https://docs.advntr.dev/minimessage/) - 唱片机歌曲描述格式化