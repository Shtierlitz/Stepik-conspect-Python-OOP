# Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие
# можно определять только по одному методу. Остальные работают по инверсии

class Clock:
    __DAY = 86400                           # Число секунд в одном дне

    def __init__(self, seconds: int):       # такой фокус напоминает какой тип данных должен быть
        if not isinstance(seconds, int):    # isinstance проверяет принадлежность экземпляра к классу (в этом случае к классу int)
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod                            # метод класса дабы не дублировать код в каждом последующем
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        print("__eq__")
        sc = self.__verify_data(other)
        return self.seconds == sc           # != работает по принципу not (x == x)

    def __ne__(self, other):
        print("__ne__")
        sc = self.__verify_data(other)
        return self.seconds != sc

    def __lt__(self, other):
        print("__lt__")
        sc = self.__verify_data(other)
        return self.seconds < sc            # __gt__ можно не переопределять так как __lt__ поменяет операторы местами

    def __gt__(self, other):
        print("__gt__")
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        print("__le__")
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __ge__(self, other):
        print("__ge__")
        sc = self.__verify_data(other)
        return self.seconds >= sc


# c1 = Clock(1000)
# c2 = Clock(2000)
#print(c1 == c2)                             # 1 пример без методов сравнения сравнивает не значения, а id экземпляров класса и выводит False
# print(c1 == с2)                            # 2 пример с методом __eq__ выводит True и сравнивает уже экземпляры класса
#print(c1 != 1000)                           # 2 != тоже работает так как __eq__ просто инвертируется (подставляет not)
# print(c1 < c2)                             # 3 < > оба работают так как тут тоже делается инверсия уже операндов. То есть с2 становится на место с1
# print(c2 > c1)

# https://www.youtube.com/watch?v=l3jMyZKDxXE&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=16


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/cHV-yuNFavg

Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:

track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); 
max_speed - максимальная скорость на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:

add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:

track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2  # True, если длина пути для track1 больше, чем для track2
track1 < track2  # True, если длина пути для track1 меньше, чем для track2
И функция:

n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
Создайте два маршрута track1 и track2 с координатами:

1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.

P.S. На экран в программе ничего выводить не нужно."""

# ((x1 - x0)**2 + (y1 - y0)**2) ** 0.5



# class TrackLine:
#     def __init__(self, to_x, to_y, max_speed):
#         self.to_x = to_x
#         self.to_y = to_y
#         self.max_speed = max_speed
#
# class Track:
#     def __init__(self, start_x=0, start_y=0):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.__tup = ()
#         self.__tup += TrackLine(self.start_x, self.start_y, 0),
#
#     def add_track(self, tr: TrackLine):
#         self.__tup += tr,
#
#     def get_tracks(self):
#         return self.__tup
#
#     def __lst_other(self, other):
#         return sum([(i.to_x-i.to_y)**2 for i in other.get_tracks()])**0.5
#
#     def __lst_self(self):
#         return sum([(i.to_x - i.to_y) ** 2 for i in self.get_tracks()]) ** 0.5
#
#     def __eq__(self, other):
#         return self.__lst_self() == self.__lst_other(other)
#
#     def __ne__(self, other):
#         return self.__lst_self() != self.__lst_other(other)
#
#     def __lt__(self, other):
#         return self.__lst_self() < self.__lst_other(other)
#
#     def __gt__(self, other):
#         return self.__lst_self() > self.__lst_other(other)
#
#     def __len__(self):
#         return int(self.__lst_self())
#
#
# track1, track2 = Track(), Track(0, 1)
# track1.add_track(TrackLine(2, 4, 100))
# track1.add_track(TrackLine(5, -4, 100))
# track2.add_track(TrackLine(3, 2, 90))
# track2.add_track(TrackLine(10, 8, 90))
# res_eq = track1 == track2
# n = len(track1)
# print(n)
# print(track1.get_tracks())
# print(res_eq)

"""Подвиг 4. Объявите класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 10000
Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.

Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства 
(property) с именами: a, b, c. Причем, в момент присваивания нового значения должна выполняться 
проверка попадания числа в диапазон [MIN_DIMENSION; MAX_DIMENSION]. Если число не попадает, 
то оно игнорируется и существующее значение не меняется.

