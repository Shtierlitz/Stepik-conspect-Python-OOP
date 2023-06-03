"""Строки"""


a = input()
b = input()
print(a + " " + b)

a, b = map(str, input().split())
a, b = a + " ", b + " "
print(a * 2 + b * 3)

a, b = map(str, input().split())
print("Переменная a = " + a + ", " + "переменная b = " + b)

"""Подвиг 9. Написать программу ввода строки и формирования новой строчки вида:
"Строка: <введенная строка>. Длина: <длина строки>". Результат сформированной строки вывести на экран.

P. S. В программе F-строки не использовать.

Sample Input:

hello Balakirev
Sample Output:

Строка: hello Balakirev. Длина: 15"""
a = input()
b = len(a)
print("Строка: " + a + ". " + "Длина: " + str(b))


"""Подвиг 10. Написать программу ввода двух слов (через пробел в одну строчку).
Определить булевы значения для оператора in проверки вхождения первого слова во второе.
А также для операторов ==, >, <. Все булевы значения объединить в одну строку через пробел и вывести на экран.

Sample Input:

hello python
Sample Output:

False False False True"""

a, b = map(str, input().split())
print(a in b, a > b, a == b, a < b)

a, b = map(str, input().split())
c = ord(a)
d = ord(b)
print("Коды: " + a + " = " + str(c) + ", " + b + " = " + str(d))





