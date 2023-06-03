"""Кортежи"""
# кортежи - упорядоченный, но не изменяемый тип данных
# a = (1,)  - чтобы в кортеже был 1 элемент, нужно оставить висящую запятую
# a = 2,    - альтернативный вариант
# x, y = (1, 2) - распаковка кортежа в переменные
# x, y, z = 3, 4, 5 - аналогично
# x, y, = ["hello", 'pithon'] - так же со списаками можно и не только
# a[0]  - обращение к элементу кортежа| Все как и в списках| Так же и срезы работают
# d = {}
# d[a] = "кортеж" - создает ключ из кортежа и ключ нельзя будет изменить
# a = () - создается кортеж
# a = tuple() - аналогично
# a = a + (1,) - обьединяет пустой кортеж с полным
# a = (2, 3) + a - обьеденяем 2 кортежа #(2, 3 ,1)
# a += (("a", "hello"),) - альтарнативный способ (2, 3, 1, ("a", "hello"))
# b = (0,) * 10 - создаст кортеж из 10 нулей (0, 0, 0, 0, 0, 0, 0, 0, 0, 0) Так же и со строками
# a = tuple([1, 2, 3]) - сделает кортеж из значений (1, 2, 3)
# a = tuple("hello") - сделает кортеж из элементов ('h', 'e', 'l', 'l', 'o')
# t = (1, 2, 3)
# list(t) - сделает список из элементов кортежа [1, 2, 3]
# Изменяемые типы в кортежах менять можно по индексам.
"""Методы кортежей"""
# count(значение) - вернет число найденых элементов
# index(el, start, stop) - вернет индекс найденого элемента и арг - параметры поиска.
# [1, 2] in a - способ проверки на наличие


"""Подвиг 3. Имеется кортеж:

t = (3.4, -56.7)

Вводится последовательность целых чисел в одну строчку через пробел.
Необходимо их добавить в кортеж t. Результат вывести на экран командой:

print(t)

Sample Input:

8 11 -5 2
Sample Output:

(3.4, -56.7, 8, 11, -5, 2)"""

# t = (3.4, -56.7)
# cort = tuple(map(int, input().split()))
# result = t + cort
# print(result)


"""Подвиг 4. Вводятся названия городов в одну строку через пробел. 
На их основе формируется кортеж. 
Если в этом кортеже нет города "Москва", 
то следует его добавить в конец кортежа. 
Результат вывести на экран в виде строки с названиями городов через пробел.

Sample Input:

Уфа Казань Самара
Sample Output:

Уфа Казань Самара Москва"""
# Мой вариант
# cort = tuple(map(str, input().split()))
# if "Москва" not in cort:
#     mosc = ("Москва", )
#     cort += mosc
# print(*cort)

# чужой
# cities = tuple(input().split())
# print(*(cities + ("Москва",)) if "Москва" not in cities else cities)

"""Подвиг 5. Вводятся названия городов в одну строку через пробел. 
На их основе формируется кортеж. Если в этом кортеже присутствует город "Ульяновск", 
то этот элемент следует удалить (создав новый кортеж). 
Результат вывести на экран в виде строки с названиями городов через пробел.

Sample Input:

Воронеж Самара Тольятти Ульяновск Пермь
Sample Output:

Воронеж Самара Тольятти Пермь"""

# мой вариант
# cities = tuple(input().split())
# result = tuple()
# for i in cities:
#     if i == "Ульяновск":
#         pass
#     else:
#         result += i,
# print(*result)

# чужой
# in_tuple = tuple(input().split())
# out_tuple = tuple(val for val in in_tuple if val != "Ульяновск")
# print(*out_tuple)


"""Подвиг 6. Вводятся имена студентов в одну строчку через пробел. 
На их основе формируется кортеж. 
Отобразите на экране все имена из этого кортежа, 
которые содержат фрагмент "ва" (без учета регистра). 
Имена выводятся в одну строчку через пробел в нижнем регистре (малыми буквами).

Sample Input:

Петя Варвара Венера Василиса Василий Федор
Sample Output:

варвара василиса василий"""

