# Наследование в объектно-ориентированном программировании

class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        print("Рисование примитива")


class Line(Geom):
    name = 'Line'

    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    pass


# g = Geom()
# l = Line()
# r = Rect()
# print(g.name)
# print(l.name)
# print(r.name)
# l.set_coords(1, 1, 2, 2,)
# r.set_coords(1, 1, 2, 2,)
# print(l.__dict__)
# print(r.__dict__)
# g.set_coords(0, 0, 0, 0,)
# print(g.__dict__)
# l.draw()
# r.draw()

# https://www.youtube.com/watch?v=7WVYqjdMa6U&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=21

"""Подвиг 4. Наследование часто используют, чтобы вынести общий код дочерних классов в базовый класс. 
Сделаем такой пример. Объявите в программе базовый класс Animal (животное), 
объекты которого можно создать командой:

an = Animal(name, old)
где name - название животного (строка); old - возраст животного (целое число). 
Такие же локальные атрибуты (name и old) должны создаваться в объектах класса.

Далее, объявите дочерний класс (от базового Animal) с именем Cat (кошки), объекты которого создаются командой:

cat = Cat(name, old, color, weight)
где name, old - те же самые параметры, что и в базовом классе; color - цвет кошки (строка); 
weight - вес кошки (любое положительное число).

В объектах класса Cat должны автоматически формироваться локальные атрибуты: name, old, color, weight. 
Формирование атрибутов name, old должен выполнять инициализатор базового класса. 

По аналогии объявите еще один дочерний класс Dog (собака), объекты которого создаются командой:

dog = Dog(name, old, breed, size)
здесь name, old - те же самые параметры, что и в базовом классе; breed - порода собаки (строка); 
size - кортеж в формате (height, length) высота и длина - числа.

В объектах класса Dog по аналогии должны формироваться локальные атрибуты: name, old, breed, size. 
За формирование атрибутов name, old отвечает инициализатор базового класса. 

Наконец, в классах Cat и Dog объявите метод:

get_info() - для получения информации о животном.

Этот метод должен возвращать строку в формате:

"name: old, <остальные параметры через запятую>"

Например, для следующего объекта класса Cat:

cat = Cat('кот', 4, 'black', 2.25)
метод get_info должен вернуть строку:

"кот: 4, black, 2.25"

P.S. В программе достаточно объявить три класса. Выводить на экран ничего не нужно."""

# class Animal:
#     def __init__(self, name: str, old: int):
#         self.name, self.old = name, old
#
# class Cat(Animal):
#     def __init__(self, name, old, color, weight):
#         super().__init__(name, old)
#         self.color = color
#         self.weight = weight
#
#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.color}, {self.weight}"
#
# class Dog(Animal):
#     def __init__(self, name, old, breed, size: tuple):
#         super().__init__(name, old)
#         self.breed = breed
#         self.size = size
#
#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.breed}, {self.size}"


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/K0w2oBTThAc

Подвиг 5. Иногда наследование используют, чтобы наделить объекты дочерних классов 
определенным набором атрибутов. Сделаем такой пример.

Предположим, вы разрабатываете программу для интернет-магазина.
 В этом магазине могут быть как реальные (физические) товары, так и электронные. 
 Для этих двух групп, очевидно, нужен разный набор атрибутов:

- для реальных физических товаров: id, name, price, weight, dims

где id - идентификатор товара (целое число); name - наименование товара (строка); 
price - цена товара (вещественное число); weight - вес товара (вещественное число); 
dims = (lenght, width, depth) - длина, ширина, глубина - габариты товара (вещественные числа);

- для электронных товаров: id, name, price, memory, frm

где id - идентификатор товара (целое число); name - наименование товара (строка);
 price - цена товара (вещественное число); memory - занимаемый размер (в байтах - целое число); 
 frm - формат данных (строка: pdf, docx и т.п.)

Так как все товары могут идти вперемешку, то мы хотим, чтобы в каждом объекте (для товара) 
присутствовали все атрибуты:

id, name, price, weight, dims, memory, frm

с начальными значениями None. А уже, затем, нужным из них будут присвоены конкретные данные.

Для реализации этой логики объявите в программе базовый класс с именем Thing (вещь, предмет), 
объекты которого могут создаваться командой:

th = Thing(name, price)
А атрибут id должен формироваться автоматически и быть уникальным для каждого товара 
(например, можно для каждого нового объекта увеличивать на единицу).

В объектах класса Thing должен формироваться полный набор локальных атрибутов 
(id, name, price, weight, dims, memory, frm) со значением None, кроме атрибутов: id, name, price.

Далее, нужно объявить два дочерних класса:

Table - для столов;
ElBook - для электронных книг.

