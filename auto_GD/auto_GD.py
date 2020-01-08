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
    pl = pyautogui.locateOnScreen('1.png', confidence=0.97)  # 疲劳值为空的判断
    if pl:
        for i in range(3):
            pyautogui.keyDown('f12')
            pyautogui.keyUp('f12')
        change_role()
    else:
        move_to()


def change_role():
    for i in range(3):
        pyautogui.keyDown('f12')
        pyautogui.keyUp('f12')
        # 在这里加一个灰色的再次挑战的判断
    for i in range(10):
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        time.sleep(random.random())
        pyautogui.moveTo(858, 713)
        time.sleep(random.random())
        pyautogui.doubleClick()
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        xzjs = pyautogui.locateOnScreen('3.png', confidence=0.95)  # 选择角色页面
        time.sleep(1)
        if xzjs:
            break
    pyautogui.keyDown("right")
    pyautogui.keyUp("right")
    time.sleep(random.random())
    for i in range(3):
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
    time.sleep(3)
    move_to()


def move_to():
    pl = pyautogui.locateOnScreen('1.png', confidence=0.97)  # 疲劳值为空的判断
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
            pyautogui.moveTo(858, 505)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        time.sleep(6.66)
        pyautogui.keyDown("down")
        time.sleep(2)
        pyautogui.keyUp("down")
        pyautogui.keyDown("right")
        time.sleep(2)
        pyautogui.keyUp("right")
        time.sleep(1)
        for i in range(5):
            pyautogui.moveTo(600, 700)
            pyautogui.doubleClick()
            pyautogui.click(button="left")
        time.sleep(1)
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')


def auto_attack():
    global a
    a += 1
    print(a)
    for i in range(3):
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("x")
        time.sleep(0.88 + random.random())
        pyautogui.keyUp("x")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        p = random.choices(l)[0]
        pyautogui.keyDown(p)
        pyautogui.keyUp(p)


def pickup():
    for i in range(3):
        pyautogui.keyDown('ctrlleft')
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyDown('ctrl')
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('x')
        time.sleep(1.33 + random.random())
        pyautogui.keyUp('x')
    one_more()


def one_more():
    zctz = pyautogui.locateOnScreen('2.png', confidence=0.95)  # 再次挑战
    if zctz:
        for i in range(3):
            pyautogui.keyDown('f10')
            pyautogui.keyUp('f10')
    else:
        for i in range(3):
            pyautogui.keyDown('f12')
            pyautogui.keyUp('f12')
        pljc()


while True:
    zctz = pyautogui.locateOnScreen('2.png', confidence=0.95)  # 再次挑战
    if zctz:
        pickup()
    t11 = time.time()-t1
    if t11 > 100.0:
        t1 = time.time()
        vs = pyautogui.locateOnScreen('4.png')
        pljc()
    auto_attack()