С объектами класса Dimensions должны выполняться следующие операторы сравнения:

dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
dim1 > dim2    # True, если объем dim1 больше объема dim2
dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
dim1 < dim2    # True, если объем dim1 меньше объема dim2
Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, price, dim)
где name - название товара (строка); price - цена товара (целое или вещественное число); 
dim - габариты товара (объект класса Dimensions).

В каждом объекте класса ShopItem должны создаваться локальные атрибуты:

name - название товара;
price - цена товара;
dim - габариты товара (объект класса Dimensions).

Создайте список с именем lst_shop из четырех товаров со следующими данными:

- кеды; 1024; (40, 30, 120)
- зонт; 500.24; (10, 20, 50)
- холодильник; 40000; (2000, 600, 500)
- табуретка; 2000.99; (500, 200, 200)

Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) 
товаров списка lst_shop, используя стандартную функцию sorted() языка Python и ее параметр 
key для настройки сортировки. Прежний список lst_shop должен оставаться без изменений.

P.S. На экран в программе ничего выводить не нужно."""



# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     def __chack_range(self, obj):
#         return Dimensions.MIN_DIMENSION <= obj <= Dimensions.MAX_DIMENSION
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, obj):
#         if self.__chack_range(obj):
#             self.__a = obj
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, obj):
#         if self.__chack_range(obj):
#             self.__b = obj
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, obj):
#         if self.__chack_range(obj):
#             self.__c = obj
#
#     def __ge__(self, other):
#         return self.a * self.b * self.c >= other.a * other.b, other.c
#
#     def __lt__(self, other):
#         return self.a * self.b * self.c < other.a * other.b, other.c
#
#
# class ShopItem:
#     def __init__(self, name, price, dim: Dimensions):
#         self.name = name
#         self.price = price
#         self.dim = dim
#
#     def get_dimension(self):
#         return self.dim.a * self.dim.b * self.dim.c
#
# lst_shop  = [
#     ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
#     ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
#     ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
#     ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200)),
# ]
# lst_shop_sorted  = sorted(lst_shop, key=lambda x: x.get_dimension())
# print([i.name for i in lst_shop_sorted])

"""Подвиг 5. Имеется стихотворение, представленное следующим списком строк:

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]
Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" 
в начале и в конце каждого слова и разбить строку по словам (слова разделяются одним или несколькими пробелами). 
На основе полученного списка слов, создать объект класса StringText командой:

st = StringText(lst_words)
где lst_words - список из слов одной строчки стихотворения. 

С объектами класса StringText должны быть реализованы операторы сравнения:

st1 > st2   # True, если число слов в st1 больше, чем в st2
st1 >= st2  # True, если число слов в st1 больше или равно st2
st1 < st2   # True, если число слов в st1 меньше, чем в st2
st1 <= st2  # True, если число слов в st1 меньше или равно st2
Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text. 
Затем, сформировать новый список lst_text_sorted из отсортированных объектов класса 
StringText по убыванию числа слов. Для сортировки использовать стандартную функцию sorted() языка Python.
 После этого преобразовать данный список (lst_text_sorted) 
 в список из строк (объекты заменяются на соответствующие строки, между словами ставится пробел).

