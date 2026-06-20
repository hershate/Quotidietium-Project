---
description: text_effects.yml 配置的完整参考
---

# 文字特效配置参考

配置 `text_effects.yml` 中文字特效的完整指南——适用于 Minecraft 1.21.1+ 的基于着色器的文本动画。

## 概述

文字特效使用 GLSL 着色器在聊天、标题、告示牌和其他文本环境中创建动画文本。特效通过 MiniMessage 格式标签触发。

**位置：** `plugins/Oraxen/text_effects.yml`

**Minecraft 版本：** 1.21.1+（推荐 1.21.11+）

**使用示例：**
```
<effect:rainbow>彩虹文字！</effect>
<effect:wave>波浪文字</effect>
```

---

## 文件结构

```yaml
version: 1  # 文件格式版本

shared:
  fragment_prelude: |
    // 在所有片段着色器的 main() 之前插入的共享 GLSL 代码
    // 在此定义辅助函数（例如 hsv2rgb）

effects:
  effect_name:
    id: 0                    # 特效 ID (0-7) - 省略时自动分配
    enabled: true            # 启用/禁用此特效
    trigger_color: "#FF5500" # 触发此特效的十六进制颜色
    description: "特效描述"  # 在 /oraxen texteffects 中显示
    snippets:
      - fragment: |          # 片段着色器代码（颜色、不透明度）
          // GLSL 代码在此
        vertex: |            # 顶点着色器代码（位置、运动）
          // GLSL 代码在此
```

---

## 特效配置

### 基本属性

#### id
```yaml
rainbow:
  id: 0  # 可选 - 省略时自动分配
```

**类型：** 整数 (0-7)

**自动分配：**
- 如果省略，ID 按文件顺序分配 (0, 1, 2, ...)
- 显式 ID 优先保留，然后自动分配填补空缺
- 你可以混合使用显式和自动 ID

**限制：**
- 最多 8 个特效（ID 0-7）
- 每个 ID 必须唯一

**示例：**
```yaml
effects:
  rainbow:
    id: 0  # 显式
  wave:
    id: 1  # 显式
  shake:
    # 自动分配 ID 2
  custom:
    id: 5  # 显式，跳过 3 和 4
  pulse:
    # 自动分配 ID 3（填补第一个空缺）
```

#### enabled
```yaml
rainbow:
  enabled: true  # 启用此特效
```

**类型：** 布尔值

**为 false 时：**
- 特效在游戏中不可用
- 不分配触发颜色
- `/oraxen texteffects` 不会显示它

**使用场景：** 临时禁用特效而不删除它们。

#### trigger_color
```yaml
rainbow:
  trigger_color: "#FD0D00"  # 触发此特效的十六进制颜色
```

**类型：** 十六进制颜色字符串（例如 "#FF5500"）

**自动生成：**
- 如果省略，默认为 `#FDxD00`，其中 `x` 是特效 ID
- 示例：ID 0 → `#FD0D00`，ID 1 → `#FD1D00`，ID 2 → `#FD2D00`

**工作原理：**
- 当文本恰好具有此颜色时，着色器应用特效
- 使用 24 位精确匹配（极不可能与渐变冲突）
- 基础颜色被特效的颜色逻辑替换

**重要：**
- 不要在普通文本中使用你的触发颜色（它会激活特效）
- 每个特效必须有唯一的触发颜色
- 颜色不需要对人类友好（它是内部使用的）

**自定义颜色：**
```yaml
rainbow:
  trigger_color: "#FF0001"  # 自定义触发器
wave:
  trigger_color: "#00FF01"  # 不同的自定义触发器
```

#### description
```yaml
rainbow:
  description: "随时间循环彩虹颜色"
```

**类型：** 字符串

**用途：**
- 在 `/oraxen texteffects` 命令中显示
- 帮助玩家理解每个特效的作用
- 可选但推荐

---

## GLSL 着色器片段

### 可用的着色器类型

#### fragment
控制颜色和不透明度。

