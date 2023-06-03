#  Магический метод __bool__ определения правдивости объектов
# Стандартно ф Bool() определяет True или False не пустой ли обьект, но можно и переопределить поведение

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return  self.x * self.x + self.y * self.y

    def __bool__(self):                         # обьязательно должен возвращать True или False
        print("__bool__")                       # у bool приоритет над len, но если bool не переопределен, то приоритет у лен
        return self.x == self.y


# p = Point(10, 10)
# print(len(p))
# print(bool(p))
# if p:
#     print("Обьект p дает True")
# else:
#     print("Обьект Р дает False")

# https://www.youtube.com/watch?v=a2L5vyCUvzo&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=18


"""Подвиг 4. Объявите в программе класс Player (игрок), объекты которого создаются командой:

player = Player(name, old, score)
где name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число). 
В каждом объекте класса Player должны создаваться аналогичные локальные атрибуты: name, old, score.

С объектами класса Player должна работать функция:

bool(player)
которая возвращает True, если число очков больше нуля, и False - в противном случае.

С помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:

"имя; возраст; очки"

Например:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0

Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими данными. 
И из этих объектов сформировать список players.

Отфильтруйте этот список (создайте новый: players_filtered), оставив всех игроков с числом очков больше нуля. 
Используйте для этого стандартную функцию filter() совместно с функцией bool() языка Python. 

P.S. На экран ничего выводить не нужно.

Sample Input:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0
"""
import sys

# class Player:
#     def __init__(self, name: str, old: int, score: int):
#         self.name = name
#         self.old = old
#         self.score = score
#
#     def __bool__(self):
#         return self.score > 0
#
#
# lst_in = ['Балакирев; 34; 2048',
# 'Mediel; 27; 0',
# 'Влад; 18; 9012',
# 'Nina P; 33; 0']
#
# players = [Player(i.split(";")[0], int(i.split(";")[1]), int(i.split("; ")[2])) for i in lst_in]
# players_filtered = list(filter(bool, players))
# print(players_filtered)

"""Подвиг 5. Объявите в программе класс MailBox (почтовый ящик), объекты которого создаются командой:

mail = MailBox()
Каждый объект этого класса должен содержать локальный публичный атрибут:

inbox_list - список из принятых писем.

Также в классе MailBox должен присутствовать метод:

receive(self) - прием новых писем

Этот метод должен читать данные из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
В результате формируется список lst_in из строк. Каждая строка записана в формате:

"от кого; заголовок; текст письма"

Например:

sc_lib@list.ru; От Балакирева; Успехов в IT!
mail@list.ru; Выгодное предложение; Вам одобрен кредит.
mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.

Каждая строчка списка lst_in должна быть представлена объектом класса MailItem, объекты которого создаются командой:

item = MailItem(mail_from, title, content)
где mail_from - email отправителя (строка); title - заголовок письма (строка), 
content - содержимое письма (строка). 
В каждом объекте класса MailItem должны формироваться соответствующие локальные 
атрибуты (с именами: mail_from, title, content). И дополнительно атрибут is_read (прочитано ли) 
с начальным значением False.

В классе MailItem должен быть реализован метод:

set_read(self, fl_read) - для отметки, что письмо прочитано 
(метод должен устанавливать атрибут is_read = fl_read, если True, то письмо прочитано, если False, то не прочитано).

С каждым объектом класса MailItem должна работать функция:

bool(item)
которая возвращает True для прочитанного письма и False для непрочитанного.

Вызовите метод:

mail.receive()
Отметьте первое и последнее письмо в списке mail.inbox_list, 
как прочитанное (используйте для этого метод set_read). 
Затем, сформируйте в программе список (глобальный) с именем inbox_list_filtered из прочитанных писем, 
используя стандартную функцию filter() совместно с функцией bool() языка Python.

P.S. На экран ничего выводить не нужно.

Sample Input:

sc_lib@list.ru; От Балакирева; Успехов в IT!
mail@list.ru; Выгодное предложение; Вам одобрен кредит.
mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить."""


lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
          'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
          'Python ООП; Балакирев С.М.; 2022',
          'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']


# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
#
#     def receive(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         self.inbox_list = [MailItem(i.split(";")[0], i.split(";")[1], i.split(";")[2]) for i in lst_in]
#
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
#
#     def set_read(self, fl_read):
#         self.is_read = fl_read
#
#     def __bool__(self):
#         return self.is_read
#
# mail = MailBox()
# mail.receive()
# mail.inbox_list[0].set_read(True)
# mail.inbox_list[-1].set_read(True)
#
# inbox_list_filtered = list(filter(bool, mail.inbox_list))
#
# print(mail.inbox_list)
# print(inbox_list_filtered)


"""Подвиг 6 (релакс). Объявите класс Line, объекты которого создаются командой:

line = Line(x1, y1, x2, y2)
где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2). 
Могут быть произвольными числами. 
В объектах класса Line должны создаваться соответствующие локальные атрибуты с именами x1, y1, x2, y2.

В классе Line определить магический метод __len__() так, чтобы функция:

bool(line)
возвращала False, если длина линии меньше 1.

P.S. На экран ничего выводить не нужно. Только объявить класс."""


# class Line:
#     """Длина отрезка это квадратный корень по формуле внизу"""
#     def __init__(self, x1, y1, x2, y2):
#         self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
#
#     def __len__(self):
#         return int(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5)
#
# s = Line(0, 0, 5, 12)
# print(len(s))


