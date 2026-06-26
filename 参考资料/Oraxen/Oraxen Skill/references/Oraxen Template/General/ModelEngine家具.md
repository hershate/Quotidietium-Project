# ModelEngine 家具配置模板

> ModelEngine 是一个独立的 Minecraft 插件，允许创建带骨骼动画的自定义实体模型。
> Oraxen 可以直接将 ModelEngine 模型作为家具使用，无需额外配置实体。

---

## 一、前置要求

1. **ModelEngine 插件**已安装（推荐 R3 或以上版本）
2. **BlockBench** 用于创建 .bbmodel 文件
3. ModelEngine 资源包已正确配置在 `plugins/ModelEngine/resource pack/` 中
4. **资源包合并**: 将 ModelEngine 的 `assets` 文件夹复制到 `Oraxen/pack/` 中

---

## 二、资源包合并步骤

```
1. 打开 ModelEngine 文件夹: plugins/ModelEngine/
   └── resource pack/
       └── assets/              ← 复制整个 assets 文件夹

2. 将 assets 粘贴到 Oraxen 目录:
   Oraxen/
   └── pack/
       └── assets/              ← 放在这里（合并，不覆盖同名文件）

3. Oraxen 打包时会将两边的资源合并到同一个资源包中
```

> **注意:** 复制整个 `assets` 文件夹，而不是其内容。如果 Oraxen `pack/` 中已有 `assets` 文件夹，合并时注意不要覆盖现有文件。

---

## 三、基础配置

### 3.1 最简 ModelEngine 家具

```yaml
# ============================================================
# 示例: 最简单的 ModelEngine 家具
# ============================================================
my_me_furniture:
  displayname: "<yellow>ModelEngine 家具</yellow>"
  material: PAPER                    # 物品栏材质

  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      barrier: true

      # ------------------------------------------------------
      # modelengine_id: ModelEngine 模型的名称
      # 对应 plugins/ModelEngine/resource pack/assets/<namespace>/models/
      # 中 .bbmodel 文件的名称（不含扩展名）
      # ------------------------------------------------------
      modelengine_id: my_model       # 你的 .bbmodel 文件名（不含 .bbmodel）
```

### 3.2 带完整配置的 ModelEngine 家具

```yaml
# ============================================================
# 示例: 完整的 ModelEngine 家具配置
# ============================================================
animated_statue:
  displayname: "<gold>动画雕像</gold>"
  material: PAPER

  Pack:
    generate_model: false
    model: default/animated_statue    # Oraxen 备用模型（Item Display 显示）

  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      barrier: true
      modelengine_id: animated_statue # ← ModelEngine 模型文件名
      rotatable: true                 # 可旋转
      hardness: 5                     # 硬度
      light: 2                        # 发光

      drop:
        silktouch: false
        loots:
          - { oraxen_item: animated_statue, probability: 1.0 }

      block_sounds:
        place_sound: block.stone.place
        break_sound: block.stone.break
        hit_sound: block.stone.hit
        step_sound: block.stone.step
        fall_sound: block.stone.fall
```

---

## 四、BlockBench 模型准备

### 4.1 模型创建步骤

1. **打开 BlockBench**，选择 `Generic Model` 格式
2. 使用 ModelEngine 插件创建项目（需要安装 BlockBench ModelEngine 插件）
3. 创建你的 3D 模型（立方体、骨骼、动画）
4. **导出为 .bbmodel 格式**
5. 将 .bbmodel 文件放入 ModelEngine 的模型目录：
   ```
   plugins/ModelEngine/resource pack/assets/minecraft/models/<你的模型名>.bbmodel
   ```

### 4.2 ModelEngine 目录结构

```
plugins/ModelEngine/
├── models/                         # .bbmodel 文件存放位置
│   └── my_furniture.bbmodel
├── resource pack/
│   └── assets/
│       └── minecraft/
│           ├── models/
│           │   └── my_furniture.bbmodel
│           └── textures/
│               └── my_furniture.png
└── config.yml
```

> **注意:** 对于家具使用，`.bbmodel` 文件需要同时存在于 `models/` 和 `resource pack/assets/minecraft/models/` 中。

---

## 五、modelengine_id 引用说明

```yaml
# modelengine_id 引用的是 .bbmodel 文件名（不含扩展名）
# 例如你的模型文件是:
#   plugins/ModelEngine/resource pack/assets/minecraft/models/my_chair.bbmodel
# 则配置:
modelengine_id: my_chair

# 如果使用了命名空间:
#   .../assets/my_namespace/models/my_chair.bbmodel
# 则配置:
modelengine_id: my_namespace:my_chair
```

---

## 六、Oraxen 家具与 ModelEngine 的交互

### 6.1 模型显示优先级

```
1. modelengine_id 存在 → 使用 ModelEngine 模型（包含动画）
2. modelengine_id 不存在 → 回退到 Pack.model 的 Oraxen 模型
```

### 6.2 可以同时存在的配置

```yaml
# ModelEngine 家具可以同时拥有 Oraxen 的所有家具功能
multi_feature_furniture:
  displayname: "<rainbow>多功能家具</rainbow>"
  material: PAPER

  Pack:
    generate_model: false
    model: default/multi_fallback         # 无 ModelEngine 时的备用模型

  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      barrier: true
      modelengine_id: my_animated_model   # ModelEngine 动画模型

      # ---- 以下为 Oraxen 通用家具功能（全部可用）----
      seat:
        height: -0.3                      # 可坐
      light: 8                            # 发光
      rotatable: true                     # 可旋转
      hardness: 10                        # 硬度
      drop:
        silktouch: true
        loots:
          - { oraxen_item: multi_feature_furniture, probability: 1.0 }
      storage:                            # 存储功能
        type: STORAGE
        rows: 3
        title: "<red>多功能容器</red>"
      jukebox:                            # 唱片机功能
        active_model: opened              # 但 active_model 切换的是 Pack.models
        volume: 1.0
      block_sounds:
        place_sound: block.metal.place
        break_sound: block.metal.break
```

