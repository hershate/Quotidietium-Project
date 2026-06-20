# 基于纹饰的盔甲 (1.20-1.21.1)

如果使用 trims 作为自定义盔甲类型，大多数事情都会为你自动处理。
与核心着色器方法不同，纹饰不仅限于使用 LEATHER 材质。

默认情况下，Oraxen 设置为使用 CHAINMAIL，但这可以在 `settings.yml` 中更改。
然后 Oraxen 会根据你配置的自定义盔甲生成一个数据包。
由于需要数据包，每次添加或移除盔甲套装时，服务器都需要完全重启一次。


将 `CustomArmor.armor_type` 更改为 `TRIMS` 后，你需要：
1. 启动服务器以让数据包生成
2. 停止服务器
3. 再次启动服务器以启用之前生成的数据包
   

### 如何配置你的盔甲？


确保你的 OraxenItem 的 itemID 遵循 `armorname_armortype` 的模式。
对于上述套装中的其余部分，应为 `ruby_chestplate`、`ruby_leggings` 和 `ruby_boots`。

确保你的盔甲层文件遵循 **armorname**_armor_layer_1/2.png 的格式。
在下面的例子中，我们需要 **ruby**_armor_layer_1.png 和 **ruby**_armor_layer_2.png


只需设置材质并指定两次纹理图标：
```yaml
ruby_helmet:
  displayname: "<gradient:#FA7CBB:#F14658>Ruby Helmet"
  material: CHAINMAIL_HELMET
  Pack:
    generate_model: true
    parent_model: "item/generated"
    textures:
      - default/armors/ruby_helmet
      - default/armors/ruby_helmet
```

要使盔甲正确显示，还需要一个纹饰图案 (trim-pattern)。
如果未手动指定，Oraxen 将自动分配它。
如果需要，你也可以选择手动分配 `trim_pattern`。
值应为 `oraxen:armorname`，在我们的例子中：
```yaml
ruby_helmet:
  trim_pattern: oraxen:ruby
```
