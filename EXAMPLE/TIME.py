from datetime import timedelta, datetime

from BUTTON_Find_Click import BUTTON_Find_Click


def WAIT(sec):

    timeStart = datetime.now()
    timeFinish = datetime.now() + timedelta(seconds=sec)
    print(timeStart)
    print(timeFinish)


    while timeStart<timeFinish:
        timeStart=datetime.now()



    print(datetime.now())


WAIT(10)


