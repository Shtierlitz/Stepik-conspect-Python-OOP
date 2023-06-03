"""5.6 Вложенные циклы"""




"""Подвиг 1. Вводится натуральное число N (то есть, положительное, целое). 
Требуется создать двумерный (вложенный) список размером N x N элементов, состоящий из всех единиц,
 а затем, в последний столбец записать пятерки. Вывести этот список на экран 
 в виде таблицы чисел, как показано в примере ниже.

P.S. Будьте внимательны в конце строк пробелов быть не должно!

Sample Input:

4
Sample Output:

1 1 1 5
1 1 1 5
1 1 1 5
1 1 1 5"""

N = 5
# N = int(input())
ones = []
for i in range(N):
    ones.append([1] * N)
for i in range(len(ones)):
    for j in range(len(ones)):
        ones[i][N-1] = 5
for r in ones:
    for x in r:
        print((str(x)+" " if x != r[-1] else str(x)), end="")
    print()
# for r in ones:
#     for x in r:
#         if x != r[-1]:
#             print(str(x) + " ", end="")
#         else:
#             print(str(x), end="")
#     print()






# N = 4
# zeros = []
# for i in range(N):
#     zeros.append([0] * N)
# for i in range(len(zeros)):
#     for j in range(len(zeros)):
#         zeros[j][i] = 0
# print(zeros)





"""Подвиг 2. Вводится список из URL-адресов (каждый с новой строки). 
Требуется в них заменить все пробелы на символ дефиса (-). 
Следует учесть, что может быть несколько подряд идущих пробелов. 
Результат преобразования вывести на экран в виде строк из URL-адресов.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

django chto  eto takoe    poryadok ustanovki
model mtv   marshrutizaciya funkcii  predstavleniya
marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya
Sample Output:

django-chto-eto-takoe-poryadok-ustanovki
model-mtv-marshrutizaciya-funkcii-predstavleniya
marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya"""

import sys

# # считывание списка из входного потока
# # lst_in = ['django chto  eto takoe    poryadok ustanovki',
# #           'model mtv   marshrutizaciya funkcii  predstavleniya',
# #           'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = None
# lst = []
# for j, line in enumerate(lst_in):
#     b = line.split()
#     d = "-".join(b)
#     lst.append(d)
# for i in lst:
#     print(i)

# еще вариант
# lst_in = ['django chto  eto takoe    poryadok ustanovki',
#           'model mtv   marshrutizaciya funkcii  predstavleniya',
#           'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# for i, line in enumerate(lst_in):
#     while line.count("  "):
#         line = "-".join(line.split())
#     lst_in[i] = line
#     print(line, end="\n")

"""Базовый шаблон формирования вложеных списков"""
# N = 4
# M = 4
# P = 10
# a  = []
#
# for n in range(N):
#    a.append([])
#    for m in range(M):
#       a[n].append([])
#       for p in range(P):
#           a[n][m].append(1)
# print(a)

"""задача Жени"""
# import random
# N = 4
# M = 4
# P = 10
# a  = []
# b = []
#
# for n in range(N):
#    a.append([])
#    for m in range(M):
#       a[n].append([])
#       for p in range(P):
#           a[n][m].append(random.randint(1, 10))
# # for i in a:
# #     print(i)
#
# for n in range(N):
#    b.append([])
#    for m in range(M):
#       b[n].append([])
#       for p in range(P):
#           b[n][m].append(a[n][m][p] - a[n][n][p])
#
# # for i in b:
# #     print(i)
# print(b[n])


"""Подвиг 3. Вводится натуральное число n. 
Необходимо найти все простые числа, которые меньше этого числа n, то есть, в диапазоне [2; n). 
Результат вывести на экран в строчку через пробел.

Sample Input:

11
Sample Output:

2 3 5 7"""
# опачки. У for есть else
# lst = [2]
# N = int(input())
# for n in range(3, N):
#     for j in range(2, n):
#         if n % j == 0:
#             break
#     else:
#         lst.append(n)
# print(*lst)

"""Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и, 
в некоторых позициях, единиц (см. пример ввода ниже). 
Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали. 
То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести ДА, иначе - НЕТ.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

1 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
Sample Output:

ДА"""

# lst_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
import sys
# lst_in = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

# count = 0
# for i in range(len(lst_in)):
#     for j in range(1, len(lst_in)):
#         if lst_in[i][j] == 1 and lst_in[i-1][j] == 1 or lst_in[i][j] == 1 and lst_in[i-1][j-1] == 1:
#             count += 1
#         elif lst_in[i][j-1] == 1 and lst_in[i-1][j] == 1:
#             count += 1
#         elif lst_in[i][j] ==  1 and lst_in[i][j-1] == 1:
#             count += 1
#
#
# print("НЕТ" if count else "ДА")
# print(count)
# for i in lst_in:
#     print(i)




"""Подвиг 5. Вводится двумерный список размерностью 5 х 5 элементов, 
состоящий из целых чисел (пример ввода см. ниже). Проверьте, 
является ли этот двумерный список симметричным относительно главной диагонали. 
Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний. 
Выведите на экран ДА, если матрица симметрична и НЕТ - в противном случае.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

2 3 4 5 6
3 2 7 8 9
4 7 2 0 4
5 8 0 2 1
6 9 4 1 2
Sample Output:

ДА"""
# lst_in = [[2, 3, 4, 5, 6], [3, 2, 7, 8, 9], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# count = 0
# for i in range(len(lst_in)):
#     for j in range(i+1, len(lst_in)):
#         if lst_in[i][j] != lst_in[j][i]:
#             count += 1
# print("НЕТ" if count else "ДА")
# print(count)
# for i in lst_in:
#     print(i)


