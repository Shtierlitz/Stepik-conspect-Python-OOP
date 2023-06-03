""" Вложенные условия и множественный выбор"""

"""Подвиг 1. Имеется следующее меню:

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
В программе вводится целое число от 1 до 6. Нужно вывести пункт меню, связанный с этим числом. 
Реализовать программу с использованием операторов if-elif


Sample Input:

2
Sample Output:

2. Строки и списки"""

# мой вариант
# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
#
# e = int(input())
# if e == 1:
#     print(m[:20].strip())
# elif e == 2:
#     print(m[20:39].strip())
# elif e == 3:
#     print(m[40:61])
# elif e == 4:
#     print(m[62:70])
# elif e == 5:
#     print(m[71:102])
# elif e == 6:
#     print(m[103:111])

# Лучший вариант

# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# s = m.split('\n')
# print(s)
# n = int(input())
# if n == 1:
#     print(f'{s[0]}')
# elif n == 2:
#     print(f'{s[1]}')
# elif n == 3:
#     print(f'{s[2]}')
# elif n == 4:
#     print(f'{s[3]}')
# elif n == 5:
#     print(f'{s[4]}')
# elif n == 6:
#     print(f'{s[5]}')

"""Подвиг 2. Вводятся три целых числа в одну строку через пробел. 
Необходимо определить наименьшее среди них и вывести его на экран. 
Реализовать программу, используя условный оператор, без использования функции min.

Sample Input:

8 11 -1
Sample Output:

-1"""
# мой вариант
# a, b, c = map(int, input().split())
# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < b and c < a:
#     print(c)
# elif a == b:
#     print(a)
# elif a == c:
#     print(c)
# elif b == c:
#     print(b)

# Вариант из урока
# a, b, c = map(int, input().split())
# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b < c:
#         print(b)
#     else:
#         print(c)


"""Подвиг 3. Вводится вес боксера-любителя (в кг, в виде вещественного числа). 
Известно, что вес таков, что боксер может быть отнесен к одной из весовых категорий:

1) легкий вес – до 60 кг (включительно);
2) первый полусредний вес – до 64 кг (включительно);
3) полусредний вес – до 69 кг (включительно);
4) остальные - более 69 кг.

Вывести на экран номер категории, в которой будет выступать боксер.

Sample Input:

62.4
Sample Output:

2"""
# a = float(input())
# if a <= 60:
#     print(1)
# elif a <= 64:
#     print(2)
# elif a <= 69:
#     print(3)
# else:
#     print(4)

"""Подвиг 4. Вводится порядковый номер дня недели (1, 2, ..., 7).
 Вывести на экран его название (понедельник, вторник, среда, четверг, пятница, суббота, воскресенье). 
 Программу реализовать с использованием операторов if-elif.

Sample Input:

2
Sample Output:

вторник"""
# a = int(input())
# if a == 1:
#     print("понедельник")
# elif a == 2:
#     print("вторник")
# elif a == 3:
#     print("среда")
# elif a == 4:
#     print("четверг")
# elif a == 5:
#     print("пятница")
# elif a == 6:
#     print("суббота")
# elif a == 7:
#     print("воскресенье")


"""Подвиг 5. Вводится порядковый номер месяца (1, 2, ..., 12). 
Вывести на экран количество дней в этом месяце. Принять, что год не является високосным. 
Реализовать через условный оператор, в котором следует использовать не более трех ветвей (блоков).

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
                                                                  1   2   3   4   5   6   7   8   9  10  11  12
Sample Input:

2
Sample Output:

28"""
# # мой вариант (не приняли)
# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print(31)
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print(31)
# elif a == 2:
#     print(28)

# их вариант
# a = int(input())
# big = [1, 3, 5, 7, 8, 10, 12]
# smal = [4, 6, 9, 11]
# h_smal = 2
# if a in big:
#     print(31)
# if a in smal:
#     print(30)
# elif a == 2:
#     print(28)


"""Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: 
m (порядковый номер месяца) и n (число). По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. 
Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; 
d - номер дня) в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
                                                                  1   2   3   4   5   6   7   8   9  10  11  12
Sample Input:

8 31
Sample Output:

08.30 09.01"""


# month, day = map(int, input().split())

