---
description: RealisticWorldGenerator 集成（已归档 - 插件已停更）
---

import { Callout } from 'nextra/components'

# RealisticWorldGenerator

<Callout type="warning">
  **已归档**：RealisticWorldGenerator 仅支持 Minecraft 1.8.8 - 1.17.1，且无法在 Minecraft 1.18+ 上运行。
</Callout>

## 状态

RealisticWorldGenerator 无法在 Minecraft 1.18 及以上版本上运行。开发者已宣布将重写以支持现代版本，但目前尚未可用。

如果你需要在 1.18+ 上使用 RealisticWorldGenerator 的世界，你可以先在 1.17.1 服务器上生成世界，然后将其转移到较新的服务器上。

## 替代方案

对于现代 Minecraft 版本，我们推荐使用 [Iris World Generator](https://www.spigotmc.org/resources/iris-world-gen-the-dimension-engine.84586/)，它积极支持最新的 Minecraft 版本，并且具有原生的 Oraxen 方块支持。

有关集成详情，请参阅我们的 [Iris World Generator 文档](/compatibility/world-generators/iris-world-generator)。

## 旧版信息

RealisticWorldGenerator 允许在运行 Minecraft 1.17.1 及以下版本的服务器上使用 Oraxen 方块生成自定义矿物。该集成通过自定义 BlockData 配置实现。
