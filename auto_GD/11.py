import pyautogui
import random
import time


def move_to1():
    pl = pyautogui.locateOnScreen('1.png', confidence=0.97)  # 疲劳值为空的判断
    if pl:
        print('change_role()')
    else:
        pyautogui.keyDown('down')
        time.sleep(2.33)
        pyautogui.keyUp('down')
        pyautogui.keyDown('n')
        pyautogui.keyUp('n')
        for i in range(10):
            pyautogui.moveTo(858, 505)
            # pyautogui.click(858,505,button="left",)
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


move_to1()




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


# move_to()