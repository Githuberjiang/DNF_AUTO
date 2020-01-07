import pyautogui
import time
import random

l = ['a', 's', 'd', 'q', 'w', 'e']


def change_role():
    while True:
        aa = pyautogui.locateOnScreen('333.png', confidence=0.94)
        time.sleep(1)
        print(aa)
        if aa:
            break
        else:
            pyautogui.keyDown('esc')
            pyautogui.keyUp('esc')
            time.sleep(random.random())
            pyautogui.moveTo(858, 713)
            time.sleep(random.random())
            pyautogui.doubleClick()
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(1)
    pyautogui.keyDown("right")
    pyautogui.keyUp("right")
    time.sleep(random.random())
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    time.sleep(3)
    bbb = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
    if bbb:
        return
    pyautogui.keyDown('down')
    time.sleep(3)
    pyautogui.keyUp('down')
    pyautogui.keyDown('n')
    pyautogui.keyUp('n')
    for i in range(3):
        pyautogui.moveTo(870, 505)
        pyautogui.click(button="left")
    time.sleep(6.66)
    pyautogui.keyDown("down")
    time.sleep(1.33)
    pyautogui.keyUp("down")
    pyautogui.keyDown("right")
    time.sleep(1.33)
    pyautogui.keyUp("right")
    time.sleep(1)
    for i in range(3):
        pyautogui.moveTo(600, 700)
        pyautogui.doubleClick()
        pyautogui.click(button="left")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')


def auto_attack():
    for i in range(3):
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("shift")
        time.sleep(random.random() + random.random())
        pyautogui.keyUp("shift")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        p = random.choices(l)[0]
        pyautogui.keyDown(p)
        pyautogui.keyUp(p)
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        print(p)


def pickup():
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyUp("ctrlleft")
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyUp("ctrlleft")
    pyautogui.keyDown("esc")
    pyautogui.keyUp("esc")
    for i in range(3):
        pyautogui.keyDown("x")
        time.sleep(1 + random.random())
        pyautogui.keyUp("x")
    pyautogui.keyDown("f10")
    pyautogui.keyUp("f10")
    pyautogui.keyDown("f10")
    pyautogui.keyUp("f10")


# while True:
#     pl = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
#     zc = pyautogui.locateOnScreen("111.png", confidence=0.95)  # 再次挑战
#     if pl:
#         change_role()
#     elif zc:
#         pickup()
#     auto_attack()
