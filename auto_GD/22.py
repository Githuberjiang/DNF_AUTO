import pyautogui
import time


t1 = time.time()
pyautogui.locateOnScreen('11.png',confidence=0.98)
print(time.time()-t1)