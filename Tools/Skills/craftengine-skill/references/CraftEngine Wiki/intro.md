# 📗 介绍

你好！欢迎来到 CraftEngine 文档！

![banner](/img/craftengine.avif)

## 什么是 CraftEngine

CraftEngine 使您能够通过创建新的方块、物品和配方来自定义您的 Minecraft 服务器体验。所有这些都可以仅通过资源包和服务端实现来完成，无需安装任何客户端模组。

:::info

CraftEngine 提供了一套完整的方块行为 API，让您能够像在 Forge/Fabric 中一样注册自定义方块行为。如果您曾是模组开发者，那么您会对 CraftEngine 的注册系统感到非常熟悉！我们推荐使用 [PaperWeight](https://github.com/PaperMC/paperweight) 作为您的首选开发依赖。

:::

## 获取插件
- 社区版可在 [**Modrinth**](https://modrinth.com/plugin/craftengine) 上下载
- 付费版可在 [**Polymart**](https://polymart.org/product/7624/craftengine) 上购买
- 中国大陆用户可在 [**爱发电**](https://afdian.com/a/xiaomomi) 上购买付费版

## 安装插件

CraftEngine 需要基于 [**Paper**](https://papermc.io/downloads/paper) 的 Minecraft 服务器才能运行。它兼容大多数常见的分支版本，包括 [**Folia**](https://papermc.io/downloads/folia), Pufferfish, Purpur 及其他类似变体。
要安装这个插件，只需将 .jar 文件拖放到您的服务器的 /plugins 文件夹中即可。

:::info

CraftEngine 运行需要 JDK 21 或更高版本。最低支持的 Minecraft 版本为 1.20，但未来可能会根据[网易](https://zh.minecraft.wiki/w/%E4%B8%AD%E5%9B%BD%E7%89%88)在中国对 Minecraft 服务器版本的支持情况调整，可能会取消对该版本的支持。

:::

## 获取插件支持
- **付费版** 用户可通过我们的 [**Discord**](https://discord.gg/xiaomomi) 机器人验证，进入专属支持频道。
- 中国大陆 **付费版** 用户可通过QQ群 `1039968907` 获得支持
- 随时随地使用大语言模型 [**DeepWiki**](https://deepwiki.com/Xiao-MoMi/craft-engine) 获取自助 AI 支持
- 如果你是一个正在制作公开项目的开发者，你可以通过 `#api-help` 频道获取免费的开发支持

## 核心差异化优势
CraftEngine 的底层实现原理与同类竞品存在本质差异。若您对技术细节感兴趣，可在 GitHub 上查阅源码深入了解。

简而言之：
- CraftEngine 实现服务端模组化，支持创建突破当前 Minecraft 版本限制的全新方块
- 采用类 ViaBackwards 的实现方案，将新方块转换为玩家可见的旧版方块格式

:::tip

您可通过 [☄️ 独家功能](intro/exclusive_feature.md) 快速浏览 CraftEngine 的专属特性

部分功能在其他插件中已有实现——但 CraftEngine 表现更优。查看 [🥕 简而不凡](intro/simply_better.md) 中的对比分析

:::
