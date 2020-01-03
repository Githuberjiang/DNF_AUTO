import pyautogui
import time
import random

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
# # pyautogui.PAUSE = 2.5
# # pyautogui.moveTo(100, 100)
# # pyautogui.click()

# a = pyautogui.position()  # current mouse x and y
# (968, 56)
# time.sleep(1)
# pyautogui.moveTo(a)

# b = pyautogui.size()
# print(b)
#
#
#
# c = pyautogui.onScreen(1500, 910)
# print(c)
# pyautogui.FAILSAFE = True
# # time.sleep(2)
# pyautogui.moveTo(300, 300, duration=random.random())
# pyautogui.moveRel(400, 200, duration=random.random())  # 将鼠标移动到当前位置 move mouse relative to its current position
# pyautogui.click(button='left')

# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=random.random())
# pyautogui.alert('This displays some text with an OK button.')
# pyautogui.confirm('This displays text and has an OK and Cancel button.')
# pyautogui.prompt('This lets the user type in a string and press OK.')


# d = pyautogui.screenshot()
# e = pyautogui.screenshot('foo.png')
# # pyautogui.locateOnScreen()
# pyautogui.move(0, 50,)
# pyautogui.drag(100, 200, button='left')
# pyautogui.dragTo(-100, 200, button='left')

# pyautogui.keyDown('shift') # hold down the shift key
# pyautogui.press('a')     # press the left arrow key
# pyautogui.press('a')     # press the left arrow key
# pyautogui.press('a')     # press the left arrow key
# pyautogui.keyUp('shift')    # release the shift key


# e = pyautogui.screenshot('/Users/yi/Desktop/FORFND/qqq111.png')
# f = pyautogui.locateOnScreen("/Users/yi/Desktop/FORFND/qqq.png", confidence=0.98)
# print(f)
#
#
# pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))


im = pyautogui.screenshot()
print(im)
print(im.getpixel((100, 200)))
print()
pix = pyautogui.pixel(100, 200)
print(pix)
i = pyautogui.pixelMatchesColor(100, 200, (143, 134, 168), tolerance=5)
print(i)

pyautogui.moveTo(100, 200)
