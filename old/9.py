import pyautogui
import time
import random

l = ['a', 's', 'd', 'f', 'g', 'h', 'q', 'w', 'e', 'r', 't', 'y']


def huanjuese():
    while True:
        aa = pyautogui.locateOnScreen('333.png', confidence=0.9)
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
    time.sleep(1 + random.random() * 3)
    bbb = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
    if bbb:
        return
    pyautogui.keyDown('down')
    time.sleep(2 + random.random() * 2)
    pyautogui.keyUp('down')
    pyautogui.keyDown('n')
    for i in range(3):
        pyautogui.moveTo(870, 505)
        pyautogui.click(button="left")
    time.sleep(8 + random.random() * 5)
    pyautogui.keyDown("down")
    time.sleep(1.5)
    pyautogui.keyUp("down")
    pyautogui.keyDown("right")
    time.sleep(1.5)
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


def zidonggongji():
    for i in range(3):
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("shift")
        time.sleep(random.random() + random.random())
        pyautogui.keyUp("shift")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("tab")
        pyautogui.keyUp("tab")
        p = random.choices(l)[0]
        pyautogui.keyDown(p)
        pyautogui.keyUp(p)
        print(p)


def shiqu():
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyUp("ctrlleft")
    pyautogui.keyDown("ctrl")
    pyautogui.keyUp("ctrl")
    pyautogui.keyDown("esc")
    pyautogui.keyUp("esc")
    for i in range(3):
        pyautogui.keyDown("shift")
        time.sleep(1 + random.random())
        pyautogui.keyUp("shift")
    pyautogui.keyDown("backspace")
    pyautogui.keyUp("backspace")
    pyautogui.keyDown("backspace")
    pyautogui.keyUp("backspace")


b = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
while True:
    b = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
    a = pyautogui.locateOnScreen("111.png", confidence=0.95)  # 再次挑战
    c = pyautogui.locateOnScreen("444.png", confidence=0.95)  # 再次挑战为灰色
    if b:
        huanjuese()
    elif c:
        shiqu()
        for i in range(2):
            pyautogui.keyDown('f12')
            pyautogui.keyUp('f12')
        time.sleep(2 + random.random())
        b = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
        if b:
            huanjuese()
        huanjuese()
    elif a:
        shiqu()
    # else:
    #     b = pyautogui.locateOnScreen("222.png", confidence=0.95)  # 疲劳为空
    zidonggongji()
