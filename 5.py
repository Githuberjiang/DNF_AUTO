# 1.4秒一个空格
# 2. x 按下 松开 随机时间
# 3 每一分半一次 拣取物品 + F10
import pyautogui
import time
import random


def x():
    a = time.time()
    d = 0
    while True:
        d += 1
        b = time.time()
        if d % 2 == 1:
            pyautogui.hotkey("right")
        else:
            pyautogui.hotkey("left")
        for i in range(random.randint(1, 10)):
            pyautogui.hotkey("x")
            time.sleep(random.random())
        time.sleep(0.2)
        pyautogui.hotkey("a")
        pyautogui.hotkey("space")
        c = b - a
        if c > 90:
            pyautogui.hotkey(",")
            pyautogui.hotkey(",")
            for i in range(15):
                pyautogui.hotkey("x")
                time.sleep(random.random())

            pyautogui.hotkey("f10")
            a = time.time()
            print(c)


x()

# # # time.sleep(2)a
# xxxxxxxxaxa  xaxxxxxxxxxxa  xxxxxxxxxxaxxxxxxa  xxxxaxxxxxa  xaxxxxa  xaxxa  xxxxxxxxaxxxxxxxa  xxaxxxa  xxxxaxxxxxxa  xxxxxxxxxaxxxxa  xxxxxxxxxxaxxxxxxa ,,xxxxxxxxxxxxxxx xxaxxa  xxx# # b = time.time()
# # # c = b-a
# # print(random.randint(1, 10))
# x惺惺相惜x惺惺相惜想学习啊啊xxxxxxxaxx # print(2 % 2)
