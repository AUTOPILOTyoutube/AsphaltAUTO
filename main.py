
# pip install pyqt5
# программа считывает логин и пароль почты из файла mail.txt
import pyautogui
import time
import os

from MAIL import senderMAIL
from BUTTON_Find_Click import BUTTON_Find_Click # Поиск картинки и клик мышью по ней
from BUTTON_FIND import BUTTON_FIND # Поиск картинки и сообщение о результате
from RECLAMA_CLOSE import RECLAMA_CLOSE # Закрывает рекламные и диалоговые сообщения

from START_NetworkGAME import START_NetworkGAME # Нажимает кнопку ИГРАТЬ, чтобы запустилась гонка
from SELECT_AUTO import SELECT_AUTO
from NETWORK import NETWORK
from GameOver import GAME_OVER
from GAME_NETWORK_SLIPSTREAM_RUN import GAME_NETWORK_SLIPSTREAM_RUN

from GAME_NETWORK_RUN import GAME_NETWORK_RUN
from ALARM import ALARM
#**********************************************************************************



import time
import sys
import logging
import socket
import winsound

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QStyle, qApp, QLineEdit, QTextEdit, QApplication, QLabel
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QCheckBox, QHBoxLayout

class Example(QMainWindow):  # Наследуемся от QMainWindow
    def __init__(self):  # Переопределяем конструктор класса
        super().__init__()
        self.title = 'AUTOPILOT'


        self.width = 260
        self.height = 20
        self.left = (QApplication.desktop().width()/5)
        self.top = 0



        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlag(Qt.WindowStaysOnTopHint) #ПОВЕРХ ВСЕХ ОКОН
        # changing the background color to yellow
        #self.setStyleSheet("background-color: blue;")



        # self.setWindowIcon(QIcon('icon.ico')) # сделать свою иконку
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))  # сделать стандартную иконку КОМПЬЮТЕР

        self.table_widget = MyTableWidget(self)  # Берём виджет из класса MyTableWidget(QWidget), созданного ниже
        self.setCentralWidget(self.table_widget)  # Устанавливаем центральный виджет

        # Инициализируем QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setToolTip(u'AUTOPILOT')
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))  # Стандартная иконка КОМПЬЮТЕР
        # self.tray_icon.setIcon(QIcon('icon.ico'))   # ИКОНКА СВОЯ

        '''
            Объявим и добавим действия для работы с иконкой системного трея
            show - показать окно
            hide - скрыть окно
            exit - выход из программы
        '''
        show_action = QAction("Показать", self)
        quit_action = QAction("Завершить работу", self)
        hide_action = QAction("Спрятать в трей", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.show()

        self.tray_icon.messageClicked.connect(self.show)

        # self.tray_icon.DoubleClick.connect(self.show) не работает!

        # self.show()

        # Переопределение метода hideEvent, для перехвата события закрытия окна


class MyTableWidget(QWidget):   # Создаём интерфейс в отдельном классе MyTableWidget, который наследуется от QWidget

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self) #QVBoxLayout–это основной класс макета, который выстраивает виджеты вертикально

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(5, 5)

        # Add tabs
        self.tabs.addTab(self.tab1, "Start")
        self.tabs.addTab(self.tab2, "Statistics")
        self.tabs.addTab(self.tab3, "Settings")

        # Create  tab 1
        self.tab1.layout = QVBoxLayout(self)

        self.pushButton1 = QPushButton("START")
        self.tab1.layout.addWidget(self.pushButton1)
        self.pushButton1.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))



        self.tab1.setLayout(self.tab1.layout)

        self.textEdit1 = QLabel(self)
        self.textEdit1.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.tab1.layout.addWidget(self.textEdit1)

        self.textEdit12 = QLabel(self)
        self.textEdit12.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.tab1.layout.addWidget(self.textEdit12)

        # Create  tab 2
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.layout)
        self.textEdit2 = QTextEdit(self)
        self.tab2.layout.addWidget(self.textEdit2)

        # Create  tab 3
        self.tab3.layout = QVBoxLayout(self)
        self.tab3.setLayout(self.tab3.layout)
        self.tab3.layout.setAlignment(Qt.AlignTop) # Выравнивание всех элементов по центру сверху

        self.CHEK_BOKS1 = QCheckBox(self)
        self.tab3.layout.addWidget(self.CHEK_BOKS1)
        self.CHEK_BOKS1.setText("ВКЛЮЧИТЬ СИГНАЛИЗАЦИЮ")
        self.CHEK_BOKS1.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Medium))

        self.CHEK_BOKS2 = QCheckBox(self)
        self.tab3.layout.addWidget(self.CHEK_BOKS2)
        self.CHEK_BOKS2.setText("ВКЛЮЧИТЬ ВЫБОР МАШИН")
        self.CHEK_BOKS2.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Medium))
        self.CHEK_BOKS2.setChecked(True)

        self.CHEK_BOKS3 = QCheckBox(self)
        self.tab3.layout.addWidget(self.CHEK_BOKS3)
        self.CHEK_BOKS3.setText("ОТПРАВКА ПИСЕМ при остановке")
        self.CHEK_BOKS3.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Medium))

        self.CHEK_BOKS4 = QCheckBox(self)
        self.tab3.layout.addWidget(self.CHEK_BOKS4)
        self.CHEK_BOKS4.setText("Управление СЛИПСТРИМ")
        self.CHEK_BOKS4.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Medium))


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.pushButton1.clicked.connect(self.pushButton1Clicked)   # Отслеживаем нажатие кнопки




        self.button = 1

    # СЧИТЫВАЕМ наличие галочки в чексбоке 1
    def readCHECK_BOX1(self):
        self.CHEK1=self.CHEK_BOKS1.isChecked()
        return self.CHEK1

    # СЧИТЫВАЕМ наличие галочки в чексбоке 2
    def readCHECK_BOX2(self):
        self.CHEK2=self.CHEK_BOKS2.isChecked()
        return self.CHEK2

    # СЧИТЫВАЕМ наличие галочки в чексбоке 3
    def readCHECK_BOX3(self):
        self.CHEK3 = self.CHEK_BOKS3.isChecked()
        return self.CHEK3

    # СЧИТЫВАЕМ наличие галочки в чексбоке 4
    def readCHECK_BOX4(self):
        self.CHEK4 = self.CHEK_BOKS4.isChecked()
        return self.CHEK4


    def updateTEXTTAB1(self, textedit, valuetext): #Добавляет текст

        if textedit == 1:
            self.textEdit1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold)) # ШРИФТ
            self.textEdit1.setText(str(valuetext))
        if textedit == 2:
            self.textEdit12.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))  # ШРИФТ
            self.textEdit12.setText(str(valuetext))


    def updateTEXTTAB2(self, valuetext, a, b, c):
        self.textEdit2.setTextColor(QColor(a, b, c, 255))
        self.textEdit2.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))  # ШРИФТ
        self.textEdit2.append(str(valuetext))



    def pushButton1Clicked(self): # запуск потока при нажатии кнопки либо при вызове этой функции

        # при первом нажатии на кнопку запускаем поток
        if self.button == 1:

            self.button=0

            self.thread = UpdateText()
            self.thread.update_textTAB1.connect(self.updateTEXTTAB1)
            self.thread.update_textTAB2.connect(self.updateTEXTTAB2)
            self.thread.updateTEXT_pushButton.connect(self.setTextButton)

            self.thread.start()
            self.thread.button = "Start"
            self.thread.CHEK1 = self.readCHECK_BOX1()
            self.thread.CHEK2 = self.readCHECK_BOX2()
            self.thread.CHEK3 = self.readCHECK_BOX3()
            self.thread.CHEK4 = self.readCHECK_BOX4()

            self.CHEK_BOKS1.setEnabled(False)
            self.CHEK_BOKS2.setEnabled(False)
            self.CHEK_BOKS3.setEnabled(False)
            self.CHEK_BOKS4.setEnabled(False)

        # при втором нажатии на кнопку останавливаем поток
        else:

            self.pushButton1.setText('Stops...Please WAIT...')
            self.pushButton1.setEnabled(False)
            self.button = 1

            self.thread.button = "Stop"
            self.CHEK_BOKS1.setEnabled(True)
            self.CHEK_BOKS2.setEnabled(True)
            self.CHEK_BOKS3.setEnabled(True)
            self.CHEK_BOKS4.setEnabled(True)


    def setTextButton(self, text, setEnabled):
        self.pushButton1.setText(text)
        self.pushButton1.setEnabled(setEnabled)




