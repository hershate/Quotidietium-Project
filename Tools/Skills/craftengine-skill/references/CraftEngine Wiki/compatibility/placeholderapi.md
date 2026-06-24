# 🅿️ 占位符

:::danger
请先查看[**注意事项**](../reference/text_format.md#注意事项)
:::

## %image_%

`image` 占位符用于根据给定的标识符返回对应图像的原始 Unicode 字符及其关联字体。

:::caution
`row` 和 `column` 都是可选的，但如果使用其中一个，就必须同时使用另一个。
:::

### %image_mm_<命名空间>:<路径>:[行]:[列]%

返回 `minimessage` 格式的图像。

![](/img/placeholderapi_1.png)

### %image_md_<命名空间>:<路径>:[行]:[列]%

返回 `minedown` 格式的图像。

![](/img/placeholderapi_2.png)

### %image_raw_<命名空间>:<路径>:[行]:[列]%

返回原始图像字符

![](/img/placeholderapi_3.png)

## %shift_%

`shift` 占位符用于获取**偏移字符**，常用于菜单标题对齐等操作。

### %shift_mm_<数值>%

返回 `minimessage` 格式的偏移字符  

### %shift_md_<数值>%

返回 `minedown` 格式的偏移字符  

### %shift_raw_<数值>%

返回原始偏移字符

:::tip

**如果你需要在其他插件中使用占位符显示图片，务必确保这些插件支持 MiniMessage 或 MineDown 格式，并能正确发送文本组件。**
(我之所以强调这一点，是因为有些设计不佳的插件会强制将富文本转换为旧版的颜色代码。)

另外，你也可以通过 CraftEngine 的数据包拦截功能来显示自定义图片。具体细节请参考[**此页面**](../configuration/image.md#与其他插件的兼容性)。

:::

## %checkceitem_%

`checkceitem` 占位符用于在其他菜单插件中检查玩家物品栏的 CraftEngine 物品。

### %checkceitem_count_<命名空间>:<路径>%

返回玩家物品栏中指定物品的数量。

### %checkceitem_has_<命名空间>:<路径>:[数量]%

返回玩家物品栏中是否有指定数量的物品。

### %checkceitem_id_[槽位]%

槽位可写不小于 0 的数字，或者 `main_hand` 和 `off_hand` 用于分别指定主手和副手槽位。 \
返回玩家物品栏中指定槽位物品的命名空间ID。

![](/img/placeholderapi_4.png)

### %checkceitem_iscustom_[槽位]%

槽位可写不小于 0 的数字，或者 `main_hand` 和 `off_hand` 用于分别指定主手和副手槽位。 \
返回玩家物品栏中指定槽位物品是否为自定义物品。

![](/img/placeholderapi_5.png)

:::tip

物品槽位数字 \
![](/img/items_slot_number.png)

:::
