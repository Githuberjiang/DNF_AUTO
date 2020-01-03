import pyautogui
import time
import random
a = time.time()
# while True:
#     pyautogui.keyDown("x")
#     b = time.time()
#     c = random.random()+1
#     if b-a > c:
#         break



import pyautogui
im1 = pyautogui.screenshot()
im = pyautogui.screenshot('my_screenshot.png', region=(0,0, 300, 400))
# im2 = pyautogui.screenshot('my_screenshot.png')

