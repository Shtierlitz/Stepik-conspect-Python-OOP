"""Инициализатор __init__ и финализатор __del__"""

# class Point:
#     color = "red"
#     circle = 2
#
#     def __init__(self, x=0, y=0):   # Создает локальные атрибуты сразу при создании экземпляра.
#         self.x = x                  # Принимает атрибуты согласно указаным инструкциям.
#         self.y = y
#
#     def __del__(self):              # Метод автоматического сборщика мустора.
#         print("deletion of class example: " + str(self))    # Нужно переопределять только когда надо изменить поведение
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# pt = Point(1, 2)
# print(pt.__dict__)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/nT_sMhJsw1E

Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, 
которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.

P.S. На экран в программе ничего выводить не нужно."""

# class Money:
#     def __init__(self, money):
#         self.money = money
#
# my_money = Money(100)
# your_money = Money(1000)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DEyOq7Gpko4

Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), 
а третий необязательный аргумент - цвет точки (локальное свойство color).
 Если цвет не указывается, то он по умолчанию принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, 
с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку). 
Для второго объекта в списке points укажите цвет 'yellow'.

P.S. На экран в программе ничего выводить не нужно."""


# class Point:
#     def __init__(self, x, y, color="black"):
#         self.x = x
#         self.y = y
#         self.color = color
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
#
# points = []
# for i in range(1, 1000*2, 2):
#     if i == 3:
#         points.append(Point(i, i, "yellow"))
#     else:
#         points.append(Point(i, i))


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/bPH4It1_d0c

Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. 
Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов 
(произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах 
sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно 
(или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения). 
Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно."""

#Мое решение
# from random import randint as ri
# from random import choice as ch
# class Line:
#     def __init__(self, a=0, b=0, c=0, d=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Rect:
#     def __init__(self, a=0, b=0, c=0, d=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Ellipse:
#     def __init__(self, a=0, b=0, c=0, d=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# lst = [Line(ri(0, 10), ri(0, 10), ri(0, 10), ri(0, 10)), Rect(ri(0, 10), ri(0, 10), ri(0, 10), ri(0, 10)), Ellipse(ri(0, 10), ri(0, 10), ri(0, 10), ri(0, 10))]
# elements = []
#
# for i in range(217):
#     a = ch(lst)
#     elements.append(a)
#
# for i in range(len(elements)):
#     if isinstance(elements[i], Line):
#         elements.pop(i)
#         elements.insert(i, Line())
#
#
#
# for e in elements:
#     if isinstance(e, Line):
#         print(e.sp)
#         assert e.sp == (0, 0) and e.ep == (0, 0), "в объектах класса Line координаты должны быть равны нулю"

#Решение короче и быстрее
# elements = []
# for _ in range(217):
#     figure = ch([Line, Rect, Ellipse])
#     coords = [0, 0, 0, 0] if figure is Line else [ri(0, 100) for _ in range(4)]
#     elements.append(figure(*coords))


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Vr4c1LgE91o

Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. 
Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).

Sample Input:

3 4 5
Sample Output:

3"""

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         for side in [self.a, self.b, self.c]:
#             if type(side) not in (int, float) or side <=0:
#                 return 1
#             elif not self.a + self.b > self.c or not self.b + self.c > self.a or not self.c + self.a > self.b:
#                 return 2
#             else:
#                 return 3
#
# # a, b, c = map(int, input().split())
# tr = TriangleChecker(0, 4, 5)
# print(tr.is_triangle())

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/a3Har3Z_89Q

Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:

gr_1 = Graph(data)
где data - список из числовых данных (данные для графика). 
При создании каждого экземпляра класса должны формироваться следующие локальные свойства:

data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);

В этом классе объявите следующие методы:

set_data(self, data) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: 
"Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: 
"Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.

Если локальное свойство is_show равно False, то методы show_table(), 
show_graph() и show_bar() должны выводить сообщение:

"Отображение данных закрыто"

Прочитайте из входного потока числовые данные с помощью команды:

data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), 
затем метод set_show() со значением fl_show = False и вызовите метод show_table(). 
На экране должны отобразиться две соответствующие строки.

Sample Input:

8 11 10 -32 0 7 18
Sample Output:

Столбчатая диаграмма: 8 11 10 -32 0 7 18
Отображение данных закрыто"""

# class Graph:
#     def __init__(self, data=None, is_show=True):
#         self.data = data[:]
#         self.is_show = is_show
#         self.s = ""
#
#     def string(self, lst):
#         s = ""
#         for i in lst:
#             s += " " + str(i)
#         s = s.strip()
#         return s
#
#     def set_data(self, data):
#         self.data = data
#
#     def show_table(self):
#         if not self.is_show:
#             return "Отображение данных закрыто"
#         else:
#             return self.string(self.data)
#
#     def show_graph(self):
#         if not self.is_show:
#             return "Отображение данных закрыто"
#         else:
#             return f"Графическое отображение данных: {self.string(self.data)}"
#
#     def show_bar(self):
#         if not self.is_show:
#             return "Отображение данных закрыто"
#         return f"Столбчатая диаграмма: {self.string(self.data)}"
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = [8, 11, 10, -32, 0, 7, 18]
# gr = Graph(data_graph)
# print(gr.show_bar())
# gr.set_show(False)
# print(gr.show_table())
#
#
# data = [1, 2, 3, 4]
# gr2 = Graph(data)
# gr3 = Graph(data)
# gr3.data.append(5)
# print(gr2.data, gr3.data)
#
#
# assert gr2.data != gr3.data, "локальный атрибут data должен быть уникальным (своим собственным) в каждом объекте класса Graph"



"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZTCdEB_6h1I

Подвиг 7. Объявите в программе следующие несколько классов:

CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory, 
максимум N - по числу слотов памяти на материнской плате (по умолчанию N = 4).

Объекты классов должны иметь следующие локальные свойства: 

для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - 
общее число слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - 
список из объектов класса Memory (максимум total_mem_slots штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).

P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям."""


# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
# class MotherBoard:
#     def __init__(self, name, cpu, *args):
#         self.name = name
#         self.cpu = cpu
#         self.args = args
#         self.total_mem_slots = 4
#         self.mem_slots = []
#         for i in self.args:
#             if len(self.mem_slots) <= 4:
#                 self.mem_slots.append(i)
#
#
#
#     def get_config(self):
#         lst = [
#             f"Материнская плата: {self.name}",
#             f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
#             f"Слотов памяти: {self.total_mem_slots}",
#             f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"
#         ]
#         return lst
#
# cp = CPU("intel", "3000")
# mem_1, mem_2 = Memory("SDRam", "256"), Memory("DDR 4", "16000")
# mb = MotherBoard("Atari", cp, mem_1, mem_2)
# print(mb.get_config())


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI

Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки 
(объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), 
два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами. 

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям."""


# class Cart:
#     def __init__(self):
#         self.goods = []
#
    # def add(self, *gd):
    #     self.goods.extend(gd)
#
#     def remove(self, indx):
#         del self.goods[indx]
#
#     def get_list(self):
#         return [f'{i.name}: {i.price}' for i in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# gd1 = Table("ROOM", 2000)
# gd2 = TV("Samsung", 5000)
# gd3 = TV("Sony", 7000)
# gd4 = Notebook("Asus", 20000)
# gd5 = Notebook("DELL", 25000)
# gd6 = Cup("Красный Октябрь", 10)
# cart = Cart()
# cart.add(gd1, gd2, gd3, gd4, gd5, gd6)
#
# print(cart.get_list())


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/3WfWCBKRKIM

Подвиг 9. Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не хранить, а формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:



Для этого объявите в программе класс ListObject, объекты которого создаются командой:

obj = ListObject(data)
Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся строки из списка lst_in (первая строка в первом объекте, вторая - во втором и  т.д.). На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.

P.S. В программе что-либо выводить на экран не нужно.

Sample Input:

1. Первые шаги в ООП
1.1 Как правильно проходить этот курс
1.2 Концепция ООП простыми словами
1.3 Классы и объекты. Атрибуты классов и объектов
1.4 Методы классов. Параметр self
1.5 Инициализатор init и финализатор del
1.6 Магический метод new. Пример паттерна Singleton
1.7 Методы класса (classmethod) и статические методы (staticmethod)"""

# как надо было

import sys

lst_in = [
    '1. Первые шаги в ООП',
    '1.1 Как правильно проходить этот курс',
    '1.2 Концепция ООП простыми словами',
    '1.3 Классы и объекты. Атрибуты классов и объектов',
    '1.4 Методы классов. Параметр self',
    '1.5 Инициализатор init и финализатор del',
    '1.6 Магический метод new. Пример паттерна Singleton',
    '1.7 Методы класса (classmethod) и статические методы (staticmethod)'
]

class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new




#
# Как стоило бы если бы автор хрень не придумал
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         if self.data:
#             self.next_obj = self.data[0]
#             self.data.pop(0)
#         else:
#             self.next_obj = None

# head_obj = ListObject(lst_in)
# obj1 = ListObject(head_obj.data)
# obj2 = ListObject(obj1.data)
# obj3 = ListObject(obj2.data)
# obj4 = ListObject(obj3.data)
# obj5 = ListObject(obj4.data)
# obj6 = ListObject(obj5.data)
# obj7 = ListObject(obj6.data)
# obj8 = ListObject(obj7.data)

# print(head_obj.next_obj,
#       obj1.next_obj,
#       obj2.next_obj,
#       obj3.next_obj,
#       obj4.next_obj,
#       obj5.next_obj,
#       obj6.next_obj,
#       obj7.next_obj,
#       obj8.next_obj,
#       sep="\n"
#       )


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/gmjwMakXk0c

Большой подвиг 10. Объявите два класса: 

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), 
означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны 
создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).



С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется 
объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - 
локальном свойстве pole объекта класса GamePole. 

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, 
разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, 
то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() 
для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. 

P.S. На экран в программе ничего выводить не нужно"""

from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self._n and 0 <= y+j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: "#" if not x.fl_open else x.around_mines if not x.mine else "*", row))


pole_game = GamePole(10, 12)
pole_game.show()

        # for i in self.pole:
        #     for j in range(len(i)):
        #         if i[j].fl_open == False:
        #             print("#", end=" ")
        #         elif not i[j].mine:
        #             print(i[j].around_mines, end=" ")
        #         else:
        #             print("*", end=" ")
        #     print()



