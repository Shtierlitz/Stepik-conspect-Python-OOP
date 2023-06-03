# Функция issubclass(). Наследование от встроенных типов и от object

# class Geom(object):     # любой класс по умолчанию наследуется от базового класса object
#     pass
#
#
# class Line(Geom):       # все последующие наследующие классы идут по иерархии Line-Geom-object и т.д.
#     pass

# print(Geom.__name__)    # Geom
# g = Geom()
# print(g)                # <__main__.Geom object at 0x0000020DDD60DA80>
# l = Line()
# print(l.__class__)      # <class '__main__.Line'>
# # Мы можем определять евляется ли класс подклассом другого класса с помощью ф issubclass()
# print(issubclass(Line, Geom))   # True  # в аргументы передаются только классы
# print(issubclass(Geom, Line))   # False
# # чтобы проверить принадлежность экземпляра класса к классу используем isinstance()
# print(isinstance(l, Geom))      # True
# print(isinstance(l, object))    # True
#
# print(issubclass(int, object))  # True  # int тоже класс и тоже наследуется от object
# print(issubclass(list, object)) # True
#
#
# class Vector(list):
#     def __str__(self):                  # Так как list является классом мы можем унаследоваться от него и переопределить работу метода __str__ к примеру
#         return " ".join(map(str, self)) # self - это список, map- к каждому обьекту применяем метод str и полученные строки записываем через пробел
#
#
# v = Vector([1, 2, 3])
# print(v)                        # 1 2 3
# print(type(v))                  # <class '__main__.Vector'>

# https://www.youtube.com/watch?v=JTmb2QHZUGg&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=22

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/pohpzoAbkrQ

Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел. 
Для этого вам ставится задача создать класс с именем ListInteger с 
базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, 
генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')
Пример использования класса ListInteger (эти строчки в программе не писать):

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно."""


# class ListInteger(list):
#     def __init__(self, item):
#         super().__init__(item)
#         self.__check_type(item)
#         if type(item) not in (list, tuple, dict, set):
#             self.lst = [item]
#         else:
#             self.lst = [i for i in item]
#
#     def __check_type(self, item):
#         if type(item) not in (list, tuple, dict, set):
#             if type(item) != int:
#                 raise TypeError('можно передавать только целочисленные значения')
#         else:
#             for i in item:
#                 if type(i) != int:
#                     raise TypeError('можно передавать только целочисленные значения')
#
#     def append(self, item):
#         self.__check_type(item)
#         super().append(item)
#
#     def __setitem__(self, key, value):
#         self.__check_type(value)
#         super().__setitem__(key, value)




# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# s[0] = 10.5 # TypeError



"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/aFKqv4b2QZ0

Подвиг 4. Разрабатывается интернет-магазин. Каждый товар предполагается представлять классом Thing,
 объекты которого создаются командой:

thing = Thing(name, price, weight)
где name - наименование товара (строка); price - цена (вещественное число); weight - вес товара (вещественное число). В каждом объекте этого класса создаются аналогичные атрибуты: name, price, weight.

Класс Thing необходимо определить так, чтобы его объекты можно было использовать в качестве ключей словаря, 
например:

d = {}
d[thing] = thing
И для каждого уникального набора данных name, price, weight должны формироваться свои уникальные ключи.

Затем, вам необходимо объявить класс словаря DictShop, унаследованный от базового класса dict. 
В этом новом словаре ключами могут выступать только объекты класса Thing. При попытке указать любой другой тип, 
генерировать исключение командой:

raise TypeError('ключами могут быть только объекты класса Thing')
Объекты класса DictShop должны создаваться командами:

dict_things = DictShop() # пустой словарь
dict_things = DictShop(things) # словарь с набором словаря things
где things - некоторый словарь. В инициализаторе следует проверять, чтобы аргумент thing был словарем, 
если не так, то выбрасывать исключение:

raise TypeError('аргумент должен быть словарем')
И проверять, чтобы все ключи являлись объектами класса Thing. Если это не так, то генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
Дополнительно в классе DictShop переопределить метод:

__setitem__()

с проверкой, что создаваемый ключ является объектом класса Thing. Иначе, генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
Пример использования классов (эти строчки в программе не писать):

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

dict_things[1] = th_1 # исключение TypeError
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


# class Thing:
#     def __init__(self, name: str, price: float, weight: float):
#         self.name, self.price, self.weight = name, price, weight
#
#     def __hash__(self):
#         return hash((self.name, self.price, self.weight))
#
#
# class DictShop(dict):
#     def __init__(self, things=None):
#         things = {} if things is None else things
#
#         if not isinstance(things, dict):
#             raise TypeError('аргумент должен быть словарем')
#         if things and not all(isinstance(i, Thing) for i in things):
#             raise TypeError('ключами могут быть только объекты класса Thing')
#
#         super().__init__(things)
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, Thing):
#             raise TypeError('ключами могут быть только объекты класса Thing')
#         super().__setitem__(key, value)


# th_1 = Thing('Лыжи', 11000, 1978.55)
# th_2 = Thing('Книга', 1500, 256)
# dict_things = DictShop()
# dict_things[th_1] = th_1
# dict_things[th_2] = th_2
# print(dict_things)
# for x in dict_things:
#     print(x.name)
#
# # dict_things[1] = th_1 # исключение TypeError


"""Подвиг 5. Объявите в программе следующие классы без содержимого (используйте оператор pass):

Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeys

