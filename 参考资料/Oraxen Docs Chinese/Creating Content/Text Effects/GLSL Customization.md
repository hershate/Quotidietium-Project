# GLSL 自定义

import { Callout, Tabs } from 'nextra/components'
import ShaderPreview from '../../../components/ShaderPreview'

Oraxen 文字特效系统最强大的功能之一是能够使用 GLSL（OpenGL 着色语言）自定义或创建新的特效。`text_effects.yml` 文件包含定义每个特效如何工作的 GLSL 代码片段。

## 交互式着色器预览

直接在浏览器中试用文字特效！选择一个模板开始，然后修改 GLSL 代码以创建你自己的特效。预览使用 Minecraft 字体，并模拟特效在游戏中的显示效果。

<ShaderPreview />

## GLSL 片段结构

每个特效在 GLSL 片段中定义其完整的视觉行为。所有参数（速度、振幅、颜色）都硬编码在片段中——不需要运行时变量：

```yaml filename="text_effects.yml"
effects:
  my_effect:
    # id: 0                        # 可选 - 省略时自动分配
    enabled: true
    # trigger_color: "#FD0D00"     # 可选 - 默认为 #FDxD00
    description: 我的自定义特效
    snippets:
      - targets:                   # 可选：版本约束
          min_pack_format: 34
          min_version: "1.21.4"
        vertex: |
          // 顶点着色器代码（位置特效）
          pos.y += sin(timeSeconds * 6.0) * 2.0;
        fragment: |
          // 片段着色器代码（颜色特效）
          texColor.rgb = vec3(1.0, 0.0, 0.0);
```

## 可用变量

这些变量在你的 GLSL 片段中可用：

| 变量 | 类型 | 描述 |
|----------|------|-------------|
| `timeSeconds` | `float` | 游戏时间（以秒为单位，用于动画） |
| `charIndex` | `float` | 字符串中的字符索引（来自 `gl_VertexID`） |
| `pos` | `vec3` | 顶点位置（仅顶点着色器） |
| `texColor` | `vec4` | 纹理颜色 RGBA（仅片段着色器） |

<Callout type="info">
与之前的版本不同，`speed` 和 `param` 变量不再可用。所有特效参数应直接硬编码在你的 GLSL 片段中，以简化并避免误触发。
</Callout>

## 共享代码

`shared` 部分定义可重用的 GLSL 函数，所有特效均可使用：

```yaml filename="text_effects.yml"
shared:
  fragment_prelude: |
    // HSV 到 RGB 转换 - 对颜色特效有用
    vec3 hsv2rgb(vec3 c) {
        vec4 K = vec4(1.0, 2.0/3.0, 1.0/3.0, 3.0);
        vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
        return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }

  vertex_prelude: |
    // 在此添加任何顶点着色器辅助函数
```

## 内置特效示例

这些是 `text_effects.yml` 中的默认特效：

<Tabs items={['彩虹', '波浪', '抖动', '脉冲']}>
<Tabs.Tab>
**彩虹特效** - 随时间循环色相颜色

```glsl
// 片段着色器
float hue = fract(charIndex * 0.03 + timeSeconds * 0.09);
texColor.rgb = hsv2rgb(vec3(hue, 0.9, 1.0));
```

**工作原理：**
- 使用 `charIndex` 为每个字符偏移色相以创建渐变效果
- `timeSeconds * 0.09` 使颜色循环动画化
- `hsv2rgb()` 将色相值转换为 RGB 颜色
- 饱和度为 0.9，亮度为 1.0

</Tabs.Tab>
<Tabs.Tab>
**波浪特效** - 垂直正弦波运动

```glsl
// 片段着色器 - 设置波浪颜色
texColor.rgb = vec3(0.333, 0.804, 0.988);

// 顶点着色器 - 应用波浪运动
float phase = charIndex * 0.6 + timeSeconds * 6.0;
pos.y += sin(phase) * 2.0;
```

**工作原理：**
- 每个字符根据其索引有相位偏移
- `sin(phase)` 创建波浪运动
- 振幅（`2.0`）和速度（`6.0`）是硬编码的
- 颜色设置为浅蓝色

</Tabs.Tab>
<Tabs.Tab>
**抖动特效** - 随机抖动

```glsl
// 片段着色器 - 设置抖动颜色
texColor.rgb = vec3(1.0, 0.42, 0.42);

// 顶点着色器 - 应用随机抖动
float seed = charIndex + floor(timeSeconds * 32.0);
pos.x += (fract(sin(seed * 12.9898) * 43758.5453) - 0.5) * 1.5;
pos.y += (fract(sin(seed * 78.233) * 43758.5453) - 0.5) * 1.5;
```

**工作原理：**
- 使用基于 `sin()` 的伪随机数生成器
- `floor(timeSeconds * 32.0)` 创建离散的抖动"帧"
- 随机偏移应用于 X 和 Y 位置
- 强度（`1.5`）是硬编码的

</Tabs.Tab>
<Tabs.Tab>
**脉冲特效** - 不透明度淡入淡出

```glsl
// 片段着色器
texColor.rgb = vec3(1.0, 0.85, 0.24);
float pulse = (sin(timeSeconds * 1.5 + charIndex * 0.3) + 1.0) * 0.5;
texColor.a *= 0.3 + pulse * 0.7;
```

**工作原理：**
- 使用 `sin()` 在 0 和 1 之间振荡
- 添加 `charIndex * 0.3` 以偏移每个字符的相位
- 乘以 alpha 通道以淡出透明度
- 最低不透明度为 0.3（30%），颜色是金色

</Tabs.Tab>
</Tabs>

## 创建自定义特效

要创建你自己的特效：

1. 将你的特效添加到 `text_effects.yml`（ID 自动分配，或显式指定一个）：

