result = 0
while True:
    try:
        ticket_cnt = input('Введите необходимое количество билетов: ')
        ticket_cnt = int(ticket_cnt)
        if type(ticket_cnt) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_cnt):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'Для какого возраста билет #{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                result += 990
                print('Стоимость билета - 990 руб.')
            else:
                result += 1390
                print('Стоимость билета - 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_cnt > 3:
    result_skidka = result - ((result / 100) * 10)
    print(f'Сумма к оплате - {result_skidka} руб. с учетом скидки 10% за количество билетов от 3-x')
else:
    print(f'Сумма к оплате - {result} руб.')
