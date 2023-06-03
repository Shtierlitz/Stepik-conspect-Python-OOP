"""Посвящение в ООП
Вы прошли серию испытаний и совершили множество подвигов, чтобы лицом к лицу столкнуться с
настоящим вызовом, достойным лишь избранных! Для подтверждения своих знаний и навыков
вам предлагается пройти этап посвящения в объектно-ориентированное программирование.
И вот задание, которое выпало на вашу долю.

Руководство компании целыми днями не знает куда себя деть. Поэтому они решили дать задание
своим программистам написать программу игры "Морской бой". Но эта игра будет немного отличаться
от классической. Для тех, кто не знаком с этой древней, как мир, игрой, напомню ее краткое описание.

Каждый игрок у себя на бумаге рисует игровое поле 10 х 10 клеток и расставляет на нем десять
 кораблей: однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1.



Корабли расставляются случайным образом, но так, чтобы не выходили за пределы игрового поля
и не соприкасались друг с другом (в том числе и по диагонали).

Затем, игроки по очереди называют клетки, куда производят выстрелы. И отмечают эти выстрелы
на другом таком же поле в 10 х 10 клеток, которое представляет поле соперника. Соперник при
этом должен честно отвечать: "промах", если ни один корабль не был задет и "попал",
если произошло попадание. Выигрывает тот игрок, который первым поразит все корабли соперника.

Но это была игра из глубокого прошлого. Теперь же, в компьютерную эру, корабли на игровом
поле могут перемещаться в направлении своей ориентации на одну клетку после каждого хода соперника,
если в них не было ни одного попадания.

Итак, лично вам поручается сделать важный фрагмент этой игры - расстановку и
управление кораблями в этой игре. А само задание звучит так.

Техническое задание
В программе необходимо объявить два класса:

Ship - для представления кораблей;
GamePole - для описания игрового поля.

Класс Ship
Класс Ship должен описывать корабли набором следующих параметров:

x, y - координаты начала расположения корабля (целые числа);
length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).



Объекты класса Ship должны создаваться командами:

ship = Ship(length)
ship = Ship(length, tp)
ship = Ship(length, tp, x, y)
По умолчанию (если не указывается) параметр tp = 1, а координаты x, y равны None.

В каждом объекте класса Ship должны формироваться следующие локальные атрибуты:

_x, _y - координаты корабля (целые значения в диапазоне [0; size), где size - размер игрового поля);
_length - длина корабля (число палуб);
_tp - ориентация корабля;
_is_move - возможно ли перемещение корабля (изначально равно True);
_cells - изначально список длиной length, состоящий из единиц (например, при length=3, _cells = [1, 1, 1]).

Список _cells будет сигнализировать о попадании соперником в какую-либо палубу корабля.
Если стоит 1, то попадания не было, а если стоит значение 2, то произошло попадание в соответствующую палубу.

При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и
перемещение корабля по игровому полю прекращается.

В самом классе Ship должны быть реализованы следующие методы (конечно, возможны и другие, дополнительные):

set_start_coords(x, y) - установка начальных координат (запись значений в локальные атрибуты _x, _y);
get_start_coords() - получение начальных координат корабля в виде кортежа x, y;
move(go) - перемещение корабля в направлении его ориентации на go клеток (go = 1 -
движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку);
движение возможно только если флаг _is_move = True;
is_collide(ship) - проверка на столкновение с другим кораблем ship (столкновением считается,
если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали);
метод возвращает True, если столкновение есть и False - в противном случае;
is_out_pole(size) - проверка на выход корабля за пределы игрового поля (size -
размер игрового поля, обычно, size = 10); возвращается булево значение True,
если корабль вышел из игрового поля и False - в противном случае;

С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к
 коллекции _cells следующим образом:

value = ship[indx] # считывание значения из _cells по индексу indx (индекс отсчитывается от 0)
ship[indx] = value # запись нового значения в коллекцию _cells
Класс GamePole
Следующий класс GamePole должен обеспечивать работу с игровым полем. Объекты этого класса создаются командой:

pole = GamePole(size)
где size - размеры игрового поля (обычно, size = 10).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_size - размер игрового поля (целое положительное число);
_ships - список из кораблей (объектов класса Ship); изначально пустой список.

В самом классе GamePole должны быть реализованы следующие методы (возможны и другие,
дополнительные методы):

init() - начальная инициализация игрового поля; здесь создается список из кораблей
(объектов класса Ship): однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный -
1 (ориентация этих кораблей должна быть случайной).

Корабли формируются в коллекции _ships следующим образом: однопалубных - 4; двухпалубных - 3;
трехпалубных - 2; четырехпалубный - 1. Ориентация этих кораблей должна быть случайной.
Для этого можно воспользоваться функцией randint следующим образом:

[Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]
Начальные координаты x, y не расставленных кораблей равны None.

После этого, выполняется их расстановка на игровом поле со случайными координатами так,
чтобы корабли не пересекались между собой.

get_ships() - возвращает коллекцию _ships;
move_ships() - перемещает каждый корабль из коллекции _ships на одну клетку
(случайным образом вперед или назад) в направлении ориентации корабля; если перемещение
в выбранную сторону невозможно (другой корабль или пределы игрового поля),
то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;
show() - отображение игрового поля в консоли (корабли должны отображаться значениями
из коллекции _cells каждого корабля, вода - значением 0);

get_pole() - получение текущего игрового поля в виде двумерного (вложенного)
кортежа размерами size x size элементов.

Пример отображения игрового поля:

0 0 1 0 1 1 1 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 1
0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0
Пример использования классов (эти строчки в программе не писать):

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
В программе требуется только объявить классы Ship и GamePole с соответствующим функционалом.
На экран выводить ничего не нужно.

P.S. Для самых преданных поклонников программирования и ООП. Завершите эту программу,
добавив еще один класс SeaBattle для управления игровым процессом в целом.
Игра должна осуществляться между человеком и компьютером.
Выстрелы со стороны компьютера можно реализовать случайным образом в свободные клетки.
Сыграйте в эту игру и выиграйте у компьютера."""

