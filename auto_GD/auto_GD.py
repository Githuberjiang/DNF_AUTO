# 检测疲劳
# 换角色
# 移动至副本
# 自动攻击
# 拾取
# 再次挑战


import pyautogui
import random
import time

l = ['a', 's', 'd', 'q', 'w', 'e']
a = 0
t1 = time.time()


def pljc():
    pl = pyautogui.locateOnScreen('a5.png', confidence=0.95)  # 疲劳值为空的判断

    plex = pyautogui.locateOnScreen('a4.png', confidence=0.95)  # ex空疲劳

    time.sleep(0.5)
    if pl or plex:
        change_role()
        return
    else:
        move_to()
        return 1


def change_role():
    global t1
    t1 = time.time()
    while True:
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        time.sleep(random.random())
        pyautogui.moveTo(622, 533)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1)
        xzjs = pyautogui.locateOnScreen('a3.png', confidence=0.9)  # 选择角色页面
        time.sleep(1)
        if xzjs:
            pyautogui.keyDown("right")
            pyautogui.keyUp("right")
            time.sleep(random.random())
            for i in range(3):
                pyautogui.keyDown('space')
                pyautogui.keyUp('space')
            move_to()
            break


def move_to():
    pl = pyautogui.locateOnScreen('111.png', confidence=0.98)  # 疲劳值为空的判断
    time.sleep(1)
    if pl:
        change_role()
    else:
        pyautogui.keyDown('down')
        time.sleep(2.33)
        pyautogui.keyUp('down')
        pyautogui.keyDown('n')
        pyautogui.keyUp('n')
        for i in range(5):
            pyautogui.moveTo(616, 323)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        time.sleep(6.66)
        pyautogui.keyDown("down")
        time.sleep(2)
        pyautogui.keyUp("down")
        pyautogui.keyDown("right")
        time.sleep(3)
        pyautogui.keyUp("right")
        time.sleep(1)
        for i in range(5):
            pyautogui.moveTo(353, 536)
            pyautogui.doubleClick()
            pyautogui.click(button="left")
        time.sleep(1)
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        pyautogui.keyDown('shift')
        pyautogui.keyUp('shift')


def auto_attack():
    global ar
    for i in range(3):
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("x")
        time.sleep(1.23 + random.random())
        pyautogui.keyUp("x")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        p = random.choices(l)[0]
        q = random.choices(l)[0]
        pyautogui.keyDown(p)
        pyautogui.keyUp(p)
        pyautogui.keyDown(q)
        pyautogui.keyUp(q)


def pickup():
    for i in range(2):
        pyautogui.keyDown('ctrlleft')
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyDown('ctrl')
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('x')
        time.sleep(2 + random.random())
        pyautogui.keyUp('x')
    one_more()



def one_more():
    for i in range(3):
        pyautogui.keyDown('f10')
        pyautogui.keyUp('f10')
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.keyDown('f12')
    pyautogui.keyUp('f12')


while True:
    sfjx = pyautogui.locateOnScreen('a1.png', confidence=0.9)  # 再次挑战
    cz = pyautogui.locateOnScreen('a2.png', confidence=0.9)  # 在城镇
    time.sleep(1)
    if sfjx:
        pickup()
    elif cz:
        pljc()

    auto_attack()
