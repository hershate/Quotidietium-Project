---
description: 也称为"如何给 Oraxen 增强能力？"
cover: >-
  https://www.veracode.com/sites/default/files/2020-12/developers-hero-developer-center_0.jpg
coverY: 0
---

# 自定义机制

## 机制系统是如何工作的？

### 什么是机制？

机制是一种自定义物品属性。同一属性可以在不同物品上有不同的变体。例如，耐久度属性允许你为物品定义自定义耐久度，但并非所有拥有耐久度机制的物品都具有相同的耐久度。


耐久度机制的工作原理是将物品的耐久度存储在其元数据中，并使用原版的耐久度条来显示其自定义耐久度，而非其原版耐久度。


### 那么如果每个物品的机制都不同，我是否每次都需要重写不同的耐久度机制？

不需要，那样太繁琐了。相反，Oraxen 提供了一个 MechanicFactory 系统。基本上，你将需要创建一个可配置的 Mechanics 类，以及一个 MechanicFactory 类来配置你的 Mechanic 类的所有不同版本。它还将管理所有这些版本的通用代码。

### 好的，但我想修改实现了我机制的那些物品以在其中存储数据，这可以做到吗？

当然可以，为此 Oraxen 允许你为每个机制关联一个 ItemModifier 列表。一个 ItemModifier 就是 `Function<ItemBuilder, ItemBuilder>`，它本质上是一小段代码，包含当服务器通过其配置生成物品时对该物品所做的更改。例如，对于耐久度机制，我使用了一个 itemModifier，它将用户选择的耐久度存储在该物品的元数据中。

```java
item -> item.setCustomTag(NAMESPACED_KEY, PersistentDataType.INTEGER, section.getInt("value"))
```

## 让我们创建我们的第一个机制


在本教程中，我将以耐久度机制为例（因为它非常容易理解），但你可以按照本教程创建你想要的任何机制。


### 第一步：创建我们的机制类

