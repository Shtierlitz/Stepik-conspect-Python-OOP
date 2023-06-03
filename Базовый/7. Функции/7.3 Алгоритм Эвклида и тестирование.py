"""Задача на нахождение наибольшего делителя"""
"""Алгоритм Евклида"""


a = 18
b = 24

def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
res = get_nod(a, b)
# print(res)

"""Быстрый алгоритм Эвклида"""
def get_nod2(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
       a, b, = b, a % b

    return a
res2 = get_nod2(a, b)

"""Тестирование функций"""

def test_nod(func):
    # --- тест 1
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("тест1 ок")
    else:
        print("fail 1")
    # тест 1
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("тест2 ок")
    else:
        print("fail 2")

    # Тест на скорость
    a = 2
    b = 1000000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("тест3 ок")
    else:
        print("fail 3")

test_nod(get_nod)
test_nod(get_nod2)