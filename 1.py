import pyautogui
screenWidth, screenHeight = pyautogui.size() # 屏幕尺寸
mouseX, mouseY = pyautogui.position() # 返回当前鼠标位置，注意坐标系统中左上方是(0, 0)
pyautogui.PAUSE = 1.5 # 每个函数执行后停顿1.5秒
pyautogui.FAILSAFE = True # 鼠标移到左上角会触发FailSafeException，因此快速移动鼠标到左上角也可以停止
w, h = pyautogui.size()
pyautogui.moveTo(w/2, h/2) # 基本移动
pyautogui.moveTo(2918, 2038, duration=2) # 移动过程持续2s完成
pyautogui.moveTo(None, 500) # X方向不变，Y方向移动到500

pyautogui.moveRel(-40, 500) # 相对位置移动
# 点击+向下拖动
pyautogui.click(941, 34, button='left')
pyautogui.dragRel(0, 100, button='left', duration=5)
pyautogui.click(300, 400, button='right') # 包含了move的点击，右键
pyautogui.click(clicks=2, interval=0.25) # 双击，间隔0.25s
pyautogui.scroll(-10)
pyautogui.click(1279, 374)
pyautogui.typewrite('hello world!')
pyautogui.press('shift') # 切换输入法的中英文
pyautogui.press(['#', ' ']) # press 可以对单个字符或者列表进行操作
pyautogui.press(['x', 'i', 'a', 'o'])# 小鱼尾兰
pyautogui.press(['y', 'u'])
pyautogui.press(['w', 'e', 'i'])
pyautogui.press(['l', 'a', 'n'])
pyautogui.press(' ')
pyautogui.hotkey('command', '1') # 可以使用组合键，本质上是
'''
pyautogui.keyDown('shift')
pyautogui.keyDown('a')
pyautogui.keyUp('shift')
pyautogui.keyUp('a')
'''
