# Магические методы __getitem__, __setitem__ и __delitem__
# __getitem__ нужен для того чтобы доставать индексы из атребутов класса
# __setitem__ нужен чтобы индексу можно было присвоить что-то новое
# __delitem__ удаляет элемент из индексов

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:     # Индекс должен быть целым не отрицательным
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        if key >= len(self.marks):                  # Если индекс больше или равен длине списка
            off = key + 1 - len(self.marks)         # добавляем все пропущенные индексы
            self.marks.extend([None]*off)           # заполняем пустые индексы значениями None по индекса off
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        del self.marks[key]

# s1 = Student("Сергей", [5, 5, 3, 2, 5])
# print(s1.marks[2])              # Так приходится записывать без __getitem__
#print(s1[2])                      # А вот так если есть __getitem__
# s1[10] = 4                         # так если мы хотим присвоить индексу значение через __setitem__
# print(s1.marks)
# del s1[2]
# print(s1.marks)

# https://www.youtube.com/watch?v=EAoiOwYQSuY&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=19


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/FWp5trS42e4

Подвиг 2. Объявите класс Record (запись), который описывает одну произвольную запись из БД. 
Объекты этого класса создаются командой:

r = Record(field_name1=value1,... , field_nameN=valueN)
где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по 
именам полей (field_name1,... , field_nameN) с соответствующими значениями. Например:

r = Record(pk=1, title='Python ООП', author='Балакирев')
В объекте r появляются атрибуты:

r.pk # 1
r.title # Python ООП
r.author # Балакирев
Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError
Если указывается неверный индекс (не целое число или некорректное целое число), 
то должно генерироваться исключение командой:

raise IndexError('неверный индекс поля')
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record."""


# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         s = self.__dict__.keys()
#         print(tuple(s)[2])
#
#     def __getitem__(self, item):
#         if (-len(self.__dict__)) <= item < len(self.__dict__) and isinstance(item, int):
#             return list(self.__dict__.values())[item]
#         else:
#             raise IndexError('неверный индекс поля')
#
#     def __setitem__(self, key, value):
#         if (-len(self.__dict__)) <= key < len(self.__dict__) and  isinstance(key, int):
#             setattr(self, tuple(self.__dict__.keys())[key], value)
#         else:
#             raise IndexError('неверный индекс поля')
#
#
# r = Record(pk=1, title='Python ООП', author='Балакирев')
# r[0] = 2 # доступ к полю pk
# r[1] = 'Супер курс по ООП' # доступ к полю title
# r[2] = 'Балакирев С.М.' # доступ к полю author
# print(r[0])
# print(r[1]) # Супер курс по ООП
# print(r[2])
# print(r[3])


"""Подвиг 3. Вам необходимо для навигатора реализовать определение маршрутов. 
Для этого в программе нужно объявить класс Track, объекты которого создаются командой:

tr = Track(start_x, start_y)
где start_x, start_y - координата начала пути.

В этом классе должен быть реализован следующий метод:

add_point(x, y, speed) - добавление новой точки маршрута (линейный сегмент), 
который можно пройти со средней скоростью speed.

Также с объектами класса Track должны выполняться команды:

coord, speed = tr[indx] # получение координаты (кортеж с двумя числами) и скорости (число) 
для линейного сегмента маршрута с индексом indx
tr[indx] = speed # изменение средней скорости линейного участка маршрута по индексу indx
Если индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1, где N - 
число линейных сегментов в маршруте), то генерируется исключение командой:

raise IndexError('некорректный индекс')
Пример использования класса (эти строчки в программе не писать):

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно."""
# class Track:
#     def __init__(self, start_x, start_y):
#         self.__start_x, self.__start_y = start_x, start_y
#         self.__line_sig = []
#
#     def add_point(self, x, y, speed):
#         c = [(x, y), speed]
#         self.__line_sig.append(c)
#
#     def __check_index(self, indx):
#         if (-len(self.__line_sig)) <= indx < len(self.__line_sig) and type(indx) != int:
#             raise IndexError('некорректный индекс')
#
#     def __getitem__(self, item):
#         self.__check_index(item)
#         return self.__line_sig[item][0], self.__line_sig[item][1]
#
#     def __setitem__(self, key, value):
#         self.__check_index(key)
#         self.__line_sig[key][1] = value
#
# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
# tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
# tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
#
# tr[2] = 60
# c, s = tr[2]
# print(c, s)

# res = tr[3] # IndexError



"""Подвиг 4. Вам необходимо написать программу по работе с массивом однотипных данных 
(например, только числа или строки и т.п.). Для этого нужно объявить класс с именем Array, 
объекты которого создаются командой:

ar = Array(max_length, cell)
где max_length - максимальное количество элементов в массиве; cell - ссылка на класс,
 описывающий отдельный элемент этого массива (см. далее, класс Integer). 
 Начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0.

Для работы с целыми числами объявите в программе еще один класс с именем Integer, 
объекты которого создаются командой:

cell = Integer(start_value)
где start_value - начальное значение ячейки (в данном случае - целое число).

В классе Integer должно быть следующее свойство (property):

value - для изменения и считывания значения из ячейки 
(само значение хранится в локальной приватной переменной; имя придумайте сами).

При попытке присвоить не целое число должно генерироваться исключение командой:

raise ValueError('должно быть целое число')
Для обращения к отдельным элементам массива в классе Array 
необходимо определить набор магических методов для следующих операций:

value = ar[0] # получение значения из первого элемента (ячейки) массива ar
ar[1] = value # запись нового значения во вторую ячейку массива ar
Если индекс не целое число или число меньше нуля или больше либо равно max_length, 
то должно генерироваться исключение командой:

raise IndexError('неверный индекс для доступа к элементам массива')
Пример использования классов (эти строчки в программе не писать):

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. В качестве дополнительного домашнего задания: объявите еще один класс 
Float для работы с вещественными числами и создайте массив, используя тот же класс Array, 
с этим новым типом данных."""

class Integer:
    def __init__(self, start_value=0):
        self.__start_value = start_value


    @property
    def value(self):
        return self.__start_value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__start_value = val

    def __repr__(self):
        return str(self.__start_value)

class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__ar = [self.__cell() for _ in range(self.__max_length)]

    def __check_index(self, indx):
        if type(indx) != int or not (-self.__max_length <= indx < self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__ar[item].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__ar[key].value = value

    def __repr__(self):
        return " ".join(map(str, self.__ar))



# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
#
# ar_int[1] = 10
#
# ar_int[8] = 1 # должно генерироваться исключение IndexError
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# # ar_int[1] = 10.5 # должно генерироваться исключение ValueError

"""Большой подвиг 5. Вам необходимо написать программу для удобного обращения с 
таблицами однотипных данных (чисел, строк, булевых значений и т.п.), то есть, 
все ячейки таблицы должны представлять какой-то один указанный тип.



Для этого в программе необходимо объявить три класса:

TableValues - для работы с таблицей в целом;
CellInteger - для операций с целыми числами;
IntegerValue - дескриптор данных для работы с целыми числами.

Начнем с дескриптора IntegerValue. Это должен быть дескриптор данных 
(то есть, и для записи и считывания значений). 
Если присваиваемое значение не является целым числом, должно генерироваться исключение командой:

raise ValueError('возможны только целочисленные значения')
Следующий класс CellInteger описывает одну ячейку таблицы для работы с целыми числами. 
В этом классе должен быть публичный атрибут (атрибут класса):

value - объект дескриптора, класса IntegerValue.

А объекты класса CellInteger должны создаваться командой:

cell = CellInteger(start_value)
где start_value - начальное значение ячейки (по умолчанию равно 0 и сохраняется в ячейке через дескриптор value).

Наконец, объекты последнего класса TableValues создаются командой:

table = TableValues(rows, cols, cell=CellInteger)
где rows, cols - число строк и столбцов (целые числа); cell - ссылка на класс, 
описывающий работу с отдельными ячейками таблицы. Если параметр cell не указан, то генерировать исключение командой:

raise ValueError('параметр cell не указан')
Иначе, в объекте table класса TableValues создается двумерный (вложенный) 
кортеж с именем cells размером rows x cols, 
состоящий из объектов указанного класса (в данном примере - класса CellInteger).

Также в классе TableValues предусмотреть возможность обращения к отдельной ячейке по ее индексам, например:

value = table[1, 2] # возвращает значение ячейки с индексом (1, 2)
table[0, 0] = value # записывает новое значение в ячейку (0, 0)
Обратите внимание, по индексам сразу должно возвращаться значение ячейки, 
а не объект класса CellInteger. И то же самое с присваиванием нового значения.

Пример использования классов (эти строчки в программе не писать):

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. В качестве домашнего задания создайте класс CellString для работы со строками и 
используйте тот же класс TableValues для этого нового типа данных.