```yaml
snippets:
  - fragment: |
      texColor.rgb = vec3(1.0, 0.0, 0.0);  // 设置为红色
      texColor.a *= 0.5;                    // 50% 不透明度
```

**可用变量：**
- `texColor` - 当前文本颜色（vec4: r, g, b, a）
- `timeSeconds` - 当前时间（以秒为单位，用于动画）
- `charIndex` - 文本中的字符索引 (0, 1, 2, ...)

**常见操作：**
- `texColor.rgb = vec3(r, g, b)` - 设置 RGB 颜色
- `texColor.a = opacity` - 设置不透明度（0.0 = 不可见，1.0 = 实心）
- `texColor.a *= multiplier` - 乘以不透明度

#### vertex
控制位置和运动。

```yaml
snippets:
  - vertex: |
      pos.y += sin(timeSeconds) * 2.0;  // 上下移动
      pos.x += charIndex * 0.5;          // 偏移每个字符
```

**可用变量：**
- `pos` - 字符位置（vec3: x, y, z）
- `timeSeconds` - 当前时间（以秒为单位）
- `charIndex` - 字符索引

**常见操作：**
- `pos.y += offset` - 垂直移动
- `pos.x += offset` - 水平移动
- `sin(timeSeconds)` - 正弦波动画
- `cos(timeSeconds)` - 余弦波动画

---

## 内置特效

### rainbow
循环彩虹颜色。

```yaml
rainbow:
  enabled: true
  description: "随时间循环彩虹颜色"
  snippets:
    - fragment: |
        float hue = fract(charIndex * 0.03 + timeSeconds * 0.09);
        texColor.rgb = hsv2rgb(vec3(hue, 0.9, 1.0));
```

**工作原理：**
- `charIndex * 0.03` - 每个字符有不同的色相
- `timeSeconds * 0.09` - 色相随时间变化
- `hsv2rgb()` - 将 HSV 转换为 RGB

**用法：** `<effect:rainbow>彩虹文字</effect>`

### wave
垂直正弦波运动。

```yaml
wave:
  enabled: true
  description: "垂直正弦波运动"
  snippets:
    - fragment: |
        texColor.rgb = vec3(0.333, 0.804, 0.988);  // 蓝色
      vertex: |
        float phase = charIndex * 0.6 + timeSeconds * 6.0;
        pos.y += sin(phase) * 2.0;
```

**工作原理：**
- `charIndex * 0.6` - 每个字符处于不同的波形位置
- `timeSeconds * 6.0` - 波形随时间移动
- `sin(phase) * 2.0` - 垂直位移（振幅 2 像素）

**用法：** `<effect:wave>波浪文字</effect>`

### shake
随机抖动/颤动特效。

```yaml
shake:
  enabled: true
  description: "随机抖动"
  snippets:
    - fragment: |
        texColor.rgb = vec3(1.0, 0.42, 0.42);  // 红色
      vertex: |
        float seed = charIndex + floor(timeSeconds * 32.0);
        pos.x += (fract(sin(seed * 12.9898) * 43758.5453) - 0.5) * 1.5;
        pos.y += (fract(sin(seed * 78.233) * 43758.5453) - 0.5) * 1.5;
```

**工作原理：**
- `floor(timeSeconds * 32.0)` - 每秒更新 32 次
- `fract(sin(seed * constant) * largeNumber)` - 伪随机值
- `- 0.5` - 使随机值居中（-0.5 到 0.5）
- `* 1.5` - 抖动振幅

**用法：** `<effect:shake>抖动文字</effect>`

### pulse
不透明度淡入淡出。

```yaml
pulse:
  enabled: true
  description: "不透明度淡入/淡出"
  snippets:
    - fragment: |
        texColor.rgb = vec3(1.0, 0.85, 0.24);  // 黄色
        float pulse = (sin(timeSeconds * 1.5 + charIndex * 0.3) + 1.0) * 0.5;
        texColor.a *= 0.3 + pulse * 0.7;
```

