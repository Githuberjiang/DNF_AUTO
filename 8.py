import pyautogui
import time
import random

# screenWidth, screenHeight = pyautogui.size()  # 获得当前屏幕的宽高

# pyautogui.moveTo(screenWidth / 2, screenHeight / 2)  # 移动光标至屏幕中心
#
# pyautogui.PAUSE = 2.5  # 代码执行完毕，延迟2.5秒结束程序
#
# pyautogui.moveTo(screenWidth / 4, screenHeight / 4)  # 移动光标至屏幕中心

# pyautogui.moveTo(100, 100)

# pyautogui.click()

# a = pyautogui.position()  # current mouse x and y
# (968, 56)
# time.sleep(1)
# pyautogui.moveTo(a)

# b = pyautogui.size()
# print(b)

# c = pyautogui.onScreen(1500, 910)  # 判断坐标是否在屏幕上，返回值是True或者False
# print(c)

# pyautogui.moveTo(300, 300, duration=random.random())  # 移动鼠标到目的地
# pyautogui.moveRel(400, 200, duration=random.random())  # 将鼠标从某点移动到当前位置 move mouse relative to its current position
# pyautogui.click(button='left')  # 鼠标点击事件，左击

# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=random.random())  # 组合键输入，按键间隔随机时间
# pyautogui.alert('This displays some text with an OK button.')  # OK弹出框
# pyautogui.confirm('This displays text and has an OK and Cancel button.')  # OK or Cancel 选择弹出框
# pyautogui.prompt('This lets the user type in a string and press OK.')  # OK or cancel 输入框


# d = pyautogui.screenshot()  # 截屏
# e = pyautogui.screenshot('foo.png')  # 截屏并保存
pyautogui.move(0, 50,)  # 区别与moveTo，参考点为鼠标当前位置
# pyautogui.drag(300, 200, button='left')  # 拖拽移动，待定
# pyautogui.dragTo(300, 200, button='left')  # 拖拽移动至，待定

# pyautogui.keyDown('shift') # hold down the shift key
# pyautogui.press('a')     # press the left arrow key
# pyautogui.press('a')     # press the left arrow key
# pyautogui.press('a')     # press the left arrow key
# pyautogui.keyUp('shift')    # release the shift key


# e = pyautogui.screenshot('/Users/yi/Desktop/FORFND/qqq111.png')
# f = pyautogui.locateOnScreen("/Users/yi/Desktop/FORFND/qqq.png", confidence=0.98)  # 图像匹配，返回值为True或者False
# print(f)


# im = pyautogui.screenshot()
# print(im.getpixel((100, 200)))  # 获取某点像素 (13, 41, 62, 255)
# pix = pyautogui.pixel(100, 200)  # RGB(red=13, green=41, blue=62)
# print(pix)

# i = pyautogui.pixelMatchesColor(100, 200, (143, 134, 168), tolerance=5)  # 像素匹配，返回值为True或者False
# print(i)