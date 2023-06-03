"Замыкание"
# def say_name(name):
#     def say_goodby():
#         print("Don't say me goodby, " + name + "!")
#
#     return say_goodby
#
# f = say_name("Sunrise")
# f2 = say_name("Igrerio")
# f()
# f2()

# def counter(start=0):
#     def step():
#         nonlocal start  # нужно чтобы ее обьявить ниже. Ибо в в нее может ничего и не передаваться
#         start += 1
#         return start
#     return step
#
# c1 = counter(10)
# c2 = counter()
# print(c1(), c2())   # 11 1
# print(c1(), c2())   # 12 2
# print(c1(), c2())   # 13 3

# def strip_string(strip_chars=" "):
#     def do_strip(string):
#         return string.strip(strip_chars)
#     return do_strip
#
# strip1 = strip_string()
# strip2 = strip_string(" !?,.;")
# print(strip1(" hello python!.. "))
# print(strip2(" hello python!.. "))

"""Подвиг 1. Используя замыкания функций, определите вложенную функцию, 
которая бы увеличивала значение переданного параметра на 5 и возвращала бы вычисленный результат. 
При этом внешняя функция должна иметь следующую сигнатуру:

def counter_add(): ...

Вызовите функцию counter_add и результат ее работы присвойте переменной с именем cnt. 
Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:

k = int(input())

Выведите результат на экран.

Sample Input:

7
Sample Output:

12"""

# def counter_add():
#     def new_add(add):
#         add += 5
#         return add
#     return new_add
#
# k = int(input())
# a1 = counter_add()
# print(a1(k))


"""Подвиг 2. Используя замыкания функций, объявите внутреннюю функцию, 
которая увеличивает значение своего аргумента на некоторую величину n - параметр внешней функции с сигнатурой:

def counter_add(n): ...

Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
 Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:

k = int(input())

Выведите результат на экран.

Sample Input:

5
Sample Output:

7"""

# def counter_add(n):
#     def new_add(s):
#         nonlocal n
#         n += s
#         return n
#     return new_add
#
# k = int(input())
# cnt = counter_add(2)
# print(cnt(k))

"""Подвиг 3. Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s (s - строка, параметр внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного замыкания. Результат выведите на экран.

P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>

Sample Input:

Balakirev
Sample Output:

<h1>Balakirev</h1>"""

# def teg_string():
#     def teg(s):
#         s = f"<h1>{s}</h1>"
#         return s
#     return teg
# inp = input()
# a = teg_string()
# print(a(inp))

"""Подвиг 4. Используя замыкания функций, 
объявите внутреннюю функцию, которая заключает строку s 
(s - строка, параметр внутренней функции) в произвольный тег, 
содержащийся в переменной tag - параметре внешней функции. 

Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым. 
Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания. 
Результат выведите на экран.

P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>

Sample Input:

div
Сергей Балакирев
Sample Output:

<div>Сергей Балакирев</div>"""

# def cool_tag(tag):
#     def string(s):
#         nonlocal tag
#         j = f"<{tag}>"
#         q = f"</{tag}>"
#         return f"{j}{s}{q}"
#     return string
# div = input()
# name = input()
# a1 = cool_tag(div)
# print(a1(name))

"""Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, 
которая преобразует строку из списка целых чисел, 
записанных через пробел, либо в список, либо в кортеж. 
Тип коллекции определяется параметром tp внешней функции. 
Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.

Далее, на вход программы поступают две строки: первая - это значение для параметра tp; 
вторая - список целых чисел, записанных через пробел. 
С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию. 
Результат вывести на экран командой (lst - ссылка на коллекцию):

print(lst)

Sample Input:

list
-5 6 8 11 0 111 -456 3
Sample Output:

[-5, 6, 8, 11, 0, 111, -456, 3]"""

# def changer(tp=None):
#     def list_or_tup(lst):
#         nonlocal tp
#         if tp == "list":
#             pass
#         else:
#             tup = ()
#             for x in lst:
#                 tup += x,
#             lst = tup
#         return lst
#     return list_or_tup
#
# tp = input()
# lst = list(map(int, input().split()))
# # lst = [-5, 6, 8, 11, 0, 111, -456, 3]
# a1 = changer(tp)
# print(a1(lst))