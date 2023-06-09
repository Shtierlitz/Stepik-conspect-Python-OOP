"""Спецсимволы и экранирование символов"""

"""Подвиг 3. Вводится два слова в одну строку через пробел.
Поставьте между этими словами символ обратного слеша (вместо пробела).
Результирующую строку отобразите на экране.

P. S. Задачу реализовать без применения F-строк.

Sample Input:

Hello Balakirev!
Sample Output:

Hello\Balakirev!"""

a, b = input().split()
print(a + "\\" + b)

"""Подвиг 4. Вводится строка со словами, разделенными пробелом. Необходимо первый пробел заменить на одинарную кавычку,
а все остальные - на двойные. Результирующую строку отобразить на экране.

Sample Input:

My best friend is Python!
Sample Output:

My'best"friend"is"Python!"""

a = "My best friend is Python!"

a = input().split()
a = '\"'.join(a).replace('\"', "\'",1)
print(a)

"""Подвиг 6. Вводится слово. Необходимо сформировать новую строку,
где введенное слово будет заключено в двойные кавычки. Результат выведите на экран.

Sample Input:

language
Sample Output:

"language"""

a = input()
print('\"' + a + '\"')