Последнее: дескрипторы здесь для повторения. В реальной разработке лучше 
использовать в таких задачах объекты-свойства (property)."""

# class IntegerValue:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.val_valid(value)
#         instance.__dict__[self.name] = value
#
#     def val_valid(self, val):
#         if type(val) != int:
#             raise ValueError('возможны только целочисленные значения')
#
# class CellInteger:
#
#     value = IntegerValue()
#
#     def __init__(self, start_value=0):
#         self.value = start_value
#
# class TableValues:
#     def __init__(self, rows, cols, cell: CellInteger):
#         self.__rows = rows
#         self.__cols = cols
#         if not cell:
#             raise ValueError('параметр cell не указан')
#         self.__cell = cell
#         self.cells = tuple(tuple(self.__cell() for _ in range(self.__cols)) for _ in range(self.__rows))
#
#
#     def __getitem__(self, item):
#         return self.cells[item[0]][item[1]].value
#
#
#     def __setitem__(self, key, value):
#         self.cells = list(self.cells)
#         self.cells[key[0]][key[1]].value = value


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/jk9AOnvm65k

Подвиг 6. Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке до последнего:



Для этого в программе объявлялись два класса: 

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)
где data - это строка с некоторым содержимым объекта (данными). 
При этом каждый объект класса StackObj должен иметь следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры
В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, 
например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, 
то должно генерироваться исключение командой:

raise IndexError('неверный индекс')
Пример использования классов Stack и StackObj (эти строчки в программе не писать):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""

#
# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#         self.__prev = None
#         self.__indx = None
#
#     @property
#     def indx(self):
#         return self.__indx
#
#     @indx.setter
#     def indx(self, indx):
#         self.__indx = indx
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, obj):
#         self.__next = obj
#
#     @property
#     def prev(self):
#         return self.__prev
#
#     @prev.setter
#     def prev(self, obj):
#         self.__prev = obj
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.__end = None
#
#     def push(self, obj):
#         self.__adder(obj)
#         h = self.top
#         count = 0
#         while h:
#             if h.indx is None:
#                 h.indx = count
#             count += 1
#             h = h.next
#
#     def get(self):
#         h = self.top
#         lst = []
#         while h:
#             lst.append(h.data)
#             h = h.next
#         return lst
#
#     def pop(self):
#         temp = self.top
#         if temp is None:
#             return
#         while temp and temp.next != self.__end:
#             temp = temp.next
#         if temp:
#             temp.next = None
#         end = self.__end
#         self.__end = temp
#         if self.__end is None:
#             self.top = None
#
#         return end
#
#     def __adder(self, obj):
#         """Доп метод который добавляет в конец списка"""
#         if not self.__check_node(obj):
#             return
#         if self.__end:
#             self.__end.next = obj
#         obj.prev = self.__end
#         self.__end = obj
#         if self.top is None:
#             self.top = obj
#
#
#     def __check_node(self, node):
#         """ Функция не допускающая рекурсию при добавлении одинаковых обьектов,
#             Спасибо (Дернов Иван)"""
#         if not self.top:                #
#             return True
#         f = self.top
#         while f:
#             if f == node:
#                 return False
#             f = f.next
#         return True
#
#     def __getitem__(self, item):
#         """Все так же как в get"""
#         h = self.top
#         lst = []
#         while h:
#             lst.append(h)
#             h = h.next
#         if not (-len(lst) <= item < len(lst)) or type(item) != int:
#             raise IndexError('неверный индекс')
#         return lst[item]
#
#     def __get_obj_key(self, key):
#         """Ищет нужный индекс в имеющемся списке"""
#         h = self.top
#         while h:
#             if h.indx == key:
#                 return h
#             h = h.next
#             if h is None:
#                 raise IndexError('неверный индекс')
#
#     def __setitem__(self, key, value: StackObj):
#         """Просто меняем у обьекта по индексу его значение на значение value.data"""
#         obj = self.__get_obj_key(key)
#         obj.data = value.data
#
#
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
# print(st[1].data) # new obj2
# res = st[3] # исключение IndexError

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/QtOqF78VlHM

Подвиг 7 (познание срезов). Объявите в программе класс с именем RadiusVector (радиус-вектор), 
объекты которого создаются командой:

v = RadiusVector(x1, x2,..., xN)
где x1, x2,..., xN - координаты радиус-вектора (числа: целые или вещественные).

В каждом объекте класса RadiusVector должен быть локальный атрибут:

coords - список из координат радиус-вектора.

Для доступа к отдельным координатам, реализовать следующий функционал:

coord = v[i] # получение значения i-й координаты (целое число, отсчет с нуля)
coords_1 = v[start:stop] # получение среза (набора) координат в виде кортежа
coords_2 = v[start:stop:step] # получение среза (набора) координат в виде кортежа
v[i] = value # изменение i-й координаты
v[start:stop] = [val_1, val_2, ...] # изменение сразу нескольких координат
v[start:stop:step] = [val_1, val_2, ...] # изменение сразу нескольких координат
Пример использования класса (эти строчки в программе не писать):

v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5"""

# class RadiusVector:
#     def __init__(self, *args):
#         self.coords = [i for i in args]
#
#     def __getitem__(self, item):
#         return tuple(self.coords[item]) if type(item) is slice else self.coords[item]
#
#     def __setitem__(self, key: slice, value):
#         self.coords[key] = value
#
#
# v = RadiusVector(1, 1, 1, 1)
# print(v[1]) # 1
# v[:] = 1, 2, 3, 4
#
# print(v[2]) # 3
# print(v[1:]) # (2, 3, 4)
# v[0] = 10.5
# print(v[:])


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Uk-cA4xC9fc

Подвиг 8. Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики". 
Для этого требуется объявить класс TicTacToe (крестики-нолики), объекты которого создаются командой:

game = TicTacToe()
Каждый объект game должен иметь публичный атрибут:

pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.

Каждая клетка игрового поля представляется объектом класса Cell и создается командой:

cell = Cell()
Объекты класса Cell должны иметь следующие публичные локальные атрибуты:

is_free - True, если клетка свободна; False в противном случае;
value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

Также с каждым объектом класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка свободна (cell.is_free=True) и False в противном случае.

Класс TicTacToe должен иметь следующий метод:

clear() - очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое состояние);

А объекты этого класса должны иметь следующую функциональность (обращение по индексам):

game[0, 0] = 1 # установка нового значения, если поле закрыто
res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)
Если указываются некорректные индексы, то должно генерироваться исключение командой:

raise IndexError('неверный индекс клетки')
Если идет попытка присвоить новое значение в открытую клетку поля, то генерировать исключение:

raise ValueError('клетка уже занята')
Также должны быть реализованы следующие срезы при обращении к клеткам игрового поля:

slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx
Пример использования классов (эти строчки в программе не писать):

game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. При передаче среза в магических методах __setitem__() и __getitem__() 
параметр индекса становится объектом класса slice. Его можно указывать непосредственно 
в квадратных скобках упорядоченных коллекций (списков, кортежей и т.п.)."""

# class Cell:
#     def __init__(self):
#         self.is_free = False
#         self.value = 0
#
#     def __bool__(self):
#         return self.is_free
#
#
#
# class TicTacToe:
#     def __init__(self):
#         self.pole = tuple(tuple(Cell() for i in range(3)) for j in range(3))
#     def clear(self):
#         for i in self.pole:
#             for j in i:
#                 j.is_free = False
#                 j.value = 0
#
#     def __check_indx(self, indx):
#         if type(indx) == slice:
#             return True
#         if not -2 <= indx <= 2:
#             raise IndexError('неверный индекс клетки')
#         return True
#
#     def __getitem__(self, item):
#         it_0 = item[0]
#         it_1 = item[1]
#         self.__check_indx(it_0)
#         self.__check_indx(it_1)
#         if type(it_0) == slice:
#             return tuple(i[it_1].value for i in self.pole[it_0])
#         if type(it_1) == slice:
#             return tuple(i.value for i in self.pole[it_1][it_0])
#         return self.pole[it_0][it_1].value
#
#
#     def __setitem__(self, key, value):
#         it_0 = key[0]
#         it_1 = key[1]
#         self.__check_indx(it_0)
#         self.__check_indx(it_1)
#         if self.pole[key[0]][key[1]].is_free is True:
#             raise ValueError('клетка уже занята')
#         self.pole[key[0]][key[1]].value = value

# game = TicTacToe()
# game.clear()
# game[0, 0] = 1
# game[1, 0] = 2
# # формируется поле:
# # 1 0 0
# # 2 0 0
# # 0 0 0
# # game[3, 2] = 2 # генерируется исключение IndexError
# if game[0, 0] == 0:
#     game[0, 0] = 2
# v1 = game[0, :]  # 1, 0, 0
# v2 = game[:, 0]  # 1, 2, 0

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/dFdXOJwMc0E

Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)
где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение). 
В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. 
Иначе, генерируется исключение:

raise ValueError('превышен суммарный вес предметов')
Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx
Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')
Пример использования классов (эти строчки в программе не писать):

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""

