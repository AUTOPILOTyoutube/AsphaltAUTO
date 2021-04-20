# Используется в программе AUTOPILOT
# Определяет, что идет игра и управляет машиной. Для режима SLEAPSTREAM.

import time
import pyautogui
from datetime import timedelta, datetime
from BUTTON_FIND import BUTTON_FIND
from EXAMPLE.Screenshot import ScreenShot


def GAME_NETWORK_SLIPSTREAM_RUN(GAME_number):
    print(time.strftime("%X", time.localtime()), 'GAME_NETWORK_SLIPSTREAM_RUN')
    if BUTTON_FIND('BUTTONS\GameRUN\RUN_GAME.PNG', confidence=0.62, sec=80)==True:

        Errors=False
        print('--------------------------------------------------------------------------------------------')
        print(time.strftime("%X", time.localtime()),'НАЧАЛАСЬ ИГРА №',GAME_number )
        pyautogui.sleep(5) # Пауза обязательна, чтобы не увеличивать время проверки, что идёт игра

        timeStart = datetime.now()
        timeFinish = datetime.now() + timedelta(seconds=150) #Максимальное время игры 150 секунд

        i=0 # Для разворота
        while BUTTON_FIND('BUTTONS\GameRUN\RUN_GAME.PNG', confidence=0.62, sec=10) and timeStart<timeFinish:
            timeStart = datetime.now()

            # нажимаем вправо
            i = 0
            while i < 3:
                pyautogui.keyDown('right')
                pyautogui.sleep(0.1)
                pyautogui.keyUp('right')
                i += 1

                # включаем двойное нитро
                pyautogui.press('space')
                pyautogui.sleep(0.1)
                pyautogui.press('space')



            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # пауза
            pyautogui.sleep(1)

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # пауза
            pyautogui.sleep(1)

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # оттормаживаемся
            pyautogui.keyDown('down')
            pyautogui.sleep(1)
            pyautogui.keyUp('down')

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # нажимаем влево
            i = 0
            while i < 3:
                pyautogui.keyDown('left')
                pyautogui.sleep(0.1)
                pyautogui.keyUp('left')
                i += 1

                # включаем двойное нитро
                pyautogui.press('space')
                pyautogui.sleep(0.1)
                pyautogui.press('space')

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # пауза
            pyautogui.sleep(1)

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # пауза
            pyautogui.sleep(1)

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # оттормаживаемся
            pyautogui.keyDown('down')
            pyautogui.sleep(0.7)
            pyautogui.keyUp('down')

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')








        ScreenShot('Game Over') # Сохраняем скриншот в папку foto/Game Over
        print(time.strftime("%X", time.localtime()),'ЗАВЕРШЕНА ИГРА №',GAME_number)
        Wait_TIME = 10

    else:
        Errors=True
        print(time.strftime("%X", time.localtime()),'Игра не началась!')
        print('_______________________________________________________________________________________________')
        #pyautogui.screenshot('BUTTONS/ErrorsScreen/screen.jpg')  # Делаем скриншот экрана
        #pyautogui.alert(text = 'Игра не началась!', title = 'ПАУЗА', button = 'ПРОДОЛЖИТЬ')
        Wait_TIME = 2





    return Wait_TIME, Errors

if __name__ == '__main__':
    print('ПРИВЕТ, МИР!')
    print(GAME_NETWORK_SLIPSTREAM_RUN(1))

# Примечание. Пока на экране находится СМАЙЛИК, программа считает, что идёт гонка!
# Но после окончания гонки СМАЙЛИК исчезает, а программа иногда думает, что СМАЙЛИК на экране - считает, что идет гонка.
# Это связано из-за низкой точности определения смайлика. Но точность нельзя увеличивать.
# Поэтому я добавил ВРЕМЯ на ГОНКУ - 150 секунд
# По истечении этого времени, программа будет считать, что гонка завершилась, даже если она будет думать, что смайлик на экране.
#
#
#
#