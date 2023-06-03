# N = 8
#
# def get_rec_N(N):
#     if N != 1:
#         get_rec_N(N-1)
#     print(N)
#
# get_rec_N(N)


# lst = list(map(int, input().split()))
# lst = [8, 11, -5, 4, 3]
# def get_rec_sum(lst, index=0):
#     if index >= len(lst):
#         return 0
#     else:
#         return lst[index] + get_rec_sum(lst, index +1)
#
# print(get_rec_sum(lst))


# lst = [8, 11, -5, 4, 3]
# def get_rec_sum(ls):
#     while len(ls) > 1:
#         a = ls[0]
#         b = ls[1:]
#         return a + get_rec_sum(b)   # тут в рекурсию передается срез уже без первого элемента и на втором круге прога
#                                     # уже не знает, что это срез, а берет за полноценный список
#     else:
#         return ls[-1]
#
# print(get_rec_sum(lst))

# lst = [8, 11, -5, 4, 3]
# def get_rec_sum(lst):
#     if len(lst) > 0:
#         return lst.pop() + get_rec_sum(lst) # Тут мы удаляем последний элемент из списка
#                                             # а потом его плюсуем со значением pop из следующей рекурсии
#     else:
#         return 0
#
# print(get_rec_sum(lst))




# n = 7
# def fib_rec(n, f=[]):
#     if len(f) < n and len(f) < 2:
#         f.append(1)
#         f.append(1)
#         fib_rec(n, f)
#         return f
#     elif len(f) < n and len(f) >= 2:
#         f.append(f[-1]+f[-2])
#         fib_rec(n, f)
#     return f
# print(*fib_rec(n))

# n = 7
# def fib_rec(n):
#     if n < 3:
#         return [1] * n
#     else:
#         return fib_rec(n - 1) + [sum(fib_rec(n - 1)[-2:])]
#
# print(*fib_rec(n))

# Самое простое решение не трогая условия
# n = 7
# def fib_rec(n, f=[]):
#     while n > 1:
#         if len(f) < 2:
#             f.extend([1, 1])
#             fib_rec(n-1, f)
#         else:
#             f.append(f[-1] + f[-2])
#             fib_rec(n-1, f)
#         return f
# print(*fib_rec(n))

# Факториал
# N = 6
# def fact_rec(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact_rec(n-1)
# print(fact_rec(N))

# def fact_rec(n, res=1, count=1):
#     if n <= 1: return 1
#     if count != n:
#         count +=1
#         res *= count
#         res = fact_rec(n, res, count)
#     return res
#
# print(fact_rec(N))

# def fact_rec(n):
#     if n == 0:
#         return 1
#     return n * fact_rec(n-1)
#
# print(fact_rec(N))


# Многомерный список
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
# def get_line_list(d, a=[]):
#     for i in d:
#         if isinstance(i, list):
#             get_line_list(i)
#         else:
#             a.append(i)
#     return a
#
# print(get_line_list(d))


# не рекурсия
# def non_rec_list(d, s=[]):
#     for i in d:
#         if isinstance(i, list): # или type(i) == list:
#             for q in i:
#                 if isinstance(q, list):
#                     for w in q:
#                         if isinstance(w, list):
#                             s.extend(w)
#                         else:
#                             s.append(w)
#                 else:
#                     s.append(q)
#         else:
#             s.append(i)
#     return s
#
# print(non_rec_list(d))


# def get_rec_N(N):
#     if N-1 != 0:
#         get_rec_N(N-1)
#     print(N)
#
# get_rec_N(8)

# a = [8, 11, -5, 4, 3]
#
# def get_rec_sum(lst, summa = 0):
#     if len(lst)!= 0:
#         summa += lst.pop()
#         return get_rec_sum(lst, summa)
#     return summa
#
# print(get_rec_sum(a))

# n = 7
# def fib_rec(N, f=[]):
#     while N:
#         if len(f) <= 1:
#             f.append(1)
#             N -= 1
#             fib_rec(N, f)
#         else:
#             f.append(f[-1]+f[-2])
#             N -= 1
#             fib_rec(N, f)
#         return f
#
# print(*fib_rec(n))


# n = 6
# def fact_rec(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact_rec(n-1)
#
# print(fact_rec(n))


# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
# def get_line_list(d,a=[]):
#     for i in d:
#         if type(i) == list:
#             get_line_list(i, a)
#         else:
#             a.append(i)
#     return a
#
# print(get_line_list(d))



# def get_path(n):
#     if n >= 2:
#         s = get_path(n-1) + get_path(n-2)
#         return s
#     else:
#         return 1
#
# print(get_path(7))


l1 = [1, 4, 10, 11]
l2 = [2 ,3 ,3, 4, 8]


def gethering(l1, l2):
    res = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1

    if i < len(l1):
        res += l1[i:]
    if j < len(l2):
        res += l2[j:]

    return res


def sorting(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = sorting(lst[:mid])
    right = sorting(lst[mid:])
    return gethering(left, right)

a = [i for i in range(-200, 500 )]
import random
random.shuffle(a)
print(a)
print(sorting(a))
