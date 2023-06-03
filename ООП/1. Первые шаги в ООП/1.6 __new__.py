# Метод __new__

class Point:
    def __new__(cls, *args, **kwargs):      # аргументы прописать надо иначе класс не примет аргументы.
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)       # Такая конструкция вернет ссылку на экземпляр, что запустит __init__

    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y


# pt = Point(1, 2)
# print(pt)


# Патерн Singleton (как я понял это невозможность создавать больше одного отдельного экземпляра класса)

class DataBase:
    __instance = None                           # это будет ссылкой на экземпляр
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) # присваеваем адрес базового класса чтоб __instance стал экземпляром
        return cls.__instance                   # возвращаем адрес ранее созданного обьекта

    def __del__(self):
        DataBase.__instance = None              # в случае удаления экземпляра __instance должен снова сать None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие сединения с БД")

    def read(self):
        return "Данные из БД"

    def write(self, data):
        print(f"запись в БД: {data}")


# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40) # ссылается на экземпляр предыдущий. но данные новое потому что не переопределен
#                                     # метод __call__ об этом позже расскажет.
# print(id(db), id(db2))
# db.connect()
# db2.connect()


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7aVqWfrAdqw

Подвиг 6. Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:

obj = AbstractClass()
переменная obj должна ссылаться на строку с содержимым:

"Ошибка: нельзя создавать объекты абстрактного класса"

P.S. В программе объявить только класс, выводить на экран ничего не нужно."""

# class AbstractClass:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             return "Ошибка: нельзя создавать объекты абстрактного класса"
#
# obj = AbstractClass()
# print(obj)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/uE1uf7Qtbh4

Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) 
должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно. """


# class SingletonFive:
#     __lst = []
#
#     def __new__(cls, *args, **kwargs):
#         if len(cls.__lst) < 5:
#             cls.__lst.append(super().__new__(cls))
#             return cls.__lst[-1]
#         else:
#             cls.__lst.append(cls.__lst[4])
#             return cls.__lst[-1]
#
#
#     def __del__(self):
#         SingletonFive.__lst.clear()
#
#     def __init__(self, name):
#         self.name = name
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# for i in objs:
#     print(i)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/sX_uP7GVqkc

Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"
Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:

dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.

Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 
и объекты класса DialogLinux, если переменная TYPE_OS не равна 1. 
При этом, переменная TYPE_OS может меняться в последующих строчках программы. 
Имейте это в виду, при объявлении класса Dialog.

P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog."""

# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
# class Dialog:
#     def __new__(cls, name):
#         if TYPE_OS == 1:
#             instance = super().__new__(DialogWindows)
#             instance.name = name
#             return instance
#         else:
#             instance = super().__new__(DialogLinux)
#             instance.name = name
#             return instance
#
#
# dlg = Dialog("Название")
# print(hasattr(dlg, "name"))
# print(dlg.name_class)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/U4zwfmbEiCI

Подвиг 9 (на повторение материала). Объявите класс Point для представления точек на плоскости. 
Создавать объекты этого класса предполагается командой:

pt = Point(x, y)
Здесь x, y - числовые координаты точки на плоскости (числа), то есть, 
в каждом объекте этого класса создаются локальные свойства x, y, которые хранят конкретные координаты точки.

Необходимо в классе Point реализовать метод clone(self), который бы создавал новый объект класса 
Point как полную копию текущего объекта (с тем же набором и значениями всех локальных свойств).

Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов метода clone.

P.S. В программе на экран ничего выводить не нужно."""


# class Point:
#     def __init__(self, x, y):
#         self.x = int(x)
#         self.y = int(y)
#
#     def clone(self):
#         clone = super().__new__(Point)
#         clone.x = self.x
#         clone.y = self.y
#         return clone
#
# pt = Point(10, 20)
# pt_clone = pt.clone()
# print(pt)
# print(pt_clone)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/5aJVuJ5jGqk

Подвиг 10 (на повторение материала). В программе предполагается реализовать парсер (обработчик) 
строки (string) в определенный выходной формат. Для этого объявлен следующий класс:

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

И предполагается его использовать следующим образом:

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
На выходе (в переменной res) ожидается получить список из набора вещественных чисел. Например, 
для заданной строки, должно получиться:

[4.0, 5.0, -6.5]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя методами:

build_sequence(self) - для создания начального пустого списка (метод должен возвращать пустой список);
build_number(self, string) - для преобразования переданной в метод строки (string) в вещественное 
значение (метод должен возвращать полученное вещественное число).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно."""

# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
# class Factory:
#     def build_sequence(self):
#         return []
#
#     def build_number(self, string):
#         return float(string)
#
# ld = Loader()
# res = ld.parse_format("4, 5, -6.5", Factory())
# print(res)