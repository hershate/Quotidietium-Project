# PlaceholderAPI

:::note
- `<required>` - 必需参数<br/>
- `[optional]` - 可选参数
:::

| 占位符                                                                                               | 描述                                                                                |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `%achievements_points_[category]_[challenge/tiered]%`                                                 | 玩家在该分类中的点数。                                                   |
| `%achievements_points_percentage_[category]_[challenge/tiered]%`                                      | 玩家在该分类中的点数百分比。                                        |
| `%achievements_points_total_[category]_[challenge/tiered]%`                                           | 分类中的可用总点数。                                                |
| `%achievements_unlocked_[category]_[challenge/tiered]%`                                               | 玩家已解锁的成就数量。                                       |
| `%achievements_unlocked_percentage_[category]_[challenge/tiered]%`                                    | 玩家已解锁的成就百分比。                                   |
| `%achievements_total_[category]_[challenge/tiered]%`                                                  | 分类中的成就总数。                                          |
| `%achievements_achievement_<id>_`<br/>`<points/requirement/progress/percentage/bar/unlocked>_[tier]%` | 关于特定成就的信息。<br/>未指定时，tier 默认为 `1`。 |
| `%achievements_tracked%`                                                                              | 玩家正在追踪的成就数量。                                       |
| `%achievements_unclaimed%`                                                                            | 未领取的奖励数量。                                                         |