Объекты этих классов должны создаваться командами:

table = Table(name, price, weight, dims)
book = ElBook(name, price, memory, frm)
Причем, атрибуты name, price (а также id) следует инициализировать в базовом классе, т.к. 
они общие для всех товаров. Остальные атрибуты должны либо принимать значение None, если не используются, 
либо инициализироваться конкретными значениями уже в дочерних классах.

Наконец, в базовом классе Thing объявите метод:

get_data() - для получения кортежа в формате (id, name, price, weight, dims, memory, frm)

Пример использования классов (эти строчки в программе писать не нужно):

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


# class Thing:
#     id = 0
#
#     def __init__(self, name, price):
#         self.name, self.price = name, price
#         Thing.id += 1
#         self.id = Thing.id
#         self.weight = None
#         self.dims = None
#         self.memory = None
#         self.frm = None
#
#     def get_data(self):
#         return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)
#
#
# class Table(Thing):
#     def __init__(self, name, price, weight=None, dims=None):
#         super().__init__(name, price)
#         self.weight = weight
#         self.dims = dims
#         self.memory = None
#         self.frm = None
#
#
# class ElBook(Thing):
#     def __init__(self, name, price, memory=None, frm=None):
#         super().__init__(name, price)
#         self.weight = None
#         self.dims = None
#         self.memory = memory
#         self.frm = frm
#
#
# table = Table("Круглый", 1024, 812.55, (700, 750, 700))
# book = ElBook("Python ООП", 2000, 2048, 'pdf')
# print(*table.get_data())
# print(*book.get_data())


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/k0xvHbnTnoo

Подвиг 6. Еще один пример, когда в базовом классе прописывается необходимый начальный функционал для дочерних классов.

Известно, что браузер (и не только) может отправлять на сервер различные типы запросов: GET, POST, PUT, DELETE и др. Каждый из этих типов запросов обрабатывается в программе на сервере своим отдельным методом. Чтобы каждый раз не прописывать все необходимые методы в классах при обработке входящих запросов, они выносятся в базовый класс и вызываются из дочерних. Выполним такой пример.

Пусть в программе объявлен следующий базовый класс с именем GenericView:

class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
Здесь каждый метод отвечает за обработку своего типа запроса. Параметр methods - это кортеж или список, 
состоящий из набора разрешенных запросов: строк с именами соответствующих методов 
(как правило, пишут заглавными буквами).
Вам необходимо объявить дочерний класс с именем DetailView, объекты которого можно создавать командами:

dv = DetailView()  # по умолчанию methods=('GET',)
dv = DetailView(methods=('PUT', 'POST'))
Для инициализации атрибута methods следует вызывать инициализатор базового класса GenericView.

Далее, в классе DetailView нужно определить метод:

def render_request(self, request, method): ...
который бы имитировал выполнение поступившего на сервер запроса. Здесь request - словарь с набором данных запроса;
 method - тип запроса (строка: 'get' или 'post' и т.д.).

Например:

html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
должен быть обработан запрос как GET-запрос с параметром url и значением 'https://site.ru/home'. 
Параметр url является обязательным в словаре request для каждого запроса.

В методе render_request() необходимо выполнить проверку: является ли указанный метод (method) 
разрешенным (присутствует в коллекции methods). Если это не так, то генерировать исключение командой:

raise TypeError('данный запрос не может быть выполнен')
Если проверка проходит, то выполнить соответствующий метод (или get(), или post(), или put() и т.д. 
с возвращением результата их работы). 

Подсказка: для получения ссылки на нужный метод можно воспользоваться магическим методом __getattribute__() 
или аналогичной функцией getattr()).

Наконец, в дочернем классе DetailView следует переопределить метод get() для нужной нам обработки GET-запросов. 
В этом методе нужно выполнить проверку, что параметр request является словарем. 
Если это не так, то генерировать исключение:

raise TypeError('request не является словарем')
Сделать проверку, что в словаре request присутствует ключ url. Если его нет, то генерировать исключение:

raise TypeError('request не содержит обязательного ключа url')
Если же все проверки проходят, то вернуть строку в формате:

"url: <request['url']>"

Пример (эти строчки в программе писать не нужно):

dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


# class GenericView:
#     def __init__(self, methods=('GET',)):
#         self.methods = methods
#
#     def get(self, request):
#         return ""
#
#     def post(self, request):
#         pass
#
#     def put(self, request):
#         pass
#
#     def delete(self, request):
#         pass
#
#
# class DetailView(GenericView):
#     def __init__(self, methods=('GET',)):
#         super().__init__(methods)
#
#     def render_request(self, request, method):
#         if method not in self.methods:
#             raise TypeError('данный запрос не может быть выполнен')
#         return self.__getattribute__(method.lower())(request)
#
#
#     def get(self, request:dict):
#         if type(request) != dict:
#             raise TypeError('request не является словарем')
#         if "url" not in request.keys():
#             raise TypeError('request не содержит обязательного ключа url')
#
#         return f"url: {request.get('url')}"
#
#
# dv = DetailView()
# html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
# print(html)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PxOfMkw962E

Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). 
Как пример, объявите в программе класс с именем:

