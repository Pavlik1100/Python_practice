# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

import time

def convert(byn):

    usd = float(byn) * 2.58

    eur = float(byn) * 2.96

    chf = float(byn) * 2.8

    gbp = float(byn) * 3.5

    cny = float(byn) * 0.40473

    print('Ты ввёл', byn, 'BYN')

    print('Конвертированная сумма в USD =', usd)

    print('Конвертированная сумма в EUR =', eur)

    print('Конвертированная сумма в chf =', chf)

    print('Конвертированная сумма в GBP =', gbp)

    print('Конвертированная сумма в CNY =', cny)

while True:

    inputValue = input('Введите число BYN конвертации в другие валюты. BYN : ')

    if inputValue.isdigit():

        convert(inputValue)

        time.sleep(4)

        break

    else:

        print('Введен неверный формат, введите число BYN для конвертации')