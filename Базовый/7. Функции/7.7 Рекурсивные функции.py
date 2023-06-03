""" Рекурсивные функции """
# def recursive(value):
#     print(value)
#     if value > 0:
#         recursive(value-1)
#     print(value)
# recursive(5)

# # Вычисление факториала по рекурсии
# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(6))


F = {
    'c:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldt.dll']
        }
    }

}

# def get_files(path, depth = 0):
#     for f in path:
#         print(" "*depth, f)
#         if type(path[f]) == dict:
#             get_files(path[f], depth+1)
#         else:
#             print(" "*(depth+1), " ".join(path[f]))
#
# get_files(F)

"""Подвиг 2. Вводится целое положительное число N. 
Необходимо написать рекурсивную функцию с именем get_rec_N, 
которая отображает на экране последовательность целых чисел от 1 до N (включительно). 
Каждое число выводится с новой строки. 

В качестве параметра функция get_rec_N должна принимать одно числовое значение. 
То есть, иметь только один параметр. Начальный вызов функции будет выглядеть так:

get_rec_N(N)
Вызывать функцию не нужно, только объявить.

Sample Input:

8
Sample Output:

1
2
3
4
5
6
7
8"""

# N = int(input())
# def get_rec_N(N):
#     if N >= 2:
#         get_rec_N(N-1)
#     print(N)
#
# get_rec_N(N)

"""Подвиг 3. Вводится список целых чисел в одну строчку через пробел. 
Необходимо вычислить сумму этих введенных значений, 
используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. 
Функция должна возвращать значение суммы. (Выводить на экран она ничего не должна).

Вызовите эту функцию и выведите вычисленное значение суммы на экран.

Sample Input:

8 11 -5 4 3
Sample Output:

21"""

# Сам я не решил.
# # lst = [8, 11, -5, 4, 3]
# lst = [int(i) for i in input().split()]
#
# def get_rec_sum(lst, summa = 0):
#     if summa >= len(lst):
#         return 0
#     return lst[summa] + get_rec_sum(lst, summa+1)
#
# print(get_rec_sum(lst))

# по прежднему нифига не понятно
# lst = [8, 11, -5, 4, 3]
# def get_rec_sum(lst):
#     while len(lst) > 0:
#         ls = lst.pop()
#         return ls + get_rec_sum(lst)
#     else:
#         return 0
# print(get_rec_sum(lst))

"""Подвиг 4. Вводится натуральное число N. Необходимо с помощью рекурсивной 
функции fib_rec(N, f=[]) (здесь N - общее количество чисел Фибоначчи; 
f - начальный список этих чисел) сформировать последовательность чисел Фибоначчи по правилу: 
первые два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих. 
Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...

Функция должна возвращать список сформированной последовательности длиной N.

Вызывать функцию не нужно, только объявить.

Sample Input:

7
Sample Output:

1 1 2 3 5 8 13"""

# Я снова не решил
# в общем тут условия в if чтобы добавил только первые 2 еденицы по рекурсии
#берется диапазон от 1 до 2
# а за тем в elif по рекурсии добавляем сумированные последние 2 значения списка
# N = int(input())
# N = 7
# def fib_rec(N, f=[]):
#     if len(f) < N and len(f) < 2:
#         f.append(1)
#         fib_rec(N, f)
#     elif len(f) < N and len(f) >= 2:
#         f.append(f[-1] + f[-2])
#         fib_rec(N, f)
#     return f
# print(fib_rec(N))

# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(6))


"""Подвиг 6. Имеется следующий многомерный список:

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений 
элементов списка d. Функция должна возвращать новый созданный одномерный список.  
(Только возвращать, выводить на экран ничего не нужно.)

Вызывать функцию не нужно, только объявить со следующей сигнатурой:

def get_line_list(d,a=[]): ...
где d - исходный список; a - новый формируемый."""

# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
#
# def get_line_list(d,a=[]):
#     for i in d:
#         if type(i) != list:
#             a.append(i)
#         elif type(i) == list:
#             get_line_list(i)
#     return a
# print(get_line_list(d))
#
# def get_line_list(d,a=[]):
#     for i in d:
#         if isinstance(i, list):
#             get_line_list(i)
#         else:
#             a.append(i)
#
#     return a
# print(get_line_list(d))