Singleton

который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). 
Как это делать, вы должны уже знать из этого курса.

Затем, объявите еще один класс с именем:

Game

который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:

game = Game(name)
где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут 
name с соответствующим содержимым.

Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, 
то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


# https://www.youtube.com/watch?v=PxOfMkw962E - смотреть чтобы правильно делать singletonы

class Singleton:
    __instance = None
    __instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base = object.__new__(cls)
            return cls.__instance_base
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name

# game = Game("Game")
# game2 = Game("TicTacToe")
#
# print(game.name)
# print(game2.name)


"""Подвиг 8. Вам необходимо создать множество классов для валидации (проверки) корректности данных. 
Для этого ваш непосредственный начальник (Senior) предлагает вам объявить в программе базовый класс с именем:

Validator

обеспечивающий базовый функционал для проверки корректности данных. 
В частности, в этом классе нужно объявить следующий метод:

def _is_valid(self, data): ...
По задумке этот метод должен возвращать булево значение True, если данные (data) 
корректны и False - в противном случае.

Так как базовый класс Validator - это общий класс для всех видов проверок, то метод _is_valid()
 будет просто возвращать True.
Кроме того, объекты класса Validator:

v = Validator()   # инициализатор в классе Validator прописывать не нужно
должны вызываться подобно функциям:

v(data)
и если данные (data) некорректны, то генерировать исключение:

raise ValueError('данные не прошли валидацию')
Проверка корректности выполняется с помощью метода _is_valid(). После этого, 
в программе нужно объявить два дочерних класса:

IntegerValidator - для проверки, что data - целое число в заданном диапазоне;
FloatValidator - для проверки, что data - вещественное число в заданном диапазоне.

Объекты этих классов предполагается создавать командами:

integer_validator = IntegerValidator(min_value, max_value)
float_validator = IntegerValidator(min_value, max_value)
где min_value, max_value - допустимый диапазон чисел [min_value; max_value]

Также в этих классах нужно переопределить метод:

def _is_valid(self, data): ...
который бы возвращал True, если data является числом верного типа 
(либо int, либо float в зависимости от валидатора) и находится в заданном диапазоне [min_value; max_value]. 
Иначе, возвращается False.

Пример использования классов (эти строчки в программе писать не нужно):

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)    # исключение ValueError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


# class Validator:
#
#     def _is_valid(self, data):
#         return True
#
#     def __call__(self, data):
#         if self._is_valid(data):
#             min_value = getattr(self, "min_value")
#             max_value = getattr(self, "max_value")
#             if not min_value <= data <= max_value:
#                 raise ValueError('данные не прошли валидацию')
#             return self._is_valid(data)
#         raise ValueError('данные не прошли валидацию')
#
#
# class IntegerValidator(Validator):
#     def __init__(self, min_value, max_value):
#         self.min_value, self.max_value = min_value, max_value
#
#     def _is_valid(self, data):
#         if type(data) != int:
#             raise ValueError('данные не прошли валидацию')
#         return True
#
#
# class FloatValidator(Validator):
#     def __init__(self, min_value, max_value):
#         self.min_value, self.max_value = min_value, max_value
#
#     def _is_valid(self, data):
#         if type(data) != float:
#             return False
#         return True
#
#
# integer_validator = IntegerValidator(-10, 10)
# float_validator = FloatValidator(-1, 1)
# res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
# # res2 = float_validator(10)    # исключение ValueError
#
# # print(res1)
# print(float_validator(1))

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/I8upOO_ZjqQ

Большой подвиг 9. Используя механизм наследования, вам поручено разработать функционал 
по построению моделей нейронных сетей. Общая схема модели очень простая:



Базовый класс Layer имеет локальный атрибут next_layer, который ссылается на 
следующий объект слоя нейронной сети (объект класса Layer или любого объекта дочерних классов). 
У последнего слоя значение next_layer = None.

Создавать последовательность слоев предполагается командами:

first_layer = Layer()
next_layer = first_layer(Layer())
next_layer = next_layer(Layer())
...
То есть, сначала создается объект first_layer класса Layer, 
а затем он вызывается как функция для образования связки со следующим слоем. 
При этом возвращается ссылка на следующий слой и переменная next_layer ссылается уже на этот следующий 
слой нейронной сети. И так можно создавать столько слоев, сколько необходимо.

В каждом объекте класса Layer также должен формироваться локальный атрибут:

name = 'Layer'

Но сам по себе класс Layer образует только связи между слоями. Никакой другой функциональности он не несет. 
Чтобы это исправить, в программе нужно объявить еще два дочерних класса:

Input - формирование входного слоя нейронной сети;
Dense - формирование полносвязного слоя нейронной сети.



Конечно, создавать нейронную сеть мы не будем. Поэтому, в классе Input нужно лишь прописать инициализатор так, 
чтобы его объекты создавались следующим образом:

inp = Input(inputs)
где inputs - общее число входов (целое число). 
Также в объектах класса Input должен автоматически формироваться атрибут:

name = 'Input'

(Не забывайте при этом, вызывать инициализатор базового класса Layer).

Объекты второго дочернего класса Dense предполагается создавать командой:

dense = Dense(inputs, outputs, activation)
где inputs - число входов в слой; outputs - число выходов слоя (целые числа); activation - 
функция активации (строка, например: 'linear', 'relu', 'sigmoid'). 
И в каждом объекте класса Dense также должен автоматически формироваться атрибут:

name = 'Dense'

Все эти классы совместно можно использовать следующим образом (эти строчки пример, писать не нужно):

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
Здесь создается три слоя нейронной сети. 

Наконец, для перебора всех слоев с помощью цикла for, 
необходимо объявить отдельный класс NetworkIterator для итерирования (перебора) слоев
 нейронной сети следующим образом:

for x in NetworkIterator(network):
    print(x.name)
Здесь создается объект класса NetworkIterator. На вход передается первый объект (слой) нейронной сети. 
Объект этого класса является итератором, который в цикле for 
последовательно возвращает объекты (слои) нейронной сети.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""

class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'


    def __call__(self, next_layer):
        if next_layer is not None:
            self.next_layer = next_layer
        return self.next_layer

class Input(Layer):
    def __init__(self, inputs: int):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs

class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.inputs, self.outputs, self.activation = inputs, outputs, activation
        self.name = 'Dense'


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        obj = self.network
        while obj.next_layer is not None:
            yield obj
            obj = obj.next_layer
        yield obj



# first_layer = Layer()
# # print(first_layer.__dict__, end='\n\n')
# sec_layer = first_layer(Layer())
# # print(first_layer.__dict__)
# # print(sec_layer.__dict__, end='\n\n')
# thrd_layer = sec_layer(Layer())
# # print(first_layer.__dict__)
# # print(sec_layer.__dict__)
# # print(thrd_layer.__dict__, end='\n\n')
#
# network = Input(128)
# layer = network(Dense(network.inputs, 1024, 'linear'))
# layer = layer(Dense(layer.inputs, 10, 'softmax'))
#
# for x in NetworkIterator(network):
#     print(x.name)

# nt = Input(12)
# layer = nt(Dense(nt.inputs, 1024, 'relu'))
# layer = layer(Dense(layer.inputs, 2048, 'relu'))
# layer = layer(Dense(layer.inputs, 10, 'softmax'))
#
# n = 0
# for x in NetworkIterator(nt):
#     assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
#     n += 1
#
# assert n == 4, "итератор перебрал неверное число слоев"


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Q_zIap6F1Lw

Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны 
быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. 
Иначе, v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


class Vector:
    def __init__(self, *args):
        self.__coords = tuple(i for i in args)


    def __check_sizes(self, vector):
        if len(vector) != len(self.__coords):
            raise TypeError('размерности векторов не совпадают')

    def __check_class(self, coords):
        try:
            return self.__class__(*coords)      # важный принцип не повторять элементов доченрих классов в базовом
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        sc = other.get_coords()
        self.__check_sizes(sc)
        coords = tuple(map(lambda x, y: x + y, self.__coords, sc))
        return self.__check_class(coords)

    def __sub__(self, other):
        sc = other.get_coords()
        self.__check_sizes(sc)
        coords = tuple(map(lambda x, y: x - y, self.__coords, sc))
        return self.__check_class(coords)

    def get_coords(self):
        return self.__coords

class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        self.__coords = ()
        for i in args:
            if type(i) != int:
                raise ValueError('координаты должны быть целыми числами')
            self.__coords += i,



# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# v = v1 + v2
# print(v.get_coords())
# v = VectorInt(1, 2, 3, 4)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
#
# v3 = v1 + v2  # v1 - объект класса VectorInt
# v4 = v1 - v2  # v1 - объект класса VectorInt
# print(v4.get_coords())

s = tuple(1, 2 ,3)
print(s)