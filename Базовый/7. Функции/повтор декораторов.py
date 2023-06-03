
# def func_show(func):
#     def wraper(*args):
#         res = func(*args)
#         print(f"Площадь прямоугольника: {res}")
#         return res
#     return wraper
# @func_show
# def get_sq(width, height):
#     return width * height
#
# res = get_sq(2, 5)

# s = "Главная Добавить Удалить Выйти"
#
# def show_menu(func):
#     def wraper(*args):
#         res = func(*args)
#         lst = []
#         for i in range(len(res)):
#             lst.append(f"{i+1}. {res[i]}")
#         for s in lst:
#             print(s, end="\n")
#         return res
#     return wraper
#
#
# @show_menu
# def get_menu(s):
#     return  [i for i in s.split()]
#
# get_menu(s)

# s = "8 11 -5 4 3 10"
#
# def dec_func(func):
#     def wraper(*args):
#         res = func(*args)
#         return sorted(res)
#     return wraper
#
# @dec_func
# def get_list(s):
#     return [int(i) for i in s.split()]
#
# lst = get_list(s)
# print(*lst)

# x = "house river tree car"
# z = "дом река дерево машина"

# def func_dec(func):
#     def wraper(*args):
#         keys, values = func(*args)
#         d = {}
#
#         for i in range(len(keys)):
#             d[keys[i]] = values[i]
#         return d
#     return wraper
#
# @func_dec
# def make_lists(x, z):
#     l1 = [i for i in x.split()]
#     l2 = [i for i in z.split()]
#     return l1, l2
#
# a = make_lists(x, z)
# print(a)

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# def dec_func(func):
#     def wraper(*args):
#         res = func(*args)
#         return res.replace("---", " ").replace(" ", "-")
#     return wraper
#
# @dec_func
# def translate(s: str, t: dict):
#     a = []
#     for i in s[0:-1]:
#         if not i.isalpha():
#             a.append("-")
#         elif i in t.keys():
#             a.append(t.get(i.lower()))
#         else:
#             a.append(i.lower())
#     a.append("!")
#     b = "".join(a)
#     return b

# s = "Python - это круто!"
# a = translate(s, t)
# print(a)

# s = input()
# def dec_summa(start=0):
#     def func_dec(func):
#         def wraper(*args):
#             res = func(*args)
#             return start+res
#         return wraper
#     return func_dec
#
# @dec_summa(start=5)
# def summa(s):
#     a = list(map(int, s.split()))
#     return sum(a)
# a = summa(s)
# print(a)

# s = input()
#
# def str_dec(tag = "div"):
#     def func_dec(func):
#         def wraper(*args):
#             res = func(*args)
#             return f"<{tag}>{res}</{tag}>"
#         return wraper
#     return func_dec
#
# @str_dec("div")
# def string_low(s):
#     return s.lower()
# a = string_low(s)
# print(a)

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# s = "Декораторы - это круто!"
#
# def str_dec(chars="!?"):
#     def f_dec(func):
#         def wraper(*args):
#             res = func(*args)
#             for i in chars:
#                 for j in res:
#                     if i == j:
#                         res = res.replace(j, "-")
#             return res.replace("---", "-")
#         return wraper
#     return f_dec
#
#
# @str_dec(chars="!:;,. ")
# def str_recower(s, t: dict):
#     a = []
#     for i in s.lower():
#         if i in t.keys():
#             a.append(t.get(i))
#         else:
#             a.append(i)
#     d = "".join(a)
#     return d
#
# a = str_recower(s, t)
# print(a)


# from functools import wraps
# def nums_dec(func):
#     @wraps(func)
#     def wraper(*args):
#         res = func(*args)
#         return sum(res)
#     wraper.__name__ = func.__name__
#     return wraper
#
# lst = "1 5 10 23 412 5432 1343246 2345634563"
# @nums_dec
# def get_list(lst):
#     a = list(map(int, lst.split()))
#     return a
#
# a = get_list(lst)
# print(get_list.__name__)

# def counter_add():
#     def counter(s):
#         return s + 5
#     return counter
#
# cnt = counter_add()
# print(cnt(5))

# n = 5
#
# def counter_add(n):
#     def new_add(k):
#         return k + n
#     return new_add
#
# cnt = counter_add(2)
# print(cnt(n))

# def dec_func():
#     def teg_func(s):
#         g = "h1"
#         return f"<{g}>{s}</{g}>"
#     return teg_func
#
# s = "Balakirev"
#
# cmt = dec_func()
# print(cmt(s))

# def tag_dec(tag):
#     def str_dec(s):
#         return f"<{tag}>{s}</{tag}>"
#     return str_dec
#
# a = tag_dec("div")
# s = "Сергей Балакирев"
# print(a(s))
# l = "list"
# lst = "-5 6 8 11 0 111 -456 3"
#
# def type_dec(tp=None):
#     def lst_ref(lst):
#         if tp == "list":
#             return [int(i) for i in lst.split()]
#         else:
#             return tuple(int(i) for i in lst.split())
#     return lst_ref
#
#
# a = type_dec("list")
# print(a(lst))

# from datetime import datetime as dt
#
# def timeit(func):
#      def wraper(*args, **kwargs):
#           start = dt.now()
#           res = func(*args, **kwargs)
#           print(dt.now() - start)
#           return res
#      return wraper
#
# @timeit
# def one(n):
#      l = []
#      for i in range(n):
#           if i % 2 == 0:
#                l.append(i)
#      return l
#
# @timeit
# def two(n):
#      l = [i for i in range(n) if i % 2 == 0]
#      return l
#
# a = one(10000)
# b = two(10000)

