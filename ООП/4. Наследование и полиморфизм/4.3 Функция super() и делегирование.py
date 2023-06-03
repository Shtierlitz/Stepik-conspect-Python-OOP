# Наследование. Функция super() и делегирование

class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):  # вызывает инициализатор этого класса
        super().__init__(x1, y1, x2, y2)            # super позволяет вызвать инициализатор родительского класса
        print("инициализатор Rect")
        self.fill = fill


    def draw(self):
        print("Рисование прямоугольника")


# l = Line(0, 0, 10, 20)
# r = Rect(1, 2, 3, 4)            # инициализатор Geom для <class '__main__.Rect'>
#                                 # инициализатор Rect
# print(r.__dict__)               # {'x1': 1, 'y1': 2, 'x2': 3, 'y2': 4, 'fill': None}
# https://www.youtube.com/watch?v=BTV9esoCwEE&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=24


"""Подвиг 3. Ранее вы уже использовали делегирование методов, когда вызывали инициализатор базового 
класса через функцию super(). Чаще всего делегирование в Python связано с вызовом магических методов 
базовых классов (так как их имена нельзя менять). Выполним такой пример.

Объявите в программе базовый класс с именем Book, объекты которого создаются командой:

book = Book(title, author, pages, year)
где title - заголовок книги (строка); author - автор книги (строка); pages - число страниц (целое число); 
year - год издания (целое число). В каждом объекте класса Book должны формироваться соответствующие локальные 
атрибуты: title, author, pages, year.

Объявите дочерний класс DigitBook от класса Book, объекты которого создаются командой:

db = DigitBook(title, author, pages, year, size, frm)
где дополнительные параметры size - размер книги в байтах (целое число); 
frm - формат книги (строка: 'pdf', 'doc', 'fb2', 'txt'). В каждом объекте класса DigitBook 
должны формироваться соответствующие локальные атрибуты: title, author, pages, year, size, frm.

Инициализация локальных атрибутов title, author, pages, year должна выполняться в базовом классе Book, 
а параметры size, frm инициализируются в дочернем классе DigitBook.

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


class Book:
    def __init__(self, title: str, author: str, pages: int, year: int):
        self.title, self.author, self.pages, self.year = title, author, pages, year

class DigitBook(Book):
    def __init__(self, title, author, pages, year, size: int, frm: str):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm



"""Подвиг 4. Создается программа по учету склада. 
Каждый предмет на складе должен описываться базовым классом Thing. Объекты этого класса создаются командой:

th1 = Thing(name, weight)
где name - наименование предмета (строка); weight - вес предмета (вещественное число).

Для описания каждого конкретного вида предметов, создаются дочерние классы (на основе базового Thing):

ArtObject - для представления арт-объектов;
Computer - для системных блоков компьютеров;
Auto - для автомобилей.

Объекты этих классов создаются командами:

obj = ArtObject(name, weight, author, date)  # author - автор (строка); date - дата создания (строка)
obj = Computer(name, weight, memory, cpu)    # memory - размер памяти (целое число); cpu - тип процессора (строка)
obj = Auto(name, weight, dims)               # dims - габариты, кортеж (width, length, height) - 
вещественные или целые числа
На основе класса Auto создаются дочерние классы Mercedes и Toyota, объекты которых определяются командами:

auto = Mercedes(name, weight, dims, model, old) # model - модель (строка); old - время использования,
в годах (целое число)
auto = Toyota(name, weight, dims, model, wheel) # model - модель (строка); wheel - тип руля: 
True - леворульный, False - праворульный
Во всех объектах классов должны создаваться соответствующие локальные атрибуты: name, weight и т.д.

Инициализация атрибутов должна выполняться в соответствующих классах (не должно быть дублирования кода).

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


class Thing:
    def __init__(self, name, weight):
        self.name, self.weight = name, weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date



class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu

class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


