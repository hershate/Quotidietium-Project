# 内部占位符

### v2.0

#### 通用占位符
> 这些占位符可用于任何菜单。

| 占位符 | 描述 |
|--------|------|
| `{player}` | 玩家名称 |
| `{uuid}` | 玩家的 UUID |
| `{points}` | 玩家的点数 |
| `{total_points}` | 所有成就的总点数 |
| `{points_percentage}` | 已获得点数的百分比 |
| `{unlocked_achievements}` | 已解锁成就的数量 |
| `{total_achievements}` | 成就的总数量 |
| `{unlocked_achievements_percentage}` | 已解锁成就的百分比 |
| `{unclaimed_rewards}` | 未领取奖励的数量 |

#### 分类占位符

| 占位符 | 描述 |
|--------|------|
| `{category_id}` | 分类的唯一标识符 |
| `{category_name}` | 分类的名称 |
| `{category_description}` | 分类的描述 |
| `{category_permission}` | 访问分类所需的权限 |
| `{category_achievements}` | 该分类中的成就数量 |
| `{category_servers}` | 可完成该分类成就的服务器 |

#### 成就占位符

| 占位符 | 描述 |
|--------|------|
| `{achievement_id}` | 成就的唯一标识符 |
| `{achievement_name}` | 成就的名称 |
| `{achievement_description}` | 成就的描述 |
| `{achievement_type}` | 成就的类型（challenge / tiered） |
| `{achievement_task}` | 成就的任务类型 |
| `{achievement_progress}` | 玩家在该成就中的进度 |
| `{achievement_progress_percentage}` | 该成就进度的百分比 |
| `{achievement_progress_bar}` | 显示当前进度的进度条 |
| `{achievement_permission}` | 在该成就中推进所需的权限 |
| `{achievement_requirements}` | 在该成就中推进所需的前置成就 |
| `{tier}` | 等级编号 |
| `{tier_roman}` | 罗马数字表示的等级编号 |
| `{tier_requirement}` | 完成该等级的要求 |
| `{tier_rewards}` | 奖励列表 |
| `{tier_progress_percentage}` | 该等级进度的百分比 |
| `{tier_progress_bar}` | 显示当前等级进度的进度条 |
| `{tier_unlock_percentage}` | 已解锁该等级的玩家百分比 |

#### 奖励等级占位符

| 占位符 | 描述 |
|--------|------|
| `{level}` | 等级编号 |
| `{points}` | 达到该等级所需的点数 |
| `{rewards}` | 奖励列表 |

#### 排序占位符

| 占位符 | 描述 |
|--------|------|
| `{sorting_type}` | 当前排序方式 |
| `{sorting_description}` | 当前排序方式的描述 |
| `{next_sorting_type}` | 下一个排序方式 |
| `{next_sorting_description}` | 下一个排序方式的描述 |
| `{completion_sorting_type}` | 完成度排序方式 |

### v1.0

#### 通用占位符
> 这些占位符可用于任何菜单。

| 占位符 | 描述 |
|--------|------|
| `{player}` | 玩家名称 |
| `{uuid}` | 玩家的 UUID |
| `{points}` | 玩家的点数 |
| `{total_points}` | 所有成就的总点数 |
| `{points_percentage}` | 已获得点数的百分比 |
| `{unlocked_achievements}` | 已解锁成就的数量 |
| `{total_achievements}` | 成就的总数量 |
| `{unlocked_achievements_percentage}` | 已解锁成就的百分比 |
| `{unclaimed_rewards}` | 未领取奖励的数量 |

#### 分类占位符

| 占位符 | 描述 |
|--------|------|
| `{category_id}` | 分类的唯一标识符 |
| `{category_name}` | 分类的名称 |
| `{category_description}` | 分类的描述 |
| `{category_permission}` | 访问分类所需的权限 |
| `{category_achievements}` | 该分类中的成就数量 |
| `{category_item}` | 主菜单中显示物品的材质 |
| `{category_item_slot}` | 主菜单中显示物品的 slot 位置 |
| `{category_servers}` | 可完成该分类成就的服务器 |

#### 成就占位符

| 占位符 | 描述 |
|--------|------|
| `{achievement_id}` | 成就的唯一标识符 |
| `{achievement_name}` | 成就的名称 |
| `{achievement_description}` | 成就的描述 |
| `{achievement_type}` | 成就的类型（challenge / tiered） |
| `{achievement_type_name}` | 成就类型的名称 |
| `{achievement_task}` | 成就的任务类型 |
| `{achievement_progress}` | 玩家在该成就中的进度 |
| `{achievement_progress_percentage}` | 该成就进度的百分比 |
| `{achievement_progress_bar}` | 显示当前进度的进度条 |
| `{achievement_permission}` | 在该成就中推进所需的权限 |
| `{achievement_required_achievements}` | 在该成就中推进所需的前置成就 |
| `{tier}` | 等级编号 |
| `{tier_roman}` | 罗马数字表示的等级编号 |
| `{tier_requirement}` | 完成该等级的要求 |
| `{tier_points}` | 完成该等级时获得的点数 |
| `{tier_rewards}` | 奖励列表 |
| `{tier_progress_percentage}` | 该等级进度的百分比 |
| `{tier_progress_bar}` | 显示当前等级进度的进度条 |

#### 奖励等级占位符

| 占位符 | 描述 |
|--------|------|
| `{level}` | 等级编号 |
| `{points}` | 达到该等级所需的点数 |
| `{status}` | 该等级的状态 |
| `{rewards}` | 奖励列表 |

#### 排序占位符

| 占位符 | 描述 |
|--------|------|
| `{sorting_type}` | 当前排序方式 |
| `{sorting_description}` | 当前排序方式的描述 |
| `{next_sorting_type}` | 下一个排序方式 |
| `{next_sorting_description}` | 下一个排序方式的描述 |
| `{completion_sorting_type}` | 完成度排序方式 |