> **重要说明:** `jukebox.active_model` 切换的是 `Pack.models` 中的 Oraxen 模型，**不是** ModelEngine 模型。ModelEngine 的动画由其自身的动画控制器驱动。

---

## 七、常见问题与故障排除

### 7.1 家具不可见（不渲染）

**可能原因:**
1. ModelEngine 资源包未合并到 Oraxen `pack/` 中
2. `.bbmodel` 文件路径不正确
3. 资源包未重新加载（执行 `/oraxen reload pack` 后客户端需重新加载资源包）

**解决步骤:**
```
1. 确认 plugins/ModelEngine/resource pack/assets/ 存在
2. 确认 assets 已复制到 Oraxen/pack/
3. 运行 /oraxen reload pack
4. 客户端 F3+T 重新加载资源包
```

### 7.2 模型显示但没有动画

**可能原因:**
1. ModelEngine 不提供动画控制器给家具
2. `modelengine_id` 指向的模型没有定义动画

**建议:** 对于需要动画的家具，考虑使用 ModelEngine 的自定义生物（Custom Mob）而非家具。

### 7.3 材质/纹理缺失

- 确认纹理文件在正确的资源包路径中
- 确认 BlockBench 中的纹理路径与资源包中的实际路径一致
- 重新导出 .bbmodel 文件

### 7.4 性能注意事项

- ModelEngine 模型比普通 Oraxen 展示实体消耗更多资源（骨骼计算、动画更新）
- 不要在一个区域放置大量 ModelEngine 家具（建议 < 20 个/视距）
- 对于无动画的静态家具，建议直接使用 Oraxen 展示实体而非 ModelEngine

---

## 八、Material 选择注意事项

ModelEngine 通常使用 `LEATHER_HORSE_ARMOR` 作为实体材质。但对于家具用途，Oraxen 使用展示实体渲染，因此：

| 场景 | 推荐 material |
|------|--------------|
| ModelEngine 家具 (Oraxen) | `PAPER` 或任意物品材质 |
| ModelEngine 自定义生物 | `LEATHER_HORSE_ARMOR` |
| 仅做物品栏图标 | 任意材质均可 |

> 对于 Oraxen 家具，`material` 仅影响物品栏中的图标外观，放置后由 ModelEngine 模型覆盖。

---

## 九、完整配置模板

```yaml
# ============================================================
# ModelEngine 家具完整模板
# 复制此模板，修改标记为 [必改] 的部分即可使用
# ============================================================
your_me_furniture:                        # [必改] 唯一物品 ID
  displayname: "<white>你的 ModelEngine 家具</white>"  # [必改] 显示名称
  material: PAPER                         # 物品栏材质

  Pack:
    generate_model: false
    model: default/your_fallback_model    # [推荐] 无 ModelEngine 时的备用模型

  Mechanics:
    furniture:
      type: DISPLAY_ENTITY
      barrier: true

      # ---- ModelEngine 核心配置 ----
      modelengine_id: your_model_name     # [必改] .bbmodel 文件名

      # ---- 以下为可选功能，按需启用 ----
      rotatable: false                    # [可选] 是否可旋转
      restricted_rotation: STRICT         # [可选] 限制旋转方向
      hardness: 1                         # [可选] 破坏硬度
      light: 0                            # [可选] 发光等级 (0-15)

      # [可选] 座位
      # seat:
      #   height: -0.3

      # [可选] 存储
      # storage:
      #   type: STORAGE
      #   rows: 6
      #   title: "<red>容器</red>"

      # [可选] 掉落
      drop:
        silktouch: false
        loots:
          - { oraxen_item: your_me_furniture, probability: 1.0 }

      # [可选] 音效
      block_sounds:
        place_sound: block.stone.place
        break_sound: block.stone.break
        hit_sound: block.stone.hit
        step_sound: block.stone.step
        fall_sound: block.stone.fall
```

---

## 十、BlockBench 建模要点

| 要点 | 说明 |
|------|------|
| 格式 | General Model，导出为 `.bbmodel` |
| 骨骼 | 可选，用于动画。静态家具不需要骨骼 |
| UV | 标准 Box UV 或 Per-face UV 均可 |
| 纹理尺寸 | 推荐 16x16 的倍数（如 64x64, 128x128） |
| 旋转点 | 模型原点(Pivot)位于方块底部中心 |
| 动画 | 在 BlockBench 的 Animate 模式中创建，导出时包含在 .bbmodel 中 |

---

## 十一、与普通展示实体家具的对比

| 特性 | ModelEngine 家具 | 展示实体家具 |
|------|-----------------|-------------|
| 模型格式 | `.bbmodel` | `.json` (Oraxen 生成或自定义) |
| 骨骼动画 | 支持 | 不支持 |
| 性能 | 较消耗资源 | 轻量 |
| 设置复杂度 | 较高（需安装 ModelEngine） | 低（仅 Oraxen 即可） |
| 适用场景 | 动画雕像、复杂机械 | 静态桌椅、装饰品 |
| 纹理要求 | ModelEngine 纹理路径 | Oraxen 纹理路径 |

> **建议:** 如果家具不需要动画，请使用普通的展示实体家具（参考 `基础家具.md`）以获得更好的性能。
