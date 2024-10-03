def send_email(message, recipient):
    sender = "university.help@gmail.com"
    for i in message:
        if i != '@' or i != '.com':
            print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")

# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# 1. Если строки recipient or sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# 2. Если же sender == recipient , то вывести "Нельзя отправить письмо самому себе!"
# 3. Если же отправитель по умолчанию - university.help@gmail.com, то вывести
# сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# 4. В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ
# ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
#   Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#   За один вызов функции выводится только одно и перечисленных
# уведомлений! Проверки перечислены по мере выполнения.
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
sender='urban.teacher@mail.ru')

# print("Нельзя отправить письмо самому себе!")
# print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
# print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")

