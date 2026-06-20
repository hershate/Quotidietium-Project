---
description: MythicHUD（前身为 HappyHUD）让你可以制作高度可定制的 HUD
---

import { Callout } from 'nextra/components'

# MythicHUD

<Callout type="info">
  HappyHUD 已更名为 **MythicHUD**，现在是 MythicCraft 生态系统的一部分。如果你正在从 HappyHUD 迁移，MythicHUD 包含自动迁移支持。
</Callout>

本文将详细介绍如何让 MythicHUD 与 Oraxen 正确兼容。

## 设置步骤

1. 在 settings.yml 中设置 `hide_scoreboard_numbers: false`
2. 删除 `Oraxen/pack/shaders/core/render_text.vsh` 和 `render_text.json`（如果存在）
3. 在 MythicHUD 的配置中，启用 `copy-resource-pack` 并设置 `path: "Oraxen/pack/assets"`

## 隐藏计分板数字

如果你确实也想隐藏计分板数字，可以手动将 Oraxen 的着色器文件合并到 MythicHUD 的 `MythicHUD/pack/minecraft/shaders/core/` 目录中。

## 资源

- [MythicHUD 文档](https://mythiccraft.io)
- [MythicHUD GitLab](https://git.mythiccraft.io/mythiccraft/mythichud)
