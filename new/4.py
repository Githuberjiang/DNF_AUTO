import pyautogui
import time
import random



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


print(time.localtime())
a = time.time()
time.sleep(1)
b= time.time()
print(round(b-a,1))