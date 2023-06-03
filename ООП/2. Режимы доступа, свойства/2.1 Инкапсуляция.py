# Инкапсуляция
# Нужно для того чтобы пользователь не мог переопределять атрибуты.
# Это все равно можно будет сделать, однако для этого нужно их явно указывать.
# Чего программист, не имеющий доступа к файлу определяющего класс, не сможет узнать.
# _x одно подчеркивание лишь сигнализирует, что атрибут не стоит использовать вне класса
# __x два подчеркивания закрывает доступ полностью и выводит ошибку не позволяя пользоваться этим атрибутами извне.
# приватные методы делаются примерно тем же способом def __check_value(self)
# чтобы полностью запретить доступ к атрибуту или методу нужно установить модуль pip install accessify

from accessify import private, protected


class Point:
    def __init__(self, x=0, y=0):  # делаем атрибуты недоступными
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @private      # закрытый метод через accessify
    @classmethod  # метод класса
    def __check_value(cls, x):  # приватный метод
        return type(x) in (int, float)

    def set_coord(self, x, y):  # (сеттер) делаем ф внутри класса которая делает атрибуты доступными
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):  # (геттер) ф возвращает нам атрибуты предыдущей ф
        return self.__x, self.__y


# pt = Point(1, 2)

# pt.x = 200
# pt.y = "cord_y"

# pt.set_coord(10, 20)
# print(pt.get_coord())
# print(pt.__x, pt.__y)
# print(dir(pt))                # способ как узнать имя обхода приватного метода
# print(pt._Point__x)
# pt.check_value(5)
# pt._Point__check_value(5)       # способ как обойти защиту приватного метода если нет eccessify

# https://www.youtube.com/watch?v=RipfqbH0eqY&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=7


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Lqo3xcfaUZU

Подвиг 3. Объявите класс с именем Clock и определите в нем следующие переменные и методы:

- приватная локальная переменная time для хранения текущего времени, целое число 
(своя для каждого объекта класса Clock с начальным значением 0);
- публичный метод set_time(tm) для установки текущего времени (присваивает значение tm
 приватному локальному свойству time, если метод check_time(tm) возвратил True);
- публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
- приватный метод класса check_time(tm) для проверки корректности времени в переменной 
tm (возвращает True, если значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: tm должна быть целым числом, 
больше или равна нулю и меньше 100 000.

Объекты класса Clock предполагается использовать командой:

clock = Clock(время)
Создайте объект clock класса Clock и установите время, равным 4530.

P.S. На экран ничего выводить не нужно."""


# class Clock:
#     def __init__(self, time=0):
#         self.__time = time
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#     @classmethod
#     def __check_time(cls, tm):
#         return 0 <= tm < 100000
#
#
# clock = Clock(4530)
# clock.set_time(15)
# print(clock.get_time())



"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/iYcfCeRTyww

Подвиг 4. Объявите класс с именем Money и определите в нем следующие переменные и методы:

- приватная локальная переменная money (целочисленная) для хранения количества денег 
(своя для каждого объекта класса Money);
- публичный метод set_money(money) для передачи нового значения приватной локальной переменной money
 (изменение выполняется только если метод check_money(money) возвращает значение True);
- публичный метод get_money() для получения текущего объема средств (денег);
- публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
- приватный метод класса check_money(money) для проверки корректности объема средств в параметре money 
(возвращает True, если значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или равным нулю.

Пример использования класса Money (эти строчки в программе не писать):

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120"""

# class Money:
#     def __init__(self, money):
#         self.__money = money
#
#     def set_money(self, m):
#         if self.__check_money(m):
#             self.__money = m
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.mn = self
#         self.__money += mn.__money
#
#     @classmethod
#     def __check_money(self, mn):
#         return type(mn) is int and mn >= 0
#
# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120
#
# print(m2)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/w0SAD6zNLlw

Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price объектов класса Book;

Объекты класса Book предполагается создавать командой:

book = Book(автор, название, цена)
При этом, в каждом объекте должны создаваться приватные локальные свойства:

__author - строка с именем автора;
__title - строка с названием книги;
__price - целое число с ценой книги.

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно."""


# class Book:
#     def __init__(self, author, title, price):
#         self.__title = title
#         self.__author = author
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZX8fVI0KTfE

Подвиг 7. Объявите класс Line для описания линии на плоскости, объекты которого предполагается создавать командой:

line = Line(x1, y1, x2, y2)
При этом в объекте line должны создаваться следующие приватные локальные свойства:

__x1, __y1 - начальная координата;
__x2, __y2 - конечная координата.

В самом классе Line должны быть реализованы следующие сеттеры и геттеры:

set_coords(self, x1, y1, x2, y2) - для изменения координат линии;
get_coords(self) - для получения кортежа из текущих координат линии.

А также метод:

draw(self) - для отображения в консоли списка текущих координат линии (в одну строчку через пробел).

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно."""


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.set_coords(x1, y1, x2, y2)
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         print(*self.get_coords())
#
# line = Line(1, 2, 3, 4)
# print(line.get_coords())
# line.draw()


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rcj0pB1aB5M

Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:

pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа). 
При этом в объектах класса Point должны формироваться следующие локальные свойства:

__x, __y - координаты точки на плоскости.

и один геттер:

get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:

r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или

r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний.
 При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:

__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).

Также к классе Rectangle должны быть реализованы следующие методы:

set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами 
прямоугольника (ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". 
Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).

P.S. На экран ничего выводить не нужно."""


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
#
# class Rectangle:
#     def __init__(self, *args):
#         if len(args) == 2:
#             self.__pt1, self.__pt2 = args
#             self.__sp = self.__pt1
#             self.__ep = self.__pt2
#         else:
#             self.__x1, self.__y1, self.__x2, self.__y2 = args
#             self.__sp = (self.__x1, self.__y1)
#             self.__ep = (self.__x2, self.__y2)
#
#
#     def set_coords(self, sp, ep):
#             self.__sp = sp
#             self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f"Прямоугольник с координатами: {self.__sp}, {self.__ep}")
#
# pt = Point(0, 0)
# pt1 = Point(20, 34)
# rect = Rectangle(pt, pt1)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YJiPpHVguyE

Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python), когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:



Для этого объявите класс LinkedList, который будет представлять связный список в целом и
 иметь набор следующих методов:

add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:

head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:

__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.

Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:

set_next(self, obj) - изменение приватного свойства __next на значение obj;
set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
get_next(self) - получение значения приватного свойства __next;
get_prev(self) - получение значения приватного свойства __prev;
set_data(self, data) - изменение приватного свойства __data на значение data;
get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:

ob = ObjList("данные 1")
А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
Объявите в программе классы LinkedList и ObjList в соответствии с заданием.

P.S. На экран ничего выводить не нужно"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_data(self, data):
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data


ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))

# import random as rnd
# from string import ascii_lowercase, digits, ascii_uppercase
#
# class EmailValidator:
#     __check_letters = ascii_lowercase + digits + ascii_uppercase + "_." + "@"
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     @classmethod
#     def check_email(cls, email):
#
#         if email:
#             if cls.__is_email_str(email) == False:
#                 return False
#             elif len(email) >= 100:
#                 return False
#             for s in range(len(email)):
#                 if email[s] not in cls.__check_letters:
#                     return False
#                 elif email[s] == '@':
#                     if len(email[s:]) >= 50:
#                         return False
#                     elif not 0 < email.count(".", s) < 2:
#                         return False
#                 elif email[s] == ".":
#                     if email[s+1] == ".":
#                         return False
#         return True
#
#     @staticmethod
#     def __is_email_str(email):
#         return isinstance(email, str)
#
#
#     @classmethod
#     def get_random_email(cls):
#         """Когда я понял, что на каком-то тысячном обороте может попасться 2 точки подряд,
#         что противоречит проверочной функции решил сделать проверку и рекурсию"""
#         rand_lst = [string for string in cls.__check_letters[0:-1]]
#         s = ""
#         for i in range(rnd.randint(5, 50)):
#             i = rnd.choice(rand_lst)
#             s += i
#         res = s + "@gmail.com"
#         for s in range(len(res)):
#             if res[s] == ".":
#                 if res[s+1] == ".":
#                     return cls.get_random_email()
#                 else:
#                     continue
#         return res
#
# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res2 = EmailValidator.check_email("sc_lib@list_ru") # False
# rese = EmailValidator.get_random_email()
# print(res)
# print(res2)
# print(rese)



