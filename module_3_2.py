def send_email(message, recipient, sender = "university.help@gmail.com"):
    for i in recipient:
        if any(i not in recipient for i in ['@', '.com', '.ru', '.net']):
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
            return
        elif recipient == sender:
            print("Нельзя отправить письмо самому себе!")
            return
        elif recipient != sender:
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
            return
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
            return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')