P.S. На экран в программе ничего выводить не нужно."""



# stich = ["Я к вам пишу – чего же боле?",
#         "Что я могу еще сказать?",
#         "Теперь, я знаю, в вашей воле",
#         "Меня презреньем наказать.",
#         "Но вы, к моей несчастной доле",
#         "Хоть каплю жалости храня,",
#         "Вы не оставите меня."]
#
# lst_words = [i.strip("–?!,.;").split(" ") for i in stich]
#
#
#
# class StringText:
#     def __init__(self, lst_words):
#         self.lst_words = lst_words
#
#     def __le__(self, other):
#         return len(self.lst_words) <= len(other)
#
#     def __lt__(self, other):
#         return len(self.lst_words) < len(other)
#
#     def __len__(self):
#         return len(self.lst_words)
#
# lst_text = [StringText(lst_words[i]) for i in range(len(lst_words))]
# lst_text_sorted = sorted(lst_text, key=lambda x: len(x.lst_words), reverse=True)
# lst = lst_text_sorted[:]
# lst_text_sorted.clear()
#
# for i in range(len(lst)):
#     for j in lst[i].lst_words:
#         lst_text_sorted.append(j)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PJsJOIxZOdM

Подвиг 6. Ваша задача написать программу поиска слова в строке. Задача усложняется тем, 
что слово должно определяться в разных его формах. Например, слово:

программирование

может иметь следующие формы:

программирование, программированию, программированием, программировании, программирования, 
программированиям, программированиями, программированиях

Для решения этой задачи необходимо объявить класс Morph (морфология), объекты которого создаются командой:

mw = Morph(word1, word2, ..., wordN)
где word1, word2, ..., wordN - возможные формы слова.

В классе Morph реализовать методы:

add_word(self, word) - добавление нового слова (если его нет в списке слов объекта класса Morph);
get_words(self) - получение кортежа форм слов.

Также с объектами класса Morph должны выполняться следующие операторы сравнения:

mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)
И аналогичная пара сравнений:

"word" == mw1
"word" != mw1
После создания класса Morph, формируется список dict_words из объектов этого класса, 
для следующих слов с их словоформами:

- связь, связи, связью, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях

Затем, прочитайте строку из входного потока командой:

text = input()
Найдите все вхождения слов из списка dict_words (используя операторы сравнения) 
в строке text (без учета регистра, знаков пунктуаций и их словоформы). Выведите на экран полученное число.

Sample Input:

Мы будем устанавливать связь завтра днем.
Sample Output:

2"""


# class Morph:
#     def __init__(self, *args):
#         self.container = tuple(i.lower() for i in args)
#
#
#     def add_word(self, word):
#         self.container += word.lower(),
#
#     def get_words(self):
#         return self.container
#
#     def __eq__(self, other):
#         return True if other.lower() in self.get_words() else False
#
# dict_words = [
#     Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
#     Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
#     Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
#     Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
#     Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
# ]
# text = input()
# result = [i.strip(".") for i in text.split()]
# count = 0
# for i in result:
#     for j in dict_words:
#         if i.lower() == j:
#             count += 1
# print(count)

"""Подвиг 7 (на повторение). Перед вами стоит задача выделения файлов с 
определенными расширениями из списка файлов, например:

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", 
"forest.jpeg", "eq_1.png", "eq_2.xls"]
Для этого необходимо объявить класс FileAcceptor, объекты которого создаются командой:

acceptor = FileAcceptor(ext1, ..., extN)
где ext1, ..., extN - строки с допустимыми расширениями файлов, например: 'jpg', 'bmp', 'jpeg'.

После этого предполагается использовать объект acceptor в стандартной функции filter языка 
Python следующим образом:

filenames = list(filter(acceptor, filenames))
То есть, объект acceptor должен вызываться как функция:

acceptor(filename) 
и возвращать True, если файл с именем filename содержит расширения, 
указанные при создании acceptor, и False - в противном случае. 
Кроме того, с объектами класса FileAcceptor должен выполняться оператор:

acceptor12 = acceptor1 + acceptor2
Здесь формируется новый объект acceptor12 с уникальными расширениями первого и второго объектов. Например:

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
Пример использования класса (эти строчки в программе писать не нужно):

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
P.S. На экран в программе ничего выводить не нужно."""

# filenames = ["qqwe.dsa", "boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
#
# class FileAcceptor:
#     def __init__(self, *args):
#         self.__d = []
#         if type(args[0]) == tuple:
#             for i in args[0]:
#                 self.__d.append(i)
#         else:
#             for i in args:
#                 self.__d.append(i)
#
#     @property
#     def ext(self):
#         d = tuple(i for i in self.__d)
#         return d
#
#     @ext.setter
#     def ext(self, obj):
#         self.__d.append(obj)
#
#     def __call__(self, filename):
#         s = filename[::-1]
#         d = s.index(".")
#         w = s[:d]
#         return True if w in [i[::-1] for i in self.ext] else False
#
#     def __add__(self, other):
#         if isinstance(other, FileAcceptor):
#             for i in other.ext:
#                 if i not in self.ext:
#                     self.__d.append(i)
#             return FileAcceptor(self.ext)
#
# acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# acceptor_docs = FileAcceptor("txt", "doc", "xls")
# filenames = list(filter(acceptor_images + acceptor_docs, filenames))
#
# print(filenames)


