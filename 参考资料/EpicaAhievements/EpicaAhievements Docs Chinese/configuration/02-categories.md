# 分类

成就是按分类组织的。<br/>
分类对于将属于同一服务器/游戏模式的成就分组尤其有用。

:::info
服务器 ID 在 `config.yml` 文件中定义：
```yaml title="config.yml"
# 服务器的标识符
server: survival
:::
  
## 必需字段
### `name`
分类的名称。
```yaml
name: "Global"
```

### `description`
分类的描述。
```yaml
description:
  - "&7Achievements that can be completed"
  - "&7across all servers."
```

### `servers`
启用该分类的服务器列表。<br/>
**使用 `ALL` 可在所有服务器上启用。**
```yaml
servers:
  - ALL
```

### `item`
在主菜单中为该分类显示的物品。
- `material`：物品的材质。
- `slot`：菜单中显示该物品的槽位。
```yaml
item:
  material: COMPASS
  slot: 12
```

## 可选字段
### `permission`
访问该分类所需的权限。<br/>
**默认值：** `None`
```yaml
permission: "achievements.global"
```
  
## 配置示例

```yaml title="categories.yml" showLineNumbers=true
# 唯一的分类标识符
survival:
  name: "Survival"
  description:
    - "&7Mine, craft and explore!"
  servers:
    - survival
  item:
    material: DIAMOND_PICKAXE
    slot: 12
```
