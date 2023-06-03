"""Введение в обработку исключений. Блоки try / except
Иерархия классов исключений в фото в папке.
чем выше уровени класса исключения тем больше он захватит дочерних классов исключений
главное правило сначала писать спец классы, а за ними уже общие."""

# print("Я к вам пишу - чего же более?")
# print("Что я могу еще сказать?")
# print("Теперь, я знаю, в вашей воле")
# print(a)
# print("Меня презреньем наказать.")
# print("Но вы, к моей несчастной доле")
# print("Хоть каплю жалости храня")
# print("Вы не оставите меня")

# try:
#     f = open('mylife2.txt')
# except FileNotFoundError:
#     print("Невозможно открыть файл")
#
# print("Штатное завершение")
#
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except (ValueError, ZeroDivisionError):
#     print('Неправильное значение')
# except ZeroDivisionError:
#     print("Деление на 0")
#
# print("Штатное завершение 2")
#
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ArithmeticError:
#     print('Неправильное значение')
#
# print("Штатное завершение 3")
#
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except Exception:
#     print('Неправильное значение')
#
# print("Штатное завершение 4")
#
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except:
#     print('Ошибка')                     # исключает вообще все ошибки
#
# print("Штатное завершение 5")

# https://www.youtube.com/watch?v=MFIlltaeIgs&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=29



"""
Подвиг 5. В программе объявлен класс Point:

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
И создается объект этого класса:

pt = Point(1, 2)
Далее, вам нужно обратиться к атрибуту z объекта pt и, если такой атрибут существует,
то вывести его значение на экран. Иначе вывести строку (без кавычек):

"Атрибут с именем z не существует"

Реализовать проверку следует с помощью блоков try/except.

Подсказка: при обращении к несуществующему атрибуту генерируется исключение AttributeError."""


# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#
# pt = Point(1, 2)
#
# try:
#     print(pt.z)
# except AttributeError:
#     print("Атрибут с именем z не существует")


"""Подвиг 7. В программе вводятся в одну строчку через пробел некоторые данные, например:

"1 -5.6 2 abc 0 False 22.5 hello world"
Эти данные разбиваются по пробелу и представляются в виде списка строк:

lst_in = input().split()
Ваша задача посчитать сумму всех целочисленных значений, присутствующих в списке lst_in.
 Результат (сумму) вывести на экран.

Подсказка: отбор только целочисленных значений можно выполнить с помощь функции filter() с 
последующим их преобразованием в целые числа с помощью функции map() и, затем, 
вычислением их суммы с помощью функции sum(). Для отбора целочисленных значений рекомендуется 
объявить вспомогательную функцию, которая бы возвращала True для строк, 
в которых присутствует целое число и False - для всех остальных строк.

Sample Input:

8 11 abcd -7.5 2.0 -5
Sample Output:

14"""

# def check_int(x):
#     try:
#         int(x)
#         return True
#     except ValueError:
#         return False
#
# lst_in = ['8', '11', 'abcd', '-7.5', '2.0', '-5']
#
#
# print(sum(list(map(int, list(filter(lambda x: check_int(x), lst_in))))))

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/zQDvmHlS6wg

Подвиг 8. В программе вводятся в одну строчку через пробел некоторые данные, например:

"1 -5.6 True abc 0 23.56 hello"
Эти данные разбиваются по пробелу и представляются в виде списка строк:

lst_in = input().split()
Ваша задача сформировать новый список с именем lst_out, в котором строки с целыми числами будут 
представлены как целые числа (тип int), строки с вещественными числами, как вещественные (тип float), 
а остальные данные - без изменений.

Например:

lst_out = [1, -5.6, 'True', 'abc', 0, 23.56, 'hello']  # после обработки введенной строки 
"1 -5.6 True abc 0 23.56 hello"
Реализовать эту задачу следует с помощью функции map() и объявления вспомогательной функции с
 механизмом обработки исключений для непосредственного преобразования данных в целые или вещественные числа.

P.S. В программе нужно только сформировать список lst_out. На экран ничего выводить не нужно.

Sample Input:

