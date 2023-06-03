# Магические методы __eq__ и __hash__
# Нужно для того чтобы сделать одинаковый хэш у двух одинаковых обьектов которые по умолчанию не одинаковые
# У одинаковых обьектов хэш одинаковый
# но у одинакового хэша не обязательно одинаковые обьекты
# ф hash() применима только для неизменяемых обьектов (нальзя для списка)

"""Короче:
a != b точно разный хэш
hash(a) != hash(b) точно разные обьекты
hash(a) == hash(b) не гарантирует одинаковые обьекты"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):                            # если мы в классе переопределяем ф __eq__ то ф hash() перестает работать
        return self.x == other.x and self.y == other.y

    def __hash__(self):                                 # чтобы hash() заработал, нужно переопределить этот метод
        return hash((self.x, self.y))                   # обязательно возвращать должно кортеж.
                                                        # по сути мы подменили вычисление обьекта hash, на вычисление координат точки

pt1 = Point(1, 2)
pt2 = Point(1, 2)
# print(hash(pt1), hash(pt2), sep="\n")                   # если определяем кортеж в __hash__, то рэш одинаковый
# print(pt1 == pt2)
d = {}
d[pt1] = 1
d[pt2] = 2
# print(d)

# https://www.youtube.com/watch?v=Cfx4VCnWeCE&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=17


"""Подвиг 4. Объявите в программе класс с именем Rect (прямоугольник), объекты которого создаются командой:

rect = Rect(x, y, width, height)
где x, y - координата верхнего левого угла (числа: целые или вещественные); 
width, height - ширина и высота прямоугольника (числа: целые или вещественные).

В этом классе определите магический метод, чтобы хэши объектов класса Rect с равными width, 
height были равны. Например:

r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2
P.S. На экран ничего выводить не нужно, только объявить класс."""


# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __hash__(self):
#         return hash((self.width, self.height))
#
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
#
# h1, h2 = hash(r1), hash(r2)   # h1 == h2
# print(h1 == h2)


"""Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число: целое или вещественное).

Определите в этом классе магические методы:

__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
__eq__() - чтобы объекты с одинаковыми хэшами были равны.

Затем, из входного потока прочитайте строки командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Строки имеют следующий формат:

название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и 
добавить в словарь с именем shop_items. Ключами словаря должны выступать сами объекты, 
а значениями - список в формате:

[item, total]

где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами).
 Подумайте, как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.

P.S. На экран ничего выводить не нужно, только объявить класс и сформировать словарь.

Sample Input:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000"""

# import sys
# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name.lower()
#         self.weight = weight
#         self.price = price
#
#     def __hash__(self):
#         return hash((self.name, self.weight, self.price))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
# lst_in = ['Системный блок: 1500 75890.56','Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545', 'Монитор Samsung: 2000 34000']
#
# shop_items = {}
# for i in range(len(lst_in)):
#     s = ShopItem(lst_in[i].split(":")[0], float(lst_in[i].split(":")[1].split()[0]), float(lst_in[i].split(":")[1].split()[1]))
#     count = lst_in.count(lst_in[i])
#     shop_items[s] = [s, count]
#
#
# print(shop_items)


"""Подвиг 7. Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:

db = DataBase(path)
где path - путь к файлу с данными БД (строка).

Также в классе DataBase нужно объявить следующие методы:

write(self, record) - для добавления новой записи в БД, представленной объектом record;
read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk 
(уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)

Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:

record = Record(fio, descr, old)
где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - 
возраст человека (целое число).

В каждом объекте класса Record должны формироваться следующие локальные атрибуты:

pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при 
создании каждого нового объекта;
fio - ФИО человека (строка);
descr - характеристика человека (строка);
old - возраст человека (целое число).

Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра). 
Если они одинаковы для разных записей, то и хэши должны получаться равными. 
Также для объектов класса Record  с одинаковыми хэшами оператор == должен выдавать значение True, 
а с разными хэшами - False.

Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase),
 ключами которого являются объекты класса Record, а значениями список из объектов с равными хэшами:

dict_db[rec1] = [rec1, rec2, ..., recN]

где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.

Для наполнения БД прочитайте строки из входного потока с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
где каждая строка представлена в формате:

"ФИО; характеристика; возраст"

Например:

Балакирев С.М.; программист; 33
Кузнецов А.В.; разведчик-нелегал; 35
Суворов А.В.; полководец; 42
Иванов И.И.; фигурант всех подобных списков; 26
Балакирев С.М.; преподаватель; 37