"""Подвиг 7. Лягушка прыгает вперед и может скакнуть либо на одно деление, 
либо сразу на два. Наша задача определить количество вариантов маршрутов, 
которыми лягушка может достичь риски под номером N (натуральное число N вводится с клавиатуры).
Решать задачу следует с применением рекурсивной функции. 
Назовем ее get_path. Алгоритм решения будет следующий. 
Рассмотрим, например, риску под номером 4. 
Очевидно, в нее лягушка может скакнуть либо с риски номер 2, либо с риски номер 3. 
Значит, общее число вариантов перемещений лягушки можно определить как: 

get_path(4) = get_path(3) + get_path(2)

Аналогично будет справедливо и для любой риски N:

get_path(N) = get_path(N-1) + get_path(N-2)

А начальные условия задачи, следующие:

get_path(1) = 1
get_path(2) = 2

Реализуйте такую рекурсивную функцию, 
которая должна возвращать количество вариантов перемещений лягушки для риски под номером N.

Вызовите эту функцию для введенного числа N и отобразите результат на экране.

Sample Input:

7
Sample Output:

21
"""

# n = 7
#
# def get_path(n):
#     if n >= 2:
#         s = get_path(n-1) + get_path(n-2)
#         return s
#     else:
#         return 1
# print(get_path(n))





"""Метод слияния кпорядоченых списков"""

"""Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел. 
Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием. 
Функция должна возвращать новый отсортированный список.
Вызовите результирующую функцию сортировки для введенного списка 
и отобразите результат на экран в виде последовательности чисел, записанных через пробел.

Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.

P. S. Теория сортировки в видео предыдущего шага.

Sample Input:

8 11 -6 3 0 1 1
Sample Output:

-6 0 1 1 3 8 11"""

# lst = [8, 11, -6, 3, 0, 1, 1]
# for i in range(len(lst)-1):
#     if lst[i] < lst[i+1]:
#         lst[i], lst[i+1] = lst[i+1], lst[i]

# # lst = [0, 4, 2, 1, 14, 6, 7, 8, 3, 30, 5, 12, 13]
# # пример разбивки списка.
# # lst_2 = lst[(len(lst)//2):]
# # lst_1 = lst[:(len(lst)//2)]
# # print(lst_1, lst_2)
#
# def merge_lists(a, b):
#     c = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j+= 1
#     if i < len(a):
#         c += a[i:]
#     if j < len(b):
#         c += b[j:]
#     return c
#
#
# def merge_sort(lst):
#     if len(lst) == 1:
#         return lst
#     mid = len(lst)//2
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return merge_lists(left, right)
#
# # print(*merge_sort(lst[::-1]))
#
#
# # Задача на слияние списков
# # lst = [8, 11, -6, 3, 0, 1, 1]
# lst = [0, 4, 2, 1, 14, 6, 7, 8, 3, 30, 5, 12, 40 ,183, 241, 521, 1, 1231312]
#
# # Пузырьковая сортировка
# stop = True
# while stop:
#     stop = False
#     for i in range(len(lst)-1):
#         if lst[i] > lst[i+1]:
#             lst[i], lst[i+1] = lst[i+1], lst[i]
#             stop = True
# print(lst)
# # l = len(lst)//3
# # lst_1 = lst[:l]
# # lst_2 = lst[l:l+l]
# # lst_3 = lst[-l:]
# # print(lst_1, lst_2, lst_3)
#
#
# # без функции
# a = lst[len(lst)//2:]
# b = lst[:len(lst)//2]
#
# i = j = 0
# c = []
# n = len(a)
# m = len(b)
#
# while i < n and j < m:
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1
#
#
# while i < n:
#     c.append(a[i])
#     i += 1
# while j < m:
#     c.append(b[j])
#     j += 1
#
# print(c)
# https://www.youtube.com/watch?v=LCfwxi2RPK4