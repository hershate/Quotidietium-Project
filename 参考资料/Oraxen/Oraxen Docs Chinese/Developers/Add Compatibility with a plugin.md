---
description: 直接从 Oraxen 源代码中使 Oraxen 与其他插件兼容
cover: https://i.insider.com/61dc71461025b20018bb0597?width=700
coverY: 0
---

# 创建你自己的兼容性

## 它是如何工作的？

### 第一步：创建一个兼容性类

你需要创建一个继承自以下类的类：

```
CompatibilityProvider<你要添加支持的插件的主类>
```

并将添加对该插件支持的代码放入你创建的类中。

### 第二步：将兼容性类添加到 Oraxen

使用

```
CompatibilitiesManager.addCompatibility(你要添加支持的插件的名称, 你在第一步中创建的类)
```

将该类添加到 Oraxen。

## 示例

&#x20;我将以 MythicMobs 为例进行演示。


### 第一步：创建一个兼容性类

```
import io.lumine.xikage.mythicmobs.MythicMobs;
import io.lumine.xikage.mythicmobs.api.bukkit.events.MythicDropLoadEvent;
import io.th0rgal.oraxen.compatibilities.CompatibilityProvider;

public class MythicMobsCompatibility extends CompatibilityProvider<MythicMobs>{

    @EventHandler
    public void onMythicDropLoadEvent(MythicDropLoadEvent event) {
    
    }
    
}
```

### 第二步：将兼容性类添加到 Oraxen

```
import io.th0rgal.oraxen.compatibilities.CompatibilitiesManager;
import org.bukkit.plugin.java.JavaPlugin;

public class OraxenMythicMobsCompatibilityPlugin extends JavaPlugin {

    public void onEnable() {
        CompatibilitiesManager.addCompatibility("MythicMobs", MythicMobsCompatibility.class)
    }

}

```