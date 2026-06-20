# 文字特效

import { Callout } from 'nextra/components'

文字特效是基于着色器的视觉效果，可以应用于 Minecraft 中的任何文本。与在精灵帧之间切换的动画字形不同，文字特效使用 GLSL 着色器修改现有字符的渲染方式（颜色、位置、不透明度）。

<Callout type="info">
文字特效需要 Minecraft 1.21.4+ 以及启用着色器的 Oraxen 资源包。
</Callout>

## 快速开始

使用 MiniMessage 标签应用文字特效：

```
<effect:rainbow>这段文字是彩虹色的！</effect>
<effect:wave>这里是波浪文字</effect>
<effect:shake>抖动文字！</effect>
```

这些标签在 MiniMessage 支持的任何地方都可以使用——物品名称、描述、聊天、告示牌等。

## 配置

文字特效在两个文件中配置：
- **`settings.yml`** - 总开关和着色器设置
- **`text_effects.yml`** - 特效定义和 GLSL 代码片段

### settings.yml

```yaml filename="settings.yml"
TextEffects:
  enabled: true                    # 所有文字特效的总开关
  shader:
    template: auto                 # auto、effects_only、animated_only
  effects:                         # 可选：按特效覆盖启用状态
    rainbow:
      enabled: true
    wave:
      enabled: false               # 禁用特定特效
```

### text_effects.yml

特效通过直接内嵌在 GLSL 代码片段中的视觉行为来定义：

```yaml filename="text_effects.yml"
version: 1

# 所有特效可用的共享 GLSL 代码
shared:
  fragment_prelude: |
    vec3 hsv2rgb(vec3 c) {
        vec4 K = vec4(1.0, 2.0/3.0, 1.0/3.0, 3.0);
        vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
        return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }

effects:
  rainbow:
    # id: 0                        # 可选 - 省略时自动分配
    enabled: true
    # trigger_color: "#FD0D00"     # 可选 - 默认为 #FDxD00
    description: 随时间循环彩虹颜色
    snippets:
      - fragment: |
          float hue = fract(charIndex * 0.03 + timeSeconds * 0.09);
          texColor.rgb = hsv2rgb(vec3(hue, 0.9, 1.0));
```

### 配置选项

| 选项 | 描述 | 值 |
|--------|-------------|--------|
| `enabled` | 所有文字特效的总开关 | `true` / `false` |
| `shader.template` | 要生成哪些着色器 | `auto`、`effects_only`、`animated_only` |

### 特效选项

| 选项 | 描述 | 默认值 |
|--------|-------------|---------|
| `id` | 数字特效 ID (0-7) | 按顺序自动分配 |
| `enabled` | 此特效是否可用 | `true` |
| `trigger_color` | 着色器匹配的十六进制颜色 | `#FDxD00` (x = id) |
| `description` | 在 `/oraxen texteffects` 中显示 | — |
| `snippets` | 特效的 GLSL 代码 | — |

### 着色器模板

- **`auto`**：同时生成文字特效和动画字形的着色器（推荐）
- **`effects_only`**：仅生成文字特效着色器
- **`animated_only`**：仅生成动画字形着色器

## 内置特效

| 特效 | 描述 |
|--------|-------------|
| `rainbow` | 随时间循环色相颜色 |
| `wave` | 垂直正弦波运动 |
| `shake` | 随机抖动/颤动 |
| `pulse` | 不透明度淡入淡出 |

所有特效参数（速度、振幅、颜色）都在 `text_effects.yml` 中定义，并在资源包生成时内嵌到着色器中。

## 命令

使用以下命令在游戏中测试特效：

```
/oraxen texteffects              # 列出所有可用特效
/oraxen texteffect <effect> <text>   # 对文本应用特效
```

### 示例

```
/oraxen texteffect rainbow Hello World!
/oraxen texteffect wave Wavy Text
/oraxen texteffect shake Very Shaky!
```

<Callout>
需要权限：`oraxen.command.texteffect`
</Callout>

## 工作原理

文字特效使用触发颜色系统来避免渐变颜色的误触发：

1. 每个特效有一个唯一的**触发颜色**（例如彩虹的 `#FD0D00`）
2. 文本使用专用的**特效字体**渲染（例如 `oraxen:effect/0`）
3. 着色器匹配确切的触发颜色并应用特效

这确保了只有有意设置样式的文本才会触发特效——普通的有色文本永远不会受影响。

### 触发颜色

默认触发颜色遵循 `#FDxD00` 模式，其中 `x` 是特效 ID：

| 特效 | ID | 默认触发颜色 |
|--------|----|-----------------------|
| rainbow | 0 | `#FD0D00` |
| wave | 1 | `#FD1D00` |
| shake | 2 | `#FD2D00` |
| pulse | 3 | `#FD3D00` |

如果需要，你可以在 `text_effects.yml` 中自定义触发颜色。

## 兼容性说明

<Callout type="warning">
文字特效可能与其他修改 Minecraft 文本着色器（`rendertype_text.vsh`、`rendertype_text.fsh`）的资源包冲突。如果你使用多个编辑着色器的资源包，请使用资源包合并系统并确保着色器文件被正确合并。
</Callout>

### 已知限制

- 特效通过着色器在客户端渲染
- 带有特效的文本的阴影会被隐藏，以避免视觉伪影
- 8 个特效槽位可用（ID 0-7）
- 着色器中的字符索引来自 `gl_VertexID`

### Minecraft 版本支持

| 版本 | 支持 |
|---------|---------|
| 1.21.4+ | 完全支持 |
| 低于 1.21.4 | 不支持 |