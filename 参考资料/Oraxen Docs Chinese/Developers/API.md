---
description: 如何将你的插件与 Oraxen 集成
cover: >-
  https://www.techyon.es/media/news/full-stack-developer-cu%C3%81les-son-las-principales-competencias_1637600851_21.jpg
coverY: 0
---

# API（接口）

## 将 Oraxen 添加到你的插件

### 仓库与依赖信息
你可以[在此处](https://github.com/oraxen/oraxen#api)找到仓库和依赖声明。


所有方法及其功能和参数的更详细说明可以在实际的类中找到。
只需在 IDE 中打开它们即可获取完整的方法列表。


## 使用示例

Oraxen 基于一个 ItemsBuilder 类构建，该类允许你轻松创建物品。当插件启动时，它会解析配置以为每种类型的物品生成构建器。每个构建器都可用于生成物品堆。

### [OraxenItems](https://github.com/oraxen/oraxen/blob/master/core/src/main/java/io/th0rgal/oraxen/api/OraxenItems.java) 类

#### 通过 OraxenID 获取 ItemBuilder

```java
OraxenItems.getItemById(itemID); // 其中 itemID 是物品配置中的一个节点
```

#### 检查 OraxenID 是否存在

```java
OraxenItems.isAnItem(itemID);
```

#### 从 ItemStack 中提取 OraxenID

你可以用它来检查一个 ItemStack 是否为 OraxenItem（如果 OraxenID 不存在则会返回 null）

```java
OraxenItems.getIdByItem(itemstack);
```

### 自定义方块与家具

#### 放置一个 OraxenBlock

在指定位置放置一个 OraxenBlock
```java
OraxenBlocks.place(itemID, location);
```

在指定位置放置一个 OraxenFurniture，可选择设置一个玩家用于旋转目的
```java
OraxenFurniture.place(itemID, location, @Nullable player);
```

#### 读取存储内容（1.209.0+）

如果你使用家具/音符盒存储机制，需要在不开 GUI 的情况下检查库存内容，可以使用 `StorageMechanic` 访问器：

```java
ItemStack[] entityContents = storageMechanic.getStorageContents(baseEntity);
ItemStack[] blockContents = storageMechanic.getStorageContents(block);
```

这些方法直接从当前打开的 GUI（如果已打开）或持久化存储数据中读取。

### 向资源包添加资源

#### 获取对 assets/ 文件夹的访问权限

```java
ResourcePack.getAssetsFolder();
```

### 机制（Mechanics）：

Oraxen 允许你向插件添加自己的机制，这比其余部分稍微复杂一些，因此有一个[专门的教程](mechanics#how-does-the-mechanic-system-work)。