from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None, ):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        self._y = v

    @property
    def tp(self):
        return self._tp

    @property
    def is_move(self):
        return self._is_move

    @is_move.setter
    def is_move(self, v):
        if type(v) is bool:
            self._is_move = v

    @property
    def cells(self):
        return self._cells

    def ship_coords_list(self):
        x, y, = self._x, self._y
        return [(x+i, y) for i in range(self._length)] if self.tp == 1 else [(x, i + y) for i in range(self._length)]

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def __linked_cells(self):
        flanks = [(x, y - a) for a in [1, -1] for x, y in self.ship_coords_list()] if self.tp == 1 \
            else [(x + a, y) for a in [1, -1] for x, y in self.ship_coords_list()]
        tops = [(self.x - 1, self.y), (self.x + self._length, self.y)] if self.tp == 1 \
            else [(self.x, self.y - 1), (self.x, self.y + self._length)]
        diagonals = [(x, y - a) for a in [1, -1] for x, y in tops] if self.tp == 1 \
            else [(x + a, y) for a in [1, -1] for x, y in tops]
        return [*flanks, *tops, *diagonals]

    def is_collide(self, ship):
        coords = ship.ship_coords_list() + ship.__linked_cells()
        if any(map(lambda x: x in coords, self.ship_coords_list())):
            return True
        return False

    def is_out_pole(self, size=10):
        if any(map(lambda x: x[0] < 0 or x[0] > size - 1 or x[1] < 0 or x[1] > size -1, self.ship_coords_list())):
            return True
        return False

    def __getitem__(self, item):
        if not type(item) == int or not 0 <= item <= len(self._cells) - 1:
            raise IndexError("Не верное значение индекса")
        return self._cells[item]

    def __setitem__(self, key, value):
        if not type(key) == int or not 0 <= key <= len(self._cells) - 1:
            raise IndexError("Не верное значение индекса")
        self._cells[key] = value


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self._defeat_ships = []
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        self._life = 0

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, val):
        self._life = val

    @property
    def defeat_ships(self):
        return self.defeat_ships

    @property
    def size(self):
        return self._size

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))
                       ]
        self.life = len(self._ships)
        ready_ships = []
        indx = 0
        while indx < len(self._ships):
            ship = self._ships[indx]
            if ship not in ready_ships:
                ship.x, ship.y = randint(0, self.size -1), randint(0, self.size -1)
                if ship.is_out_pole():
                    continue
                if ready_ships and any(map(lambda x: ship.is_collide(x), ready_ships)):
                    continue

                ready_ships.append(ship)
            indx += 1


    def show(self, player=True):
        matrix = self.get_pole()
        for r in range(self.size):
            for c in range(self.size):
                n = matrix[r][c]
                if player:
                    print("~" if n == 0 else "0" if n == 1 else "*", end=" ")
                else:
                    print("~" if n in (0, 1) else "*" if n == 2 else "0", end=" ")
            print()

    def get_ships(self):
        return self._ships

    def move_ships(self):
        a = randint(-1, 1)
        ready_ships = []
        indx = 0
        while indx < len(self._ships):
            ship = self._ships[indx]
            x, y = ship.ship_coords_list()[0]
            if ship not in ready_ships and ship._is_move:
                ready_ships.append(ship)

                ship.move(a)

                if ship.is_out_pole():
                    ship.x, ship.y = x, y
                    ship.move(-a)
                if ship.is_out_pole():
                    ship.x, ship.y = x, y

                if any(map(lambda z: ship.is_collide(z), ready_ships)):
                    ship.x, ship.y = x, y
                    ship.move(-a)

                if any(map(lambda z: ship.is_collide(z), ready_ships)):
                    ship.x, ship.y = x, y

            indx += 1

    def get_pole(self):
        matrix = self._pole
        for ship in self._ships:
            for r in range(self.size):
                for c in range(self.size):
                    if (r, c) in ship.ship_coords_list():
                        a = ship._cells[ship.ship_coords_list().index((r, c))]
                        matrix[r][c] = 1 if a == 1 else 2 if a == 2 else 0
                        self._pole[r][c] = matrix[r][c]
        return tuple(tuple(matrix[r]) for r in range(self.size))

    def search_ship(self, x, y):
        for ship in self.get_ships():
            if (x, y) in ship.ship_coords_list():
                return ship, ship.ship_coords_list().inde((x, y))
        return None, None

    def check_ship(self, ship):
        if ship not in self.defeat_ships and all(map(lambda x: x == 2, ship._cells)):
            return True
        return False

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()