hello 1 world -2 4.5 True"""

# lst_in = ['hello', '1', 'world', '-2', '4.5', 'True']
#
# def check_type(x):
#     if type(x) == bool:
#         return str(x)
#     try:
#         return int(x)
#     except ValueError:
#         try:
#             return float(x)
#         except ValueError:
#             return str(x)
#
# lst_out = list(map(lambda x: check_type(x), lst_in))
# print(lst_out)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/eKxzgkKD1fI

Подвиг 9. Объявите в программе класс Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (любые положительные числа). 
В каждом объекте класса Triangle должны формироваться локальные атрибуты _a, _b, _c с соответствующими значениями.

Если в качестве хотя бы одной величины a, b, c передается не числовое значение, или меньше либо равно нулю, 
то должно генерироваться исключение командой:

raise TypeError('стороны треугольника должны быть положительными числами')
Если из переданных значений a, b, c нельзя составить треугольник (условие: каждая сторона должна быть 
меньше суммы двух других), то генерировать исключение командой:

raise ValueError('из указанных длин сторон нельзя составить треугольник')
Затем, на основе следующего набора данных:

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
необходимо сформировать объекты класса Triangle, но только в том случае, если не возникло никаких исключений. 
Все созданные объекты представить в виде списка с именем lst_tr.

P.S. В программе нужно только сформировать список lst_tr. На экран ничего выводить не нужно."""


# class Triangle:
#     def __init__(self, a, b, c):
#         self.__check_digit(a)
#         self.__check_digit(b)
#         self.__check_digit(c)
#         self.__check_triangle(a, b, c)
#         self._a, self._b, self._c = a, b, c
#
#     @staticmethod
#     def __check_digit(x):
#         if type(x) not in (int, float) or not x > 0:
#             raise TypeError('стороны треугольника должны быть положительными числами')
#
#     @staticmethod
#     def __check_triangle(a, b, c):
#         if (a > b + c) or (b > a + c) or (c > a + b):
#             raise ValueError('из указанных длин сторон нельзя составить треугольник')
#
#
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
#
# def check_init(x):
#     try:
#         Triangle(*x)
#         return True
#     except:
#         return False
#
# lst_tr = [Triangle(*i) for i in list(filter(lambda x: check_init(x), input_data))]
# print(lst_tr)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0vmRMf5f4Iw

Подвиг 10. Объявите в программе класс FloatValidator, объекты которого создаются командой:

fv = FloatValidator(min_value, max_value)
где min_value, max_value - минимальное и максимальное допустимое значение (диапазон [min_value; max_value]).

Объекты этого класса предполагается использовать следующим образом:

fv(value)
где value - проверяемое значение. Если value не вещественное число или не принадлежит диапазону 
[min_value; max_value], то генерируется исключение командой:

raise ValueError('значение не прошло валидацию')
По аналогии, объявите класс IntegerValidator, объекты которого создаются командой:

iv = IntegerValidator(min_value, max_value)
и используются командой:

iv(value)
Здесь также генерируется исключение:

raise ValueError('значение не прошло валидацию')
если value не целое число или не принадлежит диапазону [min_value; max_value].

После этого объявите функцию с сигнатурой:

def is_valid(lst, validators): ...

где lst - список из данных; validators - список из объектов-валидаторов (объектов классов 
FloatValidator и IntegerValidator).

Эта функция должна отбирать из списка все значения, которые прошли хотя бы по одному валидатору. 
И возвращать новый список с элементами, прошедшими проверку.

Пример использования классов и функции (эти строчки в программе не писать):

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
P.S. В программе нужно только объявить классы и функцию. На экран ничего выводить не нужно."""


# class FloatValidator:
#     def __init__(self, min_value, max_value):
#         self.min_value, self.max_value = min_value, max_value
#
#     def __call__(self, val):
#         if type(val) != float or not self.min_value <= val <= self.max_value:
#             raise ValueError('значение не прошло валидацию')
#         return val
#
# class IntegerValidator:
#     def __init__(self, min_value, max_value):
#         self.min_value, self.max_value = min_value, max_value
#
#     def __call__(self, val):
#         if type(val) != int or not self.min_value <= val <= self.max_value:
#             raise ValueError('значение не прошло валидацию')
#         return val
#
#
# def is_valid(lst, validators):
#     lst_out = []
#     for i in lst:
#          for j in validators:
#              try:
#                  s = j(i)
#                  lst_out.append(s)
#              except:
#                  pass
#     return lst_out
#
# fv = FloatValidator(0, 10.5)
# iv = IntegerValidator(-10, 20)
# print(is_valid([1, 4.5, 10, 0.5], validators=[fv, iv]))   # [1, 4.5])