"""Большой подвиг 6. Вводится список целых чисел в одну строку через пробел. 
Необходимо выполнить его сортировку выбором по возрастанию (неубыванию). 
Идея алгоритма очень проста и проиллюстрирована на рисунке ниже.



Вначале мы рассматриваем первый элемент списка и ищем второй минимальный относительно 
первого элемента (включая и его). На рисунке - это последний элемент со значением -1. 
Затем, меняем местами первый и последний элементы. 
Переходим ко второму элементу списка и повторяем эту же процедуру,
 но относительно второго элемента (то есть, первый уже не рассматриваем). 
 На рисунке минимальный элемент - это 2, поэтому менять местами здесь ничего не нужно. 
 Переходим к 3-му элементы со значением 6. Относительно него находим минимальный элемент - это 3. 
 Меняем их местами. 

Вот идея алгоритма сортировки выбором. Реализуйте его для вводимого списка целых чисел. 
Результат выведите в виде списка чисел одну строку через пробел.

Sample Input:

8 11 -53 2 10 11
Sample Output:

-53 2 8 10 11 11"""

# lst = [8, 11, -53, 2, 10, 11]


# lst = [4, 5, 2, 0, 6, 3, -56, 3, -1]
# lst = list(map(int, input().split()))
# count = 0
# check = []
# while count < len(lst):
#     check.append(1)
#     for i in range(len(lst) -1):
#         check.append(1)
#         if lst[i+1] < lst[i]:
#             check.append(1)
#             lst[i], lst[i+1] = lst[i+1], lst[i]
#     count += 1
# print(*lst)
# print(len(check))

# Метод сортировки Женя
# lst = [4, 5, 2, 0, 6, 3, -56, 3, -1]
# for j in range(len(lst)-1):
#     num = lst[j+1]
#     index = j+1
#     for i in range(j+1, len(lst)):
#             if lst[i] < num:
#                 num = lst[i]
#                 index = i
#     if lst[j] > num:
#         lst[index], lst[j] = lst[j], lst[index]
# print(lst)

# print(len(check))
#
# lst = [4, 5, 2, 0, 6, 3, -56, 3, -1]
# lst = list(map(int, input().split()))
# change = 1
# check = []
# while change > 0:
#     check.append(1)
#     change = 0
#     for i in range(len(lst) - 1):
#         check.append(1)
#         if lst[i] > lst[i + 1]:
#             check.append(1)
#             lst[i], lst[i + 1] = lst[i + 1], lst[i]
#             change += 1
# print(*lst)
# print(len(check))

"""Подвиг 8. В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64. 
Вводится натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n? 
Вывести на экран список купюр для формирования суммы n (в одну строчку через пробел, 
начиная с наибольшей и заканчивая наименьшей). Предполагается, 
что имеется достаточно большое количество купюр всех достоинств.

Sample Input:

221
Sample Output:

64 64 64 16 8 4 1"""
# num = 221
# num = int(input())
# a64 = 64
# a32 = 32
# a16 = 16
# a8 = 8
# a4 = 4
# a2 = 2
# a1 = 1
#
# b64 = 0
# b32 = 0
# b16 = 0
# b8 = 0
# b4 = 0
# b2 = 0
# b1 = 0
#
# while num // a64 != 0:
#     num = num - a64
#     b64 += 1
# while num // a32 != 0:
#     num = num - a32
#     b16 += 1
# while num // a16 != 0:
#     num = num - a16
#     b16 += 1
# while num // a8 != 0:
#     num = num - a8
#     b8 += 1
# while num // a4 != 0:
#     num = num - a4
#     b4 += 1
# while num // a2 != 0:
#     num = num - a2
#     b2 += 1
# while num // a1 != 0:
#     num = num - a1
#     b1 += 1
# lst = [b64, b16, b8, b4, b1]
# if b64 != 0:
#     print("64 "*b64, end="")
# if b16 != 0:
#     print("16 "*b16, end="")
# if b8 != 0:
#     print("8 "*b8, end="")
# if b4 != 0:
#     print("4 "*b4, end="")
# if b2 != 0:
#     print("4 "*b2, end="")
# if b1 != 0:
#     print("1 "*b1, end="")

# Решением методом добавления большего числа пока вводимое не станет меньше.
# num = 221
# valute = [64, 32, 16, 8, 4, 2, 1]
# lst = []
# for i in range(len(valute)):
#     while num >= valute[i]:
#         num -= valute[i]
#         lst.append(valute[i])
# print(lst)

# пример через остатка от деления
# num = 221
# lst = [64, 32, 16, 8, 4, 2, 1]
# lst_end = []
# for i in lst:
#     if num // i != 0:           # если в остатке не ноль
#         a = num // i            # а = количество делителей
#         lst_end.append([i] * a)
#         num = num % i           # num превращаем в остаток после деления
#         # таким образом следущий оборот идет от правильного меньшего num
# for j in lst_end:
#     print(*j, end=" ")
#
# lst = [2 ** i for i in range(7)][::-1]
# print(lst)