и постройте схему наследования в соответствии со следующей иерархией древа жизни:



Затем, объявите в программе классы:

Monkey - наследуется от Monkeys и служит для описания обезьян;
Person - наследуется от Human и служит для описания человека;
Flower - наследуется от Flowering и служит для описания цветка;
Worm - наследуется от Worms и служит для описания червей.

Объекты этих классов должны создаваться командами:

obj = Monkey(name, weight, old)
obj = Person(name, weight, old)
obj = Flower(name, weight, old)
obj = Worm(name, weight, old)
где name - наименование (или имя) объекта (строка); weight - вес (вещественное число); 
old - возраст (целое число). В каждом объекте любого из этих классов должны создаваться 
соответствующие атрибуты: name, weight, old.

Создайте в программе следующие объекты и сохраните их в виде списка lst_objs:

Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1

Затем, используя функции isinstance() и генератор списков (List comprehensions), 
сформируйте следующие списки из указанных объектов:

lst_animals - все объекты, относящиеся к животным (Animals);
lst_plants - все объекты, относящиеся к растениям (Plants);
lst_mammals - все объекты, относящиеся к млекопитающим (Mammals).

P.S. В программе на экран выводить ничего не нужно."""

# class Protists:
#     def __init__(self, name, weight, old):
#         self.name, self.weight, self.old = name, weight, old
#
# class Plants(Protists):
#     pass
#
# class Animals(Protists):
#     pass
#
# class Mosses(Plants):
#     pass
#
# class Flowering(Plants):
#     pass
#
# class Worms(Animals):
#     pass
#
# class Mammals(Animals):
#     pass
#
# class Human(Mammals):
#     pass
#
# class Monkeys(Mammals):
#     pass
#
#
# class Monkey(Monkeys):
#     pass
#
# class Person(Human):
#     pass
#
# class Flower(Flowering):
#     pass
#
# class Worm(Worms):
#     pass
#
# lst_objs = [Monkey("мартышка", 30.4, 7),
#             Monkey("шимпанзе", 24.6, 8),
#             Person("Балакирев", 88, 34),
#             Person("Верховный жрец", 67.5, 45),
#             Flower("Тюльпан", 0.2, 1),
#             Flower("Роза", 0.1, 2),
#             Worm("червь", 0.01, 1),
#             Worm("червь 2", 0.02, 1)
#     ]
#
# lst_animals = [i for i in lst_objs if isinstance(i, Animals)]
# lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
# lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]

"""Подвиг 6. Известно, что с объектами класса tuple можно складывать только такие же объекты (кортежи). Например:

t1 = (1, 2, 3)
t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)
Если же мы попытаемся прибавить любой другой итерируемый объект, например, список:

t2 = t1 + [4, 5]
то возникнет ошибка. Предлагается поправить этот функционал и создать свой собственный класс Tuple, 
унаследованный от базового класса tuple и поддерживающий оператор:

t1 = Tuple(iter_obj)
t2 = t1 + iter_obj  # создается новый объект класса Tuple с новым (соединенным) набором данных
где iter_obj - любой итерируемый объект (список, словарь, строка, множество, кортеж и т.п.)

