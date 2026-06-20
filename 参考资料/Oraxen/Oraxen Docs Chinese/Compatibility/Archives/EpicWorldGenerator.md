---
description: EpicWorldGenerator 集成（已归档 - 插件已停更）
---

import { Callout } from 'nextra/components'

# EpicWorldGenerator

<Callout type="warning">
  **已归档**：EpicWorldGenerator 仅支持 Minecraft 1.15 - 1.17.1，且未针对现代版本进行更新。
</Callout>

## 状态

EpicWorldGenerator 最后支持的版本是 Minecraft 1.17.1。由于世界生成 API 的重大变化，该插件无法在 Minecraft 1.18 及以上版本上运行。

## 替代方案

对于现代 Minecraft 版本，我们推荐使用 [Iris World Generator](https://www.spigotmc.org/resources/iris-world-gen-the-dimension-engine.84586/)，它积极支持最新的 Minecraft 版本，并且具有原生的 Oraxen 方块支持。

有关集成详情，请参阅我们的 [Iris World Generator 文档](/compatibility/world-generators/iris-world-generator)。

## 旧版信息

EpicWorldGenerator 允许在运行 Minecraft 1.17.1 及以下版本的服务器上使用 Oraxen 方块生成自定义矿物。如果你仍在运行较旧的服务器，该集成通过自定义 BlockData 配置实现，与其他世界生成器类似。
