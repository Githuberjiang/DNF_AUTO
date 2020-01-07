import pyautogui
import time
import random
import datetime

# e = pyautogui.locateOnScreen('222.png', confidence=0.98)
# print(e)


# bb = pyautogui.pixelMatchesColor(824, 842, (43, 43, 43))
# aa = pyautogui.pixel(824, 842)
# print(aa, bb)


# cc = pyautogui.locateOnScreen('222.png', confidence=0.98)
# print(cc)


def huanjuese():
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(1)
    pyautogui.moveTo(910, 970)

    for i in range(3):
        pyautogui.moveTo(858, 713)
        pyautogui.doubleClick()
    # pyautogui.mouseDown()
    # pyautogui.mouseUp()
    time.sleep(3 + random.random()*3)
    pyautogui.keyDown("right")
    pyautogui.keyUp("right")
    time.sleep(random.random())
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    time.sleep(3 + random.random()*3)
    pyautogui.keyDown('down')
    time.sleep(2 + random.random()*2)
    pyautogui.keyUp('down')
    pyautogui.keyDown('n')
    for i in range(3):
        pyautogui.moveTo(870, 505)
        pyautogui.click(button="left")
    time.sleep(5 + random.random()*5)
    pyautogui.keyDown("down")
    time.sleep(1)
    pyautogui.keyUp("down")
    pyautogui.keyDown("right")
    time.sleep(1)
    pyautogui.keyUp("right")
    time.sleep(1)
    for i in range(3):
        pyautogui.moveTo(600, 700)
        pyautogui.doubleClick()
        pyautogui.click(button="left")


# huanjuese()
# c = pyautogui.locateOnScreen('333.png',confidence=0.98)
# print(c)

# c = pyautogui.locateOnScreen("444.png", confidence=0.97)  # 再次挑战为灰色
# # print(c)
# b = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
# aa = pyautogui.locateOnScreen('/Users/yi/Desktop/FORFND/333.png', confidence=0.95)
aa = pyautogui.locateOnScreen('333.png', confidence=0.9)

print(aa)