```yaml filename="text_effects.yml"
effects:
  # 自定义：发光文字，脉冲明暗变化
  glow:
    enabled: true
    description: 发光亮度脉冲
    snippets:
      - fragment: |
          float glow = (sin(timeSeconds * 3.0) + 1.0) * 0.5;
          float brightness = 0.7 + glow * 0.6;  // 0.7 到 1.3
          texColor.rgb = vec3(0.9, 0.7, 0.2) * brightness;
```

2. 使用 `/oraxen reload all` 重新加载 Oraxen
3. 使用 `/oraxen texteffect glow 你的发光文字！` 测试
4. 或者在 MiniMessage 中使用：`<effect:glow>发光！</effect>`

## GLSL 参考

### 常用函数

```glsl
sin(x), cos(x)       // 平滑振荡 (-1 到 1)
fract(x)             // 小数部分 (0 到 1)
floor(x)             // 向下取整（用于离散步进）
step(edge, x)        // 如果 x < edge 则为 0.0，否则为 1.0（二元阈值）
clamp(x, min, max)   // 将值限制在范围内
mix(a, b, t)         // 线性插值
mod(x, y)            // 取余（用于循环）
abs(x)               // 绝对值
max(a, b), min(a, b) // 两个值中的最大值/最小值
pow(x, y)            // 幂函数
sqrt(x)              // 平方根
length(vec)          // 向量长度
normalize(vec)       // 单位向量
dot(a, b)            // 点积
```

### 实用模式

```glsl
// 0 到 1 之间的平滑振荡
float wave = (sin(timeSeconds * 2.0) + 1.0) * 0.5;

// 离散步进（用于类似帧的动画）
float frame = floor(timeSeconds * 10.0);  // 10 FPS

// 每个字符的相位偏移
float phase = charIndex * 0.5 + timeSeconds * 3.0;

// 基于种子的伪随机
float rand = fract(sin(seed * 12.9898) * 43758.5453);

// 平滑步进（缓入/缓出）
float t = smoothstep(0.0, 1.0, x);

// 乒乓（振荡 0 到 1 到 0）
float pingpong = abs(mod(timeSeconds, 2.0) - 1.0);

// 从灰度值创建颜色
vec3 color = vec3(grayscale);

// 变暗颜色
texColor.rgb *= 0.5;

// 变亮颜色（可能超过 1.0）
texColor.rgb *= 1.5;

// 反转颜色
texColor.rgb = 1.0 - texColor.rgb;

// 去饱和（转换为灰度）
float gray = dot(texColor.rgb, vec3(0.299, 0.587, 0.114));
texColor.rgb = vec3(gray);
```

### 自定义特效创意

以下是一些你可以创建的自定义特效创意：

**呼吸特效** - 缓慢缩放脉冲
```glsl
// 顶点着色器
float breath = (sin(timeSeconds * 1.5) + 1.0) * 0.1 + 0.9;
pos *= breath;
```

**颜色偏移** - 循环变换颜色
```glsl
// 片段着色器
float shift = timeSeconds * 0.5;
texColor.rgb = vec3(
    sin(shift) * 0.5 + 0.5,
    sin(shift + 2.094) * 0.5 + 0.5,
    sin(shift + 4.188) * 0.5 + 0.5
);
```

**故障特效** - 随机颜色/位置跳变
```glsl
// 片段着色器
float glitch = step(0.95, fract(sin(floor(timeSeconds * 20.0) * charIndex) * 43758.5453));
texColor.rgb = mix(texColor.rgb, 1.0 - texColor.rgb, glitch);
```

**淡入** - 字符从透明淡入
```glsl
// 片段着色器
float fadeTime = 2.0;  // 完全显示所需的秒数
float progress = clamp(timeSeconds / fadeTime, 0.0, 1.0);
float alpha = smoothstep(charIndex / 20.0, charIndex / 20.0 + 0.1, progress);
texColor.a *= alpha;
```

## 版本特定的代码片段

你可以为不同的 Minecraft 版本定义不同的 GLSL 代码：

```yaml filename="text_effects.yml"
effects:
  custom:
    enabled: true
    snippets:
      # 适用于 1.21.6+ 的片段
      - targets:
          min_version: "1.21.6"
        fragment: |
          // 现代着色器代码
          texColor.rgb = vec3(1.0, 0.5, 0.0);

      # 旧版本的回退
      - targets:
          max_version: "1.21.5"
        fragment: |
          // 旧版着色器代码
          texColor.rgb = vec3(0.8, 0.4, 0.0);
```

使用第一个匹配的片段（基于 `targets`）。没有 targets 的片段始终匹配。

### 目标选项

| 选项 | 描述 |
|--------|-------------|
| `min_pack_format` | 最低资源包格式 |
| `max_pack_format` | 最高资源包格式 |
| `min_version` | 最低 Minecraft 版本（例如 "1.21.4"） |
| `max_version` | 最高 Minecraft 版本（例如 "1.21.5"） |

## 调试技巧

<Callout type="info">
开发自定义特效时，你可以通过在编辑 `text_effects.yml` 后使用 `/oraxen reload all` 来快速测试更改。
</Callout>

**常见问题：**

1. **特效未显示**：检查特效名称是否与你在标签中使用的名称一致
2. **语法错误**：GLSL 很严格——确保分号和正确的类型
3. **什么都看不见**：检查 `texColor.a` 是否被设置为 0
4. **闪烁**：使用 `floor()` 进行离散动画，不要使用连续值
5. **特效未触发**：确保在配置中启用了特效

**本地测试你的 GLSL：**
使用本页顶部的[交互式着色器预览](#interactive-shader-preview)在添加到 Oraxen 之前对特效进行原型设计。它使用相同的 Minecraft 字体并模拟着色器环境。