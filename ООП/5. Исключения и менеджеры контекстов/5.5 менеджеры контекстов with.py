""" Менеджеры контекстов. Оператор with"""

# fp = None
# try:                                # Длинный вариант
#     fp = open("myfile.txt")
#     for t in fp:
#         print(t)
# except Exception as e:
#     print(e)
# finally:
#     if fp is not None:
#         fp.close()
#
# try:                                # Короткий вариант с менеджером контекста
#     with open("myfile.txt") as f:
#         for t in fp:
#             print(t)
# except Exception as e:
#     print(e)
#
# # создаем свой класс менеджера контекста который будет менять значение вектора
#
# class DefenderVector:
#     def __init__(self, v):
#         self.__v = v
#
#     def __enter__(self):
#         self.__temp = self.__v[:]
#         return self.__temp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.__v[:] = self.__temp
#
#         return False
#
# v1 = [1, 2, 3]
# v2 = [2, 3]
# try:
#     with DefenderVector(v1) as dv:
#         for i, a in enumerate(dv):
#             dv[i] += v2[i]
# except:
#     print("Ошибка")
#
# print(v1)
# https://www.youtube.com/watch?v=FkhnVkl0EgM&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=33


"""Подвиг 3. Объявите класс PrimaryKey, который должен работать совместно с менеджером контекста следующим образом:

with PrimaryKey() as pk:
    raise ValueError
где pk - ссылка на объект класса PrimaryKey. Класс PrimaryKey должен в момент входа в менеджер контекста выводить на экран сообщение "вход", а при завершении работы менеджера контекста выводить тип возникшего исключения. 

Класс PrimaryKey следует реализовать так, чтобы менеджер контекста сам обрабатывал возникшее исключение."""

# class PrimaryKey:
#     def __enter__(self):
#         print('вход')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         return True
#
# with PrimaryKey() as pk:
#     raise ValueError

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/4SewG1p3f-s

Подвиг 4. Вам поручено разработать класс DatabaseConnection для управления подключением к базе данных. 
Объекты этого класса создаются командой:

conn = DatabaseConnection()
В самом классе необходимо объявить метод:

def connect(self, login, password): ...

для подключения к БД. В данной реализации этот метод должен устанавливать локальный атрибут 
_fl_connection_open в значение True:

_fl_connection_open = True
и генерировать исключение с помощью собственного класса ConnectionError унаследованного от базового класса Exception.

Также в классе DatabaseConnection должен быть метод:

def close(self): ...

для закрытия соединения. В этом методе нужно атрибут _fl_connection_open установить в значение False.

Метод close() необходимо вызывать всякий раз после завершения работы с БД, вне зависимости от того, 
произошли какие-либо исключения или нет.

Этот функционал (автоматическое закрытие соединения с БД) предполагается реализовывать 
посредством менеджера контекста с использованием класса DatabaseConnection следующим образом:

with DatabaseConnection() as conn:
    # операторы менеджера контекста
Пропишите дополнительно в классе DatabaseConnection необходимые магические методы для такого его 
использования совместно с оператором with.

P.S. В программе нужно объявить только класс. На экран ничего выводить не нужно."""

# class ConnectionError(Exception): pass
#
# class DatabaseConnection():
#     def __init__(self):
#         self._fl_connection_open = False
#
#     def connect(self, login=None, password=None):
#         self._fl_connection_open = True
#         raise ConnectionError()
#
#
#     def close(self):
#         self._fl_connection_open = False
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return self.close()


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YPppgpsCo3E

Подвиг 5. Объявите класс Box (ящик), объекты которого создаются командой:

box = Box(name, max_weight)
где name - название ящика (строка); max_weight - максимальный суммарный вес вещей в ящике
 (любое положительное число). 

В каждом объекте этого класса должны формироваться локальные атрибуты:

_name - ссылка на параметр name;
_max_weight - ссылка на параметр max_weight;
_things - список из вещей, хранящиеся в ящике (изначально пустой список).

В классе Box объявите метод:

def add_thing(self, obj)

для добавления новой вещи в ящик, где obj - кортеж из двух значений:

(название_вещи, вес_вещи)

Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится 
больше величины _max_weight, то генерировать исключение командой:

raise ValueError('превышен суммарный вес вещей')
Затем, объявите еще один класс BoxDefender, который должен работать совместно с 
менеджером контекста следующим образом (эти строчки в программе не писать):

box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))
    ...
Здесь b - это ссылка на объект класса Box. Если при добавлении вещей возникает исключение ValueError, 
то объект box должен оставаться без изменений (с теми вещами, что были до вызова менеджера контекста). 
Иначе, все добавленные вещи остаются в объекте box.

P.S. В программе только объявить классы. Выводить что-либо на экран и использовать классы не нужно."""

import copy
class Box:
    def __init__(self, name, max_weight):
        self._name, self._max_weight = name, max_weight
        self._things = []
        self.__weight = 0

    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, lst):
        self._things = lst

    def add_thing(self, obj):
        name, weight = obj
        if self.__weight + weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self.__weight += weight
        self.things.append(obj)

class BoxDefender:
    def __init__(self, box):
        self._box = box
        self._things = box.things[:]


    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box.things = self._things

        return False


