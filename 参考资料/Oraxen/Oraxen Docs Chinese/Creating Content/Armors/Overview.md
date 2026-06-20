---
description: 如何创建具有独特纹理的自定义盔甲
cover: >-
  https://cdn.discordapp.com/attachments/896841738621177896/966823919917080626/unknown.png
coverY: 0
---

import { Callout } from 'nextra/components'

# 自定义盔甲

Oraxen 允许你创建在穿戴时具有独特纹理的自定义盔甲套装。有三种方法可供选择，每种方法针对不同的 Minecraft 版本设计。

## 快速对比

| 方法 | MC 版本 | 基础材质 | 着色器兼容 | 推荐 |
|--------|------------|---------------|-------------------|-------------|
| [组件 (Components)](/creating-content/armors/components) | 1.21.2+ | 任意 | ✅ 是 | ✅ 最佳选择 |
| [纹饰 (Trims)](/creating-content/armors/trims) | 1.20-1.21.1 | 锁链 | ✅ 是 | 适用于 1.20-1.21.1 |
| [着色器 (Shaders)](/creating-content/armors/shaders) | 1.18-1.19.4 | 皮革 | ❌ 需要 CIT | 旧版服务器 |

## 选择合适的方法

### 使用组件 (Components) 适用于：
- **所有 1.21.2+ 服务器** - 这是最佳选择
- **任意盔甲材质** - 不受限于皮革或锁链
- **完全着色器兼容** - 与 Optifine、Iris 等兼容

### 使用纹饰 (Trims) 适用于：
- 不支持组件的 **1.20-1.21.1 服务器**
- 无需额外模组的**着色器兼容性**
- **非皮革材质** - 默认使用锁链

### 使用着色器 (Shaders) 适用于：
- **1.20 之前的服务器**或允许旧版客户端连接的服务器
- 已在使用此方法的**旧版配置**

<Callout type="warning">
**着色器方法的限制**

着色器方法在 Optifine/Iris 着色器下会失效。Oraxen 会生成 CIT 纹理来为 Optifine 修复此问题，但 Iris 用户需要安装 [CIT Resewn](https://modrinth.com/mod/cit-resewn)。
</Callout>

## 功能对比

| 功能 | 组件 | 纹饰 | 着色器 |
|---------|------------|-------|---------|
| 任意基础材质 | ✅ | ❌ 锁链 | ❌ 皮革 |
| 与着色器兼容 | ✅ | ✅ | ⚠️ 需要 CIT |
| 动画纹理 | ✅ | ✅ | ✅ |
| 纹饰图案 | ✅ | ✅ | ❌ |
| 可染色 | ✅ | ❌ | ✅ |
| 性能 | ✅ 最佳 | ✅ 良好 | ⚠️ 一般 |

## 基本配置

所有盔甲方法共享类似的基础配置：

```yaml
my_helmet:
  displayname: "<gradient:#4B36B1:#6699FF>My Helmet"
  material: DIAMOND_HELMET  # 着色器方法使用 LEATHER_HELMET
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - my_helmet.png
  # 具体方法的配置见下文
```

## 下一步

- [组件 (1.21.2+)](/creating-content/armors/components) - 推荐现代服务器使用
- [纹饰 (1.20-1.21.1)](/creating-content/armors/trims) - 适用于 1.20.x 服务器
- [着色器 (1.18-1.19.4)](/creating-content/armors/shaders) - 适用于旧版服务器
