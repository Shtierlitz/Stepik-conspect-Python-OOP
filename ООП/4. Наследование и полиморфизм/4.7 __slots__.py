"""Коллекция __slots__
Этот метод запрещает создавать новые локальные атрибуты класса кроме тех которые прописаны
в коллекции в виде строк.
то есть мы не можем создать более никаких других локальных атрибутов и прочие атрибутивные
команды так же становятся недоступными.
локальные в смысле те которые в инициализаторе и присваиваются экземпляру класса. Атрибуты
прописывать в самом классе можно.
Использование __slots__ уменьшает обьем памяти занимаемый экземпляром класса"""
"""В ООП так же работает с @property и их можно создавать"""
"""При наследовании не наследуется логически. Унаследуется только то, что выбранные атрибуты не будут попадать 
в словарь __dict__ в остальном будут работать как прежде если __slots__ не переопределить в дочернем классе 
(определять стоит только новые атрибуты. остальные унаследуются. (оставить висячую замятую))"""

import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


# p = Point(1, 2)
# p2 = Point2D(10, 20)
# t1 = timeit.timeit(p.calc)
# t2 = timeit.timeit(p2.calc)
# print(t1, t2)
# https://www.youtube.com/watch?v=Cz-grBsGGkQ&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=27


"""Подвиг 4. Объявите класс Person, в объектах которого разрешены только локальные атрибуты с 
именами (ограничение задается через коллекцию __slots__):

_fio - ФИО сотрудника (строка);
_old - возраст сотрудника (целое положительное число);
_job - занимаемая должность (строка).

Сами объекты должны создаваться командой:

p = Person(fio, old, job)
Создайте несколько следующих объектов этого класса с информацией:

Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель

Сохраните все эти объекты в виде списка с именем persons.

P.S. В программе следует объявить только класс и создать список. На экран выводить ничего не нужно."""


# class Person:
#     __slots__ = ("_fio", "_old", "_job")
#     def __init__(self, fio, old, job):
#         self._fio, self._old, self._job = fio, old, job
#
#
# persons = [Person('Суворов', 52, 'полководец'),
#            Person('Рахманинов', 50, 'пианист, композитор'),
#            Person('Балакирев', 34, 'программист и преподаватель'),
#            Person('Пушкин', 32, 'поэт и писатель')
#            ]



"""Подвиг 5. Объявите класс Planet (планета), объекты которого создаются командой:

p = Planet(name, diametr, period_solar, period)
где name - наименование планеты; diametr - диаметр планеты (любое положительное число); 
period_solar - период (время) обращения планеты вокруг Солнца (любое положительное число); 
period - период обращения планеты вокруг своей оси (любое положительное число).

В каждом объекте класса Planet должны формироваться локальные атрибуты с именами: _name, _diametr, 
_period_solar, _period и соответствующими значениями.



Затем, объявите класс с именем SolarSystem (солнечная система). 
В объектах этого класса должны быть допустимы, следующие локальные атрибуты 
(ограничение задается через коллекцию __slots__):

_mercury - ссылка на планету Меркурий (объект класса Planet);
_venus - ссылка на планету Венера (объект класса Planet);
_earth - ссылка на планету Земля (объект класса Planet);
_mars - ссылка на планету Марс (объект класса Planet);
_jupiter - ссылка на планету Юпитер (объект класса Planet);
_saturn - ссылка на планету Сатурн (объект класса Planet);
_uranus - ссылка на планету Уран (объект класса Planet);
_neptune - ссылка на планету Нептун (объект класса Planet).

Объект класса SolarSystem должен создаваться командой:

s_system = SolarSystem()
и быть только один (одновременно в программе два и более объектов класса SolarSystem недопустимо). 
Используйте для этого паттерн Singleton.

В момент создания объекта SolarSystem должны автоматически создаваться перечисленные локальные 
атрибуты и ссылаться на соответствующие объекты класса Planet со следующими данными по планетам:



Создайте в программе объект s_system класса SolarSystem.

P.S. В программе следует объявить только классы и создать объект s_system. На экран выводить ничего не нужно."""


# class Planet:
#     def __init__(self, name, diametr, period_solar, period):
#         self._name, self._diametr, self._period_solar, self._period = name, diametr, period_solar, period
#
#
# class SolarSystem:
#     __slots__ = ("_mercury", "_venus", "_earth", "_mars", "_jupiter", "_saturn", "_uranus", "_neptune")
#     __instance = None
#     __instance_base = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls == SolarSystem:
#             if cls.__instance_base is None:
#                 cls.__instance_base = object.__new__(cls)
#             return cls.__instance_base
#
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self):
#         self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
#         self._venus = Planet('Венера', 12104, 224.7, 5832.45)
#         self._earth = Planet('Земля', 12756, 365.3, 23.93)
#         self._mars = Planet('Марс', 6794, 687, 24.62)
#         self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
#         self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
#         self._uranus = Planet('Уран', 51118, 30665, 17.2)
#         self._neptune = Planet('Нептун', 49528, 60150, 16.1)
#
# s_system = SolarSystem()
# print(
#     [
#         [
#             getattr(s_system, attr)._name,
#             getattr(s_system, attr)._diametr,
#             getattr(s_system, attr)._period_solar,
#             getattr(s_system, attr)._period,
#         ] for attr in s_system.__slots__
#     ]
# )

