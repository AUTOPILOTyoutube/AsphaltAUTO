# Используется в программе AUTOPILOT
# Кликает по кнопкам "ИГРАТЬ"
# Проходит по каждому изображеню в папке один круг.

import pyautogui
import time
import os

from BUTTON_Find_Click import BUTTON_Find_Click
from EXAMPLE.Screenshot import ScreenShot

def START_NetworkGAME(Wait_TIME): #запускаем игру
    pyautogui.sleep(1)
    pyautogui.moveTo(10, 10)  # Перенос курсора в левый верхний угол, чтоб не мешался
    pyautogui.sleep(1)
    print(time.strftime("%X", time.localtime()), 'START_NetworkGAME')
    ScreenShot('START')  # Сохраняем скриншот в папку foto/START


    # Каталог из которого будем брать файлы
    directory = 'BUTTONS/START_NetworkGAME'
    # Получаем список файлов в переменную files
    files = os.listdir(directory)
    # Ищем кнопку каждого файла и кликаем по ней
    for f in files:
        path = str(directory + '/' + f)
        # Ищем кнопку и кликаем по ней
        if BUTTON_Find_Click(path=path, confidence=0.6, click=2, sec=Wait_TIME) == True:
            Wait_TIME = 10
            error = False
        else:
            error = True
            Wait_TIME = 2

    if error == True:
        print(time.strftime("%X", time.localtime()),'Не получилось запустить гонку - нажать на кнопку ИГРАТЬ')
        ScreenShot('Errors') # Сохраняем скриншот в папку foto/Errors
    return Wait_TIME, error

if __name__ == '__main__':
    print('ПРИВЕТ, МИР!')
    print(START_NetworkGAME(10))