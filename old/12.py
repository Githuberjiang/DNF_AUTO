import pyautogui
import time
import random


pyautogui.keyDown('esc')
pyautogui.keyUp('esc')
for i in range(2):
    pyautogui.moveTo(858, 713)
    pyautogui.doubleClick()
    pyautogui.mouseDown()
    pyautogui.mouseUp()
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
