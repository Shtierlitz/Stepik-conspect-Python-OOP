"""Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/1dSxnEFfDu8

Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и решило дать вам испытание
для подтверждения уровня полученных навыков. Вам выпала великая честь создать полноценную программу
игры в "Крестики-нолики". И вот перед вами текст с заданием самого испытания.

Техническое задание
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом.
Объекты этого класса будут создаваться командой:

game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]),
то следует генерировать исключение командой:

raise IndexError('некорректно указанные индексы')
Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики,
в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в
противном случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно
было бы сыграть в "Крестики-нолики" между человеком и компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.

P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз."""

import random
class Cell:
    def __init__(self):
        self.value = 0  # value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        """True, если клетка свободна и False - в противном случае."""
        return True if self.value == 0 else False

class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))    # pole - двумерный кортеж, размером 3x3.
        self.__is_computer_win = False
        self.__is_human_win = False
        self.__is_draw = False

    @property
    def is_human_win(self):
        return self.is_human()

    @is_human_win.setter
    def is_human_win(self, some):
        self.__is_human_win = some

    @property
    def is_draw(self):
        return self.draw()

    @is_draw.setter
    def is_draw(self, some):
        self.__is_draw = some

    @property
    def is_computer_win(self):
        res = self.is_computer()
        return res

    @is_computer_win.setter
    def is_computer_win(self, some):
        self.__is_computer_win = some
        
    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))


    def show(self):
        for i in self.pole:
            for j in i:
                print(j.value, end=" ")
            print()
        print()

    def human_go(self):
        """Рекурсивный метод чтобы игрок не ставил отметки на уже занятые клетки"""
        try:
            a, b = tuple(map(int, input("Сделайте свой шаг. Введите 2 целых числа через пробел: ").split()))
            temp = list([i for i in j] for j in self.pole)
            if temp[a][b].value != TicTacToe.FREE_CELL:
                print("Нельзя поставить на уже отмеченную клетку")
                return self.human_go()
            else:
                temp[a][b].value = TicTacToe.HUMAN_X
            self.pole = tuple(tuple(i for i in j) for j in temp)
        except ValueError:
            print("Вводить нужно только целые числа")
            return self.human_go()

    def computer_go(self):
        """Рекурсивный метод чтобы компьютер не ставил отметки на уже занятые клетки"""
        a = random.randrange(0, 3)
        b = random.randrange(0, 3)
        temp = list([i for i in j] for j in self.pole)
        if temp[a][b].value != TicTacToe.FREE_CELL:
             return self.computer_go()
        temp[a][b].value = TicTacToe.COMPUTER_O
        self.pole = tuple(tuple(i for i in j) for j in temp)

    def __check_true(self, a, b, c, d, e, f, num):
        if self.pole[a][b].value == num and self.pole[c][d].value == num \
                and self.pole[e][f].value == num:
            return True
        return False

    def is_human(self):
        if self.__check_true(0, 0, 0, 1, 0, 2, TicTacToe.HUMAN_X):
            return True
        if self.__check_true(1, 0, 1, 1, 1, 2, TicTacToe.HUMAN_X):
            return True
        if self.__check_true(2, 0, 2, 1, 2, 2, TicTacToe.HUMAN_X):
            return True
        if self.__check_true(0, 0, 1, 0, 2, 0, TicTacToe.HUMAN_X):
            return True
        if self.__check_true(0, 1, 1, 1, 2, 1, TicTacToe.HUMAN_X):
            return True
        if self.__check_true(0, 2, 1, 2, 2, 2, TicTacToe.HUMAN_X):
            return True
        if self.__check_true(0, 0, 1, 1, 2, 2, TicTacToe.HUMAN_X):
            return True
        if self.__check_true(0, 2, 1, 1, 2, 0, TicTacToe.HUMAN_X):
            return True

        return False

    def is_computer(self):
        if self.__check_true(0, 0, 0, 1, 0, 2, TicTacToe.COMPUTER_O):
            return True
        if self.__check_true(1, 0, 1, 1, 1, 2, TicTacToe.COMPUTER_O):
            return True
        if self.__check_true(2, 0, 2, 1, 2, 2, TicTacToe.COMPUTER_O):
            return True
        if self.__check_true(0, 0, 1, 0, 2, 0, TicTacToe.COMPUTER_O):
            return True
        if self.__check_true(0, 1, 1, 1, 2, 1, TicTacToe.COMPUTER_O):
            return True
        if self.__check_true(0, 2, 1, 2, 2, 2, TicTacToe.COMPUTER_O):
            return True
        if self.__check_true(0, 0, 1, 1, 2, 2, TicTacToe.COMPUTER_O):
            return True
        if self.__check_true(0, 2, 1, 1, 2, 0, TicTacToe.COMPUTER_O):
            return True

        return False

    def draw(self):
        if not self.is_human and not self.is_computer:
            return True
        return False

    def __bool__(self):
        count = 0
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    count += 1

        if self.is_human():
            return False
        if self.is_computer():
            return False
        if count:
            return True
        return False


    def __check_indx(self, indx):
        a, b = indx
        if not 0 <= a <= 2 or not 0 <= b <= 2:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_indx(item)
        a, b = item
        return self.pole[a][b].value

    def __setitem__(self, key, value):
        self.__check_indx(key)
        a, b = key
        self.pole[a][b].value = value



game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

