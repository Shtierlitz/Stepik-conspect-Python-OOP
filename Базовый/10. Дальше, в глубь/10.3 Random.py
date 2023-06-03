"""Модуль random стандартной библиотеки"""

import random
# a = random.random()         # Случайное число от 0 до 1
# b = random.uniform(1, 5)    # Случайное от а до b   # 4.3939125155585135
# c = random.randint(2, 5)    # диапазон целочисленых включительно
# d = random.randrange(5, 12, 2)  # тоже диапазон но с шагом как range()


# e = random.gauss(mu, sigma) # Гауссовские велечины. mu = мат.ожидание sigma =среднеквадратическое отклонение
# То есть это значит, что числа будут более приближенные к отклонению от ожидания
# e = random.gauss(0, 3.5)

# lst = [4, 5, 0, -1, 10, 76, 3]
# a = random.choice(lst)         # Выбирает случайное значение из списка
# random.shuffle(lst)            # Перемешивает значения списка (ничего не возвращает. Мешает сам список)
# a = random.sample(lst, 3)      # Возвращает случайны список уникальных эл списка. 2й арг = количество ел

# формирование одинаковых последовательностей случайных чисел при новом запуске программы.
# random.seed(123)
# a = [random.randint(0, 10) for i in range(20)]
# [3, 0, 0, 10, 7, 6, 7, 1, 8, 0, 6, 8, 8, 7, 2, 9, 2, 7, 5, 1]
# print(a)

"""Подвиг 2. Вводятся два натуральных числа a, b (a < b) в одну строчку через пробел. 
Выполните генерацию вещественной случайной величины в диапазоне [a; b). 
Округлите результат до сотых и выведите его на экран.

Sample Input:

-4 5
Sample Output:

-2.79"""
# a = -4
# b = 5
# random.seed(1)
# a, b = map(int, input().split())
# c = random.uniform(a, b)
# print(round(c, 2))


"""Подвиг 3. Вводятся два натуральных числа a, b (a < b) в одну строчку через пробел. 
Выполните генерацию целочисленной случайной величины в диапазоне [a; b]. 
Выведите результат на экран.

Sample Input:

-2 3
Sample Output:

-1"""
# random.seed(1)
# a, b = map(int, input().split())
# a = -2
# b = 3
# c = random.randint(a, b)
# print(c)

"""Подвиг 4. Вводится список названий городов в одну строчку через пробел. 
Выберите из этого списка один город случайным образом и отобразите его на экране.

Sample Input:

Тула Казань Смоленск Семипалатинск Уфа Москва Самара
Sample Output:

Казань"""
# random.seed(1)
# # lst = [i for i in input().split()]
# lst = ['Тула', 'Казань', 'Смоленск', 'Семипалатинск', "Уфа", "Москва", "Самара"]
# print(random.choice(lst))

"""Подвиг 5. Вводится таблица целых чисел, записанных через пробел. 
Необходимо перемешать столбцы этой таблицы, 
используя функции shuffle и zip и вывести результат на экран (также в виде таблицы).

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

1 2 3 4
5 6 7 8
9 8 6 7
Sample Output:

4 1 3 2
8 5 7 6
7 9 6 8"""

# import sys
# import random
# random.seed(1)
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['1 2 3 4', '5 6 7 8', '9 8 6 7']
# nums = [i.replace(" ", "") for i in lst_in]
# lst2D = [[i for i in j] for j in zip(*nums)]
# random.shuffle(lst2D)
# for i in zip(*lst2D):
#     print(*i, sep=" ")

"""Подвиг 6. Вводятся имена студентов в одну строчку через пробел. 
Требуется случайным образом выбрать трех студентов из этого списка, используя функцию sample. 
(Полагается, что в исходном списке более трех студентов). 
Результат вывести на экран в одну строчку через пробел.

Sample Input:

Петров Иванов Сидоров Балакирев Фридман
Sample Output:

Иванов Петров Фридман"""

# import random
# random.seed(1)
# # lst = [i for i in input().split()]
# lst = ['Петров', 'Иванов', 'Сидоров', 'Балакирев', 'Фридман']
#
# print(*random.sample(lst, 3))


"""Значимый подвиг 7. Имеется двумерное игровое поле размером N x N 
(N - натуральное число, вводится с клавиатуры), 
представленное в виде вложенного списка:

P = [[0] * N for i in range(N)]

Требуется расставить в нем случайным образом M = 10 единиц (целочисленных) так, 
чтобы они не соприкасались друг с другом 
(то есть, вокруг каждой единицы должны быть нули, либо граница поля). 

P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.

Sample Input:

10
Sample Output:

True"""

import random
random.seed(1)
N = 10
P = [[0] * N for i in range(N)]
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



def is_isolate(lst_in):
    for row in range(len(lst_in)-1):
        for item in range(len(lst_in)-1):
            if (lst_in[row][item] + lst_in[row + 1][item] + lst_in[row][item + 1] + lst_in[row + 1][item + 1]) > 1:
                return False
    return True


def verify(lst):
    for i in lst:
        for j in i:
            if j == 1:
                return is_isolate(lst)
    return True

def counter(lst):
    count = 0
    for i in P:
        for j in i:
            if j == 1:
                count += 1
    return count



count = 0
while count != 10:
    row = random.randint(0, N - 1)
    col = random.randint(0, N - 1)
    P[row][col] = 1
    if verify(P):
        count = counter(P)
        continue
    else:
        P[row][col] = 0


for i in P:
    print(*i)
count = 0
for i in P:
    for j in i:
        if j == 1:
            count += 1
print(count)









massive = [1, 2, 3]
print("ДА" if 1 in massive else "Нет")











# Вариант без рандома
# for i in range(len(P)):
#     if M == 0:
#         break
#     else:
#         for j in range(len(P[i])):
#             if i % 2 == 0:
#                 if j % 2 == 0:
#                     P[i][j] = 1
#                     M -= 1
#                     if M == 0:
#                         break
# for i in P:
#     print(*i)
# count = 0
# for i in P:
#     for j in i:
#         if j == 1:
#             count += 1
# print(count)