# class Thing:
#     def __init__(self, name: str, weight: (int, float)):
#         self.name, self.weight = name, weight
#
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.bag_list = []
#         self.weight = 0
#
#     def add_thing(self, thing: Thing):
#         if self.__weight_check(thing):
#             self.bag_list.append(thing)
#             self.weight += thing.weight
#
#     def __index_check(self, index):
#         if not (-len(self.bag_list) <= index <= len(self.bag_list)):
#             raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.__index_check(item)
#         return self.bag_list[item]
#
#     def __weight_check(self, obj, old_obj=None):
#         if old_obj is None:
#             if obj.weight + self.weight > self.max_weight:
#                 raise ValueError('превышен суммарный вес предметов')
#             return True
#         else:
#             if (self.weight - old_obj.weight) + obj.weight > self.max_weight:
#                 raise ValueError('превышен суммарный вес предметов')
#             return True
#
#     def __setitem__(self, key, value):
#         self.__index_check(key)
#         t = self.bag_list[key]
#         if self.__weight_check(value, t):
#             self.bag_list[key] = value
#             self.weight += value.weight
#
#     def __delitem__(self, key):
#         self.__index_check(key)
#         del self.bag_list[key]
#
# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError

"""Подвиг 10. Вам необходимо описывать в программе очень большие и разреженные таблицы данных 
(с большим числом пропусков). Для этого предлагается объявить класс SparseTable, 
объекты которого создаются командой:

st = SparseTable()
В каждом объекте этого класса должны создаваться локальные публичные атрибуты:

rows - общее число строк таблицы (начальное значение 0);
cols - общее число столбцов таблицы (начальное значение 0).

В самом классе SparseTable должны быть объявлены методы:

add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам row, col 
(целые неотрицательные числа);
remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами (row, col).

При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, 
cols объекта класса SparseTable. Если происходит попытка удалить несуществующую ячейку, 
то должно генерироваться исключение:

raise IndexError('ячейка с указанными индексами не существует')
Ячейки таблицы представляют собой объекты класса Cell, которые создаются командой:

data = Cell(value)
где value - данные ячейки (любой тип).

Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j, 
а значениями - объекты класса Cell.

Также с объектами класса SparseTable должны выполняться команды:

res = st[i, j] # получение данных из таблицы по индексам (i, j)
st[i, j] = value # запись новых данных по индексам (i, j)
Чтение данных возможно только для существующих ячеек. Если ячейки с указанными индексами нет, 
то генерировать исключение командой:

raise ValueError('данные по указанным индексам отсутствуют')
При записи новых значений их следует менять в существующей ячейке или добавлять новую, 
если ячейка с индексами (i, j) отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols).

Пример использования классов (эти строчки в программе не писать):

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""

class Cell:
    def __init__(self, value):
        self.value = value

class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.__dic = {}


    def __r_c_recount(self):
        """Method recount and adding +1 to rows and cols"""
        items = tuple(self.__dic.keys())
        r, c = [], []
        for i, j in items:
            r.append(i)
            c.append(j)
        r, c = max(r), max(c)
        self.rows, self.cols = r, c
        self.rows += 1
        self.cols += 1

    def __check_indx(self, obj):
        """Method cheking indexes (keys) are they exist in dict or not"""
        if obj not in self.__dic.keys():
            raise IndexError('ячейка с указанными индексами не существует')

    def add_data(self, row, col, data):
        self.__dic[(row, col)] = data
        self.__r_c_recount()

    def remove_data(self, row, col):
        self.__check_indx((row, col))
        self.__dic.pop((row, col))
        self.__r_c_recount()

    def __getitem__(self, item):
        if item not in self.__dic.keys():
            raise ValueError('данные по указанным индексам отсутствуют')
        s = self.__dic.get(item)
        if type(s) == Cell:
            return self.__dic.get(item).value
        return self.__dic.get(item)

    def __setitem__(self, key, value):
        if type(value) == Cell:
            self.__dic[key] = value
            self.__r_c_recount()
        else:
            self.__dic[key] = Cell(value)
            self.__r_c_recount()

    def __delitem__(self, key):
        self.__check_indx(key)
        self.__dic.pop(key)
        self.__r_c_recount()

# st = SparseTable()
# st.add_data(2, 5, Cell(25))
# st.add_data(1, 1, Cell(11))
# st.add_data(3, 4, Cell(23))
# st.remove_data(1, 1)
# print(st.rows, st.cols)