"""Подвиг 6. Объявите класс с именем Star (звезда), в объектах которого разрешены только локальные атрибуты 
с именами (ограничение задается через коллекцию __slots__):

_name - название звезды (строка);
_massa - масса звезды (любое положительное число); часто измеряется в массах Солнца;
_temp - температура поверхности звезды в Кельвинах (любое положительное число).

Объекты этого класса должны создаваться командой:

star = Star(name, massa, temp)
На основе класса Star объявите следующие дочерние классы:

WhiteDwarf - белый карлик;
YellowDwarf - желтый карлик;
RedGiant - красный гигант;
Pulsar - пульсар.

В каждом объекте этих классов должны быть разрешены (дополнительно к атрибутам базового класса Star) 
только следующие локальные атрибуты:

_type_star - название типа звезды (строка);
_radius - радиус звезды (любое положительное число); часто измеряется в радиусах Солнца.

Соответственно, объекты этих классов должны создаваться командой:

star = Имя_дочернего_класса(name, massa, temp, type_star, radius)
Создайте в программе следующие объекты звезд:

RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1

Все эти объекты сохраните в виде списка stars. Затем, с помощью функций isinstance() и filter() 
сформируйте новый список с именем white_dwarfs, состоящий только из белых карликов (WhiteDwarf).

P.S. В программе следует объявить только классы и создать списки. На экран выводить ничего не нужно."""


# class Star:
#     __slots__ = ("_name", "_massa", "_temp")
#
#     def __init__(self, name, massa, temp):
#         self._name, self._massa, self._temp = name, massa, temp
#
#
# class WhiteDwarf(Star):
#     __slots__ = "_type_star", "_radius",
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class YellowDwarf(Star):
#     __slots__ = "_type_star", "_radius",
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class RedGiant(Star):
#     __slots__ = "_type_star", "_radius",
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class Pulsar(Star):
#     __slots__ = "_type_star", "_radius",
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
#          WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
#          WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
#          YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]
#
# white_dwarfs = list(filter(lambda x: type(x) == WhiteDwarf, stars))
# print(white_dwarfs)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rtma49Ye7hY

Подвиг 7. Объявите класс Note (нота), объекты которого создаются командой:

note = Note(name, ton)
где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си); ton - тональность ноты 
(целое число). Тональность (ton) принимает следующие целые значения:

-1 - бемоль (flat);
0 - обычная нота (normal);
1 - диез (sharp).

Если в названии (name) или тональности (ton) передаются недопустимые значения, то генерируется исключение командой:

raise ValueError('недопустимое значение аргумента')
В каждом объекте класса Note должны формироваться локальные атрибуты с именами _name и _ton 
с соответствующими значениями.

Объявите класс с именем Notes, в объектах которого разрешены только локальные атрибуты с 
именами (ограничение задается через коллекцию __slots__):

_do - ссылка на ноту до (объект класса Note);
_re - ссылка на ноту ре (объект класса Note);
_mi - ссылка на ноту ми (объект класса Note);
_fa - ссылка на ноту фа (объект класса Note);
_solt - ссылка на ноту соль (объект класса Note);
_la - ссылка на ноту ля (объект класса Note);
_si - ссылка на ноту си (объект класса Note).

Объект класса Notes должен создаваться командой:

notes = Notes()
и быть только один (одновременно в программе два и более объектов класса Notes недопустимо).
 Используйте для этого паттерн Singleton. 

В момент создания объекта Notes должны автоматически создаваться перечисленные локальные атрибуты 
и ссылаться на соответствующие объекты класса Note (тональность (ton) у всех нот изначально равна 0).

Обеспечить возможность обращения к нотам по индексам: 0 - до; 1 - ре; ... ; 6 - си. Например:

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа
Если указывается недопустимый индекс (не целое число, или число, выходящее за интервал [0; 6]), 
то генерируется исключение командой:

raise IndexError('недопустимый индекс')
Создайте в программе объект notes класса Notes.

