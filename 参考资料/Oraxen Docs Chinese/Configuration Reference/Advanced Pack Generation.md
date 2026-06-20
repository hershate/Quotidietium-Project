---
description: 用于优化和验证的高级资源包生成设置
---

# 高级资源包生成

用于资源包生成、验证、优化和图集管理的高级配置选项。

## 概述

除了基础的资源包生成设置外，Oraxen 还提供了以下高级选项：
- 资源包文件验证与错误处理
- Unicode/强制Unicode兼容性
- 纹理格式转换（1.20.2+ 图集系统）
- 图集生成与优化
- 自定义文件排除
- 资源键混淆

**位置:** `settings.yml` → `Pack.generation`

---

## 资源包验证

### verify_pack_files

验证所有纹理和模型，确保它们遵循有效的资源包格式。

```yaml
Pack:
  generation:
    verify_pack_files: true  # 启用验证（默认: true）
```

**检查内容：**
- 纹理文件格式（PNG有效性）
- 模型JSON语法
- 文件命名规范（小写，无空格）
- 所需的模型属性
- 纹理尺寸（某些格式需要是2的幂）

**启用时：**
- ✅ 在资源包生成前捕获错误
- ✅ 防止损坏的文件破坏资源包
- ✅ 记录无效文件的详细警告
- ❌ 资源包生成稍慢

**禁用时：**
- ✅ 资源包生成更快
- ❌ 无效文件可能破坏资源包
- ❌ 更难调试问题

**建议**: 保持 `true`，除非您确定所有资源都是有效的。

### exclude_malformed_from_atlas

防止损坏的纹理被包含在纹理图集中。

```yaml
Pack:
  generation:
    atlas:
      exclude_malformed_from_atlas: true  # 默认: true
```

**它做什么：**
- 检查纹理文件是否损坏
- 从 atlas.png 中排除损坏的纹理
- 防止资源包因一个损坏的纹理而无法加载

**启用时：**
- ✅ 即使有部分损坏的纹理，资源包仍然可用
- ✅ 记录哪些纹理被排除
- ✅ 允许修复纹理而不破坏整个资源包

**禁用时：**
- ❌ 一个损坏的纹理可能损坏整个图集
- ❌ 资源包可能无法加载

**建议**: 对于生产服务器，始终保持 `true`。

---

## Unicode 和字体兼容性

### fix_force_unicode_glyphs

修复在 Minecraft 客户端设置中启用"强制Unicode"时字形不显示的问题。

```yaml
Pack:
  generation:
    fix_force_unicode_glyphs: true  # 默认: true
```

**问题：**
- Minecraft 的"强制Unicode"选项（在语言设置中）强制所有文本使用Unicode字体
- 没有此修复时，自定义字形在强制Unicode开启时不渲染
- 影响表情符号、自定义字体和界面字形

**工作原理：**
- 生成与强制Unicode兼容的额外字体变体
- 添加回退字体定义
- 确保字形在普通模式和强制Unicode模式下都能渲染

**启用时：**
- ✅ 字形在强制Unicode开启和关闭时都能正常工作
- ✅ 更好的玩家体验（某些语言需要强制Unicode）
- ❌ 资源包大小略有增加

**禁用时：**
- ✅ 资源包大小更小
- ❌ 强制Unicode启用时字形不工作
- ❌ 使用亚洲语言的玩家可能会遇到问题

**建议**: 对于国际服务器，保持 `true`。

---

## 纹理格式转换

### texture_slicer

通过切片超大纹理，将纹理转换为新的 1.20.2+ 图集格式。

```yaml
Pack:
  generation:
    texture_slicer: true  # 默认: true
```

**它做什么（Minecraft 1.20.2+）：**
- 自动切片大于 16x16 的纹理
- 将旧的"高"纹理格式转换为新的基于精灵的系统
- 确保与现代 Minecraft 版本的兼容性

**示例：**
- **旧格式**: 16x64 纹理用于动画（4帧垂直堆叠）
- **新格式**: 4个独立的 16x16 精灵 + mcmeta 动画定义

**启用时：**
- ✅ 纹理在 1.20.2+ 上正常工作
- ✅ 向后兼容旧版本
- ✅ 遵循现代资源包标准

**禁用时：**
- ❌ 大纹理在 1.20.2+ 上可能无法正确显示
- ❌ 动画纹理可能损坏

**建议**: 对于 1.20.2+ 服务器，保持 `true`。

---

## 图集生成

图集系统控制 Minecraft 如何将多个纹理合并到单个纹理图集中以提高性能。

### generate

启用或禁用图集生成。

```yaml
Pack:
  generation:
    atlas:
      generate: true  # 默认: true
```

**什么是图集？**
- 将许多小纹理合并为一个大纹理表
- 减少 GPU 纹理切换 = 更好的性能
- Minecraft 自动对方块、物品等使用图集

