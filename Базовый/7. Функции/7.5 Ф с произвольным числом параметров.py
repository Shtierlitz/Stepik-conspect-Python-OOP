"""7.5 Функции с произвольным числом параметров"""




"""Подвиг 3. Объявите функцию с именем get_even, которая принимает произвольное количество 
чисел в качестве аргументов и возвращает список, составленный только из четных переданных значений.

Функцию выполнять не нужно, только определить.

Sample Input:

45 4 8 11 12 0
Sample Output:

4 8 12 0"""

# Мой вариант
# def get_even(*args):
#     s = args
#     lst = []
#     for i in s:
#         if int(i) == 0:
#             lst.append(int(i))
#         elif int(i) % 2 == 0:
#             lst.append(int(i))
#     return lst

# чужой
# def get_even(*args):
#     return [i for i in args if i % 2 == 0]

# print(get_even(45, 4, 8, 11, 12, 0))


"""Подвиг 4. Объявите функцию с именем get_biggest_city, 
которой можно передавать произвольное количество названий городов через аргументы. 
Данная функция должна возвращать название города наибольшей длины. Если таких городов несколько, 
то первый найденный (из наибольших). Программу реализовать без использования сортировки.

Функцию выполнять не нужно, только определить.

Sample Input:

Питер Москва Самара Воронеж
Sample Output:

Воронеж"""

# def get_biggest_city(*args):
#     s = [i for i in args if i == max(args, key=len)]
#     return "".join(s)
#
# print(get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж'))


"""Подвиг 5. Объявите функцию с именем get_data_fig для вычисления периметра произвольного 
N-угольника. На вход этой функции передаются N длин сторон через аргументы. 
Дополнительно могут быть указаны именованные аргументы:

type - булево значение True/False
color - целое числовое значение
closed - булево значение True/False
width - целое значение

Функция должна возвращать в виде кортежа периметр многоугольника и 
указанные значения именованных параметров в порядке их перечисления в 
тексте задания (если они были переданы). Если какой-либо параметр отсутствует, 
его возвращать не нужно (пропустить).

Функцию выполнять не нужно, только определить."""

# Мой вариант, не прошел, но работает
# def get_data_fig(*args, **kwargs):
#     P = sum(args)
#     tup = ()
#     tup += P,
#
#     K = ["type", "color", "closed", "width"]
#     lst = []
#     for i, j in kwargs.items():
#         for s in range(len(K)):
#             if i == K[s]:
#                 lst.insert(s, j)
#     for q in lst:
#         tup += q,
#     return tup
#
# print(get_data_fig(5, 4, 9, 9, 9, 9, closed=True, width=10))
# print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
# print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))
#
# Чужой
# def get_data_fig(*args, **kwargs):
#     s = sum(args)
#     d = {'s': s, 'type': None, 'color': None, 'closed': None, 'width': None}
#     for i in kwargs:
#         d[i] = kwargs[i]
#     lst = []
#     for j in d.values():
#         if j != None:
#             lst.append(j)
#     return tuple(lst)
#
# print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))

# Мой - чужой
# def get_data_fig(*args, **kwargs):
#     P = sum(args)
#     tup = P,
#     K = ["type", "color", "closed", "width"]
#     for s in range(len(K)):
#         if K[s] in kwargs.keys():
#             tup += kwargs[K[s]],
#
#     return tup
#
# #
# print(get_data_fig(5, 4, 9, 9, 9, 9, closed=True, width=10))
# print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
# print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))


"""Большой подвиг 6. (Для закрепления предыдущего материала). 
Вводится таблица целых чисел (см. пример ниже) размером N x N элементов 
(N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы. 
С помощью функции с именем verify, на вход которой передается двумерный список чисел, 
необходимо проверить, являются ли единицы изолированными друг от друга, то есть, 
вокруг каждой единицы должны быть нули.

Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка. 
Для каждого элемента (списка) со значением 1 вызывать еще одну вспомогательную функцию is_isolate 
для проверки изолированности единицы. То есть, функция is_isolate должна возвращать True, 
если единица изолирована и False - в противном случае.

Как только встречается не изолированная единица, функция verify должна возвращать False. 
Если успешно доходим (по элементам списка) до конца, то возвращается значение True.

Функцию выполнять не нужно, только определить.

P. S. При реализации функции is_isolate не следует прописывать восемь операторов if. 
Подумайте, как это можно сделать красивее (с точки зрения реализации алгоритма). 

Sample Input:

1 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
Sample Output:

True"""

# Мой вариат и правильный) Таки получилось)
# def is_isolate(lst_in, i, j):
#     if lst_in[i][j] == 1 and lst_in[i - 1][j] == 1:
#         return False
#     elif lst_in[i][j - 1] == 1 and lst_in[i - 1][j] == 1:
#         return False
#     elif lst_in[i][j] == 1 and lst_in[i - 1][j - 1] == 1:
#         return False
#     elif lst_in[i][j] == 1 and lst_in[i - 1][j - 1] == 1:
#         return False
#
# def verify(lst):
#     lst_in = lst
#     for i in lst:
#         print(i, end=" ")
#         print()
#     for i in range(1, len(lst_in)):
#         for j in range(len(lst_in[i])):
#             if lst_in[i][j] == 1:
#                 count = is_isolate(lst_in, i, j)
#                 if count == False:
#                     return False
#     return True

# Чужой непонятный
# def verify(args):
#     limit = len(args)
#     for i in range(limit):
#         for j in range(limit):
#             if args[i][j] == 1 and is_isolate(args, i, j, limit) == False:
#                 return False
#     return True
#

# def is_isolate(args, i, j, limit):
#     row1 = sum(args[i][j:j+2])
#     print(row1)
#     row2 = sum(args[i+1][(0 if j == 0 else j-1):j+2]) if i != limit-1 else 0
#     print(row2)
#     if row1 + row2 > 1:
#         return False
#     return True
# print(verify([[0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]))
# print(verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]))


"""Значимый подвиг 7. (Для закрепления предыдущего материала). 
Объявите функцию с именем str_min, 
которая сравнивает две переданные строки и возвращает минимальную из них 
(то есть, выполняется лексикографическое сравнение строк). 
Затем, используя функциональный подход к программированию 
(то есть, более сложные функции реализуются путем вызова более простых), 
реализовать еще две аналогичные функции:

- с именем str_min3 для поиска минимальной строки из трех переданных строк;
- с именем str_min4 для поиска минимальной строки из четырех переданных строк.

Выполнять функции не нужно, только записать."""


# Мой вариант (бессмыслица) Просто "лексикографическое сравнивание это как раз не по длине, а по упорядочености символов
# def str_min(*args):
#     if len(args) == 3:
#         a, b, c = args
#         result = str_min3(a, b, c)
#         return result
#     elif len(args) == 3:
#         a, b, c, d = args
#         result = str_min4(a, b, c, d)
#         return result
#     else:
#         m_str = min(args)
#         return m_str
#
#
# def str_min3(a, b, c):
#     m_str = min(a, b, c)
#     return m_str
# def str_min4(a, b, c, d):
#     m_str = min(a, b, c, d)
#     return m_str

# Как надо было
# def str_min(*args):
#     m_str = min(args)
#     return m_str
#
# def str_min3(*args):
#     m_str = min(args)
#     return m_str
#
# def str_min4(*args):
#     m_str = min(args)
#     return m_str
#
# print(str_min("sergey", "balakirev"))