# students = ("Петя", "Варвара", "Венера", "Василиса", "Василий", "Федор", "вавилон", "варя", "вареники", "вАван")
# students = tuple(input().split())
# for i in students:
#     if "ва" in i.lower():
#         print(i.lower(), end=" ")


"""Подвиг 7. Вводятся целые числа в одну строку через пробел. 
На их основе формируется кортеж. Необходимо создать еще один кортеж 
с уникальными (не повторяющимися) значениями из первого кортежа. 
Результат отобразите в виде списка чисел через пробел.

P. S. Подобные задачи решаются, как правило, с помощью множеств, 
но в качестве практики пока обойдемся без них.

Sample Input:

8 11 -5 -2 8 11 -5
Sample Output:

8 11 -5 -2"""
# nums = (8, 11, -5, -2, 8, 11, -5)
# nums = tuple(map(int, input().split()))
# result = tuple()
# for i in nums:
#     if i not in result:
#         result += i,
# print(*result)

"""Подвиг 8. Вводятся целые числа в одну строку через пробел. 
На их основе формируется кортеж. Необходимо найти и вывести 
все индексы неуникальных (повторяющихся) значений в этом кортеже. 
Результат отобразите в виде строки чисел, записанных через пробел.

Sample Input:

5 4 -3 2 4 5 10 11
Sample Output:

0 1 4 5"""
# nums = (5, 4, -3, 2, 4, 5, 10, 11)
# nums = tuple(map(int, input().split()))
# reserv = tuple()
# for i in nums:
#     if nums.count(i) > 1:
#         reserv += i,
# print(*[num for num in range(len(nums)) if nums[num] in reserv])


""" t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
Вводится натуральное число N (N < 5). 
Необходимо на основе кортежа t сформировать новый аналогичный 
кортеж t2 размером N x N элементов. Результат вывести на экран в виде таблицы чисел.

Sample Input:

3
Sample Output:

1 0 0
0 1 0
0 0 1"""

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

# мой вариант
# r = 3
# r = int(input())
# n = 5 - r
# tup = ()
# tup2 = ()
# for j in range(len(t)-n):
#     for i in range(len(t[j]) -n):
#         tup += t[j][i],
#     tup2 += (tup),
#     print(*tup)
#     tup = ()

# чужой
# n = int(input())
#
# for i in range(n):
#     tup = ()
#     for j in range(n):
#         tup = tup + (t[i][j],)
#     print(*tup)

"""Подвиг 10. Вводятся пункты меню (каждый пункт с новой строки) в формате:

название_1 URL-адрес_1
название_2 URL-адрес_2
...
название_N URL-адрес_N

Необходимо эту информацию представить в виде вложенного кортежа menu в формате:

((название_1, URL-адрес_1), (название_2, URL-адрес_2), ... (название_N, URL-адрес_N))

Результат вывести на экран в виде кортежа командой:

print(menu)

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

Главная home
Python learn-python
Java learn-java
PHP learn-php
Sample Output:

(('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))"""
import sys
# считывание списка из входного потока
# мой вариант
# lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst = [i.split() for i in lst_in]
# lst_2 = []
# for i in range(len(lst)):
#     for j in lst[i]:
#         lst_2.append(j)
# tup = ()
# for i in range(0, len(lst_2)-1, 2):
#     tup += ((lst_2[i], lst_2[i+1]),)
# print(tup)


# чужой
# import sys
# t = tuple(tuple(line.split()) for line in list(map(str.strip, sys.stdin.readlines())))
# print(t)

# еще чужой
# menu = []
# for el in lst_in:
#     menu.append(tuple(el.split()))
#
# menu = tuple(menu)
# print(menu)

# самый простой
# print(tuple(tuple(i.split()) for i in lst_in))

