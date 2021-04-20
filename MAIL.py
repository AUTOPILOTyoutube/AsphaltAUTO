#Чтобы отправить письмо необходимо отключить двухэтапную аутентификацию в настройках почтового ящика
#Необходимо отключить всю безопасность в настройках почтового ящика

import smtplib, ssl


def senderMAIL():
    try:
        # Открываем текстовый файл и считываем строки в массив
        with open('mail.txt') as fp:
            lines = fp.readlines()


        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = lines[0]  # Считываем имя почтового ящика из текстового файла
        password = lines[1] # Считываем пароль к почтовому ящику
        receiver_email = lines[2]  # Считываем На какой почтовый ящик отправлять письмо

        message = """Subject: AUTOPILOT STOP!!!"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        print('Не получилось отправить почту')
if __name__ == '__main__':
    senderMAIL()
