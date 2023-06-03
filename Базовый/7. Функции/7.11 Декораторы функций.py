"""Введение в декораторы функций"""

# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("something before")
#         res = func(*args, **kwargs)
#         print("something after")
#         return res
#
#     return wrapper

# def some_func(title, tag):
#     print(f"title = {title}, tag = {tag}")
#     return f"<{tag}>{title}</{tag}>"
#
#
# some_func = func_decorator(some_func)
# res = some_func("Python навсегда!", "h1")
# print(res)
# something before
# title = Python навсегда!, tag = h1
# something after
# <h1>Python навсегда!</h1>

# универсальный пример теста скорости ф на медленом алгоритме эвклида
import time


def tester_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper


@ tester_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
#
# быстрый алгоритм евклида для сравнения
@tester_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a

get_nod = tester_time(get_nod)
res = get_nod(2, 100000)
print(res)
#
get_fast_nod = tester_time(get_fast_nod)
res = get_fast_nod(2, 100000)
print(res)

# def decorator(func):  # Сюда передаём функцию которую нужно декорировать
#     def wrapper(*args, **kwargs):  # Сюда передаём аргументы декорированной функции
#         print(f'{func.__name__} started')  # декорирующие действия 1
#         result = func(*args, **kwargs)  # *args -чтобы работать с разным кол-вом аргументов
#         print(f'{func.__name__} finished')  # декорирующие действия 2
#         return result  # возвращаем результат
#
#     return wrapper  # передаём ссылку на вложенную функцию
#
#
# @decorator  # сахар для вызова декоратора (навешиваем декоратор)
# def summ(a, b):  # функция которую нужно декорировать в этот момент: summ = wrapper
#     return a + b
#
#
# print(summ(2, 3))









"""Подвиг 1. Объявите функцию с именем get_sq, 
которая вычисляет площадь прямоугольника по двум параметрам: 
width и height - ширина и высота прямоугольника. 
И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:

def get_sq(width, height): ...

Определите декоратор func_show для этой функции, 
который отображает результат на экране в виде строки (без кавычек):

"Площадь прямоугольника: <значение>"

Вызывать функцию и декоратор не нужно, только объявить. 
Применять декоратор к функции также не нужно.

Sample Input:

8 11
Sample Output:

Площадь прямоугольника: 88"""

# w, h = 8, 11

# def func_show(func):
#     def wraper(*args):
#         res = func(*args)
#         print(f"Площадь прямоугольника: {res}")
#         return res
#     return wraper
#
#
#
# def get_sq(width, height):
#     s = width * height
#     return s
#
# print(get_sq(w, h))


"""Подвиг 2. На вход программы поступает строка с названиями пунктов меню, 
записанные в одну строчку через пробел. Необходимо задать функцию с именем get_menu, 
которая преобразует эту строку в список из слов и возвращает этот список. Сигнатура функции, следующая:

def get_menu(s): ...

Определите декоратор для этой функции с именем show_menu, 
который отображает список на экран в формате:
1. Пункт_1
2. Пункт_1
...
N. Пункт_N

Примените декоратор show_menu к функции get_menu, используя оператор @. 
Более ничего в программе делать не нужно. Сами функции не вызывать.

Sample Input:

Главная Добавить Удалить Выйти
Sample Output:

1. Главная
2. Добавить
3. Удалить
4. Выйти"""
# w = input()
#
# w = "Главная Добавить Удалить Выйти"
#
# def show_menu(func):
#     def wraper(*args):
#         res = func(*args)
#         lst = [[str(i+1)+".", res[i]] for i in range(len(res))]
#         for i in lst:
#             print(*i)
#         return res
#     return wraper
#
#
# @show_menu
# def get_menu(s):
#     s = s.split()
#     return s
# print(get_menu(w))

"""Подвиг 3. На вход программы поступает строка из целых чисел, 
записанных через пробел. Напишите функцию get_list, 
которая преобразовывает эту строку в список из целых чисел и возвращает его. 
Определите декоратор для этой функции, который сортирует список чисел по возрастанию. 
Результат сортировки должен возвращаться при вызове декоратора.

Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:

print(*lst)

Sample Input:

8 11 -5 4 3 10
Sample Output:

-5 3 4 8 10 11"""

# s = "8 11 -5 4 3 10"
# s = input()
# def show_sort_list(func):
#     def wraper(*args):
#         lst = func(*args)
#         stop = True
#         while stop:
#             stop = False
#             for i in range(len(lst) - 1):
#                 if lst[i] > lst[i + 1]:
#                     lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                     stop = True
#         print(*lst)
#         return lst
#     return wraper
#
# @show_sort_list
# def get_list(s):
#     lst = list(map(int, s.split()))
#     return lst
#
# get_list(s)


"""Подвиг 4. Вводятся две строки из слов (слова записаны через пробел). 
Объявите функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти списки.

Определите декоратор для этой функции, который из двух списков формирует словарь, 
в котором ключами являются слова из первого списка, а значениями - соответствующие элементы из второго списка. 
Полученный словарь должен возвращаться при вызове декоратора.

Примените декоратор к первой функции и вызовите ее для введенных строк. 
Результат (словарь d) отобразите на экране командой:

print(*sorted(d.items()))

Sample Input:

house river tree car
дом река дерево машина
Sample Output:

('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')"""

# eng = "house river tree car"
# rus = "дом река дерево машина"

# eng = input()
# rus = input()
#
# def show_tup_lists(func):
#     def wraper(*args):
#         keys, values = func(*args)
#         d = {}
#         for i in range(len(keys)):
#             d[keys[i]] = values[i]
#         print(*sorted(d.items()))
#     return wraper
#
# @show_tup_lists
# def make_lists(e, r):
#     e = e.split()
#     r = r.split()
#     return e, r
#
# make_lists(eng, rus)



"""Подвиг 5. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, 
используя следующий словарь для замены русских букв на соответствующее латинское написание:

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
Функция должна возвращать преобразованную строку. Замены делать без учета регистра 
(исходную строку перевести в нижний регистр - малые буквы). Все небуквенные символы ": ;.,_" 
превращать в символ '-' (дефиса).

Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис. 
Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).

Примените декоратор к первой функции и вызовите ее для введенной строки s на кириллице:

s = input()

Результат работы декорированной функции отобразите на экране.

Sample Input:

Python - это круто!
Sample Output:

python-eto-kruto!"""

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# s = input()
#
# def replacer(func):
#     def wraper(*args):
#         res = func(*args)
#         print(res.replace(" ", "-").replace("---", "-"))
#
#         return res
#
#     return wraper
#
#
# @replacer
# def string_changer(s):
#     lst = []
#     for i in s:
#         if i.lower() in t:
#             lst.append(t.get(i.lower()))
#         elif i not in t:
#             lst.append(i.lower())
#     return "".join(lst)
#
# string_changer(s)