# Мой вариант. Решал сутки
def near_date(month, day):
    big = [1, 3, 5, 7, 8, 10, 12]
    smal = [4, 6, 9, 11]
    d_l, d_r, m_l, m_r = 0, 0, 0, 0
    if month == 2:
        m_l = month
        m_r = month

        if day == 28:
            d_l = day - 1
            d_r = 1
            m_r = m_r + 1
        elif day == 1:
            d_l = 31
            d_r = day + 1
            m_l = month - 1
            if month == 3:
                d_l = 28
        elif day > 28:
            d_l = day
            d_r = 1
            m_r = m_r + 1
        else:
            d_l = day - 1
            d_r = day + 1

    elif month in big:
        m_l = month
        m_r = month
        if day == 31:
            d_r = 1
            d_l = day - 1
            m_r = m_r + 1

        elif day == 1:
            d_l = 30
            d_r = day + 1
            m_l = month - 1
            if month == 3:
                d_l = 28
        elif month == 8 and day == 31:
            d_l = 30
            d_r = day + 1
            m_l = month - 1
            m_r = month
        else:
            d_l = day - 1
            d_r = day + 1
    elif month in smal:
        m_l = month
        m_r = month
        if day == 30:
            d_l = day - 1
            d_r = 1
            m_r = m_r + 1
        elif day == 1:
            d_l = 31
            d_r = day + 1
            m_l = m_l - 1
        else:
            d_l = day - 1
            d_r = day + 1

    if month in big and day > 31:
        raise ValueError("Вводить надо только даты месяцев")
    elif day < 1:
        raise ValueError("Вводить надо только даты месяцев")
    elif month in smal and day > 30:
        raise ValueError("Вводить надо только даты месяцев")
    elif month == 2 and day > 28:
        raise ValueError("Этот год не высокосный")
    elif month == 12 and day == 31:
        raise ValueError("По условиям задачи этот день не используется")
    elif month == 1 and day == 1:
        raise ValueError("По условиям задачи этот день не используется")
    else:
        print(f"{m_l:02}.{d_l:02} {m_r:02}.{d_r:02}")


# near_date(8, 1)
# near_date(8, 2)
# near_date(8, 3)
# near_date(8, 4)
# near_date(8, 5)
# near_date(8, 6)
# near_date(8, 7)
# near_date(8, 8)
# near_date(8, 9)
# near_date(8, 10)
# near_date(8, 11)
# near_date(8, 12)
# near_date(8, 13)
# near_date(8, 14)
# near_date(8, 15)
# near_date(8, 16)
# near_date(8, 17)
# near_date(8, 18)
# near_date(8, 19)
# near_date(8, 20)
# near_date(8, 21)
# near_date(8, 22)
# near_date(8, 23)
# near_date(8, 24)
# near_date(8, 25)
# near_date(8, 26)
# near_date(8, 27)
# near_date(8, 28)
# near_date(8, 29)
# near_date(8, 30)
# near_date(8, 31)


# Женин (прошел)
# d_in_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month, day = tuple(int(e) for e in input().split(" ")) # here it starts from 0
# day_next, month_next = day+1,month
# if (day_next > d_in_m[month-1]):
#     day_next = 1
#     month_next += 1
# day_prev, month_prev = day-1, month
# if (day_prev < 1):
#     day_prev = d_in_m[month_prev-1-1]
#     month_prev -= 1
# print(f"{'%02d' % month_prev}.{'%02d' % day_prev} {'%02d' % month_next}.{'%02d' % day_next}")

# кусок моего варианта начального
# if month == 2:
#     if day == 1:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day < 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
#     elif day == 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day == 10:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day >= 28:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day > 10 and day < 28:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month <= 8:
#     if day == 1:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day < 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
#     elif day == 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day == 10:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     elif month in big and day == 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     elif month in big and day == 31:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif month in smal and day >= 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month == 9:
#     if day == 1:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day < 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
#     elif day == 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day == 10:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     elif day >= 30:
#         print(f"0{m_l}.{d_l} {m_r}.0{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month == 10:
#     if day == 1:
#         print(f"0{m_l}.{d_l} {m_r}.0{d_r}")
#     elif day < 9:
#         print(f"{m_l}.0{d_l} {m_r}.0{d_r}")
#     elif day == 9:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day == 10:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 31:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month > 10:
#     if day == 1:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     elif day < 9:
#         print(f"{m_l}.0{d_l} {m_r}.0{d_r}")
#     elif day == 9:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day == 10:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 31:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     elif month in smal and day >= 30:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     else:
#         print(f"{m_l}.0{d_l} {m_r}.0{d_r}")

"""Подвиг 7. Вводится целое число k (1 <= k <= 365). 
Определить, каким днем недели (понедельник, вторник, среда, четверг, пятница, суббота или воскресенье) 
является k-й день не високосного года, в котором 1 января является понедельником.

Sample Input:

121
Sample Output:

вторник"""

# k = int(input())
# if (1 <= k <= 365):
#     if k % 7 == 1:
#         print("понедельник")
#     elif k % 7 == 2:
#         print("вторник")
#     elif k % 7 == 3:
#         print("среда")
#     elif k % 7 == 4:
#         print("четверг")
#     elif k % 7 == 5:
#         print("пятница")
#     elif k % 7 == 6:
#         print("суббота")
#     elif k % 7 == 7:
#         print("воскресенье")

