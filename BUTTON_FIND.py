# Используется в программе AUTOPILOT
# Выполняет поиск изображения на экране и возвращает результат: ИСТИНА или ЛОЖЬ
import pyautogui
import time
from datetime import timedelta, datetime



#def BUTTON_FIND(path, region, confidence, sec):   Поиск в регионе
def BUTTON_FIND(path, confidence, sec):

    print(time.strftime("%X", time.localtime()), 'Поиск изображения:', path)
    pyautogui.moveTo(x=10, y=10) # Перенос курсора в левый верхний угол, чтоб не мешался


    timeStart = datetime.now()
    timeFinish = datetime.now() + timedelta(seconds=sec)

    while timeStart < timeFinish:
        timeStart = datetime.now()
        if pyautogui.locateOnScreen(path, confidence=confidence) != None: # Если кнопка найдена, то...
            result=True

            #print(time.strftime("%X", time.localtime()),'Найдено изображение:', path)
            break
        else:
            result=False
            #print(time.strftime("%X", time.localtime()),'Изображение не найдено!', path)


    if result == True:
        print(time.strftime("%X", time.localtime()), 'Найдено изображение:', path)
    else:
        print(time.strftime("%X", time.localtime()), 'Изображение не найдено:', path)

    #pyautogui.moveTo(x=10, y=10)  # Перенос курсора в левый верхний угол, чтоб не мешался




    return result



if __name__ == '__main__':
    print('Ищем кнопку!')
    path = str('BUTTONS/START_NetworkGAME/StartNetworkGame.PNG')
    print(BUTTON_FIND(path=path, confidence=0.99, sec=5))
    #print(BUTTON_FIND(path=path, region = (1450,850,1910,1070), confidence=0.99, sec=5))