Пример использования класса (эти строчки в программе не писать):

t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно."""

# class Tuple(tuple):
#
#     def __add__(self, other):
#         tup = tuple(i for i in other)
#         return Tuple(tuple(self) + tup)

# t = Tuple([1, 2, 3])
# print(t)
# t = t + "Python"
# print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
# print(type(t))
# t = t + "ООП"
# print(t)


"""4.2 Функция issubclass(). Наследование от встроенных типов
7 из 10 шагов пройдено
13 из 20 баллов  получено
Подвиг 7 (на повторение). Необходимо в программе объявить класс VideoItem для представления одного
 видео (например, в youtube). Объекты этого класса должны создаваться командой:

video = VideoItem(title, descr, path)
где title - заголовок видео (строка); descr - описание видео (строка); path - путь к видеофайлу. 
В каждом объекте класса VideoItem должны создаваться соответствующие атрибуты: title, descr, path.

Затем, нужно создать класс для формирования оценки видео в баллах от 0 до 5. 
Для этого нужно объявить еще один класс с именем VideoRating, объекты которого создаются командой:

rating = VideoRating()
В каждом объекте класса VideoRating должен быть локальный приватный атрибут с именем __rating, 
содержащий целое число от 0 до 5 (по умолчанию 0). А для записи и считывания значения из этого 
приватного атрибута должно быть объект-свойство (property) с именем rating.

Так как атрибут __rating - это целое число в диапазоне [0; 5], то в момент присвоения ему какого-либо 
значения необходимо проверять, что присваиваемое значение - целое число в диапазоне [0; 5]. Если это не так, 
то генерировать исключение командой:

raise ValueError('неверное присваиваемое значение')
Далее, в каждом объекте класса VideoItem должен быть локальный атрибут rating - объект класса VideoRating.

Пример использования классов (эти строчки в программе не писать):

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно."""


# class VideoItem:
#     def __init__(self, title: str, descr: str, path: str):
#         self.title, self.descr, self.path = title, descr, path
#         self.rating = VideoRating()
#
# class VideoRating:
#     def __init__(self):
#         self.__rating = 0
#
#     @property
#     def rating(self):
#         return self.__rating
#
#     @rating.setter
#     def rating(self, rate: int):
#         if type(rate) is not int or not 0 <= rate <= 5:
#             raise ValueError('неверное присваиваемое значение')
#         self.__rating = rate

# v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
# print(v.rating.rating) # 0
# v.rating.rating = 5
# print(v.rating.rating) # 5
# title = v.title
# descr = v.descr
# # v.rating.rating = 6  # ValueError


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0Jy6n9KESPE

Подвиг 9 (на повторение). Объявите в программе базовый класс с именем 
IteratorAttrs для перебора всех локальных атрибутов объектов класса. 
Напомню, что для этого используются два магических метода:

__iter__() - для получения объекта-итератора (в данном случае - это сам объект self)
__next__() - для перебора локальных атрибутов объекта self (используйте для этого словарь __dict__)

Метод __next__() на каждой итерации должен возвращать кортеж в формате: (имя атрибута, значение).

Подсказка: здесь можно определить один метод __iter__() как функцию-генератор.

Объявите дочерний класс SmartPhone, объекты которого создаются командой:

phone = SmartPhone(model, size, memory)
где model - модель смартфона (строка); size - габариты (ширина, длина) в виде кортежа двух чисел; 
memory - размер ОЗУ (памяти), как целое число. В каждом объекте класса SmartPhone должны 
создаваться соответствующие локальные атрибуты: model, size, memory.

Благодаря наследованию от базового класса IteratorAttrs, с объектами класса SmartPhone должен 
выполняться оператор for:

for attr, value in phone:
    print(attr, value)
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""

# class IteratorAttrs:
#
#     def __iter__(self):
#         for x in self.__dict__.items():
#             yield x
#
# class SmartPhone(IteratorAttrs):
#     def __init__(self, model: str, size: tuple, memory: int):
#         self.model, self.size, self.memory = model, size, memory
#
# phone = SmartPhone("Xaomi Redmi note 8 PRO", (12, 24), 64)
#
# for attr, value in phone:
#     print(attr, value)

