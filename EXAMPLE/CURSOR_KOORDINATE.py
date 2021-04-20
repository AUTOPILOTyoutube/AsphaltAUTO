#Отображает координаты положения курсора

import pyautogui



while True:
    pyautogui.sleep(1)

    xy=pyautogui.position()
    print(xy)

    print()
