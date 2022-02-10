# Задача №4
# ===============================================
# В процедурном виде (весь код в одной процедуре)
# ===============================================
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.

import time

def justDo():

    while True:

        print("Конвертация BYN в одну из выбранных ['USD','EUR','CHF','GBP','CNY']")

        inputValueV = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY'] :")

        if inputValueV == 'USD' or inputValueV == 'EUR' or inputValueV == 'CHF' or inputValueV == 'GBP' or inputValueV == 'CNY':

            inputValue = input('Введите сумму BYN для конвертации : ')

            if not inputValue.isdigit() and len(inputValue) == 0:

                print('Вы ввели пустое поле. Введите число')

            else:

                for i in inputValue:

                    if not inputValue.isdigit() and i[0] == '-':

                        print('Некорректный ввод числа')

                        print('Введите положительное число')

                    elif 'a' <= i <= 'z':

                        print('Некорректный ввод числа')

                        print('Вы ввели не число. Введите число')

            if inputValue.isdigit() and inputValue[0] != '-':

                print("Вы ввели СУММУ : ВАЛЮТЫ =", inputValue, ': BYN')

                if inputValueV == 'USD':

                    usd = float(inputValue) * 2.58

                    print("Конвертированная СУММА : ВАЛЮТА =", usd, ':', inputValueV)

                elif inputValueV == 'EUR':

                    eur = float(inputValue) * 2.96

                    print("Конвертированная СУММА : ВАЛЮТА =", eur, ':', inputValueV)

                elif inputValueV == 'CHF':

                    chf = float(inputValue) * 2.8

                    print("Конвертированная СУММА : ВАЛЮТА =", chf, ':', inputValueV)

                elif inputValueV == 'GBP':

                    gbp = float(inputValue) * 3.5

                    print("Конвертированная СУММА : ВАЛЮТА =", gbp, ':', inputValueV)

                elif inputValueV == 'CHY':

                    cny = float(inputValue) * 0.40473

                    print("Конвертированная СУММА : ВАЛЮТА =", cny, ':', inputValueV)

                time.sleep(4)

                break

        else:

            print('Некорректный ввод валюты')

justDo()