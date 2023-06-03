"""Импорт стандартных модулей. Команды import и from"""
# from math import ceil as mc, pi
# import time
# from pydoc import *
# import pprint
#
# pprint.pprint(locals())


"""Подвиг 2. На вход программы подается вещественное число. Необходимо импортировать модуль math, вызывать функцию ceil этого модуля для введенного числа и отобразить результат на экране.

Sample Input:

5.67
Sample Output:

6"""

# import math
#
# a = float(input())
# print(math.ceil(a))

"""Подвиг 3. На вход программы подается вещественное число. 
Необходимо импортировать только одну функцию floor из модуля math, 
вызывать ее для введенного числа и отобразить результат на экране.

Sample Input:

8.11
Sample Output:

8"""

# from math import floor
#
# a = float(input())
# print(floor(a))

"""Подвиг 4. В программе имеется функция factorial (см. листинг). 
В начале программы (до определения функции) необходимо из модуля math 
импортировать функцию с тем же именем factorial, 
используя команду from, но так, чтобы они не "затирали" друг друга.

Уже объявленную функцию не менять. Выполнять функции не нужно, только прописать импорт."""

# from math import factorial as fc
# def factorial(n):
#     p = 1
#     for i in range(2, n+1):
#         p *= i
#
#     print("my factorial")
#     return p

"""Подвиг 5. Из модуля random импортируйте только две функции: 
seed и randint. Затем, в программе выполните их, следующим образом:"""

# from random import randint, seed
# seed(1)
# print(randint(10, 50))

"""Подвиг 6. Из модуля random импортируйте только две функции: seed и random, 
но у последней должен быть синоним rnd (имя, через которое она будет вызываться в программе). 
Выполните в программе эти функции, следующим образом:"""

# from random import seed, random as rnd
# seed(10)
# print(round(rnd(), 2))