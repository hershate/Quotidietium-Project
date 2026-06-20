"""
🎯 自动连点器 — Auto Clicker

快捷键：
  F7    切换连点开/关
  Esc   退出程序

依赖：
  pip install pynput
"""

import time
import threading
from pynput import mouse, keyboard

# ============ 配置 ============
INTERVAL = 0.01                # 点击间隔（秒）
BUTTON = mouse.Button.left     # left / right / middle
TOGGLE_KEY = keyboard.Key.f7   # 切换连点
EXIT_KEY = keyboard.Key.esc    # 退出程序
# =============================

clicking = False
running = True

def click_loop():
    """后台点击线程"""
    global clicking
    mouse_ctrl = mouse.Controller()
    while running:
        if clicking:
            mouse_ctrl.click(BUTTON)
        time.sleep(INTERVAL)

def on_press(key):
    global clicking, running

    if key == TOGGLE_KEY:
        clicking = not clicking
        status = "▶️ 开始" if clicking else "⏹ 停止"
        print(f"  {status}连点 (间隔 {INTERVAL}s)")

    elif key == EXIT_KEY:
        print("  退出连点器")
        running = False
        return False

def main():
    print("=" * 40)
    print("  🎯 自动连点器")
    print(f"  间隔: {INTERVAL}s | 按键: {BUTTON.name}")
    print(f"  {TOGGLE_KEY.name}  切换连点")
    print(f"  {EXIT_KEY.name}  退出程序")
    print("=" * 40)

    # 启动后台点击线程
    t = threading.Thread(target=click_loop, daemon=True)
    t.start()

    # 监听键盘
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
