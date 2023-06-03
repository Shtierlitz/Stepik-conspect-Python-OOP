"""Функции all и any"""
# all - Возвращает True или Flase если все значение возвращают True или False
# a = [False, True, True, True]
# b = all(a)
# print(b)    # True

# Все пустое или 0 интерпертируется как False
# a = [0, 1, 2.5, "", "python", [], [1, 2], {}]
# b = all(a)
# print(b)        # False

# a = [1, 2, 3.4, {1, 2}, [1], True, "python"]
# b = all(a)
# print(b)        # True

# Без функции all
# a = [1, 2, 3.4, {}, [1], True, "python"]
# allres = True
# for x in a:
#     allres = allres and bool(x)
# print(allres)       # false


# any - возвражает True если встретила хотя бы одно True, но если все False, то вернет False
# print(any([False, True, False])) # True
# print(any([False, False, False])) # False

# без функции any
# a = [1, 2, 3.4, {}, [1], True, "python"]
# allres = False
# for x in a:
#     allres = allres or bool(x)
# print(allres)       # True


# # Крестики-нолики
# def true_x(a):
#     return a == "x"
#
#
# P = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
#
# # По горизонтали
# row_1 = all(map(true_x, P[:3]))
# row_2 = all(map(true_x, P[3:6]))
# row_3 = all(map(true_x, P[6:]))
#
# # По вертикали
# col_1 = all(map(true_x, P[::3]))    # шаг 3
# col_2 = all(map(true_x, P[1::3]))
# col_3 = all(map(true_x, P[2::3]))
#
# # по диагонали
# diagon_1 = all(map(true_x, P[0::4]))
# diagon_2 = all(map(true_x, P[2:6:2]))
#
#
# print(row_1, row_2, row_3)      # False False True
# print(col_1, col_2, col_3)      # False True False
# print(diagon_1, diagon_2)       # True False


# Сапер (результат)
# n = 10
# p = [0] * (n*n) # размер поля из нулей
#
# p[4] = "*" # встречающаяся мина
#
# loss = any(map(lambda x: x == "*", p)) # ищем встречается ли хотя бы одна мина
# print(loss) # True - пользователь проиграл

"""Подвиг 1. Вводится строка целых чисел через пробел. 
Необходимо определить, являются ли все эти числа четными. 
Вывести True, если это так и False - в противном случае.

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:

2 4 6 8 22 56
Sample Output:

True"""

# a = [int(i) for i in input().split()]
# b = all(map(lambda x: x % 2 == 0, a))
# print(b)


"""Подвиг 2. Вводится строка вещественных чисел через пробел. 
Необходимо определить, есть ли среди них хотя бы одно отрицательное. 
Вывести True, если это так и False - в противном случае.

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:

8.2 -11.0 20 3.4 -1.2
Sample Output:

True"""

# a = [float(i) for i in input().split()]
# b = any(map(lambda x: x < 0, a))
# print(b)

"""Подвиг 3. Объявить функцию с именем is_string, 
на вход которой поступает коллекция (список, кортеж, множество). 
Она должна возвращать True, если все элементы коллекции строки и False - в противном случае.

Сигнатура функции должна быть, следующей:

def is_string(lst): ...

Вызывать функцию не нужно, только определить. 
Также ничего не нужно выводить на экран. 
Задачу реализовать с использованием одной из функций: any или all.

Sample Input:

Sample Output:

True"""

# мой вариант
# def is_string(lst):
#     res = []
#     for i in lst:
#         res.append(isinstance(i, str))
#     return all(res)


# a = ["ptsdf", 1, 'sdf', 'asdfasdf']
# b = ['sadfsadf', 'sdfgsdfg', "hgfhfg"]
# c = ("sdfsdf", "sdfsd")
# d = (True, "sdfasdf", 1.2)
# s = {123, "asdasd", True}
# print(is_string(s))
# print(s)

# чужой
# def is_string(lst):
#     return not any(map(lambda x: type(x) is not str, lst))

# или
# def is_string(lst):
#     return all(map(lambda x: isinstance(x, str), lst))

"""Подвиг 4. Вводятся оценки студента в одну строчку через пробел. 
Необходимо определить, имеется ли в этом списке хотя бы одна оценка ниже тройки. 
Если это так, то вывести на экран строку "отчислен", иначе - "учится".

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:

3 3 3 2 3 3
Sample Output:

отчислен"""

# a = list(map(int, input().split()))
# a = [3, 3, 3, 3, 3, 3]
#
# if all(map(lambda x: x >= 3, a)) == False:
#         print("отчислен")
# else:
#     print("учится")

# переделал
# print("отчислен" if all(map(lambda x: x >= 3, list(map(int, input().split())))) is False else "учится")


"""Подвиг 5. Вводится текущее игровое поле для игры "Крестики-нолики" в виде следующей таблицы:

# x o
x # x
o o #

Здесь # - свободная клетка. Нужно объявить функцию с именем is_free, 
на вход которой поступает игровое поле в виде двумерного (вложенного) списка. 
Данная функция должна возвращать True, если есть хотя бы одна свободная клетка и False - в противном случае.

Сигнатура функции должна быть, следующей:

def is_free(lst): ...

Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран. 
Задачу реализовать с использованием одной из функций: any или all.

P. S. Считывание входного списка делать не нужно!!! Только определить функцию."""

lst = ['# x o', 'x # x', 'o o #']
def is_free(lst):
    for i in lst:
        if any(map(lambda x: x == "#", i)):
            return True
        else:
            return False

print(is_free(lst))
