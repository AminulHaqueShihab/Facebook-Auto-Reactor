import pyautogui
import time
pyautogui.FAILSAFE = False
for i in range (0, 100):
    time.sleep(2)
    pyautogui.press('j')
    time.sleep(1)
    pyautogui.press('l')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')