# 自动连点器 — Auto Clicker

> 说明：
> 一个轻量级的鼠标自动连点工具，按下快捷键即可启动/停止自动点击。
>
> 基于 `pynput` 库实现，使用后台线程进行点击操作，不影响前台其他输入。

该脚本由正版ID为 **ZTF3** 的玩家编写与维护。

## 快捷键

| 按键 | 功能 |
|:----:|:----:|
| `F7` | 切换连点 开/关 |
| `Esc` | 退出程序 |

## 配置参数

| 参数 | 默认值 | 说明 |
|:----:|:------:|:----:|
| 点击间隔 | `0.01` 秒 | 每次点击之间的间隔时间 |
| 鼠标按键 | 左键 | 可改为左键/右键/中键 (left/right/middle) |
| 切换键 | `F7` | 启动/停止连点的快捷键 |
| 退出键 | `Esc` | 退出程序的快捷键 |

如需修改默认行为，可直接编辑脚本顶部的配置区：

```python
INTERVAL = 0.01                # 点击间隔（秒）
BUTTON = mouse.Button.left     # left / right / middle
TOGGLE_KEY = keyboard.Key.f7   # 切换连点
EXIT_KEY = keyboard.Key.esc    # 退出程序
```

## 使用前提

- Python 3.12
- 安装依赖：`pip install pynput`

## 使用方法

```bash
python auto-clicker.py
```

启动后控制台会显示当前配置。按下 `F7` 开始连点，再次按下 `F7` 停止。按下 `Esc` 退出程序。

该文件夹内容和仓库中其他内容一样，统一采用 Apache License 2.0 协议开源。
