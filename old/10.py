import pyautogui
import time
import random
# b = pyautogui.pixelMatchesColor(1342, 261, (60, 63, 65), tolerance=5)
# print(b)
# pyautogui.moveTo(1342,261)

# while True:
#     # a = pyautogui.position()
#     # print(a)
#     # time.sleep(1)
#     # e = pyautogui.screenshot('foo1.png')  # 截屏并保存
#     # f = pyautogui.locateOnScreen("333.png",confidence=0.98)  # 图像匹配，返回值为True或者False
#     # print(f)
#     pyautogui.keyDown(',')
#     time.sleep(1)
#     b = pyautogui.locateOnScreen("333.png", confidence=0.98)
#     print(b)
# d = pyautogui.locateOnScreen("444.png", confidence=0.98)
# print(d)
# pyautogui.keyDown('f12')
# pyautogui.keyUp('f12')
# pyautogui.keyDown('esc')
#
# pyautogui.keyUp('esc')
pyautogui.keyDown('esc')
pyautogui.keyUp('esc')
pyautogui.mouseDown(858, 713, button="left",)
time.sleep(random.random())
for i in range(3):
    pyautogui.moveTo(858, 713)
    pyautogui.doubleClick()
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.mouseUp(858, 713, button="left")
time.sleep(5)
pyautogui.keyDown("right")
pyautogui.keyUp("right")
pyautogui.keyDown('space')
pyautogui.keyUp('space')
time.sleep(5)
pyautogui.keyDown('down')
time.sleep(3)
pyautogui.keyUp('down')
pyautogui.keyDown('n')
for i in range(3):
    pyautogui.moveTo(870, 505)
    pyautogui.click(button="left")
time.sleep(5)
pyautogui.keyDown("down")
time.sleep(1)
pyautogui.keyUp("down")
pyautogui.keyDown("right")
time.sleep(1)
pyautogui.keyUp("right")
time.sleep(1)
for i in range(3):
    pyautogui.moveTo(600, 700)
    pyautogui.click(button="left")


