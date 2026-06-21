---
sidebar_position: 3
---

# 命令与权限

:::note
- `<required>` - 必需参数<br/>
- `[optional]` - 可选参数
  :::

### 玩家命令

- `/achievements` <br/>
  打开主成就菜单。

- `/achievements menu [category] [type]` <br/>
  打开指定的成就菜单。 <br/>

- `/achievements rewards` <br/>
  打开奖励界面。

- `/achievements tracker` <br/>
  打开追踪器界面。

- `/achievements search [query]` <br/>
  搜索与查询匹配的成就。

- `/achievements help` <br/>
  显示帮助信息。

### 管理命令

- `/achievements open <player> [category] [type]` <br/>
  为指定玩家打开指定的成就菜单。

- `/achievements progress <player> <achievement> <set/add/remove> <amount>` <br/>
  设置玩家某项成就的进度。

- `/achievements unlock <player> <achievement> [tier]` <br/>
  为玩家解锁一项成就。

- `/achievements reset <player> [achievement/category/rewards] [id]` <br/>
  重置玩家某项成就的进度。

- `/achievements reload` <br/>
  重新加载插件的配置文件。

### 权限

- `achievements.admin` <br/>
  使用管理命令所需的权限。

- `achievements.track` <br/>
  追踪成就所需的权限。
