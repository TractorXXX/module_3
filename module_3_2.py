def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    p = len(recipient)
    p_1 = len(sender)
    a = recipient.find('.com', p - 4)
    b = recipient.find('.ru',  p - 3)
    c = recipient.find('.net', p - 4)
    a_1 = sender.find('.com', p_1 - 4)
    b_1 = sender.find('.ru',  p_1 - 3)
    c_1 = sender.find('.net', p_1 - 4)
    if (a != -1 or b != -1 or c != -1) and (a_1 != -1 or b_1 != -1 or c_1 != -1):
        flag_1 = True    # Флаг проверки окончания адреса
    else:
        flag_1 = False

    if '@' in recipient and '@' in sender and flag_1:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')