# Задача №3
# ===============================================
# В процедурном виде (весь код в одной процедуре)
# ===============================================
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# 	1. На вход обменнику вводишь количество денег int.
# 	2. На выходе в консоль выводится отввет в таком виде:
# 				"Ты ввёл int (Валюта)"
# 				"конвертированная сумма в USD = int"
# 				"конвертированная сумма в EUR = int"
# 				"конвертированная сумма в CHF = int"
# 				"конвертированная сумма в GBP = int"
# 				"конвертированная сумма в CNY = int"
#
# 	3. Скипт должен выдать сообщение
# 				"Введите положительное число." Если число меньше 0.
# 				"Вы ввели не число. Введите число." Если введены буквы.
# 				"Вы ввели пустое поле. Введите число." Если введено пустое значение.
# 	4. Валюту пользователя определите сами.

import time

def justDo():

    while True:

        inputValue = input('Введите число BYN конвертации в другие валюты. BYN : ')

        if not inputValue.isdigit() and len(inputValue) == 0:

            print('Вы ввели пустое поле. Введите число')

        else:

            for i in inputValue:

                print('Некорректный ввод')

                if not inputValue.isdigit() and i[0] == '-':

                    print('Введите положительное число')

                elif 'a' <= i <= 'z':

                    print('Вы ввели не число. Введите число')

        if inputValue.isdigit() and inputValue[0] != '-':

            usd = float(inputValue) * 2.58

            eur = float(inputValue) * 2.96

            chf = float(inputValue) * 2.8

            gbp = float(inputValue) * 3.5

            cny = float(inputValue) * 0.40473

            print('Ты ввёл', inputValue, 'BYN')

            print('Конвертированная сумма в USD =', usd)

            print('Конвертированная сумма в EUR =', eur)

            print('Конвертированная сумма в chf =', chf)

            print('Конвертированная сумма в GBP =', gbp)

            print('Конвертированная сумма в CNY =', cny)

            time.sleep(4)

            break

justDo()