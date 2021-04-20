# Звуковая сигнализация
import pyautogui
import winsound


def ALARM():

    for i in range(0, 3):
        winsound.Beep(800, 200)
    for i in range(0, 3):
        winsound.Beep(800, 400)
    for i in range(0, 3):
        winsound.Beep(800, 200)

if __name__ == '__main__':
    ALARM()