# HW_2-Arithmetic_operations
## [arithmetic.py](https://github.com/Pavlik1100/Python_practis_on_course_Vadim_Ksendzov/blob/main/HW_2-Arithmetic_operations/arithmetic.py) |-|-| [arithmetic_2.py](https://github.com/Pavlik1100/Python_practis_on_course_Vadim_Ksendzov/blob/main/HW_2-Arithmetic_operations/arithmetic_2.py) |-|-| [boolean.py](https://github.com/Pavlik1100/Python_practis_on_course_Vadim_Ksendzov/blob/main/HW_2-Arithmetic_operations/boolean.py)
## Part 1 - Arithmetic operations [arithmetic.py](https://github.com/Pavlik1100/Python_practis_on_course_Vadim_Ksendzov/blob/main/HW_2-Arithmetic_operations/arithmetic.py) 
1. Создать переменную `item_1` типа `integer`.
```py
item_1 = 10
```
2. Создать переменную `item_2` типа `integer`.
```py
item_2 = 20
```
3. Создать переменную `result_sum` в которой вы суммируете `item_1` и `item_2`.
```py
result_sum = item_1 + item_2
```
4. Вывести `result_sum` в консоль.
```py
print('result_sum =', result_sum)
```
5. Создать переменную `result_subtr` в которой вы вычитаете большую по значению переменную из меньшей по значению.
```py
result_subtr = item_2 - item_1
```
6. Вывести `result_subtr` в консоль.
```py
print('result_subtr =', result_subtr)
```
7. Создать переменную `result_multi` в которой вы умножаете `item_1` на `item_2`.
```py
result_multi = item_1 * item_2
```
8. Вывести `result_multi` в консоль.
```py
print('result_multi =', result_multi)
```
9. Создать переменную `result_exp` в которой вы `item_1` возводите в степень `item_2`.
```py
result_exp = item_1 ** item_2
```
10. Вывести `result_exp` в консоль.
```py
print('result_exp =', result_exp)
```
11. Создать переменную `result_m_exp` в которой вы `item_1` возводите в степень `item_2` используя библиотеку `math`.
```py
import math
result_m_exp = math.pow(item_1, item_2)
```
12. Вывести `result_m_exp` в консоль.
```py
print('result_m_exp =', result_m_exp)
```
13. Создать переменную `result_s_root` в которой вы найдёте квадратный корень любой из переменной `item`
```py
result_s_root = item_2 ** (0.5)
```
14. Вывести `result_s_root` в консоль.
```py
print('result_s_root = ', result_s_root)
```
15. Создать переменную `result_m_s_root` в которой вы найдёте квадратный корень любой из переменной `item` используя библиотеку `math`.
```py
result_m_s_root = math.sqrt(item_2)
```
16. Вывести `result_m_s_root` в консоль.
```py
print('result_m_s_root =', result_m_s_root)
```
17. Создать переменную `result_mp_s_root` в которой вы найдёте квадратный корень любой из переменной `item` используя библиотеку `math` используя метод `pow`.
```py
result_mp_s_root = math.pow(item_2, 0.5)
```
18. Вывести `result_mp_s_root` в консоль.
```py
print('result_mp_s_root =', result_mp_s_root)
```
19. Присвоить переменной `item_1` odd значение
```py
item_1 = 11
```
20. Присвоить переменной `item_2` even значение
```py
item_2 = 4
```
21. Создать переменную `result_division` в которой вы разделите `item_1` на `item_2`.
```py
result_division = item_1 / item_2
```
22. Вывести `result_division` в консоль.
```py
print('result_division =', result_division)
```
23. Создать переменную `result_m_floor` и `result_division` округлить до ближайшего целого меньшего чем `result_division`.
```py
result_m_floor = math.floor(result_division)
```
24. Вывести `result_m_floor` в консоль.
```py
print('result_m_flor =', result_m_floor)
```
25. Создать переменную `result_m_ceil` и округлить до ближайшего целого большего чем `result_division`.
```py
result_m_ceil = math.ceil(result_division)
```
26. Вывести `result_m_ceil` в консоль.
```py
print('result_m_ceil =', result_m_ceil)
```
27. Создать переменную `result_int` и округлить до ближайшего целого через явное приведение.
```py
result_int = int(result_division)
```
28. Вывести `result_int` в консоль.
```py
print('result_int =', result_int)
```
29. Создать переменную `result_no_division_loss` в которой вы разделите `item_1` на `item_2` без остатка.
```py
result_no_division_loss = item_1 // item_2
```
30. Вывести `result_no_division_loss` в консоль.
```py
print('result_no_division_loss =', result_no_division_loss)
```
31. Создать переменную `result_division_loss` в которой вы найдёте остаток от деления `item_1` на `item_2`.
```py
result_division_loss = item_1 % item_2
```
32. Вывести `result_division_loss` в консоль.
```py
print('result_division_loss =', result_division_loss)
```
## Part 2 - Arithmetic operations [arithmetic_2.py](https://github.com/Pavlik1100/Python_practis_on_course_Vadim_Ksendzov/blob/main/HW_2-Arithmetic_operations/arithmetic_2.py)
# Дальше будет реализация через арифметические действия с присваиванием.
33. Создать переменную `item_3` и присвоить ей целое число
```py
item_3 = 4
```
34. Прибавить `10` к `item_3` с присвоением.
```py
item_3 += 10
```
35. Вывести `item_3` в консоль.
```py
print('item_3 =', item_3)
```
36. Отнять `5` от `item_3` с присвоением.
```py
item_3 -= 5
```
37. Вывести `item_3` в консоль.
```py
print('item_3 =', item_3)
```
38. Умножить `item_3` на `3` с присвоением.
```py
item_3 *= 3
```
39. Вывести `item_3` в консоль.
```py
print('item_3 =', item_3)
```
40. Разделить `item_3` на `2` с присвоением.
```py
item_3 /= 2
```
41. Вывести `item_3` в консоль.
```py
print('item_3 =', item_3)
```
42. Возвести в степень `2` `item_3` с присвоением.
```py
item_3 **= 2
```
43. Вывести `item_3` в консоль.
```py
print('item_3 =', item_3)
```
44. Найти квадратный корень `item_3` с присвоением.
```py
item_3 **= 0.5
```
45. Вывести `item_3` в консоль.
```py
print('item_3 =', item_3)
```
46. Присвоить остаток от деления `item_3`
```py
item_3 %= 13
```
47. Вывести `item_3` в консоль.
```py
print('item_3 =', item_3)
```
## Part 3 - Arithmetic operations with boolean type [boolean.py](https://github.com/Pavlik1100/Python_practis_on_course_Vadim_Ksendzov/blob/main/HW_2-Arithmetic_operations/boolean.py)
# Boolean
48. Создать переменную `b_item_t` и присвоить `True`
```py
b_item_t = True
```
49. Создать переменную `b_item_f` и присвоить `False`
```py
b_item_f = False
```
50. Создать переменную `b_item_relult_sum` и присвоить сумму `b_item_t` и `b_item_f`
```py
b_item_result_sum = b_item_f + b_item_t
```
51. Вывести `b_item_relult_sum` в консоль.
```py
print('b_item_reslt_sum =', b_item_result_sum)
```
52. Создать переменную `b_item_relult_subtr` и присвоить разницу `b_item_t` и `b_item_f`
```py
b_item_result_subtr = b_item_t - b_item_f
```
53. Вывести `b_item_relult_subtr` в консоль.
```py
print('b_item_result_subtr =', b_item_result_subtr)
```
54. Создать переменную `b_item_relult_multi` и присвоить умножение `b_item_t` и `b_item_f`
```py
b_item_result_multi = b_item_t * b_item_f
```
55. Вывести `b_item_relult_multi` в консоль.
```py
print('b_item_result_multi =', b_item_result_multi)
```
56. Создать переменную `b_item_relult_division` и присвоить деление `b_item_t` и `b_item_f`
```py
b_item_result_decision = b_item_t / b_item_f
```
57. Вывести `b_item_relult_division` в консоль. (Получить ошибку)
```py
#  print('b_item_result_decision', b_item_result_decision)
```
58. Создать переменную `b_item_1_int` и присвоить явное приведение `b_item_t` к `int`
```py
b_item_1_int = int(b_item_t)
```
59. Вывести `b_item_1_int` в консоль.
```py
print('b_item_1_int =', b_item_1_int)
```
60. Создать переменную `b_item_2_int` и присвоить явное приведение `b_item_2` к `int`
```py
b_item_2_int = int(b_item_f)
```
61. Вывести `b_item_2_int` в консоль.
```py
print('b_item_2_int =', b_item_2_int)
```