"""Подвиг 5. Вам поручено организовать представление объектов для продажи в риэлтерских агентствах.
 Для этого в программе нужно объявить базовый класс SellItem, объекты которого создаются командой:

item = SellItem(name, price)
где name - название объекта продажи (строка); price - цена продажи (число: целое или вещественное).

Каждые конкретные типы объектов описываются следующими классами, унаследованные от базового SellItem:

House - дома;
Flat - квартиры;
Land - земельные участки.



Объекты этих классов создаются командами:

house = House(name, price, material, square)
flat = Flat(name, price, size, rooms)
land = Land(name, price, square)
В каждом объекте этих классов должны формироваться соответствующие локальные атрибуты: name, price и т.д.

Формирование атрибутов name и price должно выполняться в инициализаторе базового класса.

Далее, объявить еще один класс с именем Agency, объекты которого создаются командой:

ag = Agency(name)
где name - название агентства (строка). В классе Agency объявить следующие методы:

add_object(obj) - добавление нового объекта недвижимости для продажи (один из объектов классов: House, Flat, Land);
remove_object(obj) - удаление объекта obj из списка объектов для продажи;
get_objects() - возвращает список из всех объектов для продажи.

Пример использования классов (эти строчки в программе не писать):

ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


class SellItem:
    def __init__(self, name: str, price: (int, float)):
        self.name, self.price = name, price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name: str):
        self.name = name
        self.__obj_list = []

    def add_object(self, obj):
        self.__obj_list.append(obj)

    def remove_object(self, obj):
        self.__obj_list.remove(obj)

    def get_objects(self):
        return self.__obj_list


# ag = Agency("Рога и копыта")
# ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
# ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
# ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
# ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
# ag.add_object(Land("участок под застройку", 3000000, 6.74))
# for obj in ag.get_objects():
#     print(obj.name)
#
# lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов
# print(lst_houses)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/as-ZOz8i4OU

Подвиг 6 (на повторение). Ваша команда создает небольшой фреймворк для веб-сервера. Для этого был объявлен класс:

class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func
И его предполагается использовать следующим образом:

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)
Здесь Callback - это класс-декоратор с параметрами: path = '/' - маршрут; router_cls = Router - класс роутера. 
Декоратор Callback должен обеспечивать добавление функции (в примере index) в словарь app класса Router. 
Ключом словаря выступает маршрут (path), а значением - ссылка на декорируемую функцию. 
Для этого следует использовать метод add_callback класса Router.

Затем, из роутера (Router) методом get выбирается ранее добавленная функция (в примере index), 
и если она существует, то вызывается с выводом результата в консоль.

Ваша задача реализовать класс-декоратор Callback. 

Небольшая справка.

Для реализации декоратора с параметрами на уровне класса в инициализаторе __init__(self, methods) 
прописываем параметр для декоратора, а магический метод __call__() объявляем для декорирования функции:

class Handler:
    def __init__(self, path, route_cls):
        # здесь нужные строчки

    def __call__(self, func):
        # здесь строчки 
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


# class Callback:
#     def __init__(self, path, router_cls ):
#         self.__path, self.__router_cls = path, router_cls
#
#     def __call__(self, func):
#         self.__router_cls.add_callback(self.__path, func)
#
#
# class Router:
#     app = {}
#
#     @classmethod
#     def get(cls, path):
#         return cls.app.get(path)
#
#     @classmethod
#     def add_callback(cls, path, func):
#         cls.app[path] = func
#
#
# @Callback('/', Router)
# def index():
#     return '<h1>Главная</h1>'
#
#
# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/pF1ito-hcZI

Подвиг 7. В программе объявлена функция integer_params для класса Vector, 
которая применяет к каждому методу класса декоратор integer_params_decorated:

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]
Декоратор integer_params_decorated должен проверять, чтобы все передаваемые аргументы 
в методы класса (кроме первого self) были целыми числами (имели тип int). 
Если это не так, то должно генерироваться исключение командой:

raise TypeError("аргументы должны быть целыми числами")
Ваша задача объявить эту функцию-декоратор.

Пример использования класса (эти строчки в программе не писать):

vector = Vector(1, 2)
print(vector[1])
vector[1] = 20.4 # TypeError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно."""