Каждая строка должна быть представлена объектом класса Record и записана в БД db (в словарь db.dict_db).

P.S. На экран ничего выводить не нужно."""


import sys
# lst_in = ['Балакирев С.М.; программист; 33', 'Кузнецов Н.И.; разведчик-нелегал; 35', 'Суворов А.В.; полководец; 42', 'Иванов И.И.; фигурант всех подобных списков; 26', 'Балакирев С.М.; преподаватель; 33']
# class DataBase:
#     def __init__(self, path):
#         self.path = path
#         self.dict_db = {}
#
#     def write(self, record):
#         if isinstance(record, Record):
#             if record in self.dict_db.keys():
#                 self.dict_db[record].append(record)
#             else:
#                 self.dict_db[record] = []
#                 self.dict_db[record].append(record)
#
#     def read(self, pk):
#         val = self.dict_db.values()
#         for i in val:
#             for j in i:
#                 if j.pk == pk:
#                     return j
#
#
# class Record:
#     PK = 0
#     def __init__(self, fio: str, descr: str, old: int):
#         self.fio = fio
#         self.descr = descr
#         self.old = old
#         self.pk = Record.PK
#         Record.PK += 1
#
#     def __eq__(self, other):
#         return self.fio.lower() == other.fio.lower() and self.old == other.old
#
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
#
#
# db = DataBase("asdasd")
# for i in range(len(lst_in)):
#     s = Record(lst_in[i].split("; ")[0], lst_in[i].split("; ")[1], int(lst_in[i].split("; ")[2]))
#     db.write(s)

"""Подвиг 8. Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"

Например:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021

Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:

bs = BookStudy(name, author, year)
где name - название пособия (строка); author - автор пособия (строка); 
year - год издания (целое число). 
Такие же публичные локальные атрибуты должны быть в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in). 
После этого определить число книг с уникальными хэшами. 
Это число сохранить через переменную unique_books (целое число).

P.S. На экран ничего выводить не нужно.

Sample Input:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021"""

lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

# class BookStudy:
#     def __init__(self, name: str, author: str, year: int):
#         self.name = name
#         self.author = author
#         self.year = year
#
#     def __eq__(self, other):
#         return self.name.lower() == other.name.lower() and self.author.lower() == other.author.lower()
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
#
# lst_bs = [BookStudy(i.split("; ")[0], i.split("; ")[1], int(i.split("; ")[2])) for i in lst_in]
# set_bs = {i for i in lst_bs}
# unique_books = len(set_bs)
#
# print(unique_books)

"""Подвиг 9 (релакс). Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, 
ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c 
(с соответствующими числовыми значениями). 
Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку, записанную в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю, 
то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. 
После этого отсортируйте этот список по возрастанию (неубыванию) хэшей этих объектов так, 
чтобы объекты с равными хэшами стояли друг за другом.

P.S. На экран ничего выводить не нужно.

Sample Input:

1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"""
# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if self.__val_valid(value):
#             instance.__dict__[self.name] = value
#
#     def __val_valid(self, val):
#         if val <= 0:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#         return True
#
# class Dimensions:
#
#     a = Descriptor()
#     b = Descriptor()
#     c = Descriptor()
#
#     def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
#
#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b and self.c == other.c
#
#
# s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
#
# lst_dims = [Dimensions(float(i.split()[0]), float(i.split()[1]), float(i.split()[2])) for i in s_inp.split(";")]
# lst = sorted(lst_dims, key=hash)
# lst_dims = lst
# print(lst_dims)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0EYz8-qG2iU

Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные). 
В классе Triangle объявите следующие дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). 
Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. 
То есть, должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle."""

# import math
# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#     def __set__(self, instance, value):
#         if self.__val_valid(value):
#             instance.__dict__[self.name] = value
#     def __val_valid(self, val):
#         if val <= 0:
#             raise ValueError("длины сторон треугольника должны быть положительными числами")
#
#         return True
#
# class Triangle:
#
#     a = Descriptor()
#     b = Descriptor()
#     c = Descriptor()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         if not 2 * max(self.a, self.b, self.c) < self.a + self.b + self.c:
#             raise ValueError("с указанными длинами нельзя образовать треугольник")
#
#     def tr(self):
#         p = (self.a + self.b + self.c) / 2
#         s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#         return s
#
#     def __len__(self):
#         return int(self.a +self.b + self.c)
#
#     def __call__(self, *args, **kwargs):
#         return self.tr()


