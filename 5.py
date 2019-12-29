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
            pyautogui.keyDown("right")
        else:
            pyautogui.keyDown("left")
        for i in range(random.randint(1, 10)):
            pyautogui.keyDown("x")
            time.sleep(random.random())
        time.sleep(0.2)
        pyautogui.keyDown("a")
        pyautogui.keyDown("space")
        c = b - a
        if c > 90:
            pyautogui.keyDown(",")
            pyautogui.keyDown(",")
            for i in range(15):
                pyautogui.keyDown("x")
                time.sleep(random.random())

            pyautogui.keyDown("f10")
            a = time.time()
            print(c)


x()

# # time.sleep(2)
# # b = time.time()
# # c = b-a
# print(random.randint(1, 10))
# print(2 % 2)