**工作原理：**
- `sin(timeSeconds * 1.5)` - 用于脉冲的正弦波
- `+ 1.0) * 0.5` - 归一化到 0.0-1.0 范围
- `0.3 + pulse * 0.7` - 不透明度范围从 0.3 到 1.0

**用法：** `<effect:pulse>脉冲文字</effect>`

---

## 共享代码

### fragment_prelude

所有特效可用的共享 GLSL 函数。

```yaml
shared:
  fragment_prelude: |
    // HSV 到 RGB 的转换
    vec3 hsv2rgb(vec3 c) {
        vec4 K = vec4(1.0, 2.0/3.0, 1.0/3.0, 3.0);
        vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
        return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }

    // 在此添加更多辅助函数
```

**用途：**
- 一次定义可重用函数
- 在所有片段着色器中可用
- 保持特效代码简洁和 DRY

**示例 - 添加颜色函数：**
```yaml
shared:
  fragment_prelude: |
    vec3 hsv2rgb(vec3 c) {
        vec4 K = vec4(1.0, 2.0/3.0, 1.0/3.0, 3.0);
        vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
        return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }

    // 自定义渐变函数
    vec3 gradient(float t, vec3 color1, vec3 color2) {
        return mix(color1, color2, t);
    }
```

然后在特效中使用：
```yaml
custom_gradient:
  snippets:
    - fragment: |
        float t = fract(charIndex * 0.1 + timeSeconds * 0.2);
        texColor.rgb = gradient(t, vec3(1.0, 0.0, 0.0), vec3(0.0, 0.0, 1.0));
```

---

## 创建自定义特效

### 简单颜色更改

```yaml
effects:
  green:
    enabled: true
    description: "绿色文本"
    snippets:
      - fragment: |
          texColor.rgb = vec3(0.0, 1.0, 0.0);  // RGB 绿色
```

### 动画颜色循环

```yaml
effects:
  color_cycle:
    enabled: true
    description: "在红色和蓝色之间循环"
    snippets:
      - fragment: |
          float cycle = (sin(timeSeconds * 2.0) + 1.0) * 0.5;  // 0.0 到 1.0
          texColor.r = 1.0 - cycle;  // 红色渐出
          texColor.b = cycle;        // 蓝色渐入
          texColor.g = 0.0;          // 无绿色
```

### 弹跳动画

```yaml
effects:
  bounce:
    enabled: true
    description: "字符上下弹跳"
    snippets:
      - vertex: |
          float delay = charIndex * 0.2;  // 每个字符错开弹跳
          float bounce = abs(sin((timeSeconds - delay) * 3.0)) * 3.0;
          pos.y += bounce;
```

### 旋转文字

```yaml
effects:
  spin:
    enabled: true
    description: "缓慢旋转的字符"
    snippets:
      - vertex: |
          float angle = timeSeconds * 0.5 + charIndex * 0.3;
          float radius = 2.0;
          pos.x += cos(angle) * radius;
          pos.y += sin(angle) * radius;
```

### 故障特效

```yaml
effects:
  glitch:
    enabled: true
    description: "随机的故障位移"
    snippets:
      - fragment: |
          // 随机颜色偏移
          float r = fract(sin(timeSeconds * 100.0 + charIndex) * 43758.5);
          if (r > 0.95) {
            texColor.rgb = vec3(1.0, 0.0, 0.0);  // 偶尔的红色闪烁
          }
      vertex: |
          // 随机位移
          float glitch = fract(sin(floor(timeSeconds * 20.0) + charIndex) * 43758.5);
          if (glitch > 0.9) {
            pos.x += (fract(sin(charIndex) * 43758.5) - 0.5) * 5.0;
          }
```

---

## GLSL 参考

### 内置函数

**三角函数:**
- `sin(x)` - 正弦函数
- `cos(x)` - 余弦函数
- `tan(x)` - 正切函数

**数学:**
- `abs(x)` - 绝对值
- `floor(x)` - 向下取整
- `ceil(x)` - 向上取整
- `fract(x)` - 小数部分 (x - floor(x))
- `mod(x, y)` - 取模
- `min(x, y)` - 最小值
- `max(x, y)` - 最大值
- `clamp(x, min, max)` - 限制在最小值和最大值之间
- `mix(a, b, t)` - 线性插值 (a * (1-t) + b * t)