首先创建一个继承自 Mechanic 的类，如果你使用 [intelliJ](https://www.jetbrains.com/idea/)，你应该会得到类似这样的代码：

```java
class DurabilityMechanic extends Mechanic {

    public DurabilityMechanic(MechanicFactory mechanicFactory, 
                    ConfigurationSection section,
                    Function<ItemBuilder, ItemBuilder>... modifiers) {
        super(mechanicFactory, section, modifiers);
    }

}
```

Mechanic 构造函数接受三个参数：

```
- 创建该 Mechanic 的工厂实例
- 用于配置该 Mechanic 的配置节
- 物品修改器
```

我希望我的机制的每个变体都有不同的耐久度，因此我将读取机制的配置并存储 value 字段的值。

#### 机制配置节的结构如下：

```java
class DurabilityMechanic extends Mechanic {

    private int itemDurability;

    public DurabilityMechanic(MechanicFactory mechanicFactory, 
                              ConfigurationSection section) {
        /* 我们提供：
        - 创建该机制的工厂实例
        - 用于配置该机制的配置节
        - 物品修改器
         */
        super(mechanicFactory, section, item ->
                item.setCustomTag(NAMESPACED_KEY,
                        PersistentDataType.INTEGER, section.getInt("value")));
        this.itemDurability = section.getInt("value");
    }

    public int getItemMaxDurability() {
        return itemDurability;
    }
}
```

所以现在我们有了一个 DurabilityMechanic 类，它能够适配任何物品，并且会调用我们的 DurabilityModifier 类来告诉 Oraxen 在创建物品之前需要做哪些修改（这里我们只是在物品中添加了一个包含所需新耐久度的数据）。

### 第二步：创建我们的机制工厂类

和之前一样，使用你的 IDE 功能自动创建一个继承自 MechanicFactory 的类：

```java
class DurabilityMechanicFactory extends MechanicFactory {

    public DurabilityMechanicFactory(ConfigurationSection section) {
        super(section);
    }

    @Override
    public Mechanic parse(ConfigurationSection itemMechanicConfiguration) {
        return null;
    }
}
```

我们重写 parse 方法来创建一个新的 Mechanic（通过之前创建的 DurabilityMechanic 类）。我们还想通过 `addToImplemented` 方法告诉 Oraxen 该机制已成功实现并可以被加载。因此我们的类现在看起来是这样的：

```java
public class DurabilityMechanicFactory extends MechanicFactory {

    public DurabilityMechanicFactory(ConfigurationSection section) {
        super(section);
    }

    @Override
    public Mechanic parse(ConfigurationSection itemMechanicConfiguration) {
        Mechanic mechanic = new DurabilityMechanic(this, itemMechanicConfiguration);
        addToImplemented(mechanic);
        return mechanic;
    }

}
```

### 第三步：添加我们的功能（事件）

在我的例子中，我只需要使用一个事件来处理耐久度，我将创建一个 DurabilityMechanicsManager 类
来实现 Listener 接口，以保持代码整洁，不过我也可以直接在 DurabilityMechanicFactory 中完成。
我在工厂构建时告诉 Bukkit 哪个类管理事件：

```java
public class DurabilityMechanicFactory extends MechanicFactory {

    public DurabilityMechanicFactory(String mechanicId) {
        super(mechanicId);
        MechanicsManager.registerListeners(OraxenPlugin.get(),
                new DurabilityMechanicsManager(this));
    }

    @Override
    public Mechanic parse(ConfigurationSection itemMechanicConfiguration) {
        Mechanic mechanic = new DurabilityMechanic(this, itemMechanicConfiguration);
        addToImplemented(mechanic);
        return mechanic;
    }

}
```

为了根据插件管理的实际耐久度来计算物品上显示的耐久度，我使用一些简单的数学公式：

$$
bukkitDamage = bukkitMaxDurability - \frac{realDurability*bukkitMaxDurability}{realMaxDurability}
$$

所以这是我的 DurabilityMechanicsManager 类：

```java
class DurabilityMechanicsManager implements Listener {

    private DurabilityMechanicFactory factory;

    public DurabilityMechanicsManager(DurabilityMechanicFactory factory) {
        this.factory = factory;
    }

    @EventHandler(priority = EventPriority.HIGH, ignoreCancelled = true)
    private void onItemDamaged(PlayerItemDamageEvent event) {
        ItemStack item = event.getItem();
        String itemID = OraxenItems.getIdByItem(item);
        if (factory.isNotImplementedIn(itemID))
            return;

        DurabilityMechanic durabilityMechanic = 
                (DurabilityMechanic) factory.getMechanic(itemID);

        ItemMeta itemMeta = item.getItemMeta();
        PersistentDataContainer persistentDataContainer = 
                itemMeta.getPersistentDataContainer();
        int realDurabilityLeft = persistentDataContainer
                .get(DurabilityMechanic.NAMESPACED_KEY, PersistentDataType.INTEGER) 
                        - event.getDamage();

        if (realDurabilityLeft > 0) {
            double realMaxDurability = 
                    //因为整数取整的值很糟糕
                    durabilityMechanic.getItemMaxDurability();
            persistentDataContainer.set(DurabilityMechanic.NAMESPACED_KEY,
                    PersistentDataType.INTEGER, realDurabilityLeft);
            ((Damageable) itemMeta).setDamage((int) (item.getType()
                    .getMaxDurability() - realDurabilityLeft 
                    / realMaxDurability * item.getType().getMaxDurability()));
            item.setItemMeta(itemMeta);
        } else {
            item.setAmount(0);
        }

    }

}
```

### 最后一步：注册我们的机制

最后我们需要注册我们的 MechanicFactory 并重新加载物品以将新机制应用到它们上面。
建议在 `OraxenNativeMechanicsRegisteredEvent` 的 EventListener 中注册它，因为 `/oraxen reload all` 会清空此注册表。
为此我们需要在插件的 onEnable 方法中添加以下几行：

```java
Bukkit.getPluginManager().registerEvents(new Listener() {
    @EventHandler
    public void onMechanicRegister(OraxenNativeMechanicsRegisteredEvent event) {
        MechanicsManager.registerMechanicFactory("durability", DurabilityMechanicFactory::new, true);
        OraxenItems.loadItems();
    }
}, this);
```

## 总结

要正确创建一个新机制，建议将其代码分为三个部分：

* 一个继承自 [MechanicFactory](https://github.com/Th0rgal/Oraxen/blob/master/src/main/java/io/th0rgal/oraxen/items/mechanics/MechanicFactory.java) 的工厂
* 一个继承自 [Mechanic](https://github.com/Th0rgal/Oraxen/blob/master/src/main/java/io/th0rgal/oraxen/items/mechanics/Mechanic.java) 的机制
* 你自己的功能放在一个 \<YourMechanicName>MechanicsManager 类中（也是可选的）


同时，你可以通过 ItemModifier 使用你的机制来修改物品：

```java
item -> item.setCustomTag(NAMESPACED_KEY,
                        PersistentDataType.INTEGER, section.getInt("value"))
```

你也可以以类似的方式修改资源包：

```java
ResourcePack.addModifiers(packFolder -> {/* 你的修改 */});
```


最后注册你的机制！

为总结本教程，[这里提供了耐久度机制的完整源代码](https://github.com/Th0rgal/Oraxen/blob/master/src/main/java/io/th0rgal/oraxen/items/mechanics/provided/durability/DurabilityMechanicFactory.java)。