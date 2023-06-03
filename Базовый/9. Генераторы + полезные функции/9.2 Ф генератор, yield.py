"""Функция-генератор. Оператор yield"""

# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x
#
# a = get_list()
# for x in a:
#     print(x)

# def get_list():
#     for x in range(1, 10):
#         a = range(x, 11)
#         yield sum(a)/len(a)

# поиск индексов слов в файле
# def find_word(f, word):
#     g_index = 0
#     for line in f:
#         indx = 0
#         while(indx != -1):
#             indx = line.find(word, indx)
#             if indx > -1:
#                 yield g_index + indx
#                 indx += 1
#         g_index += len(line)
#
#
# try:
#     with open("маринина.txt", encoding="windows-1251") as file:
#         a = find_word(file, "уже")
#         print(list(a))
# except FileNotFoundError:
#     print("Файл не найден")
# except:
#     print("Ошибка обработки файла")


"""Подвиг 1. Вводится натуральное число N. 
Необходимо определить функцию-генератор с именем get_sum, 
которая бы возвращала текущую сумму чисел последовательности 
длины N в диапазоне целых чисел [1; N]. Например:

- для первого числа 1 сумма равна 1;
- для второго числа 2 сумма равна 1+2 = 3
....
- для N-го числа сумма равна 1+2+...+(N-1)+N

Реализовать функцию-генератор get_sum без использования коллекций. 
Вызывать ее не нужно, только определить.

Sample Input:

5
Sample Output:

1 3 6 10 15"""

# a = 5
# def get_sum(a, c=0):
#     for i in range(1, a+1):
#         c += i
#         yield c
#
# d = get_sum(a)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


"""Подвиг 2. Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи,
 которая строится по правилу: каждое последующее число равно сумме двух предыдущих. 
 Для разнообразия давайте будем генерировать каждое последующее как сумму трех предыдущих чисел. 
 При этом первые три числа равны 1 и имеем такую последовательность:

1, 1, 1, 3, 5, 9, 17, 31, 57, ...

Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева. 

Итак, на вход программы поступает натуральное число N (N > 5) и необходимо определить функцию-генератор, 
которая бы возвращала N первых чисел последовательности Балакирева (включая первые три единицы).

Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.). 
Вызовите ее N раз для получения N чисел и выведите полученные числа на экран в одну строчку через пробел.

Sample Input:

7
Sample Output:

1 1 1 3 5 9 17"""
# n = int(input())
#
# def get_fib_balakirev(n):
#     a = 1
#     yield a
#     b = 1
#     yield b
#     c = 1
#     yield c
#     for i in range(n-3):
#         a, b, c, = b, c, a + b + c
#         yield c
#
# s = get_fib_balakirev(n)
# for i in s:
#     print(i, end=" ")


"""Подвиг 3. Вводится натуральное число N (N > 8). 
Необходимо определить функцию-генератор, 
которая бы выдавала пароль длиной N символов из случайных букв, 
цифр и некоторых других знаков. Для получения последовательности 
допустимых символов для генерации паролей в программе 
импортированы две строки: 
ascii_lowercase, ascii_uppercase (см. листинг ниже), 
на основе которых формируется общий список:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
Функция-генератор должна при каждом вызове возвращать 
новый пароль из случайно выбранных символов chars длиной N и 
делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. 
Сгенерировать случайный индекс indx в диапазоне [a; b] 
для символа можно с помощью функции randint модуля random:

import random
random.seed(1)
indx = random.randint(a, b)
Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).

Sample Input:

10
Sample Output:

riGp?58WAm
!dX3a5IDnO
dcdbWB2d*C
4?DSDC6Lc1
mxLpQ@2@yM"""

# from string import ascii_lowercase, ascii_uppercase
# import random
#
# random.seed(1)
# n = 10
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# def sword_fish(n, s=""):
#     a = 0
#     b = len(chars) - 1
#     for i in range(n):
#         indx = random.randint(a, b)
#         s += chars[indx]
#     yield s
# for i in range(5):
#     s = sword_fish(n)
#     for i in s:
#         print(i)


"""Для формирования случайного индекса для строки chars используйте функцию randint модуля random:

import random
random.seed(1)
indx = random.randint(0, len(chars)-1)
Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно. 
Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).

Sample Input:

8
Sample Output:

iKZWeqhF@mail.ru
WCEPyYng@mail.ru
FbyBMWXa@mail.ru
SCrUZoLg@mail.ru
ubbbPIay@mail.ru"""


# from string import ascii_lowercase, ascii_uppercase
# import random
#
# random.seed(1)
# n = 8
# chars = ascii_lowercase + ascii_uppercase
# def sword_fish(n, s=""):
#     a = 0
#     b = len(chars) - 1
#     for i in range(n):
#         indx = random.randint(a, b)
#         s += chars[indx]
#     yield s
# for i in range(5):
#     s = sword_fish(n)
#     for i in s:
#         print(i+"@mail.ru")

"""Подвиг 5. Определите функцию-генератор, 
которая бы возвращала простые числа. 
(Простое число - это натуральное число, которое делится только на себя и на 1). 
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел."""

# https://habr.com/ru/post/122538/ - Варианты решенией

# def get_simple_num(n=2):
#     while True:
#         if all((n % i) for i in range(2, int(n ** 0.5) + 1)):
#             yield n
#         n += 1
#
#
# gen = get_simple_num()
# print(*(next(gen) for _ in range(20)))


# def get_simple(n = 100):
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 n += 1
#                 break
#         else:
#             yield i
#             n += 1
#
# a = get_simple()
# print(*(next(a) for _ in range(20)))
#
# def gen(n=2):
#     while True:
#         for i in range(2, n):
#             if n % i == 0:
#                 n += 1
#                 break
#         else:
#             yield n
#             n += 1
#
# p = gen()
# for i in range(20):
#     print(next(p), end = ' ' )