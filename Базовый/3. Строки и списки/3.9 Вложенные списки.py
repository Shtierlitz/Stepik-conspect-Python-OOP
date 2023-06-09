"""Вложенные списки"""

"""Подвиг 1. В список:

a = [5.4, 6.7, 10.4]

добавить в конец вложенный список со значениями, вводимыми в программу (целые числа вводятся в строчку через пробел). 
Результирующий список lst вывести на экран командой:

print(lst)

Sample Input:

8 11
Sample Output:

[5.4, 6.7, 10.4, [8, 11]]"""

# a = [5.4, 6.7, 10.4]
# b = input().split()
# b[0], b[1] = int(b[0]), int(b[1])
# a.append(b)
# print(a)


"""Подвиг 2. Вводятся три строчки стихотворения (каждая с новой строки). 
Сохранить его в виде вложенного списка с разбивкой по строкам и словам (слова разделяются пробелом). 
Результирующий список lst вывести на экран командой:

print(lst)

Sample Input:

Мороз и солнце день чудесный
Еще ты дремлешь друг прелестный
Пора красавица проснись
Sample Output:

[['Мороз', 'и', 'солнце', 'день', 'чудесный'], ['Еще', 'ты', 'дремлешь', 'друг', 'прелестный'], 
['Пора', 'красавица', 'проснись']]"""

# a = input().split()
# b = input().split()
# c = input().split()
# d = [a, b, c]
# print(d)

"""Подвиг 3. Вводится  матрица чисел из трех строк. 
В каждой строке числа разделяются пробелом. 
Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.

Sample Input:

8 11 12 1
9 4 36 -4
1 12 49 5
Sample Output:

1 -4 5"""

# a, b, c = input().split(), input().split(), input().split()
#
# print(a[3], b[3], c[3])

# a = [True, [1, 0, ["True", ["Истина", "Ложь"], "False"]], False]
# print(a[1][2][2])


"""Подвиг 6. Имеется вложенный список из трех строк:

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
Необходимо реализовать проверку на наличие в этом списке введенного слова. 
Результат (True или False) вывести на экран. Решить задачу необходимо без применения условного оператора.

Sample Input:

дядя
Sample Output:

True"""

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
a = input()
print(a in str(t))