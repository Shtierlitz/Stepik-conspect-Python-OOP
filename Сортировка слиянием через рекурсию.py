lst = [0, 4, 2, 1, 14, 6, 7, 8, 3, 30, 5, 12, 13]
# пример разбивки списка.
# lst_2 = lst[(len(lst)//2):]
# lst_1 = lst[:(len(lst)//2)]
# print(lst_1, lst_2)

def merge_lists(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j+= 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])    # рекурсия дробит список до 1го элемента
    right = merge_sort(lst[mid:])
    return merge_lists(left, right)

print(*merge_sort(lst[::-1]))


# Задача на слияние списков
lst = [8, 11, -5, 4, 3, 10]
# lst = [0, 4, 2, 1, 14, 6, 7, 8, 3, 30, 5, 12, 40 ,183, 241, 521, 1, 1231312]

# Пузырьковая сортировка
stop = True
while stop:
    stop = False
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            stop = True
print(lst)
# l = len(lst)//3
# lst_1 = lst[:l]
# lst_2 = lst[l:l+l]
# lst_3 = lst[-l:]
# print(lst_1, lst_2, lst_3)


# без функции
a = lst[len(lst)//2:]
b = lst[:len(lst)//2]

i = j = 0
c = []
n = len(a)
m = len(b)

while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1


while i < n:
    c.append(a[i])
    i += 1
while j < m:
    c.append(b[j])
    j += 1

print(c)
# https://www.youtube.com/watch?v=LCfwxi2RPK4