"""Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)
где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла. 
Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. 
Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты x1, y1, x2, y2 существуют и False - в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() 
должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')
Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. 
Два объекта должны быть созданы командой 

Ellipse()
и еще два - командой:

Ellipse(x1, y1, x2, y2)
Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2. 
(Помните, что для этого был определен магический метод __bool__()).

P.S. На экран ничего выводить не нужно."""


# class Ellipse:
#     def __init__(self, x1=None, y1=None, x2=None, y2=None):
#         if x1 and x2 and y1 and y2 is not None:
#             self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
#
#     def __bool__(self):
#         return len(self.__dict__) == 4
#
#     def get_coords(self):
#         try:
#             s = (self.x1, self.y1, self.x2, self.y2)
#             return s
#         except:
#             raise AttributeError('нет координат для извлечения')
#
# lst_geom = [Ellipse(2, 3, 4, 5), Ellipse(), Ellipse(4, 3, 2, 1), Ellipse()]
#
# for i in lst_geom:
#     if bool(i):
#         i.get_coords()



"""Сапер улучшенный"""
# from random import randint
#
# class Cell:
#     def __init__(self):
#         self.__is_mine = False
#         self.__number = 0
#         self.__is_open = False
#
#     def __check_value(self, val):
#         if type(val) == bool:
#             return val
#         elif 0 <= val <= 8:
#             return val
#         else:
#             raise ValueError("недопустимое значение атрибута")
#
#     @property
#     def is_mine(self):
#         return self.__is_mine
#
#     @is_mine.setter
#     def is_mine(self, val):
#         self.__check_value(val)
#         self.__is_mine = val
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, val):
#         self.__check_value(val)
#         self.__number = val
#
#     @property
#     def is_open(self):
#         return self.__is_open
#
#     @is_open.setter
#     def is_open(self, value):
#         self.__check_value(value)
#         self.__is_open = value
#
#     def __bool__(self):
#         return False if self.is_open else True
#
#
#
# class GamePole:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __del__(self):
#         GamePole.__instance = None
#
#     def __init__(self, N, M, total_mines):
#         self.n = N
#         self.m = M
#         self.total_mines = total_mines
#         self.__pole_cells = [[Cell() for n in range(self.m)] for n in range(self.n)]
#         self.init_pole()
#
#     @property
#     def pole(self):
#         return self.__pole_cells
#
#     def init_pole(self):
#         m = 0
#         while m < self.total_mines:
#             i = randint(0, self.n - 1)
#             j = randint(0, self.m - 1)
#             if self.pole[i][j].is_mine:
#                 continue
#             self.pole[i][j].is_mine = True
#             m += 1
#
#         indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
#         for x in range(self.n):
#             for y in range(self.m):
#                 if not self.pole[x][y].is_mine:
#                     mines = sum((self.pole[x+i][y+j].is_mine for i, j in indx if 0 <= x+i < self.n and 0 <= y+j < self.m))
#                     self.pole[x][y].number = mines
#
#
#     def show_pole(self):
#         for row in self.pole:
#             print(*map(lambda x: "#" if not x.is_open else x.number if not x.is_mine else "*", row))
#
#     def open_cell(self, i: int, j):
#         try:
#             self.pole[i][j].is_open = True
#         except:
#             raise IndexError('некорректные индексы i, j клетки игрового поля')
#
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# # pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()

"""Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) 
координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, 
то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс."""

# class Vector:
#     def __init__(self, *args):
#         self.coords = [i for i in args if args]
#
#     def __add__(self, other):
#         if type(other) == Vector:
#             if len(self.coords) != len(other.coords):
#                 raise ArithmeticError('размерности векторов не совпадают')
#             sc = other.coords
#             lst = list(map(lambda x, y: x + y, sc, self.coords))
#             return Vector(*lst)
#
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#     def __iadd__(self, other):
#         if type(other) == Vector:
#             if len(self.coords) != len(other.coords):
#                 raise ArithmeticError('размерности векторов не совпадают')
#             sc = other.coords
#             self.coords = list(map(lambda x, y: x + y, sc, self.coords))
#             return self
#         sc = other
#         self.coords = list(map(lambda x: x + sc, self.coords))
#         return self
#
#     def __sub__(self, other):
#         if type(other) == Vector:
#             sc = other.coords
#             lst = list(map(lambda x, y: x - y, self.coords, sc))
#             return Vector(*lst)
#
#     def __rsub__(self, other):
#         return self.__sub__(other)
#
#     def __isub__(self, other):
#         if type(other) == Vector:
#             sc = other.coords
#             self.coords = list(map(lambda x, y: x - y, self.coords, sc ))
#             return self
#         sc = other
#         self.coords = list(map(lambda x: x - sc, self.coords))
#         return self
#
#     def __mul__(self, other):
#         if type(other) == Vector:
#             if len(self.coords) != len(other.coords):
#                 raise ArithmeticError('размерности векторов не совпадают')
#             sc = other.coords
#             lst = list(map(lambda x, y: x * y, self.coords, sc))
#             return Vector(*lst)
#
#     def __eq__(self, other):
#         sc = other.coords
#         return True if all(list(map(lambda x, y: x == y, self.coords, sc))) else False
#
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# print((v1 + v2).coords)  # [5, 7, 9]
# print((v1 - v2).coords)  # [-3, -3, -3]
# print((v1 * v2).coords)  # [4, 10, 18]
#
# v1 += 10
# print(v1.coords)  # [11, 12, 13]
# v1 -= 10
# print(v1.coords)  # [1, 2, 3]
# v1 += v2
# print(v1.coords)  # [5, 7, 9]
# v2 -= v1
# print(v2.coords)  # [-1, -2, -3]
# #
# print(v1 == v2)  # False
# print(v1 != v2)  # True