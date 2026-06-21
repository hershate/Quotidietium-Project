# EpicAchievements 配置模板

> 本目录提供 EpicAchievements 插件的完整配置模板（简体中文），基于官方文档翻译整理。
>
> 官方文档：<https://wiki.pixelstudios.dev/epicachievements>
>
> 该模板由正版ID为 **ZTF3** 的玩家制作。

## 目录结构

```
EpicAchievements Template/
├── README.md                    ← 本文件
├── General/                     ← 通用模板（参数速查、全字段列举）
│   ├── 成就配置.md              ← 成就完整配置模板
│   ├── 分类配置.md              ← 分类完整配置模板
│   ├── 任务类型参考.md          ← 35+ 种任务类型速查表
│   ├── 条件配置.md              ← 所有条件类型完整参考
│   ├── 奖励配置.md              ← 所有奖励类型完整参考
│   ├── 奖励等级系统.md          ← rewards.yml 等级系统配置
│   └── 占位符参考.md            ← 内部 & PAPI 占位符大全
└── Example/                     ← 实战示例（可直接复制使用的配置）
    ├── 成就/
    │   ├── 1. 基础挑战成就.md    ← 单等级挑战成就
    │   ├── 2. 分级成就.md        ← 多等级分级成就
    │   ├── 3. 隐藏成就.md        ← 秘密/彩蛋成就
    │   └── 4. 条件成就.md        ← 复杂条件组合成就
    ├── 分类/
    │   └── 1. 服务器分类配置.md  ← 多服务器分类方案
    ├── 任务/
    │   ├── 1. 基础任务类型.md    ← 常用内置任务类型
    │   ├── 2. 进度任务.md        ← Advancement 原版进度任务
    │   ├── 3. 命令任务.md        ← Command 命令触发任务
    │   └── 4. 占位符任务.md      ← Placeholder 占位符任务
    └── 奖励/
        └── 1. 奖励等级系统配置.md ← 奖励等级系统实战配置
```

## 模板说明

### General（通用模板）

提供每个配置类型的**完整参数速查**，适合在编写配置时查阅字段说明：
- 所有字段及其说明
- 必填/可选标记
- 默认值标注
- 示例值参考

### Example（实战示例）

提供**可直接复制使用的真实配置**，适合学习和参考：
- 设计思路说明
- 完整 YAML 配置
- 多个变体对比
- 关键概念总结表

## 相关链接

- [EpicAchievements 官方文档](https://wiki.pixelstudios.dev/epicachievements)
- [EpicAchievements SpigotMC](https://www.spigotmc.org/resources/116800/)
- [EpicAchievements Polymart](https://polymart.org/r/5931)
- [EpicAchievements BuiltByBit](https://builtbybit.com/resources/44823)
- [PlaceholderAPI](https://www.spigotmc.org/resources/6245/)
- [EpicAchievements UI 附加组件](https://polymart.org/resource/epicachievements-ui.6523)

## 许可

该文件夹内容和仓库中其他内容一样，统一采用 Apache License 2.0 协议开源。
