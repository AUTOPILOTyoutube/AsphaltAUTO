# Используется в программе AUTOPILOT
# Закрывает окна после завершения игры
# Проходит по каждому изображеню в папке один круг.


import time
import os

from BUTTON_Find_Click import BUTTON_Find_Click


def GAME_OVER(Wait_TIME):


    print(time.strftime("%X", time.localtime()), 'GAME_OVER')

    # Каталог из которого будем брать файлы
    directory = 'BUTTONS/GameOver'
    # Получаем список файлов в переменную files
    files = os.listdir(directory)
    # Ищем кнопку каждого файла и кликаем по ней
    for f in files:
        path = str(directory + '/' + f)
        # Ищем кнопку и кликаем по ней
        if BUTTON_Find_Click(path=path, confidence=0.7, click=2, sec=Wait_TIME) == True:
            Wait_TIME = 13
        else:
            Wait_TIME = 3

    return Wait_TIME

if __name__ == '__main__':

    GAME_OVER(10)