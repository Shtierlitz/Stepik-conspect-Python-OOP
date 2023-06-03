"""5.3 Оператор цикла for и функция range"""

"""Подвиг 1. С помощью функции range() сформируйте следующую последовательность чисел:

0, 1, 2, ..., 10

Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.

Sample Input:

Sample Output:

0 1 2 3 4 5 6 7 8 9 10"""

# for i in range(11):
#     print(i, end=" ")

"""Подвиг 2. С помощью функции range() сформируйте следующую последовательность чисел:

10, 9, 8, ..., 0

Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.

Sample Input:

Sample Output:

10 9 8 7 6 5 4 3 2 1 0"""

# for i in range(10, -1, -1):
#     print(i, end=" ")
"""Подвиг 3. С помощью функции range() сформируйте следующую последовательность чисел:

-10, -8, -6, -4, -2

Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.

Sample Input:

Sample Output:

-10 -8 -6 -4 -2"""

# for i in range(-10, 0, 2):
#     print(i, end=" ")

"""Подвиг 4. С помощью функции range() сформируйте следующую последовательность чисел:

1, 4, 7, 10, 13, 16, 19

Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.

Sample Input:

Sample Output:

1 4 7 10 13 16 19"""

# for i in range(1, 20, 3):
#     print(i, end=" ")

"""Подвиг 5. Вводятся целые числа в одну строчку через пробел. 
Необходимо преобразовать эти данные в список целых чисел. 
Затем, перебрать этот список в цикле for и просуммировать все нечетные значения. 
Результат вывести на экран.

Sample Input:

8 11 -2 4 0 13 19 12 7
Sample Output:

50"""

# lst = list(map(int, input().split()))
# x = 0
# for i in range(len(lst)):
#     lst[i] = abs(lst[i])              # вот так почему-то нельзя ибо сравнивается модуль. хз
#     if lst[i] % 2 != 0:
#         x += lst[i]
# print(x)

# lst = list(map(int, input().split()))
# x = 0
# for i in range(len(lst)):
#     if abs(lst[i] % 2 != 0):
#         x += lst[i]
# print(x)

"""Подвиг 6. Вводятся названия городов в одну строчку через пробел. 
Необходимо преобразовать входные данные в список. 
Затем, перебрать его циклом for и заменить значения элементов на длину названия соответствующего города. 
Результат вывести на экран в виде последовательности чисел через пробел в одну строчку.

Sample Input:

Москва Уфа Караганда Тверь Минск Казань
Sample Output:

6 3 9 5 5 6"""

# lst = input().split()
# for i in range(len(lst)):
#     lst[i] = len(lst[i])
# print(*lst)

"""Подвиг 7. Вводится натуральное число n. С помощью цикла for найти все делители этого числа. 
Найденные делители выводить сразу в столбик без формирования списка.

Sample Input:

12
Sample Output:

1
2
3
4
6
12"""
# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

"""Подвиг 8. Вводится натуральное число n. С помощью цикла for определить,
 является ли оно простым (то есть, делится нацело только на само себя и на 1). 
 Вывести на экран ДА, если n простое и НЕТ - в противном случае.

Sample Input:

11
Sample Output:


ДА"""

# lst = []
# n = int(input())
# for i in range(2, n):
#     i = n % i == 0
#     lst.append(i)
# if lst.count(True):
#     print("НЕТ")
# else:
#     print("ДА")

"""Подвиг 9. Вводится список названий городов в одну строчку через пробел. 
Перебрать все эти названия с помощью цикла for и определить, 
начинается ли название следующего города на последнюю букву предыдущего города в списке. 
Если последними встречаются буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква. Вывести на экран ДА, 
если последовательность удовлетворяет этому правилу и НЕТ - в противном случае.

Sample Input:

Москва Астрахань Новгород Димитровград Душанбе
Sample Output:

ДА"""
# Первый мой вариант тяжелый
# lst = ["Москва", "Астрахань", "Новгород", "Димитровград", "Душанбе"]

# lst = input().split()
# result = []
# for x in range(len(lst)-1):
#     if lst[x][-1].count("ь") or lst[x][-1].count("ъ") or lst[x][-1].count("ы"):
#         if lst[x][-2].lower() == lst[x+1][0].lower():
#             result.append("ДА")
#     elif lst[x][-1].lower() == lst[x+1][0].lower():
#             result.append("ДА")
#     else:
#         result.append("НЕТ")
# if result.count("НЕТ"):
#     print("НЕТ")
# else:
#     print("ДА")

# Второй вариант покороче
# lst = input().split()
# result = 0
# for x in range(len(lst)-1):
#     if lst[x][-1].count("ь") or lst[x][-1].count("ъ") or lst[x][-1].count("ы"):
#         if lst[x][-2].lower() != lst[x+1][0].lower():
#             result += 1
#     elif lst[x][-1].lower() != lst[x+1][0].lower():
#             result += 1
#
# if result:
#     print("НЕТ")
# else:
#     print("ДА")

"""Подвиг 10. Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n, 
которые кратны или 3 или 5. Результат (сумму) вывести на экран. Пример: n = 10, 
имеем числа: 3, 5, 6, 9. Их сумма равна 23.

Sample Input:

21
Sample Output:

98"""

# # num = 21
# num = int(input())
# result = 0
# for i in range(num):
#     if i % 3 == 0 or i % 5 == 0:
#         result += i
# print(result)

