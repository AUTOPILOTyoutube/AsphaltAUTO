# Используется в программе AUTOPILOT
# Определяет, что идет игра и управляет машиной. Для режима СЕТЬ - Классика.



import time
import pyautogui
from datetime import timedelta, datetime
from BUTTON_FIND import BUTTON_FIND
from EXAMPLE.Screenshot import ScreenShot


def GAME_NETWORK_RUN(GAME_number):
    print(time.strftime("%X", time.localtime()), 'GAME_NETWORK_RUN')
    #Ждем появление смайлика в течении 80 секунд
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
            # Нажимаем кнопку AZOT (нитро).
            #pyautogui.doubleClick(x=1622, y=835)
            #print(time.strftime("%X", time.localtime()),'ЖМЁМ НИТРО!')

            # нажимаем вправо
            i=0
            while i<3:
                pyautogui.keyDown('right')
                pyautogui.sleep(0.1)
                pyautogui.keyUp('right')
                i+=1

            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # пауза
            pyautogui.sleep(2.7)

            # оттормаживаемся
            pyautogui.keyDown('down')
            pyautogui.sleep(1)
            pyautogui.keyUp('down')

            # нажимаем влево
            i=0
            while i<3:
                pyautogui.keyDown('left')
                pyautogui.sleep(0.1)
                pyautogui.keyUp('left')
                i+=1



            # включаем двойное нитро
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('space')

            # пауза
            pyautogui.sleep(3)

            # оттормаживаемся
            pyautogui.keyDown('down')
            pyautogui.sleep(1)
            pyautogui.keyUp('down')



            """
            # Каталог из которого будем брать файлы
            directory = 'BUTTONS/GameRUN/BUTTONS'
            # Получаем список файлов в переменную files
            files = os.listdir(directory)
            # Ищем кнопку каждого файла и кликаем по ней
            for f in files:
                path = str(directory + '/' + f)
                # Ищем кнопку и кликаем по ней
                if BUTTON_Find_Click(path=path, confidence=0.65, click=2, sec=0.2) == True:
                    pyautogui.sleep(0.1)
                    # Нажимаем кнопку AZOT (нитро).
                    #pyautogui.doubleClick(x=1622, y=835)
                    pyautogui.press('space')
                    pyautogui.press('space')
                    pyautogui.sleep(0.1)
                else:
                    # Нажимаем кнопку AZOT (нитро).
                    #pyautogui.doubleClick(x=1622, y=835)
                    pyautogui.press('space')
                    pyautogui.sleep(0.1)
            """

        ScreenShot('Game Over') # Сохраняем скриншот в папку foto/Game Over
        print(time.strftime("%X", time.localtime()),'ЗАВЕРШЕНА ИГРА №',GAME_number)
        Wait_TIME = 10

    else:
        Errors=True
        print(time.strftime("%X", time.localtime()),'Игра не началась!')
        print('_______________________________________________________________________________________________')
        #pyautogui.screenshot('BUTTONS/ErrorsScreen/screen.jpg')  # Делаем скриншот экрана
        #pyautogui.alert(text = 'Игра не началась!', title = 'ПАУЗА', button = 'ПРОДОЛЖИТЬ')
        Wait_TIME = 1



    return Wait_TIME, Errors

if __name__ == '__main__':
    print('ПРИВЕТ, МИР!')
    print(GAME_NETWORK_RUN(1))

# Примечание. Пока на экране находится СМАЙЛИК, программа считает, что идёт гонка!
# Но после окончания гонки СМАЙЛИК исчезает, а программа иногда думает, что СМАЙЛИК на экране - считает, что идет гонка.
# Это связано из-за низкой точности определения смайлика. Но точность нельзя увеличивать.
# Поэтому я добавил ВРЕМЯ на ГОНКУ - 150 секунд
# По истечении этого времени, программа будет считать, что гонка завершилась, даже если она будет думать, что смайлик на экране.
#
#
#
#