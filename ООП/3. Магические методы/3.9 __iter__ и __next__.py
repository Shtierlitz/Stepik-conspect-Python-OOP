# Магические методы __iter__ и __next__
# по сути это функция range только в классах для перебора содержимого
# __next__ позволяет использовать экземпляр класса как итерируемый обьект и помещать его в ф next()
# но сам по себе экземпляр не становится итерационным элементом
# для этого нужен метод __iter__

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


# fr = FRange(0, 2& 0|5)
# # print(next(fr))
# # print(next(fr))
# # print(next(fr))
# # print(next(fr))
# for x in fr:
#     print(x)


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


#
# fr = FRange2D(0, 2, 0.5, 4)
# for row in fr:
#     for x in row:
#         print(x, end=' ')
#     print()

# https://www.youtube.com/watch?v=SDJ-Vmf_pxk&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=20


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/-ZvYUtWMUFw

Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)
где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); 
salary - зарплата (число: целое или вещественное); 
year_job - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: 
fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута 
(порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. 
Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
Пример использования класса (эти строчки в программе не писать):

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно."""

# class Person:
#     def __init__(self, fio: str, job: str, old: int, salary: (int, float), year_job: int):
#         self.fio, self.job, self.old, self.salary, self.year_job = fio, job, old, salary, year_job
#         self.__lst = [self.fio, self.job, self.old, self.salary, self.year_job]
#
#     def __check_indx(self, indx):
#         if type(indx) != int or not 0 <= indx <=4:
#             raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.__check_indx(item)
#         return self.__lst[item]
#
#     def __setitem__(self, key, value):
#         self.__check_indx(key)
#         self.__lst[key] = value
#
#     def __iter__(self):
#         self.value = -1
#         return self
#
#     def __next__(self):
#         while self.value < len(self.__lst) -1:
#             self.value += 1
#             return self.__lst[self.value]
#         else:
#             raise StopIteration
#
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError

"""Подвиг 6. Вам дают задание разработать итератор для последовательного 
перебора элементов вложенных (двумерных) списков следующей структуры:

lst = [[x00],
       [x10, x11],
       [x20, x21, x22],
       [x30, x31, x32, x33],
       ...
      ]
Для этого необходимо в программе объявить класс с именем TriangleListIterator,
 объекты которого создаются командой:

it = TriangleListIterator(lst)
где lst - ссылка на перебираемый список.

Затем, с объектами класса TriangleListIterator должны быть доступны следующие операции:

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
Итератор должен перебирать элементы списка по указанной треугольной форме. 
Даже если итератору на вход будет передан прямоугольная таблица (вложенный список), 
то ее перебор все равно должен осуществляться по треугольнику. 
Если же это невозможно (из-за структуры списка), 
то естественным образом должна возникать ошибка 
IndexError: index out of range (выход индекса за допустимый диапазон).

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно."""

# lst = [['x00', 'x01', 'x02'],
#        ['x10', 'x11'],
#        ['x20', 'x21', 'x22', 'x23', 'x24'],
#        ['x30', 'x31', 'x32', 'x33']]
#
# class TriangleListIterator:
#     def __init__(self, lst: list):
#         self.lst = lst
#
#     def __iter__(self):
#         for i in range(len(self.lst)):
#             for j in self.lst[i]:
#                 yield j
#
# it = TriangleListIterator(lst)
# for x in it:
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)
# print(next(it_iter))

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kxCAnaAqdOk

Подвиг 7. Теперь, вам необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка. Список представляет собой двумерную таблицу из данных:

lst = [[x11, x12, ..., x1N],
       [x21, x22, ..., x2N],
       ...
       [xM1, xM2, ..., xMN]
      ]
Для этого в программе необходимо объявить класс с именем IterColumn, объекты которого создаются командой:

it = IterColumn(lst, column)
где lst - ссылка на двумерный список; column - индекс перебираемого столбца (отсчитывается от 0).

Затем, с объектами класса IterColumn должны быть доступны следующие операции:

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
P.S. В программе нужно объявить только класс итератора. Выводить на экран ничего не нужно."""

# lst = [['x00', 'x01', 'x02'],
#        ['x10', 'x11'],
#        ['x20', 'x21', 'x22', 'x23', 'x24'],
#        ['x30', 'x31', 'x32', 'x33']]

# class IterColumn:
#     def __init__(self, lst: list, column: int):
#         self.lst = lst
#         self.column = column
#
#     def __iter__(self):
#         for i in range(len(self.lst)):
#             yield lst[i][self.column]
#
# it = IterColumn(lst, 1)
# for x in it:
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/WrZ1TMwuvis

Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:



Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
При работе с индексами (indx), нужно проверять их корректность. 
Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""

# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#             instance.__dict__[self.name] = value
#
# class StackObj:
#
#     data = Descriptor()
#     next = Descriptor()
#     prev = Descriptor()
#     indx = Descriptor()
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#         self.indx = None
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.tail = None
#
#     def get(self):
#         h = self.top
#         lst = []
#         while h:
#             lst.append(h.data)
#             h = h.next
#         return lst
#
#     def __adder(self, obj):
#         if not self.__check_node(obj):
#             return
#         if self.tail:
#             self.tail.next = obj
#         obj.prev = self.tail
#         self.tail = obj
#         if self.top is None:
#             self.top = obj
#
#     def __check_node(self, node):       # Функция не допускающая рекурсию при добавлении одинаковых обьектов
#         if not self.top:                # Спасибо (Дернов Иван)
#             return True
#         f = self.top
#         while f:
#             if f == node:
#                 return False
#             f = f.next
#         return True
#
#     def push_back(self, obj):
#         self.__adder(obj)
#         self.__indx_recounter()
#
#     def push_front(self, obj):
#         if self.top:
#             obj.next = self.top
#             self.top = obj
#             self.__indx_recounter()
#         if self.top is None:
#             self.__adder(obj)
#             self.__indx_recounter()
#
#     def __indx_recounter(self):
#         """Доп метод для перерасчета индексов"""
#         h = self.top
#         count = 0
#         while h:
#             if h.indx is None:
#                 h.indx = count
#             count += 1
#             h = h.next
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
#         return lst[item].data
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
#     def __setitem__(self, key, value):
#         """Просто меняем у обьекта по индексу его значение на значение value или value.data"""
#         obj = self.__get_obj_key(key)
#         if type(value) == StackObj:
#             obj.data = value.data
#         else:
#             obj.data = value
#
#     def __len__(self):
#         lst = self.get()
#         return len(lst)
#
#     def __iter__(self):
#         h = self.top
#         lst = []
#         while h:
#             lst.append(h)
#             h = h.next
#         for i in lst:
#             yield i


# st = Stack()
# st.push_front(StackObj("front"))
# st.push_back(StackObj("obj1"))
# st.push_back(StackObj("obj2"))
# st.push_back(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# data = st[2]
# st[0] = "0"
# print(st.get())
# print(st[0])

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kmmvxZWxaAY

Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:



Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию,
 float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный 
атрибут __data с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

При попытке записать данные другого типа (не совпадающего с 
атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')
С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
При работе с индексами row, col, необходимо проверять их корректность. 
Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


# class Cell:
#     def __init__(self, data=0):
#         self.__data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, val):
#         self.__data = val
#
#
# class TableValues:
#     def __init__(self, rows: int, cols: int, type_data=0):
#         self.__indx_chech_init(rows)
#         self.__indx_chech_init(cols)
#         self.rows = rows
#         self.cols = cols
#         self.type_data = type_data
#         self.__lst = [[Cell(self.type_data) for _ in range(self.cols)] for _ in range(self.rows)]
#
#     def __type_data_check(self, data):
#         if type(data) != type(self.type_data):
#             raise TypeError('неверный тип присваиваемых данных')
#
#     def __indx_chech_init(self, indx):
#         if type(indx) != int:
#             raise IndexError('неверный индекс')
#
#     def __indx_check(self, indx):
#         if type(indx[0]) != int or type(indx[1]) != int:
#             raise IndexError('неверный индекс')
#         if not (-len(self.__lst[indx[0]])) <= indx[0] <= len(self.__lst[indx[0]]):
#             raise IndexError('неверный индекс')
#         if not (-len(self.__lst[indx[1]])) <= indx[1] <= len(self.__lst[indx[1]]):
#             raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.__indx_check(item)
#         return self.__lst[item[0]][item[1]].data
#
#     def __setitem__(self, key, value):
#         self.__indx_check(key)
#         self.__type_data_check(value)
#         self.__lst[key[0]][key[1]].data = value
#
#     def __iter__(self):
#         for i in self.__lst:
#             yield (x.data for x in i)
#
#
# #
# table = TableValues(3, 5, "rhby;")
# table[0, 0] = "value"  # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
# value = table[0, 0]  # считывание значения из ячейки с индексами row, col
#
# for row in table:  # перебор по строкам
#     for value in row:  # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/yX9qxE8X1OA

Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. 
Объекты этого класса должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы; fill_value - 
заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное). 
Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
Также объекты можно создавать командой:

m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). 
Если список list2D не прямоугольный, или хотя бы один из его элементов не число, 
то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')
Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')
Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), 
то генерировать исключение:

raise IndexError('недопустимые значения индексов')
Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
Во всех этих операция должна формироваться новая матрица с соответствующими значениями. 
Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')
Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно."""


class Matrix:
    def __init__(self, rows_or_lst, cols=0, fill_value=0):
        if type(rows_or_lst) != list:
            self.__indx_chech_init(rows_or_lst)
            self.__indx_chech_init(cols)
            self.__val_check_init(fill_value)
            self.rows = rows_or_lst
            self.cols = cols
            self.fill_value = fill_value
            self.lst = [[fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.__list_check(rows_or_lst)
            self.rows = len(rows_or_lst)
            self.cols = len(rows_or_lst[0])
            self.lst = rows_or_lst
            self.fill_value = rows_or_lst[0][0]

    def __indx_chech_init(self, indx):
        if type(indx) != int:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __val_check_init(self, val):
        if type(val) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __list_check(self, lst):
        cols = 0
        for i in lst:
            for j in i:
                if type(j) not in (int, float):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
                cols += 1
            row = len(i)
        rows = (cols // row) * row
        if rows != cols:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __list_compare(self, lst1, lst2):
        cols1 = 0
        for i in lst1:
            cols1 += 1
            row1 = len(i)
        rows1 = (cols1 // row1) * row1

        cols2 = 0
        for i in lst2:
            cols2 += 1
            row2 = len(i)
        rows2 = (cols2 // row2) * row2
        if cols1 != cols2 or rows1 != rows2:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __indx_check(self, indx):
        if type(indx[0]) != int or type(indx[1]) != int:
            raise IndexError('недопустимые значения индексов')
        if not 0 <= indx[0] < self.rows:
            raise IndexError('недопустимые значения индексов')
        if not 0 <= indx[1] < self.cols:
            raise IndexError('недопустимые значения индексов')

    def __type_data_check(self, data):
        if type(data) != type(self.fill_value):
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, item):
        self.__indx_check(item)
        return self.lst[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.__indx_check(key)
        if not type(value) in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.lst[key[0]][key[1]] = value

    def __add__(self, other):
        if isinstance(other, Matrix):
            m2 = other.lst
            self.__list_check(m2)
            self.__list_compare(self.lst, m2)
            return Matrix([[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__type_data_check(other)
            return Matrix([[self[i, j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            m2 = other.lst
            self.__list_check(m2)
            self.__list_compare(self.lst, m2)
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__type_data_check(other)
            return Matrix([[self[i, j] - other for j in range(self.cols)] for i in range(self.rows)])

    def __rsub__(self, other):
        return self.__sub__(other)

lst1 = [[1, 1],[1, 1]]
lst2 = [[1, 1],[1, 1]]
res = [[lst1[i][j] - lst2[i][j] for j in range(len(lst1))] for i in range(len(lst2))]
print(res)