# def integer_params_decorated(func):
#     def wraper(self, *args, **kwargs):
#         if not all(type(x) == int for x in args):
#             raise TypeError("аргументы должны быть целыми числами")
#         if not all(type(x) == int for x in kwargs.values()):
#             raise TypeError("аргументы должны быть целыми числами")
#         return func(self, *args, **kwargs)
#
#     return wraper
#
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#
#     return cls
#
#
# @integer_params
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
#
#     def set_coords(self, *coords, reverse=False):
#         c = list(coords)
#         self.__coords = c if not reverse else c[::-1]
#
#
# vector = Vector(1, 2)
# print(vector[1])
# vector[1] = 20.4 # TypeError

"""Подвиг 8 (на повторение). Объявите класс SoftList, который наследуется от стандартного класса list. 
В классе SoftList следует объявить необходимые магические методы так, чтобы при 
обращении к несуществующему элементу (по индексу) возвращалось значение False (а не исключение Out of Range). 
Например:

sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
sl[-7] # False
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно."""

# class SoftList(list):
#     def __init__(self, lst):
#         super().__init__()
#         self.__lst = lst
#
#     def __getitem__(self, item):
#         if not (-len(self.__lst)) < item < len(self.__lst):
#             return False
#         return self.__lst[item]
#
# sl = SoftList("python")
# print(sl[0]) #'p'
# print(sl[-1]) # 'n'
# print(sl[6]) #False
# print(sl[-7]) # False


"""Подвиг 9 (на повторение). Объявите класс StringDigit, 
который наследуется от стандартного класса str. Объекты класса StringDigit должны создаваться командой:

sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). 
Если в строке string окажется хотя бы один не цифровой символ, то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")
Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:

sd = sd + "123"
sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). 
Если же при соединении строк появляется не цифровой символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")
Пример использования класса (эти строчки в программе не писать):

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно."""


# class StringDigit(str):
#     def __init__(self, string: str):
#         super().__init__()
#         for i in string:
#             if not i.isdigit():
#                 raise ValueError("в строке должны быть только цифры")
#         self.string = string
#
#     def __add__(self, other):
#         for i in other:
#             if not i.isdigit():
#                 raise ValueError("в строке должны быть только цифры")
#         return StringDigit(self.string + other)
#
#     def __radd__(self, other):
#         for i in other:
#             if not i.isdigit():
#                 raise ValueError("в строке должны быть только цифры")
#         return StringDigit(other + self.string)


# sd = StringDigit("123")
# print(sd)       # 123
# sd = sd + "456" # StringDigit: 123456
# print(type(sd), sd)
# sd = "789" + sd # StringDigit: 789123456
# print(type(sd), sd)
# # sd = sd + "12f" # ValueError
# # print(type(sd), sd)

"""Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs,
 который бы позволял обращаться к локальным атрибутам объектов дочерних классов по индексу. 
 Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости. 
Объекты этого класса должны создаваться командой:

pt = Point(x, y)
где x, y - целые или вещественные числа.

Пример использования классов (эти строчки в программе не писать):

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""

# Вот это почему-то не работает(
# class ItemAttrs:
#
#     def __getitem__(self, item):
#         count = 0
#         for key in self.__dict__:
#             if count == item:
#                 return self.__dict__.get(key)
#             count += 1
#
#     def __setitem__(self, key, value):
#         count = 0
#         for ind in self.__dict__:
#             if count == key:
#                 self.__dict__[ind] = value
#         count += 1
#
# class Point(ItemAttrs):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

class ItemAttrs:

    def __getitem__(self, item):
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        setattr(self, list(self.__dict__.keys())[key], value)

class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# pt = Point(1, 5)
#
# x = pt[0]   # 1
# print(x)
# y = pt[1]   # 2.5
# print(y)
# pt[1] = 5
# print(pt[0])
# #
# # assert pt[1] == 5, "неверные значения при обращении к атрибутам по индексам"

