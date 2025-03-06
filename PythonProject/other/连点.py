import threading
import time
import pyautogui
from pynput import keyboard

clicking = False  # 控制点击状态
interval = 0.01  # 点击间隔（秒）

def click_mouse():
    """ 持续点击鼠标，直到 clicking 变为 False """
    while clicking:
        pyautogui.click()
        time.sleep(interval)

def on_press(key):
    """ 监听键盘事件 """
    global clicking
    if key == keyboard.Key.f6:  # 按 F6 开始
        if not clicking:
            clicking = True
            thread = threading.Thread(target=click_mouse)
            thread.daemon = True
            thread.start()
            print("鼠标连点器已启动...")
    elif key == keyboard.Key.f7:  # 按 F7 停止
        clicking = False
        print("鼠标连点器已停止...")

# 监听键盘
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()