import pyautogui
import time
import random

l = ['a', 's', 'd', 'q', 'w', 'e']


def move_to():
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


def change_role():
    for i in range(5):
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
            for i in range(3):
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
    move_to()


def auto_attack():
    for i in range(3):
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("x")
        time.sleep(random.random() + random.random())
        pyautogui.keyUp("x")
        for i in range(5):
            pyautogui.keyDown("space")
            pyautogui.keyUp("space")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        p = random.choices(l)[0]
        pyautogui.keyDown(p)
        pyautogui.keyUp(p)
        print(p)


def pickup():
    for i in range(4):
        pyautogui.keyDown("ctrlleft")
        pyautogui.keyUp("ctrlleft")
        pyautogui.keyDown("ctrlleft")
        pyautogui.keyUp("ctrlleft")
    pyautogui.keyDown("x")
    time.sleep(1 + random.random())
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    time.sleep(1 + random.random())
    pyautogui.keyUp("x")
    bbb = pyautogui.locateOnScreen("222.png", confidence=0.96)  # 疲劳为空
    time.sleep(1)
    if bbb:
        pyautogui.keyDown('f12')
        pyautogui.keyUp('f12')
        auto_attack()
        change_role()
    pyautogui.keyDown("f10")
    pyautogui.keyUp("f10")
    pyautogui.keyDown("f10")
    pyautogui.keyUp("f10")


st = time.time()
at = time.time()
pt = time.time()
while True:
    jt = time.time()
    at1 = time.time()
    pt1 = time.time()
    jrt = round(jt - st, 0)
    at2 = round(at1 - at, 0)
    pt2 = round(pt1 - pt, 0)
    if jrt > 600:
        st = time.time()
        pl = pyautogui.locateOnScreen("222.png", confidence=0.97)  # 疲劳为空
        if pl:
            change_role()
        else:
            move_to()
    elif at2 > 10:
        at = time.time()
        zc = pyautogui.locateOnScreen("111.png", confidence=0.95)  # 再次挑战
        if zc:
            pickup()
    elif pt2 > 600:
        pt = time.time()
        pl = pyautogui.locateOnScreen("222.png", confidence=0.97)  # 疲劳为空
        if pl:
            for i in range(5):
                pyautogui.keyDown('f12')
                pyautogui.keyUp('f12')
            auto_attack()
            change_role()
    auto_attack()