"""Тестовая задача на работу в РФ пример"""
# s = "aaaAAAdddddddddddddddeebbzzzzzzzzzzzbc"
# def sting_analys(s):
#     """Написать функцию чтоб проверяла строку, считала максимальную по количеству в ней букву
#     и возвращала кортеж по примерру : ('d', 15)"""
#     st = s.lower()
#     counter = 0
#     d = {}
#     result = tuple()
#     for i in range(len(st)):
#         for j in range(len(st)):
#             if st[i] == st[j]:
#                 counter += 1
#             else:
#                 pass
#         if st[i] not in d:
#             d[st[i]] = counter
#         counter = 0
#     res = max(d.values())
#     for k, v in d.items():
#         if v == res:
#             result += k, v,
#     return result
#
# print(sting_analys(s))




"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/qKTQLo-plpc

Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:

MoneyR - для рублевых кошельков
MoneyD - для долларовых кошельков
MoneyE - для евро-кошельков



Объекты этих классов могут создаваться командами:

rub = MoneyR()   # с нулевым балансом
dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро
В каждом объекте этих классов должны формироваться локальные атрибуты:

__cb - ссылка на класс CentralBank (центральный банк, изначально None);
__volume - объем денежных средств в кошельке (если не указано, то 0).

Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property) для работы с
 локальными атрибутами:

cb - для изменения и считывания данных из переменной __cb;
volume - для изменения и считывания данных из переменной __volume.

Объекты классов должны поддерживать следующие операторы сравнения:

rub < dl
dl >= euro
rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
euro > rub
При реализации операторов сравнения считываются соответствующие значения __volume из 
сравниваемых объектов и приводятся к рублевому эквиваленту в соответствии с курсом валют центрального банка.

Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки, необходимо 
в программе объявить еще один класс CentralBank. Объекты класса CentralBank создаваться 
не должны (запретить), при выполнении команды:

cb = CentralBank()

должно просто возвращаться значение None. А в самом классе должен присутствовать атрибут:

rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
Здесь числа (в значениях словаря) - курс валюты по отношению к доллару. 

Также в CentralBank должен быть метод уровня класса:

register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и MoneyE.

При регистрации значение __cb объекта money должно ссылаться на класс CentralBank. 
Через эту переменную объект имеет возможность обращаться к атрибуту rates класса 
CentralBank и брать нужные котировки.

Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:

