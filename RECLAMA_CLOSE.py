# Используется в программе AUTOPILOT
# Закрывает рекламные окна и сообщения - нажимает на "крестики", кнопки "Далее", "Пропустить", "ОК"...
# Проходит по каждому изображеню в папке один круг.

import pyautogui
import time
import os


from BUTTON_Find_Click import BUTTON_Find_Click

def RECLAMA_CLOSE(Wait_TIME):
    pyautogui.moveTo(10, 10)  # Перенос курсора в левый верхний угол, чтоб не мешался
    print(time.strftime("%X", time.localtime()), 'RECLAMA_CLOSE')

    # Каталог из которого будем брать файлы
    directory = 'BUTTONS/CLOSE'
    # Получаем список файлов в переменную files
    files = os.listdir(directory)
    # Ищем кнопку каждого файла и кликаем по ней
    for f in files:
        path = str(directory + '/' + f)
        #Ищем кнопку и кликаем по ней
        if BUTTON_Find_Click(path=path, confidence=0.7, click=2, sec=Wait_TIME) == True:
            Wait_TIME=10
        else: Wait_TIME=0.2

    #Закрываем рекламные окна, которые не получается закрыть с помощью распознавания изображений



    return Wait_TIME

if __name__ == '__main__':

    print(RECLAMA_CLOSE(5))