**启用时：**
- ✅ 更好的性能（更少的纹理切换）
- ✅ 标准的 Minecraft 行为

**禁用时：**
- ❌ 更差的性能
- ❌ 可能导致渲染问题

**建议**: 始终保持 `true`。

### type

图集生成策略。

```yaml
Pack:
  generation:
    atlas:
      type: "SPRITE"  # 选项: SPRITE 或 DIRECTORY
```

**SPRITE**（默认，推荐）：
- 从单个精灵定义生成图集
- 对包含内容有更多控制
- 现代方法（1.19+）

**DIRECTORY**：
- 从目录中的所有纹理生成图集
- 更简单但控制更少
- 旧版方法

**建议**: 对于现代资源包使用 `SPRITE`。

---

## 模型路径行为

### auto_generated_models_follow_texture_path

控制自动生成的模型是否遵循纹理目录结构放置。

```yaml
Pack:
  generation:
    auto_generated_models_follow_texture_path: false  # 默认: false
```

**当为 false 时（默认）：**
```
textures/items/weapons/legendary_sword.png
models/items/legendary_sword.json  # 模型在平级的 items/ 目录中
```

**当为 true 时：**
```
textures/items/weapons/legendary_sword.png
models/items/weapons/legendary_sword.json  # 模型遵循纹理路径
```

**使用场景：**

**保持 `false` 时：**
- 您希望所有模型采用平级结构
- 小型资源包更简单的组织方式
- 默认的 Oraxen 行为

**设为 `true` 时：**
- 您有许多按子目录组织的物品
- 您希望模型在概念上与纹理相邻
- 更容易找到相关文件

---

## 文件排除

### excluded_file_extensions

从最终资源包 ZIP 中排除特定文件类型。

```yaml
Pack:
  generation:
    excluded_file_extensions:
      - ".psd"
      - ".xcf"
      - ".kra"
      - ".blend"
      - ".tmp"
```

**常见排除项：**

| 扩展名 | 描述 | 为何排除？ |
|-----------|-------------|--------------|
| `.psd` | Photoshop文件 | 源文件，资源包不需要 |
| `.xcf` | GIMP文件 | 源文件，体积大 |
| `.kra` | Krita文件 | 源文件，体积大 |
| `.blend` | Blender文件 | 3D源文件，非常大 |
| `.tmp` | 临时文件 | 不需要，可能导致问题 |
| `.bak` | 备份文件 | 重复项，增加资源包大小 |
| `.md` | Markdown文档 | 文档，资源包不需要 |

**配置示例：**
```yaml
Pack:
  generation:
    excluded_file_extensions:
      # 图像编辑源文件
      - ".psd"
      - ".xcf"
      - ".kra"
      - ".ai"

      # 3D建模文件
      - ".blend"
      - ".obj"
      - ".fbx"

      # 开发文件
      - ".tmp"
      - ".bak"
      - ".old"
      - ".backup"

      # 文档
      - ".md"
      - ".txt"
      - ".doc"
```

**好处：**
- ✅ 更小的资源包大小
- ✅ 玩家下载更快
- ✅ 更清晰的资源包结构
- ✅ 源文件不会泄露给玩家

---

## 资源键混淆

### obfuscation.type

控制生成的资源包中模型、纹理和声音路径是否在最终资源包中被重命名。

```yaml
Pack:
  generation:
    obfuscation:
      type: NONE  # 选项: NONE, SIMPLE, FULL
```

| 类型 | 行为 |
|------|----------|
| `NONE` | 默认。保持生成的资源键可读。 |
| `SIMPLE` | 重命名资源包内部的模型、纹理和声音路径，同时保留命名空间。 |
| `FULL` | 重命名资源包内部路径，并替换被重命名资源使用的命名空间。 |

`false`、`off` 和 `disabled` 也被接受为禁用值。

这仅改变生成的资源包输出。物品和家具配置应继续引用正常的逻辑模型、纹理和声音路径。

**启用时：**
- 使发布的资源包内部更难通过原始名称检查
- 重写生成的模型、图集、字体和声音中的 JSON 引用
- 适用于普通和多版本资源包生成

**禁用时：**
- 生成的资源包路径保持可读
- 更容易调试自定义资源包文件

**建议**: 在开发或调试资源包文件时保持 `NONE`。仅在确认生成的资源包加载正确后使用 `SIMPLE` 或 `FULL`。

---

## 完整示例

生产服务器的最佳设置：

