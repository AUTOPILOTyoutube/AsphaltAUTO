# Используется в программе AUTOPILOT
# Нажимает на изображения, чтобы запустить сетевую игру
# Проходит по каждому изображеню в папке один круг.
import pyautogui
import time
from EXAMPLE.Screenshot import ScreenShot
from BUTTON_Find_Click import BUTTON_Find_Click
from BUTTON_FIND import BUTTON_FIND


def NETWORK(Wait_TIME):
    print(time.strftime("%X", time.localtime()), 'NETWORK')
    ScreenShot('Credits')

    if BUTTON_Find_Click(path='BUTTONS/NETWORK/01networkGame.PNG', confidence=0.9, click=1, sec=Wait_TIME) == True:
        pyautogui.sleep(3)
        Wait_TIME = 10
    else:
        Wait_TIME = 3

    if BUTTON_Find_Click(path='BUTTONS/NETWORK/02selectNetworkGame_WORLD.PNG', confidence=0.9, click=1, sec=Wait_TIME) == True:
        pyautogui.sleep(3)
        Wait_TIME = 10
    else:
        Wait_TIME = 3

    if BUTTON_FIND(path='BUTTONS/NETWORK/03leagueBRONZE.PNG', confidence=0.9, sec=Wait_TIME) == True:
        liga = "BRONZE"
    else:
        if BUTTON_FIND(path='BUTTONS/NETWORK/03leagueSILVER.PNG', confidence=0.9, sec=Wait_TIME)==True:
            liga = "SILVER"
        else:
            if BUTTON_FIND(path='BUTTONS/NETWORK/03leagueGOLD.PNG', confidence=0.9, sec=Wait_TIME) == True:
                liga = "GOLD"
            else:
                liga = "BRONZE"

    if BUTTON_Find_Click(path='BUTTONS/NETWORK/04startNETWORKgame.PNG', confidence=0.95, click=1, sec=Wait_TIME) == True:
        pyautogui.sleep(3)
        Wait_TIME = 10
    else:
        Wait_TIME = 3




    return liga, Wait_TIME

if __name__ == '__main__':

    liga, Wait_Time = NETWORK(8)

    print(liga)