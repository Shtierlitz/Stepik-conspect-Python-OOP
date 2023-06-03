# Наследование. Атрибуты private и protected

class Geom:
    __name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def _verify_coord(self, coord):
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):  # вызывает инициализатор этого класса
        super().__init__(x1, y1, x2, y2)            # super позволяет вызвать инициализатор родительского класса
        self._fill = fill
        self._verify_coord(x1)

    def get_coords(self):
        return (self._x1, self._y1)



# r = Rect(0, 0, 10, 20)
# print(r.__dict__)           # инициализатор Geom для <class '__main__.Rect'>
#                             # {'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, '_Geom__y2': 20, '_Rect__fill': 'red'}
#
# r.get_coords()
# print(r.__dict__)
# https://www.youtube.com/watch?v=zHgPAm-imvY&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=24



"""Подвиг 5. Объявите класс Animal (животное), объекты которого создаются командой:

an = Animal(name, kind, old)
где name - название животного (строка); kind - вид животного (строка); old - возраст (целое число). 
В каждом объекте этого класса должны создаваться соответствующие приватные атрибуты: __name, __kind, __old.

В классе Animal должны быть объявлены объекты-свойства для изменения и считывания приватных атрибутов:

name - для работы с приватным атрибутом __name;
kind - для работы с приватным атрибутом __kind;
old - для работы с приватным атрибутом __old.

Создайте в программе список с именем animals, который содержит три объекта класса Animal со следующими данными:

Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3

P.S. В программе нужно объявить только класс и создать список animals. На экран выводить ничего не нужно."""



# class Animal:
#     def __init__(self, name: str, kind: str, old: int):
#         self.__name, self.__kind, self.__old = name, kind, old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def kind(self):
#         return self.__kind
#
#     @kind.setter
#     def kind(self, kind):
#         self.__kind = kind
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#
#
# animals = [Animal('Васька', 'дворовый кот', 5),
#            Animal('Рекс', 'немецкая овчарка', 8),
#            Animal('Кеша', 'попугай', 3)]