```yaml
Pack:
  generation:
    generate: true

    # 验证
    verify_pack_files: true

    # 兼容性
    fix_force_unicode_glyphs: true
    texture_slicer: true

    # 图集
    atlas:
      exclude_malformed_from_atlas: true
      generate: true
      type: "SPRITE"

    # 组织
    auto_generated_models_follow_texture_path: false

    # 排除源文件
    excluded_file_extensions:
      - ".psd"
      - ".xcf"
      - ".kra"
      - ".blend"
      - ".tmp"
      - ".bak"
      - ".md"

    # 压缩与保护
    compression: BEST_COMPRESSION
    obfuscation:
      type: SIMPLE
    protection: true

    comment: "© 2026 MyServer - All Rights Reserved"
```

---

## 性能优化

### 小型资源包（少于100个物品）

标准设置即可正常工作：

```yaml
Pack:
  generation:
    verify_pack_files: true
    fix_force_unicode_glyphs: true
    texture_slicer: true
    atlas:
      generate: true
      type: "SPRITE"
```

### 大型资源包（100-500个物品）

优化资源包大小：

```yaml
Pack:
  generation:
    verify_pack_files: true
    fix_force_unicode_glyphs: true
    texture_slicer: true
    compression: BEST_COMPRESSION

    # 更积极地排除
    excluded_file_extensions:
      - ".psd"
      - ".xcf"
      - ".kra"
      - ".blend"
      - ".tmp"
      - ".bak"
      - ".md"
      - ".txt"
      - ".json.bak"

    atlas:
      exclude_malformed_from_atlas: true
      generate: true
      type: "SPRITE"
```

### 超大型资源包（500+个物品）

考虑拆分为多个资源包或采取激进的优化：

```yaml
Pack:
  generation:
    # 更快的生成（跳过部分验证）
    verify_pack_files: false  # 仅在您确定文件有效时使用

    # 必要功能
    fix_force_unicode_glyphs: true
    texture_slicer: true

    # 激进压缩
    compression: BEST_COMPRESSION

    # 排除所有非必要文件
    excluded_file_extensions:
      - ".psd"
      - ".xcf"
      - ".kra"
      - ".ai"
      - ".blend"
      - ".obj"
      - ".fbx"
      - ".tmp"
      - ".bak"
      - ".old"
      - ".backup"
      - ".md"
      - ".txt"
      - ".doc"
      - ".docx"
```

---

## 故障排除

### "资源包生成很慢"

**解决方案：**
- 如果您确定资源是有效的，禁用 `verify_pack_files`
- 减少物品数量
- 排除更多文件扩展名
- 检查是否有非常大的纹理（>512x512）

### "部分纹理不显示"

**检查：**
- `verify_pack_files: true` - 在控制台检查错误
- `exclude_malformed_from_atlas: true` - 检查纹理是否被排除
- 纹理文件格式（必须是PNG）
- 纹理文件名（必须小写，无空格）

### "强制Unicode启用后字形不显示"

**解决方案：**
```yaml
fix_force_unicode_glyphs: true
```

然后重新生成资源包：`/oraxen reload all`

### "资源包太大（超过100MB）"

**解决方案：**
- 在 `excluded_file_extensions` 中添加更多扩展名
- 使用 `compression: BEST_COMPRESSION`
- 优化纹理：
   - 尽可能降低分辨率
   - 使用8位PNG代替24位
   - 删除未使用的纹理
- 临时启用 `protection: false` 以检查未压缩大小

### "1.20.2+ 上纹理显示异常"

**解决方案：**
```yaml
texture_slicer: true
```

确保您使用的是现代纹理格式。

### "模型未在预期位置生成"

**检查：**
```yaml
auto_generated_models_follow_texture_path: false  # 或根据偏好设为 true
```

验证您的纹理路径与预期的模型路径匹配。

---

## 最佳实践

### 开发环境

用于测试和迭代：

```yaml
Pack:
  generation:
    verify_pack_files: true  # 尽早捕获错误
    fix_force_unicode_glyphs: true
    texture_slicer: true
    compression: BEST_SPEED  # 更快的生成
    protection: false  # 可以解压资源包进行调试
    excluded_file_extensions:
      - ".tmp"
      - ".bak"
```

### 生产环境

用于正式服务器：

```yaml
Pack:
  generation:
    verify_pack_files: true
    fix_force_unicode_glyphs: true
    texture_slicer: true
    compression: BEST_COMPRESSION
    protection: true  # 更难被盗取
    excluded_file_extensions:
      # 所有源文件
      - ".psd"
      - ".xcf"
      - ".kra"
      - ".blend"
      - ".tmp"
      - ".bak"
      - ".md"
    atlas:
      exclude_malformed_from_atlas: true
      generate: true
      type: "SPRITE"
```

---

## 另请参阅

- [插件设置](../plugin-setup/plugin-settings) - 基础资源包生成设置
- [资源包托管](../plugin-setup/pack-hosting) - 托管选项
- [资源包导入](../plugin-setup/plugin-settings#import) - 合并多个资源包
- [外观系统](../plugin-setup/plugin-settings#appearance-systems-1214) - 1.21.4+ 物品系统