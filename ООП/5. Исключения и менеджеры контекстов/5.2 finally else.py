"""Обработка исключений. Блоки finally и else"""

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:  # Вывод стандартного сообщения об ошибке через переменную
#     print(z)
# except ValueError as z:
#     print(z)
# else:
#     print("Не произошло исключений")
# finally:
#     print("Блок finally выполняется всегда")
# from pip._internal import self_outdated_check
#
# try:
#     f = open("myfile.txt")
#     # f.write("Hello")
# except FileNotFoundError as z:
#     print(z)
# except:
#     print("Другая ошибка")
# finally:
#     if f:
#         f.close()
#         print("Файл закрыт")
#
#
# try:  # В этом случае уже не нужен блок finally
#     with open("myfile.txt") as f:  # так как менеджер контекста with автоматически его закроет
#         f.write("Hello")
# except FileNotFoundError as z:
#     print(z)
# except:
#     print("Другая ошибка")
#
# # исключения в функциях
# def get_values():
#     try:
#         x, y = map(int, input().split())
#         return x, y
#     except ValueError as z:
#         print(z)
#         return 0, 0                     # Важно помнить что return отрабатывает в последнюю очередь
#     finally:
#         print("finally выполняется до return")
#
# x, y = get_values()
# print(x, y)
#
# # Вложенные исключения
# try:
#     x, y = map(int, input().split())
#     try:
#         rex = x / y
#     except ZeroDivisionError as z:
#         print(z)
# except ValueError as z:
#     print(z)


# https://www.youtube.com/watch?v=3DmzotEptvM&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=30

"""Подвиг 4. В программе вводятся два значения в одну строчку через пробел. 
Значениями могут быть числа, слова, булевы величины (True/False). 
Необходимо прочитать эти значения из входного потока. 
Если оба значения являются числами, то вычислить их сумму, 
иначе соединить их в одну строку с помощью оператора + (конкатенации строк). 
Результат вывести на экран (в блоке finally).

P.S. Реализовать программу с использованием блоков try/except/finally.

Sample Input:

8 11
Sample Output:

19"""

# a, b = input().split()
#
# try:
#     a, b = int(a), int(b)
# except:
#     try:
#         a, b = float(a), float(b)
#     except:
#         pass
# finally:
#     print(a + b)

"""Подвиг 5. Объявите в программе класс Point, объекты которого должны создаваться командами:

pt = Point()
pt = Point(x, y)
где x, y - произвольные числа (координаты точки). 

В каждом объекте класса Point должны формироваться локальные атрибуты _x, _y с соответствующими значениями. 
Если аргументы не указываются (первая команда), то _x = 0, _y = 0.

Далее, в программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, 
булевы величины (True/False). Необходимо прочитать эти значения из входного потока. 
Если оба значения являются числами, то формировать объект pt командой:

pt = Point(x, y)
Если хотя бы одно из значений не числовое, то формировать объект pt командой:

pt = Point()
Реализовать этот функционал с помощью блоков try/except. А в блоке finally вывести на экран сообщение в 
формате (без кавычек):

"Point: x = <значение x>, y = <значение y>"

Sample Input:

10 20
Sample Output:

Point: x = 10, y = 20"""

# class Point:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#
# a, b = input().split()
# try:
#     pt = Point(int(a), int(b))
# except:
#     try:
#         pt = Point(float(a), float(b))
#     except:
#         pt = Point()
# finally:
#     print(f"Point: x = {pt._x}, y = {pt._y}")

"""Подвиг 7. В практике программирования блок else используют как элемент отладки программы: 
в него прописывают текст программы, в котором заведомо не произойдет исключений, отлавливаемых в блоке try. 
Выполним на практике такой пример.

Вам необходимо объявить функцию с сигнатурой:

def get_loss(w1, w2, w3, w4): ...

где w1, w2, w3, w4 - любые числа. Функция должна возвращать значение, вычисленное по формуле:

y = 10 * w1 // w2 - 5 * w2 * w3 + w4

Здесь фрагмент вычисления w1 // w2 содержит потенциальную ошибку деления на ноль, поэтому его следует делать в 
блоке try. А в блоке else продолжить вычисления, где не используются операции деления.

Если происходит деление на ноль, то функция должна возвращать строку:

"деление на ноль"

P.S. В программе нужно объявить только функцию. Вызывать ее и выводить на экран ничего не нужно."""


# def get_loss(w1, w2, w3, w4):
#     try:
#         y = 10 * w1 // w2 - 5 * w2 * w3 + w4
#     except ZeroDivisionError:
#         return "деление на ноль"
#     else:
#         return y
#
# print(get_loss(2, 0, 3, 4))

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/o66Is1ab4ho

Подвиг 8. Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:

r = Rect(x, y, width, height)
где x, y - координаты верхнего левого угла (любые числа); width, height - ширина и высота прямоугольника 
(положительные числа).

В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и 
соответствующими значениями. Если переданные аргументы x, y (не числа) и width, height не положительные числа, 
то генерировать исключение командой:

raise ValueError('некорректные координаты и параметры прямоугольника')
В классе Rect реализовать метод:

def is_collision(self, rect): ...

который проверяет пересечение текущего прямоугольника с другим (с объектом rect). 
Если прямоугольники пересекаются, то должно генерироваться исключение командой:

raise TypeError('прямоугольники пересекаются')
Сформировать в программе несколько объектов класса Rect со следующими значениями:

0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1

Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision, 
в котором должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.

P.S. В программе требуется объявить только класс и списки. На экран выводить ничего не нужно.

Подсказка. Для определения пересечения двух прямоугольников, у которых стороны параллельны осям координат 
(как в этом подвиге) достаточно проверить, что верхняя грань первого прямоугольника находится ниже нижней 
грани второго, или нижняя грань первого прямоугольника выше верхней грани второго. И то же самое для 
вертикальных граней."""

class Rect:
    def __init__(self, x, y, width, height):
        self._x, self._y, self._width, self._height = x, y, width, height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ("_width", "_height") and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise ValueError("аргументом метода is_collision() должен быть объект класса Rect")
        if not (self._x + self._width < rect._x or rect._x + rect._width < self._x or
                self._y + self._height < rect._y or rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))
                     if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]

