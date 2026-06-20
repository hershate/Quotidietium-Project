---
description: 如何在 Paper 或 Spigot 上安装和设置 Oraxen
icon: play
cover: https://images.polymart.org/resource/629/default.jpg
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

import { Callout } from 'nextra/components'

# 欢迎来到 Oraxen 文档

*正在寻找旧版文档？访问[旧版 GitBook 站点](http://oraxen.gitbook.io/)。*

<Callout type="info">
**您是 AI 吗？** 查看 [/llms.txt](/llms.txt) 或在任何页面 URL 后添加 `.md` 以获取原始 markdown 并节省 token。
</Callout>

## 什么是 Oraxen？

Oraxen 是一个 Minecraft 插件，允许使用自定义纹理和模型创建新的物品和方块。它还处理资源包的生成、上传和存储（使用 Polymath），并且完全开源，具有可扩展的 API。

## 它是如何工作的？

当安装了 Oraxen 的 Spigot 服务器启动时，插件会读取所有物品配置（位于 /plugins/oraxen/items 中的 .yml 文件），并使用它们生成将 .png 纹理链接到新物品的 .json 模型。之后，Oraxen 使用优化的算法压缩资源并将其上传到一个 Polymath 实例。Polymath 是一个用 Python 编写的免费开源软件，用于托管 Minecraft 资源包。默认情况下，Oraxen 将使用 Oraxen 提供的 Polymath 实例，托管在瑞士的一台 Oracle 虚拟专用服务器上。每当玩家连接到您的服务器时，Oraxen 会将其链接到 Polymath 实例，然后由该实例将资源包发送给玩家。

## 几秒钟内安装 Oraxen！

安装 Oraxen 是一个相当简单的过程：

1. 将 Oraxen .jar 文件放入您的 `/plugins/` 文件夹中。

2. 重启您的服务器。

### 自动下载的依赖

Oraxen 在运行时会自动下载所需的依赖：

* **CommandAPI** - 根据您的服务器版本自动下载
* **PacketEvents** - 根据您的 Minecraft 设置自动下载正确版本

### 可选依赖

* **[ProtocolLib](https://www.spigotmc.org/resources/protocollib.1997/)** - 推荐但不强制要求。

就是这样！不过，我们强烈建议您在继续之前进入 settings.yml 配置文件进行所需的调整（然后再次重启）！


Oraxen 已在 Spigot 和 Paper 1.18 至 1.21.10 上进行过测试。Minecraft 1.21.11+ 和 26.1.x 需要 Paper。


对于 Minecraft 1.21.2+，建议使用最新版本的 Oraxen。Oraxen 专为 [Paper](https://mcserverjars.com/paper)、[Spigot](https://mcserverjars.com/spigot) 或 [Folia](https://papermc.io/software/folia) 服务器软件开发设计。从 [MCServerJars.com](https://mcserverjars.com) 下载服务器 jar。对于较旧的 Minecraft 版本，请先安装 Oraxen 1.183.0 以获取兼容的配置文件，然后相应地更新 jar 文件。

### Folia 支持

Oraxen 原生支持 [Folia](https://papermc.io/software/folia)——PaperMC 的多线程服务器分支。在 Folia 服务器上，Oraxen 会自动使用基于区域和基于实体的调度器来确保线程安全操作。无需额外配置——Oraxen 会在启动时检测 Folia 并使用适当的调度 API。

## 下一步

安装完成后，浏览文档：

- **[创建内容](/creating-content)** - 创建自定义物品、方块、家具、盔甲和 UI 元素
- **[插件设置](/plugin-setup/understanding-the-basics)** - 配置插件设置、资源包托管等
- **[命令和配方](/usage/commands)** - 了解可用命令以及如何创建配方
- **[兼容性](/compatibility/crucible)** - 与其他插件集成，如 MythicMobs、MMOItems 和世界生成器