class UpdateText(QtCore.QThread):  # ГЛАВНЫЙ ПОТОК
    update_textTAB1 = pyqtSignal(int,str)
    update_textTAB2 = pyqtSignal(str, int, int, int)
    updateTEXT_pushButton = pyqtSignal(str, bool)



    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):

        self.updateTEXT_pushButton.emit('STOP',True)

        # Создаём лог-файл`
        # Создайте Logger
        logfile = 'AUTOPILOT.log'
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.WARNING)
        # Создайте обработчик для записи данных в файл
        logger_handler = logging.FileHandler(logfile)
        logger_handler.setLevel(logging.WARNING)
        # Создайте Formatter для форматирования сообщений в логе
        logger_formatter = logging.Formatter('%(message)s')
        # Добавьте Formatter в обработчик
        logger_handler.setFormatter(logger_formatter)
        # Добавьте обработчик в Logger
        logger.addHandler(logger_handler)

        menu = 'START_NetworkGAME'
        GAME_number = 0
        Wait_TIME = 10
        ErrorsRUN = 0
        StopGAME = 0
        prevLiga = "BRONZE"
        liga = "BRONZE"


        while self.button == "Start":
            try:
                print("НАЧИНАЕМ")
                if menu == 'START_NetworkGAME' and self.button == "Start":
                    self.update_textTAB1.emit(1,str(GAME_number)+'   START Network GAME')
                    self.update_textTAB2.emit('_______________________________________________________________________',
                                              0, 0, 255)
                    self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime()) +
                                              ' START Network GAME ', 0, 0, 255)
                    logger.warning(time.strftime("%d %B %Y  %X",time.localtime())+str(GAME_number)+' START Network GAME')

                    Wait_TIME, Errors = START_NetworkGAME(Wait_TIME)
                    if Errors == False:
                        ErrorsRUN = 0
                        # menu = 'GAME_NETWORK_SLIPSTREAM_RUN'
                        menu = 'GAME_NETWORK_RUN'
                    if Errors == True:
                        ErrorsRUN = ErrorsRUN + 1
                        if ErrorsRUN > 1:

                            CHEK_BOX = self.CHEK1  # Состояние чек-бокса для включения звукового сигнала
                            if CHEK_BOX == True:
                                self.update_textTAB1.emit(1,str(GAME_number) + '   ALARM!')
                                ALARM()

                            CHEK_BOX = self.CHEK3  # Состояние чек-бокса для включения звукового сигнала
                            if CHEK_BOX == True:
                                self.update_textTAB1.emit(1,str(GAME_number) + '   SEND MAIL')
                                senderMAIL()

                            menu = 'GAME_OVER'
                            # a=pyautogui.confirm(title="ВНИМАНИЕ", text="АВТОПИЛОТ ЗАСТРЯЛ",buttons=['ЗАВЕРШИТЬ','ПРОДОЛЖИТЬ'])
                            # if a=='ЗАВЕРШИТЬ':
                            # exit()
                            # if a=='ПРОДОЛЖИТЬ':
                            # menu = 'START_NetworkGAME'
                        if ErrorsRUN <= 1:
                            menu = 'GAME_OVER'

                if menu == 'SELECT_AUTO' and self.button == "Start":
                    self.update_textTAB1.emit(1,str(GAME_number) + '   SELECT AUTO '+liga)
                    logger.warning(time.strftime("%d %B %Y  %X", time.localtime()) + '  SELECT AUTO ' + liga)
                    self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime()) + str(GAME_number) +
                                              '   SELECT AUTO ' + liga, 0, 0, 255)

                    prevLiga, Wait_TIME = SELECT_AUTO(prevLiga, liga, Wait_TIME)
                    menu = 'START_NetworkGAME'

                if menu == 'GAME_NETWORK_RUN' and self.button == "Start":
                    self.update_textTAB1.emit(1,str(GAME_number) + '   GAME NETWORK RUN')
                    logger.warning(time.strftime("%d %B %Y  %X", time.localtime()) + ' GAME NETWORK RUN')
                    self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime()) + str(GAME_number) +
                                              ' GAME NETWORK RUN', 0, 0, 255)

                    CHEK_BOX = self.CHEK4  # Состояние чек-бокса для включения режима СЛИПСТРИМ
                    if CHEK_BOX == True:
                        Wait_TIME, Errors =GAME_NETWORK_SLIPSTREAM_RUN(GAME_number)
                    else:
                        Wait_TIME, Errors = GAME_NETWORK_RUN(GAME_number)


                    if Errors == False:
                        GAME_number = GAME_number + 1
                        menu = 'GAME_OVER'
                    if Errors == True:
                        menu = 'GAME_OVER'

                if menu == 'GAME_OVER' and self.button == "Start":
                    self.update_textTAB1.emit(1,str(GAME_number) + '   GAME OVER')
                    logger.warning(time.strftime("%d %B %Y  %X", time.localtime()) + '  GAME OVER')
                    self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime())  +
                                              ' GAME OVER ' + str(GAME_number), 0, 0, 255)

                    self.update_textTAB1.emit(2, " ")

                    if Errors == False:
                        Wait_TIME = GAME_OVER(Wait_TIME)
                        menu = 'NETWORK'
                    if Errors == True:
                        Wait_TIME = GAME_OVER(Wait_TIME)
                        menu = 'RECLAMA_CLOSE'

                if menu == 'NETWORK' and self.button == "Start":
                    self.update_textTAB1.emit(1,str(GAME_number) + '   NETWORK')
                    logger.warning(time.strftime("%d %B %Y  %X", time.localtime()) + '  NETWORK')
                    self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime()) + str(GAME_number) +
                                              '  NETWORK', 0, 0, 255)

                    liga, Wait_TIME = NETWORK(Wait_TIME)
                    self.update_textTAB1.emit(2, "LEAGUE: " + liga)
                    logger.warning(time.strftime("%d %B %Y  %X", time.localtime()) + " LEAGUE: " + liga)
                    self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime()) + " LEAGUE: " + liga
                                              , 0, 0, 255)



                    CHEK_BOX2 = self.CHEK2  # Состояние чек-бокса для включения меню выбора машин
                    if CHEK_BOX2 == True:
                        menu = 'SELECT_AUTO'
                    else:
                        menu = 'START_NetworkGAME'

                if menu == 'RECLAMA_CLOSE' and self.button == "Start":
                    self.update_textTAB1.emit(1,str(GAME_number) + '   RECLAMA CLOSE')
                    logger.warning(time.strftime("%d %B %Y  %X", time.localtime()) + '  RECLAMA CLOSE')
                    self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime()) + str(GAME_number) +
                                              '  RECLAMA CLOSE', 0, 0, 255)

                    Wait_TIME = RECLAMA_CLOSE(Wait_TIME)

                    #Когда после определения лиги вырубается интернет...
                    if prevLiga == "BRONZE":
                        prevLiga = "SILVER"
                    else:
                        prevLiga = "BRONZE"

                    menu = 'NETWORK'






            except:
                print('ERROR PILOT')




        self.updateTEXT_pushButton.emit('START',True)
        self.update_textTAB1.emit(1,str(GAME_number))
        self.update_textTAB2.emit(time.strftime("%d %B %Y  %X", time.localtime()) + ' STOP PROGRAMM', 255, 0, 255)
        logger.warning(
            time.strftime("%d %B %Y  %X", time.localtime()) + ' STOP PROGRAMM')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())