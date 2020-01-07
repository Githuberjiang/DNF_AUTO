import pyautogui
import time
import random

l = ['a', 's', 'd', 'q', 'w', 'e']


def pickup():
    for i in range(2):
        pyautogui.keyDown("ctrlleft")
        pyautogui.keyUp("ctrlleft")
        pyautogui.keyDown("ctrlleft")
        pyautogui.keyUp("ctrlleft")
        pyautogui.keyDown("x")
        time.sleep(2 + random.random())
        pyautogui.keyUp("x")
    bbb = pyautogui.locateOnScreen("222.png", confidence=0.94)  # 疲劳为空
    time.sleep(1)
    if bbb:
        pyautogui.keyDown('f12')
        pyautogui.keyUp('f12')
        change_role()
    pyautogui.keyDown("f10")
    pyautogui.keyUp("f10")
    pyautogui.keyDown("f10")
    pyautogui.keyUp("f10")


def auto_attack():
    for i in range(3):
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("x")
        time.sleep(random.random() + random.random())
        pyautogui.keyUp("x")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        p = random.choices(l)[0]
        pyautogui.keyDown(p)
        pyautogui.keyUp(p)
        print(p)


def change_role():
    pyautogui.keyDown('f12')
    pyautogui.keyUp('f12')
    pyautogui.keyDown('f12')
    pyautogui.keyUp('f12')
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
    for i in range(10):
        pyautogui.moveTo(600, 700)
        pyautogui.doubleClick()
        pyautogui.click(button="left")
    time.sleep(1)
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')



while True:
    pl = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
    zc = pyautogui.locateOnScreen("111.png", confidence=0.95)  # 再次挑战
    if pl:
        pyautogui.keyDown('f12')
        pyautogui.keyUp('f12')
        change_role()
    elif zc:
        pickup()
    auto_attack()
