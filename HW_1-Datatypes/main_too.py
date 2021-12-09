# 1) Создать переменную типа String
a = "Hello"

# 2) Создать переменную типа Integer
b = 2

# 3) Создать переменную типа Float
c = 3.0

# 4) Создать переменную типа Bytes
d = bytes(94)

# 5) Создать переменную типа List
e = [1, 2, 3]

# 6) Создать переменную типа Tuple
f = (4, 5, 6)

# 7) Создать переменную типа Set
g = set('hello')

# 8. Создать переменную типа Frozen set
h = frozenset("Hello")

# 9) Создать переменную типа Dict
i = {1:'yes', 2:'no'}


# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
j = 'Hello'
k = 'World'
l = j+k
print(l)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print (b, l)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
m = str(b)
print(m+l)