raise ValueError("Неизвестен курс валют.")
Пример использования классов (эти строчки в программе писать не нужно):

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
P.S. В программе на экран ничего выводить не нужно, только объявить классы."""


# class MoneyR:
#     def __init__(self, volume=0.0):
#         self.__volume = volume
#         self.__cb = None
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, vol):
#         self.__volume = vol
#
#     @property
#     def cb(self):
#         return self.__cb
#
#     @cb.setter
#     def cb(self, bank):
#         self.__cb = bank
#
#     @property
#     def class_money(self):
#         return self.class_money
#
#     @class_money.setter
#     def class_money(self, class_m):
#         self.class_money = class_m
#
#     def __comparison_rubl(self, other):
#         "Доп метод чтобы конвертировать валюту у прибавляемого обьекта"
#         if isinstance(other, MoneyD):
#             return (other.volume * self.cb.get("dollar")) * self.cb.get("rub")
#         if isinstance(other, MoneyE):
#             return (other.volume * self.cb.get("euro")) * self.cb.get("rub")
#         if isinstance(other, MoneyR):
#             return other.volume
#
#     def __self_compr(self):
#         """Доп метод чтобы конвертировать валюту в собственном классе"""
#         if type(self) is MoneyR:
#             return self.volume
#         if type(self) is MoneyD:
#             return (self.volume * self.cb.get("dollar")) * self.cb.get("rub")
#         if type(self) is MoneyE:
#             return (self.volume * self.cb.get("euro")) * self.cb.get("rub")
#
#     def __check_bank(self):
#         """Метод проверки на регистрацию в банке (чтоб код не дублировать)"""
#         if self.cb is None:
#             raise ValueError("Неизвестен курс валют.")
#
#     def __eq__(self, other):
#         """Нагуглил, что сравнивать обьекты с погрешностью проще
#         отняв их друг от друга и сравнивать с самой погрешностью"""
#         self.__check_bank()
#         temp = abs(self.__self_compr() - self.__comparison_rubl(other))
#         allowed_error = 0.1
#         return temp <= allowed_error
#
#     def __lt__(self, other):
#         self.__check_bank()
#         return self.__self_compr() < self.__comparison_rubl(other)
#
#     def __ge__(self, other):
#         self.__check_bank()
#         return self.__self_compr() >= self.__comparison_rubl(other)
#
#
# class MoneyD(MoneyR):
#     pass
#
#
# class MoneyE(MoneyR):
#     pass
#
#
# class CentralBank:
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
#     @classmethod
#     def register(cls, money):
#         money.cb = cls.rates
#
#
# rub = MoneyR()  # с нулевым балансом
# dl = MoneyD(1501.25)  # с балансом в 1501.25 долларов
# euro = MoneyE(100)  # с балансом в 100 евро
#
# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
# r = MoneyR(800.0005)
# r1 = MoneyR(83.375)
# d = MoneyD(11.0344828)
# d1 = MoneyD(800.0005)
# e = MoneyE(1)
# e1 = MoneyE(800.0005)
#
# CentralBank.register(r1)
# CentralBank.register(r)
# CentralBank.register(e)
# CentralBank.register(e1)
#
# CentralBank.register(d)
# CentralBank.register(d1)
#
#
# if r1 >= e:
#     print("неплохо")
# else:
#     print("нужно поднажать")

"""Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); 
volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно."""

# class Body:
#     def __init__(self, name: str, ro: (int, float), volume: (int, float)):
#         self.name = name
#         self.ro = ro
#         self.volume = volume
#         self.mass = self.ro * self.volume
#
#     def __eq__(self, other):
#         if type(other) == Body:
#             return self.mass == other.mass
#         return self.mass == other
#
#     def __lt__(self, other):
#         if type(other) == Body:
#             return self.mass < other.mass
#         return self.mass < other
#
#
# body1 = Body("Тушкан", 20.1, 120)
# body2 = Body("Потап", 20.1, 120)
# print(body1 < body2)
# print(body1 < 100)


"""Подвиг 10. Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()
А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса 
Thing одного ящика и можно найти ровно один равный объект из второго ящика).

Пример использования классов:

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
P.S. В программе только объявить классы, выводить на экран ничего не нужно."""

# class Thing:
#     def __init__(self, name, mass):
#         self.name = name.lower()
#         self.mass = mass
#
#     def __eq__(self, other):
#         if isinstance(other, Thing):
#             return self.name == other.name and self.mass == other.mass
#
#
# class Box:
#     def __init__(self):
#         self.__box = []
#
#     def add_thing(self, obj):
#         self.__box.append(obj)
#
#     def get_things(self):
#         return self.__box
#
#     def __eq__(self, other):
#         """Еще раз. Только по одному обьекту должно быть равным и списки должны быть по длине равными"""
#         if not isinstance(other, Box):
#             raise ValueError("Сравнение должно быть только с классом Box")
#         counter = 0
#         s = self.get_things()
#         o = other.get_things()
#
#         for i in s:
#             for j in o:
#                 if i == j:
#                     counter += 1
#         return True if counter == len(self.get_things()) else False
#
#
#
# b1 = Box()
# b2 = Box()
#
# b1.add_thing(Thing('мел', 100))
# b1.add_thing(Thing('тряпка', 200))
# b1.add_thing(Thing('доска', 2000))
#
# b2.add_thing(Thing('тряпка', 200))
# b2.add_thing(Thing('доска', 2000))
# b2.add_thing(Thing('мел', 100))
#
# res = b1 == b2 # True
# print(res)