"""Подвиг 6. Объявите класс Furniture (мебель), объекты которого создаются командой:

f = Furniture(name, weight)
где name - название предмета (строка); weight - вес предмета (целое или вещественное число).

В каждом объекте класса Furniture должны создаваться защищенные локальные атрибуты с именами _name и _weight. 
В самом классе Furniture нужно объявить приватные методы:

__verify_name() - для проверки корректности имени;
__verify_weight() - для проверки корректности веса.

Метод __verify_name() проверяет, что имя должно быть строкой, если это не так, 
то генерируется исключение командой:

raise TypeError('название должно быть строкой')
Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля), 
если это не так, то генерируется исключение командой:

raise TypeError('вес должен быть положительным числом')
Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight 
(а также при их создании).

На основе базового класса Furniture объявить следующие дочерние классы:

Closet - для представления шкафов;
Chair - для представления стульев;
Table - для представления столов.

Объекты этих классов должны создаваться командами:

obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе; False - обычный шкаф; doors - 
число дверей (целое число)
obj = Chair(name, weight, height)       # height - высота стула (любое положительное число)
obj = Table(name, weight, height, square) # height - высота стола; square - площадь поверхности 
(любые положительные числа)
В каждом объекте этих классов должны создаваться соответствующие защищенные атрибуты:

- в объектах класса Closet: _name, _weight, _tp, _doors
- в объектах класса Chair: _name, _weight, _height
- в объектах класса Table: _name, _weight, _height, _square

В каждом классе (Closet, Chair, Table) объявить метод:

get_attrs()
который возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.

Пример использования классов (эти строчки в программе писать не нужно):

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


# class Furniture:
#     def __init__(self, name: str, weight: (int, float)):
#         self.__verify_name(name)
#         self.__verify_weight(weight)
#         self._name, self._weight = name, weight
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self.__verify_name(name)
#         self._name = name
#
#     @property
#     def weight(self):
#         return self._weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.__verify_weight(weight)
#         self._weight = weight
#
#     def __verify_name(self, name):
#         if not isinstance(name, str):
#             raise TypeError('название должно быть строкой')
#
#     def __verify_weight(self, weight):
#         if not isinstance(weight, (int, float)) and not weight > 0:
#             raise TypeError('вес должен быть положительным числом')
#
#
# class Closet(Furniture):
#     def __init__(self, name, weight, tp, doors):
#         super().__init__(name, weight)
#         self._tp, self._doors = tp, doors
#
#     def get_attrs(self):
#         return self.name, self.weight, self._tp, self._doors
#
#
# class Chair(Furniture):
#     def __init__(self, name, weight, height):
#         super().__init__(name, weight)
#         self._height = height
#
#     def get_attrs(self):
#         return self.name, self.weight, self._height
#
#
# class Table(Furniture):
#     def __init__(self, name, weight, height, square):
#         super().__init__(name, weight)
#         self._height, self._square = height, square
#
#     def get_attrs(self):
#         return self.name, self.weight, self._height, self._square


# cl = Closet('шкаф-купе', 342.56, True, 3)
# chair = Chair('стул', 14, 55.6)
# tb = Table('стол', 34.5, 75, 10)
# print(tb.get_attrs())


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/d5aNVdHGj44

Подвиг 7 (введение в паттерн слушатель). Своей работой вы немного впечатлили начальство и оно поручило вам 
доделать паттерн слушатель (listener). Идея этого паттерна очень проста и основа реализуется следующим образом:

class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()
Здесь в объектах класса Subject можно зарегистрировать (добавить) множество объектов класса Observer 
(наблюдатель, слушатель). Это делается с помощью метода add_observer(). Затем, когда данные 
(self.__data) меняются путем вызова метода change_data() класса Subject, то у всех слушателей 
автоматически вызывается метод update(). В этом методе можно прописать самую разную логику 
работы при изменении данных в каждом конкретном слушателе.

В проекте данный паттерн предполагается использовать для отображения информации о погоде в различных форматах:

- текущая температура;
- текущее атмосферное давление;
- текущая влажность воздуха.

Для этого сами данные определяются классом:

class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность
А вам поручается разработать дочерние классы, унаследованные от класса Observer, с именами:

TemperatureView - слушатель для отображения информации о температуре;
PressureView - слушатель для отображения информации о давлении;
WetView - слушатель для отображения информации о влажности.

Каждый из этих классов должен переопределять метод update() базового класса так, чтобы выводилась 
в консоль информация в формате:

TemperatureView: "Текущая температура <число>"
PressureView: "Текущее давление <число>"
WetView: "Текущая влажность <число>"

Важно: для вывода информации в консоль используйте функцию print() с одним аргументом в виде F-строки.

Пример использования классов (эти строчки в программе писать не нужно):

subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))
# выведет строчки:
# Текущая температура 23
# Текущее давление 150
# Текущая влажность 83
subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))
# выведет строчки:
# Текущая температура 24
# Текущее давление 148
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


# class Observer:
#     def update(self, data):
#         pass
#
#     def __hash__(self):
#         return hash(id(self))
#
#
# class Subject:
#     def __init__(self):
#         self.__observers = {}
#         self.__data = None
#
#     def add_observer(self, observer):
#         self.__observers[observer] = observer
#
#     def remove_observer(self, observer):
#         if observer in self.__observers:
#             self.__observers.pop(observer)
#
#     def __notify_observer(self):
#         for ob in self.__observers:
#             ob.update(self.__data)
#
#     def change_data(self, data):
#         self.__data = data
#         self.__notify_observer()
#
#
# class Data:
#     def __init__(self, temp, press, wet):
#         self.temp = temp    # температура
#         self.press = press  # давление
#         self.wet = wet      # влажность
#
#
# class TemperatureView(Observer):
#     def update(self, data):
#         if data:
#             print(f"Текущая температура {data.temp}")
#
#
# class PressureView(Observer):
#     def update(self, data):
#         if data:
#             print(f"Текущее давление {data.press}")
#
#
# class WetView(Observer):
#     def update(self, data):
#         if data:
#             print(f"Текущая влажность {data.wet}")


# subject = Subject()
# tv = TemperatureView()
# pr = PressureView()
# wet = WetView()
#
# subject.add_observer(tv)
# subject.add_observer(pr)
# subject.add_observer(wet)
#
# subject.change_data(Data(23, 150, 83))
# # выведет строчки:
# # Текущая температура 23
# # Текущее давление 150
# # Текущая влажность 83
# subject.remove_observer(wet)
# subject.change_data(Data(24, 148, 80))
# # выведет строчки:
# # Текущая температура 24
# # Текущее давление 148


"""Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:

air = Aircraft(model, mass, speed, top)
где model - модель самолета (строка); mass - подъемная масса самолета (любое положительное число); 
speed - максимальная скорость (любое положительное число); 
top - максимальная высота полета (любое положительное число).

В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами: 
_model, _mass, _speed, _top и соответствующими значениями. 
Если передаваемые аргументы не соответствуют указанным критериям 
(строка, любое положительное число), то генерируется исключение командой:

raise TypeError('неверный тип аргумента')
Далее, в программе объявите следующие дочерние классы:

PassengerAircraft - пассажирский самолет;
WarPlane - военный самолет.

Объекты этих классов создаются командами:

pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест 
(целое положительное число)
wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь); 
ключи - название оружия, значение - количество
В каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты с 
именами _chairs и _weapons соответственно. Инициализация остальных атрибутов должна выполняться 
через инициализатор базового класса.

В инициализаторах классов PassengerAircraft и WarPlane проверять корректность 
передаваемых аргументов chairs и weapons. Если тип данных не совпадает, то генерировать исключение командой:

raise TypeError('неверный тип аргумента')
Создайте в программе четыре объекта самолетов со следующими данными:

PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}

Все эти объекты представить в виде списка planes.

P.S. В программе нужно объявить только классы и сформировать список На экран выводить ничего не нужно."""


# class Aircraft:
#     def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float)):
#         self.__check_str(model)
#         self.__check_val(mass)
#         self.__check_val(speed)
#         self.__check_val(top)
#         self._model, self._mass, self._speed, self._top = model, mass, speed, top
#
#     def __check_str(self, string):
#         if not isinstance(string, str):
#             raise TypeError('неверный тип аргумента')
#
#     def __check_val(self, val):
#         if not isinstance(val, (int, float)) or not val > 0:
#             raise TypeError('неверный тип аргумента')
#
# class PassengerAircraft(Aircraft):
#     def __init__(self, model, mass, speed, top, chairs):
#         super().__init__(model, mass, speed, top)
#         if type(chairs) != int:
#             raise TypeError('неверный тип аргумента')
#         self._chairs = chairs
#
#
# class WarPlane(Aircraft):
#     def __init__(self, model, mass, speed, top, weapons):
#         super().__init__(model, mass, speed, top)
#         if type(weapons) != dict:
#             raise TypeError('неверный тип аргумента')
#         self._weapons = weapons
#
#
# planes = [
#     PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
#     PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
#     WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
#     WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
# ]


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ArF90ldgm70

Подвиг 9 (на повторение). Необходимо объявить функцию-декоратор class_log для класса, 
которая бы создавала логирование вызовов методов класса. Например следующие строчки программы:

vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
декорируют класс Vector и в список vector_log добавляются имена методов, 
которые были вызваны при использовании этого класса. В частности, после выполнения команд:

v = Vector(1, 2, 3)
v[0] = 10
в списке vector_log должны быть два метода:

['__init__', '__setitem__']

Ваша задача реализовать декоратор с именем class_log.

Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим образом:

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls
Используйте этот принцип для успешного прохождения подвига.

P.S. В программе нужно объявить только класс и необходимые функции. На экран выводить ничего не нужно."""



# def class_log(lst):
#     def log_methods(cls):
#         methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#         for k, v in methods.items():
#             setattr(cls, k, log(v))
#         return cls
#
#     def log(func):
#         def wraper(*args, **kwargs):
#             lst.append(func.__name__)
#             return func(*args, **kwargs)
#
#         return wraper
#     return log_methods
#
#
#
# vector_log = []
#
#
# @class_log(vector_log)
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
# v = Vector(1, 2, 3)
# v[0] = 10
# print(vector_log)


"""Подвиг 10 (на повторение). В программе объявлены два класса и глобальная переменная:

CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов
Вам необходимо объявить класс с именем FileDialogFactory (фабрика классов), который бы при выполнении команды:

dlg = FileDialogFactory(title, path, exts)
возвращал объект класса WindowsFileDialog, если CURRENT_OS равна строке 'windows', в противном случае - 
объект класса LinuxFileDialog. Объект самого класса FileDialogFactory создаваться не должен.

Для реализации такой логики, объявите внутри класса FileDialogFactory два статических метода:

def create_windows_filedialog(title, path, exts) - для создания объектов класса WindowsFileDialog;
def create_linux_filedialog(title, path, exts) - для создания объектов класса LinuxFileDialog.

Эти методы следует вызывать в магическом методе __new__() класса FileDialogFactory. 
Подумайте, как это правильно сделать, чтобы не создавался объект самого класса, а лишь 
возвращался объект или класса WindowsFileDialog, или класса LinuxFileDialog.

Пример использования класса (эту строчку в программе не писать):

dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
P.S. В программе нужно дополнительно объявить только класс FileDialogFactory. На экран выводить ничего не нужно."""


CURRENT_OS = 'linux'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __new__(cls, title, path, exts):
        if CURRENT_OS == "windows":
            return cls.create_windows_filedialog(title, path, exts)
        else:
            return cls.create_linux_filedialog(title, path, exts)

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg)