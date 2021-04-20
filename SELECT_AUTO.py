# Используется в программе AUTOPILOT
# Выполняет выбор машины  и возвращает результат: секунды, ИСТИНА или ЛОЖЬ

import pyautogui
import time
import os

from BUTTON_Find_Click import BUTTON_Find_Click


def SELECT_AUTO(prevLiga, liga, Wait_TIME):
    print(time.strftime("%X", time.localtime()), 'SELECT_AUTO')

    if liga == "GOLD":
        if prevLiga == "GOLD":
            directory = 'BUTTONS/SelectAUTO/GOLD'
            prevLiga = liga
            time.sleep(1)
            Wait_TIME = 10
        else:
            BUTTON_Find_Click(path='BUTTONS/SelectAUTO/ligaGOLD.JPG', confidence=0.9,click=1, sec = 7)
            # Каталог из которого будем брать файлы
            directory = 'BUTTONS/SelectAUTO/GOLD'
            prevLiga = liga
            time.sleep(1)
            Wait_TIME=10




    if liga == "SILVER":
        if prevLiga == "SILVER":
            directory = 'BUTTONS/SelectAUTO/SILVER'
            prevLiga = liga
            time.sleep(1)
            Wait_TIME = 10
        else:
            BUTTON_Find_Click(path='BUTTONS/SelectAUTO/ligaSILVER.JPG', confidence=0.9,click=1, sec = 7)
            # Каталог из которого будем брать файлы
            directory = 'BUTTONS/SelectAUTO/SILVER'
            prevLiga = liga
            time.sleep(1)
            Wait_TIME=10

    if liga == "BRONZE":
        if prevLiga == "BRONZE":
            directory = 'BUTTONS/SelectAUTO/BRONZE'
            prevLiga = liga
            time.sleep(1)
            Wait_TIME = 10
        else:
            # Каталог из которого будем брать файлы
            BUTTON_Find_Click(path='BUTTONS/SelectAUTO/ligaBRONZE.JPG', confidence=0.9, click=1, sec=7)
            directory = 'BUTTONS/SelectAUTO/BRONZE'
            prevLiga = liga
            time.sleep(1)
            Wait_TIME = 10

    # Получаем список файлов в переменную files
    files = os.listdir(directory)

    errors = 0

    STOP = False
    while STOP==False:
        # Ищем кнопку каждого файла и кликаем по ней
        for f in files:
            path = str(directory + '/' + f)
            # Ищем кнопку и кликаем по ней
            if BUTTON_Find_Click(path=path, confidence=0.95, click=2, sec=Wait_TIME) == True:
                Wait_TIME = 15

                error = -1
                STOP=True
                break
            else:

                Wait_TIME = 0.4
                error = 1

        errors =error +errors


        if errors>1:
            print(time.strftime("%X", time.localtime()), 'Не получилось выбрать машину')
            STOP=True
            break


        if errors>0:
            # Если мы не нашли заправленный автомобиль, то переходим в начальные автомобили для текущей лиги
            if liga == "BRONZE":
                BUTTON_Find_Click(path='BUTTONS/SelectAUTO/ligaBRONZE.JPG', confidence=0.9, click=1, sec=7)
                time.sleep(2)

            if liga == "SILVER":
                BUTTON_Find_Click(path='BUTTONS/SelectAUTO/ligaSILVER.JPG', confidence=0.9, click=1, sec=7)
                time.sleep(2)

            Wait_TIME = 15








        #if errors >0:
            #pyautogui.dragTo(x=500, y=636, mouseDownUp=False)  # Двигаем немного влево
            #pyautogui.dragRel(800, 0, duration=1)

    return prevLiga, Wait_TIME

if __name__ == '__main__':
    print('ПРИВЕТ, МИР!')
    SELECT_AUTO(prevLiga="BRONZE", liga="BRONZE",Wait_TIME=10)