P.S. В программе следует объявить только классы и создать объект notes. На экран выводить ничего не нужно."""


# class Note:
#     __keys = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
#     __tones = (-1, 0, 1)
#
#     def __init__(self, name, ton):
#         self._name = name
#         self._ton = ton
#
#     def __setattr__(self, key, value):
#         if key == "_name" and value not in self.__keys:
#             raise ValueError('недопустимое значение аргумента')
#         if key == "_ton" and value not in self.__tones:
#             raise ValueError('недопустимое значение аргумента')
#         object.__setattr__(self, key, value)
#
#
# class Notes:
#     __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si")
#     __instance = None
#     __instance_base = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls == Notes:
#             if cls.__instance_base is None:
#                 cls.__instance_base = object.__new__(cls)
#             return cls.__instance_base
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self):
#         self._do = Note('до', 0)
#         self._re = Note("ре", 0)
#         self._mi = Note("ми", 0)
#         self._fa = Note("фа", 0)
#         self._solt = Note("соль", 0)
#         self._la = Note("ля", 0)
#         self._si = Note("си", 0)
#
#     def __getitem__(self, item):
#         if not (0 <= item < 7):
#             raise IndexError('недопустимый индекс')
#         return getattr(self, self.__slots__[item])
#
# notes = Notes()
# nota = notes[2]  # ссылка на ноту ми
# notes[3]._ton = -1 # изменение тональности ноты фа
# print(notes[3]._ton)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/V1fqV9pfARQ

Подвиг 8 (на повторение). В программе объявлен базовый класс Function (функция) следующим образом:

class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj
Здесь в инициализаторе создаются два локальных атрибута:

_amplitude - амплитуда функции;
_bias - смещение функции по оси ординат (Oy).

Далее, в методе __call__() берется значение функции в точке x через метод _get_function(), 
который должен быть определен в дочерних классах, умножается на амплитуду функции и добавляется ее смещение. 
Следующий метод __add__() позволяет менять смещение функции, изменяя атрибут _bias на указанное значение other.

Обратите внимание, в методе __add__() происходит создание нового объекта командой:

obj = self.__class__(self)
Здесь __class__ - это ссылка на класс, к которому относится объект self. 
Благодаря этому в базовом классе можно создавать объекты соответствующих дочерних классов. 
В момент создания объекта ему передается параметр self как аргумент. Так будет создаваться копия объекта, 
т.е. новый объект с тем же набором и значениями локальных атрибутов.

Чтобы обеспечить этот функционал, объявите дочерний класс с именем Linear (линейная функция y = k*x + b), 
объекты которого должны создаваться командами:

obj = Linear(k, b)
linear = Linear(obj)  # этот вариант используется в базовом классе в методе __add__()
В первом случае происходит создание объекта линейной функции с параметрами k и b. Во втором - 
создание объекта со значениями параметров k и b, взятыми из объекта obj.

В каждом объекте класса Linear должны создаваться локальные атрибуты с именами _k и _b с 
соответствующими значениями.
В результате будет создан универсальный базовый класс Function для работы с произвольными функциями 
от одного аргумента.

Применять эти классы можно следующим образом (эти строчки в программе писать не нужно):

f = Linear(1, 0.5)
f2 = f + 10   # изменение смещения (атрибут _bias)
y1 = f(0)     # 0.5
y2 = f2(0)    # 10.5
Пропишите в базовом классе Function еще один магический метод для изменения масштаба (амплитуды) функции, 
чтобы был доступен оператор умножения:

f = Linear(1, 0.5)
f2 = f * 5    # изменение амплитуды (атрибут _amplitude)
y1 = f(0)     # 0.5
y2 = f2(0)    # 2.5
P.S. В программе следует объявить только классы. На экран выводить ничего не нужно."""


# class Function:
#     def __init__(self):
#         self._amplitude = 1.0     # амплитуда функции
#         self._bias = 0.0          # смещение функции по оси Oy
#
#     def __call__(self, x, *args, **kwargs):
#         return self._amplitude * self._get_function(x) + self._bias
#
#     def _get_function(self, x):
#         raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')
#
#     def __add__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('смещение должно быть числом')
#
#         obj = self.__class__(self)
#         obj._bias = self._bias + other
#         return obj
#
#     def __mul__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('смещение должно быть числом')
#
#         obj = self.__class__(self)
#         obj._amplitude = self._amplitude * other
#         return obj
#
#
# class Linear(Function):
#     def __init__(self, *args):
#         super().__init__()
#         if len(args) == 1:
#             self._k = args[0]._k
#             self._b = args[0]._b
#         else:
#             self._k = args[0]
#             self._b = args[1]
#
#     def _get_function(self, x):
#         return self._k * x + self._b

# f = Linear(1, 0.5)
# f2 = f * 5    # изменение амплитуды (атрибут _amplitude)
# y1 = f(0)     # 0.5
# y2 = f2(0)    # 2.5
# print(y1)

