# Используется в программе AUTOPILOT
# Выполняет поиск изображения на экране и делает по нему щелчок мышью
import mouse

import pyautogui
import time
from datetime import timedelta, datetime
import winsound


#def BUTTON_Find_Click(path, region, confidence, click, sec):
def BUTTON_Find_Click(path, confidence, click, sec):

    timeStart = datetime.now()
    timeFinish = datetime.now() + timedelta(seconds=sec)

    print(time.strftime("%X", time.localtime()), 'Поиск кнопки для клика:', path)

    while timeStart < timeFinish:

        timeStart = datetime.now()
        button = pyautogui.locateOnScreen(path, confidence=confidence)

        if button != None:  # Если кнопка найдена, то...
            pyautogui.click(button,button="SECONDARY") #ОБЯЗАТЕЛЬНО, ЧТОБЫ ОБОЙТИ ЗАЩИТУ ИГРЫ - ЗАМОРАЖИВАТЬ КУРСОР ПОСЕРЕДИНЕ ЭКРАНА

            if click==1:

                pyautogui.click(button)  # Щелкаем мышкой по изображению
                print(time.strftime("%X", time.localtime()),'Одиночный клик по кнопке:', path, ' Координаты ', button)

            if click==2:

                pyautogui.doubleClick(button)  # Двойной щелчок мышкой по изображению
                print(time.strftime("%X", time.localtime()),'Двойной клик по кнопке',path, ' Координаты ', button)

                pyautogui.sleep(1)


            pyautogui.moveTo(10,10)
            result=True
            break
        else:
            result=False


    if result ==False:
        print(time.strftime("%X", time.localtime()), 'Кнопка не найдена:', path, ' Координаты ', button)
    return result

if __name__ == '__main__':

    BUTTON_Find_Click('BUTTONS/NETWORK/04startNETWORKgame.PNG', confidence = 0.95,click=1, sec = 10)