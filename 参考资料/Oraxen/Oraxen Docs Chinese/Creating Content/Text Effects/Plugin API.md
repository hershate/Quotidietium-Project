# 插件 API

import { Callout } from 'nextra/components'

Oraxen 提供了一个 Java API，用于在你的插件中以编程方式应用文字特效。

## 基本用法

```java
import io.th0rgal.oraxen.font.TextEffect;
import net.kyori.adventure.text.Component;

// 获取特定的特效定义
TextEffect.Definition rainbow = TextEffect.getEffect("rainbow");

// 对文本应用特效
Component text = TextEffect.apply("Hello World!", rainbow);

// 通过名称应用特效
Component wave = TextEffect.apply("Wavy text!", "wave");

// 内置特效的便捷方法
Component rainbowText = TextEffect.rainbow("Rainbow text!");
Component wavyText = TextEffect.wave("Wavy text!");
Component shakyText = TextEffect.shake("Shaky text!");
Component pulsingText = TextEffect.pulse("Pulsing text!");

// 检查特效是否启用
boolean enabled = TextEffect.isEnabled();
boolean rainbowEnabled = TextEffect.isEffectEnabled(rainbow);
boolean waveEnabled = TextEffect.isEffectEnabled("wave");
```

## 可用方法

| 方法 | 描述 |
|--------|-------------|
| `TextEffect.getEffect(name)` | 通过名称获取特效定义 |
| `TextEffect.getEffect(id)` | 通过 ID 获取特效定义 |
| `TextEffect.getEffects()` | 获取所有可用的特效定义 |
| `TextEffect.getEnabledEffects()` | 获取所有已启用的特效定义 |
| `TextEffect.apply(text, definition)` | 对文本应用特效 |
| `TextEffect.apply(text, name)` | 通过名称应用特效 |
| `TextEffect.isEnabled()` | 检查文字特效是否全局启用 |
| `TextEffect.isEffectEnabled(definition)` | 检查特定特效是否启用 |
| `TextEffect.isEffectEnabled(name)` | 通过名称检查特效是否启用 |
| `TextEffect.rainbow(text)` | 应用彩虹特效 |
| `TextEffect.wave(text)` | 应用波浪特效 |
| `TextEffect.shake(text)` | 应用抖动特效 |
| `TextEffect.pulse(text)` | 应用脉冲特效 |

## 特效定义

每个特效定义包含：

```java
TextEffect.Definition effect = TextEffect.getEffect("rainbow");

String name = effect.getName();           // "rainbow"
int id = effect.getId();                  // 0
String desc = effect.getDescription();    // "随时间循环彩虹颜色"
boolean enabled = effect.isEnabled();     // true
TextColor trigger = effect.getTriggerColor(); // 此特效的触发颜色
```

## MiniMessage 集成

使用文字特效最简单的方式是通过 MiniMessage 标签：

```java
import io.th0rgal.oraxen.utils.AdventureUtils;

// AdventureUtils.MINI_MESSAGE 包含文字特效标签解析器
Component text = AdventureUtils.MINI_MESSAGE.deserialize(
    "<effect:rainbow>彩虹文字！</effect>"
);

// 与其他 MiniMessage 标签一起使用
Component mixed = AdventureUtils.MINI_MESSAGE.deserialize(
    "<bold><effect:wave>粗体波浪文字！</effect></bold>"
);
```

### 自定义标签解析器

如果你需要将文字特效解析器添加到自己的 MiniMessage 实例中：

```java
import io.th0rgal.oraxen.font.TextEffectTag;
import net.kyori.adventure.text.minimessage.MiniMessage;
import net.kyori.adventure.text.minimessage.tag.resolver.TagResolver;

MiniMessage mm = MiniMessage.builder()
    .tags(TagResolver.resolver(
        TagResolver.standard(),
        TextEffectTag.RESOLVER
    ))
    .build();

Component text = mm.deserialize("<effect:rainbow>你好！</effect>");
```

## 特效工作原理

当你应用文字特效时，Oraxen 会：

1. 将每个字符设置为使用**特效专用字体**（例如彩虹的 `oraxen:effect/0`）
2. 用特效的**触发颜色**为每个字符着色（例如彩虹的 `#FD0D00`）
3. 着色器匹配这个确切的颜色并应用视觉特效

```java
// 返回的组件已逐字符设置了字体和颜色
Component rainbow = TextEffect.apply("Hi", TextEffect.getEffect("rainbow"));
// 结果：每个字符的 font=oraxen:effect/0, color=#FD0D00
```

## PlaceholderAPI

文字特效可以与 PlaceholderAPI 结合使用：

```java
// 示例：对占位符结果应用特效
String placeholderResult = PlaceholderAPI.setPlaceholders(player, "%player_name%");
Component effectComponent = TextEffect.apply(placeholderResult, "rainbow");
```

## 启用/禁用特效

你可以通过编程方式切换特效：

```java
// 切换全局状态
TextEffect.setGlobalEnabled(false);

// 切换特定特效
TextEffect.setEffectEnabled("rainbow", false);

TextEffect.Definition wave = TextEffect.getEffect("wave");
TextEffect.setEffectEnabled(wave, true);
```

<Callout type="warning">
在运行时更改特效状态不会重新生成着色器。特效只能通过编辑 `text_effects.yml` 并重新加载资源包来完全添加/移除。
</Callout>

## 性能考量

- 文字特效通过着色器在客户端渲染，因此对服务器的影响最小
- 特效组件在创建时计算一次
- 缓存 `TextEffect.Definition` 对象，而不是重复调用 `getEffect()`
- MiniMessage 标签解析器自动处理所有编码