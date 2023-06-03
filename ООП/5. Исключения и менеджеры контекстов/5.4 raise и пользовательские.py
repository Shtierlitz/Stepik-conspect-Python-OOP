"""Инструкция raise и пользовательские исключения
Смотри видео когда понадобится. Тут сложно и запутанно"""
# class ExceptionPrint(Exception):
#     """Общий класс исключений принтера"""
#
#
# class ExceptionPrintSendData(Exception):
#     '''Класс исключения при отправки данных принтеру'''
#     def __init__(self, *args):
#         self.message = args[0] if args else None
#
#     def __str__(self):
#         return f"Ошибка: {self.message}"
#
#
# class PrintData:
#     def print(self, data):
#         self.send_data(data)
#         print(f"печать: {str(data)}")
#
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise ExceptionPrintSendData("принтер не отвечает")
#
#     def send_to_print(self, data):
#         return False


# p = PrintData()
# # p.print("123")
# try:
#     p.print("123")
# except ExceptionPrintSendData:
#     print("Принтер не отвечает")
# except ExceptionPrint:
#     print("Общая ошибка печати")

# https://www.youtube.com/watch?v=XR-16WMXZOY&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=32

# class StringException(Exception):
#     """Общее исключение в строке"""
#
# class NegativeLengthString(StringException):
#     """ошибка, если длина отрицательная;"""
#
# class ExceedLengthString(StringException):
#     """ошибка, если длина превышает заданное значение;"""
#
#
# try:
#     raise ExceedLengthString
# except NegativeLengthString:
#     print("NegativeLengthString")
# except ExceedLengthString:
#     print("ExceedLengthString")
# except StringException:
#     print("StringException")


"""5.4 Инструкция raise и пользовательские исключения
5 из 8 шагов пройдено
5 из 15 баллов  получено
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6wnJd7OrNaI

Подвиг 5. Объявите в программе класс-исключение с именем PrimaryKeyError, 
унаследованным от базового класса Exception. Объекты класса PrimaryKeyError должны создаваться командами:

e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
В первом варианте команды должно формироваться сообщение об ошибке 
"Первичный ключ должен быть целым неотрицательным числом". При втором варианте:

"Значение первичного ключа id = <id> недопустимо"

И при третьем:

"Значение первичного ключа pk = <pk> недопустимо"

Эти сообщения должны формироваться при отображении объектов класса PrimaryKeyError, например:

print(e2) # Значение первичного ключа id = abc недопустимо
Затем, сгенерируйте это исключение с аргументом id = -10.5, обработайте его и отобразите 
на экране объект исключения.

Sample Input:


Sample Output:

Значение первичного ключа id = -10.5 недопустимо"""


# class PrimaryKeyError(Exception):
#     def __init__(self, id=None, pk=None):
#         self.id = id
#         self.pk = pk
#
#     def __str__(self):
#         if self.id is not None:
#             return f"Значение первичного ключа id = {self.id} недопустимо"
#         if self.pk is not None:
#             return f"Значение первичного ключа pk = {self.pk} недопустимо"
#         return f"Первичный ключ должен быть целым неотрицательным числом"
#
# e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
# e2 = PrimaryKeyError(id='-10.5')  # Значение первичного ключа id = abc недопустимо
# e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
# print(e2)


"""Подвиг 6. Объявите класс DateString для представления дат, объекты которого создаются командой:

date = DateString(date_string)
где date_string - строка с датой в формате:

"DD.MM.YYYY"

здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12); YYYY - 
год (целое число от 1 до 3000).
Например:

date = DateString("26.05.2022")
или

date = DateString("26.5.2022") # незначащий ноль может отсутствовать
Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с 
помощью собственного класса:

DateError - класс-исключения, унаследованный от класса Exception.

В самом классе DateString переопределить магический метод __str__() для формирования строки даты в формате:

"DD.MM.YYYY"

(здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022" должна формироваться строка 
"26.05.2022").

Далее, в программе выполняется считывание строки из входного потока командой:

date_string = input()
Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:

print(date) # date - объект класса DateString
Если же произошло исключение, то вывести сообщение (без кавычек):

"Неверный формат даты"

Sample Input:

1.2.1812
Sample Output:

01.02.1812"""

# class DateError(Exception):
#     """Неверный формат даты"""
#
# class DateString:
#     def __init__(self, date_string: str):
#         try:
#             self.date = int(date_string[:date_string.find(".")])
#             self.month = int(date_string[date_string.find(".")+1:date_string.rfind(".")])
#             self.year = int(date_string[date_string.rfind(".")+1:])
#         except:
#             raise DateError
#         if not 1 <= self.date <= 31 or not 1 <= self.month <= 12 or not 1 <= self.year <= 3000:
#             raise DateError
#
#
#     def __str__(self):
#         return f"{self.date:02}.{self.month:02}.{self.year:04}"
#
# date_string = input()
#
# try:
#     date = DateString(date_string)
#     print(date)
# except DateError:
#     print("Неверный формат даты")



"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wLaOyNN8x7E

Значимый подвиг 7. Вам поручается разработать класс TupleData, 
элементами которого могут являются только объекты классов: CellInteger, CellFloat и CellString.



Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:

cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)
где min_value, max_value - минимальное и максимальное допустимое значение в ячейке; min_length, max_length - 
минимальная и максимальная допустимая длина строки в ячейке.

В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value, 
_max_value или _min_length, _max_length и соответствующими значениями.

Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:

value - для записи и считывания значения в ячейке (изначально возвращает значение None).

Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или 
[min_length; max_length], то генерируется исключения командами:

raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
Все три класса исключений должны быть унаследованы от одного общего класса:

CellException

Далее, объявите класс TupleData, объекты которого создаются командой:

ld = TupleData(cell_1, ..., cell_N)
где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:

value = ld[index] # считывание значения из ячейке с индексом index
ld[index] = value # запись нового значения в ячейку с индексом index
Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. 
Если значение index выходит за диапазон [0; число ячеек-1], то генерировать исключение IndexError.

Также с объектами класса TupleData должны выполняться следующие функции и операторы:

res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)
Все эти классы в программе можно использовать следующим образом:

ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно."""


class CellException(Exception):
    """Общее исключение"""


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value, self._max_value = min_value, max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, item):
        if not self._min_value <= item <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self.__value = item


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value, self._max_value = min_value, max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, item):
        if not self._min_value <= item <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        self.__value = item


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length, self._max_length = min_length, max_length
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, item):
        if not self._min_length <= len(item) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self.__value = item


class TupleData:
    def __init__(self, *args):
        self.cells = [i for i in args]

    def __getitem__(self, item: int):
        if type(item) != int or not 0 <= item <= len(self.cells)-1:
            raise IndexError
        return self.cells[item].value

    def __setitem__(self, key, value):
        if type(key) != int or not 0 <= key <= len(self.cells)-1:
            raise IndexError
        self.cells[key].value = value

    def __len__(self):
        lst = [i.value for i in self.cells]
        return len(lst)


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))


try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")