import random as rnd
N, M = (5, 10)


def getTotalMines(PM, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            x = i+k
            y = j+k
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if PM[x*N+y] < 0:
                n += 1
    return n

def create_game(PM):
    n = M
    while n > 0:
        i = rnd.randrange(N)
        j = rnd.randrange(N)
        if PM[i*N+j] != 0:
            continue
        PM[i*N+j] = -1
        n -= 1

    for i in range(N):
        for j in range(N):
            if PM[i*N+j] == 0:
                PM[i*N+j] = getTotalMines(PM, i, j)



def show(pole):
    for i in range(N):
        for j in range(N):
            print(str(pole[i*N+j]).rjust((3)), end="")
        print()

def go_player():
    flLoopInput = True
    while flLoopInput:
        x, y = input("Введите координату через пробел ").split()
        if not x.isdigit() or not y.isdigit():
            print("Координаты введены неверно")
            continue
        x = int(x)-1
        y = int(y)-1
        if x < 0 or x >= N or y < 0 or y >= N:
            print("Координаты выходят за пределы поля")
            continue

        flLoopInput = False
    return (x,y)


def is_finish(PM, P):
    for i in range(N*N):
        if P[i] != -2 and PM[i] < 0: return -1
    for i in range(N*N):
        if P[i] == -2 and PM[i] >= 0: return 1
    return -2

def startGame():
    PM = [0]*N*N
    P = [-2]*N*N
    create_game(PM)
    show(PM)
    go_player()

    finishstat = is_finish(PM, P)
    while finishstat > 0:
        show(P)
        x,y = go_player()
        P[x*N+y] = PM[x*N+y]
        finishstat = is_finish(PM, P)
    return finishstat


res = startGame()
if res == -1:
    print("Вы проиграли")
else:
    print("Вы выиграли")

print("Игра завершена")