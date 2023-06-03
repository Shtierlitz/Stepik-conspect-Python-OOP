from math import sin
def f(x):
    return abs(sin(x))**(x+2)
# медленный способ с вычислением каждой последовательности
f_hold = 0.00001
lst_1 = []
per = int(4/f_hold)
rang = range(0, per)

for i in range(0, int(4/f_hold)):
    lst_1.append(f(i*f_hold))
max_value = max(lst_1)
max_index = lst_1.index(max_value)
max_x = max_index * f_hold

print(max_x, "max_x(lst_1)")

# метод короткий
def rang(min_a, max_a, f_hold):
    if (max_a - min_a <= f_hold):
        if f(min_a) > f(max_a):
            return min_a
        else:
            return max_a

    center = (min_a+max_a)/2
    if f(center-f_hold) > f(center+f_hold):
        new_min = min_a
        new_max = center
    else:
        new_max = max_a
        new_min = center

    return rang(new_min, new_max, f_hold)

print(rang(0, 4, 0.00001))


