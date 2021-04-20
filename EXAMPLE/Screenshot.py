#Делает скриншот экрана и сохраняет в папку foto/text
#где text - название каталога


import pyautogui
import time
import os


def ScreenShot(text):

    try:
        os.makedirs('foto/'+text)
    except OSError:
        directoria = False
    else:
        directoria = True

    path = str('foto/'+text+'/'+time.strftime("%Y.%m.%d %H-%M-%S.png"))

    pyautogui.screenshot(path)

if __name__ == '__main__':

    ScreenShot('Game Over')