**向量:**
- `length(v)` - 向量长度
- `normalize(v)` - 单位向量
- `dot(a, b)` - 点积

### 变量类型

- `float` - 单个数字
- `vec2` - 2D 向量 (x, y)
- `vec3` - 3D 向量 (x, y, z) 或 RGB 颜色
- `vec4` - 4D 向量 (x, y, z, w) 或 RGBA 颜色

### 基于时间的动画

```glsl
// 平滑振荡 (0.0 到 1.0)
float wave = (sin(timeSeconds * speed) + 1.0) * 0.5;

// 锯齿波 (0.0 到 1.0 重复)
float saw = fract(timeSeconds * speed);

// 阶梯动画
float step = floor(timeSeconds * stepsPerSecond);
```

### 基于字符的变化

```glsl
// 每个字符不同的值
float offset = charIndex * 0.1;

// 错开动画
float stagger = charIndex * 0.3;
float anim = sin((timeSeconds - stagger) * speed);

// 分组字符
float group = floor(charIndex / 3.0);  // 3 个一组
```

---

## 故障排除

### "特效不工作"

**检查：**
1. text_effects.yml 中 `enabled: true`
2. Minecraft 版本 1.21.1+（推荐 1.21.11+）
3. settings.yml 中 TextEffects 已启用：
```yaml
TextEffects:
  enabled: true
```
4. 重新加载：`/oraxen reload all`

### "着色器编译错误"

**常见问题：**
- 行尾缺少分号 `;`
- 未定义的变量（检查拼写：`texColor` 而不是 `textColor`）
- 在片段着色器中使用顶点变量（或反之）
- GLSL 语法错误（检查控制台错误消息）

### "特效随机触发"

**原因：** 触发颜色出现在普通文本/渐变中

**解决方案：**
- 选择更独特的触发颜色
- 使用默认自动生成的颜色（`#FDxD00` 模式）
- 避免在普通消息中使用触发颜色

### "特效 ID 冲突"

**原因：** 重复的 ID 或过多特效（最多 8 个）

**解决方案：**
```yaml
# 移除或禁用一个特效
old_effect:
  enabled: false

# 或者分配显式 ID 以防止冲突
effect1:
  id: 0
effect2:
  id: 1
```

### "文本不可见/黑色"

**原因：** `texColor.a = 0.0` 或 `texColor.rgb = vec3(0.0, 0.0, 0.0)`

**解决方案：**
确保你设置了可见的颜色：
```glsl
texColor.rgb = vec3(1.0, 1.0, 1.0);  // 白色（始终可见）
texColor.a = 1.0;  // 完全不透明
```

---

## 性能考量

### 优化提示

**轻量级特效：**
- 仅片段（无顶点运动）
- 简单的数学运算
- 避免每个字符的复杂计算

**示例 - 高效：**
```yaml
simple_red:
  snippets:
    - fragment: |
        texColor.rgb = vec3(1.0, 0.0, 0.0);
```

**示例 - 沉重：**
```yaml
complex:
  snippets:
    - fragment: |
        // 避免大量循环或过多计算
        for (int i = 0; i < 100; i++) {  // 不好
          texColor.rgb += someCalculation(i);
        }
      vertex: |
        // 每帧的复杂顶点操作
```

### 客户端性能

特效在客户端 GPU 上运行：
- 现代 GPU：可以轻松处理复杂特效
- 较旧/集成 GPU：可能难以处理重型着色器特效
- 移动设备：保持特效简单

**建议：** 如果面向广泛受众，在低端硬件上进行测试。

---

## 另请参阅

- [文字特效概述](./index) - 介绍和基本用法
- [GLSL 自定义](./glsl-customization) - 高级着色器编程
- [插件设置](../../plugin-setup/plugin-settings) - 全局启用/禁用文字特效
- [品牌自定义](../../configuration/branding-customization) - 在消息中使用特效