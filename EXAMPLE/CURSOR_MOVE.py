import pyautogui

pyautogui.sleep(3)


pyautogui.moveTo(100,100,duration=1)

pyautogui.moveTo(100, 200, 2)

pyautogui.moveTo(100,100,duration=1)

pyautogui.dragTo(x=500, y=638, mouseDownUp=False, duration=1)  # Двигаем немного влево
pyautogui.dragRel(800, 0, duration=1)