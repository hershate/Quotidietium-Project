# 资源包合并指南

Oraxen 提供了一个强大的系统，将多个资源包合并为一个统一的资源包。您可以使用两种方法合并资源包。**ZIP 文件上传**或**直接文件夹结构**。两种方法都会在资源包生成过程中自动处理。



## 概述

当 Oraxen 生成资源包时，它会按特定顺序合并来自多个来源的文件。

1. **默认 Oraxen 资源**（内置纹理、模型、字体等）
2. **直接文件夹结构**（`Oraxen/pack/assets/`、`Oraxen/pack/textures/` 等）
3. **上传的 ZIP 资源包**（`Oraxen/pack/uploads/`）

这使您可以：
- 添加自定义纹理和模型
- 覆盖默认行为
- 组合多个社区资源包
- 轻松管理优先级



## ZIP 上传系统

### 快速开始

1. 将您的资源包 ZIP 文件放入 **`Oraxen/pack/uploads/`**
2. 重载或重启服务器
3. 文件会自动合并到最终资源包中

### 目录结构

```
plugins/Oraxen/
├── pack/
│   ├── uploads/
│   │   ├── 01_base_textures.zip      ← 最先处理
│   │   ├── 02_custom_models.zip      ← 第二个处理
│   │   └── 99_overlay_pack.zip       ← 最后处理（最高优先级）
│   ├── assets/
│   ├── textures/
│   ├── models/
│   ├── sounds/
│   └── pack.zip                       ← 最终合并的资源包
```

### 优先级系统

ZIP 文件按**文件名字母顺序**处理。发生冲突时，最后处理的文件胜出。

**示例**
```
uploads/
├── 0_base_pack.zip          （包含: texture.png, model.json）
├── 1_custom_pack.zip        （包含: texture.png, new_item.json）
└── 2_override_pack.zip      （包含: texture.png）
```

**处理顺序和结果**

1. `0_base_pack.zip` → 添加 texture.png
2. `1_custom_pack.zip` → texture.png **覆盖** v1，添加 new_item.json
3. `2_override_pack.zip` → texture.png **覆盖** v2

**最终资源包包含**
- `texture.png` 来自 `2_override_pack.zip`
- `model.json` 来自 `0_base_pack.zip`
- `new_item.json` 来自 `1_custom_pack.zip`

### 控制台输出

#### 正常合并（无冲突）
```
[14:32:35 INFO] Oraxen | 正在处理资源包 | base_textures.zip
[14:32:35 INFO] Oraxen | 从 base_textures.zip 添加了 45 个文件
```

#### 有文件覆盖
```
[14:32:36 INFO] Oraxen | 正在处理资源包 | custom_overlay.zip
[14:32:36 WARN] Oraxen | custom_overlay.zip 将覆盖 base_textures.zip 中的现有文件 assets/minecraft/textures/gui/window.png
[14:32:36 INFO] Oraxen | 从 custom_overlay.zip 添加了 12 个新文件，8 个覆盖
```

#### 最终摘要
```
[14:32:37 INFO] Oraxen | 从 3 个上传的资源包中合并了 156 个文件
```



## 直接文件夹结构

### 快速开始

1. 将您的资源包文件直接放入 **`Oraxen/pack/assets/`** 或 **`Oraxen/pack/`** 文件夹中
2. 重载或重启服务器
3. 文件会自动合并到最终资源包中

### 优点（相比 ZIP 上传）
- 持久化的自定义内容
- 方便开发和迭代
- 避免重复上传

### 目录结构

```
plugins/Oraxen/
└── pack/
    ├── assets/                    ← 直接的资源包文件
    │   ├── minecraft/
    │   │   ├── textures/
    │   │   ├── models/
    │   │   ├── lang/
    │   │   └── sounds/
    │   └── [custom_namespace]/
    ├── textures/                  ← 替代：平级结构
    ├── models/
    ├── sounds/
    ├── lang/
    ├── pack.mcmeta
    ├── pack.png
    └── uploads/                   ← ZIP 文件放这里
```

### 优先级系统

直接文件夹文件会覆盖默认值，但可以被上传的 ZIP 覆盖。同一来源中的文件按文件夹结构顺序处理。

**示例**
```
默认（Minecraft）
├── assets/minecraft/textures/block/dirt.png
├── assets/minecraft/models/block/stone.json
└── assets/minecraft/textures/item/sword.png

直接文件夹（pack/）
├── assets/minecraft/textures/block/dirt.png        ← 不同版本
└── assets/minecraft/textures/item/axe.png          ← 新文件

上传的 ZIP（pack/uploads/）
├── 01_base_pack.zip       （包含: sword.png）
└── 02_override_pack.zip   （包含: dirt.png）
```

**处理顺序和结果**

1. Oraxen 默认 → 加载 dirt.png、stone.json、sword.png
2. 直接文件夹 → dirt.png **覆盖**默认版本，添加 axe.png
3. `01_base_pack.zip` → sword.png **覆盖**默认版本
4. `02_override_pack.zip` → dirt.png **覆盖**直接文件夹版本

**最终资源包包含**
- `dirt.png` 来自 `02_override_pack.zip`
- `stone.json` 来自 Oraxen 默认
- `sword.png` 来自 `01_base_pack.zip`
- `axe.png` 来自直接文件夹

## 优先级

```
1. Oraxen 默认资源
   ↓ （可被以下覆盖）
2. pack/assets/              （直接文件夹）
   pack/textures/            （替代结构）
   pack/models/
   pack/sounds/
   等等。
   ↓ （可被以下覆盖）
3. pack/uploads/01_*.zip     （按字母顺序排第一）
   pack/uploads/02_*.zip
   ...
   pack/uploads/99_*.zip     （按字母顺序排最后 = 最高优先级）
```

### 冲突如何解决

当相同文件路径出现在多个来源中时：
- **直接文件夹覆盖默认值**
- **ZIP 资源包覆盖直接文件夹**
- **较后的 ZIP 文件（按字母顺序）覆盖较早的文件**

**示例**

- `Oraxen/pack/assets/minecraft/textures/block/dirt.png`（直接文件夹）
- `Oraxen/pack/uploads/custom_pack.zip`（包含 `assets/minecraft/textures/block/dirt.png`）

**结果 |** 使用 `custom_pack.zip` 中的文件（ZIP 具有更高优先级）