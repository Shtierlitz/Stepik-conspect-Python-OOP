"""Тернарный оператор (a if a < b else b)"""

"""Подвиг 1. Вводится два вещественных числа, каждое с новой строки. 
Необходимо с помощью тернарного условного оператора наибольшее значение присвоить 
переменной d и вывести ее на экран.

Sample Input:

5.4
-3.8
Sample Output:

5.4"""

# a = float(input())
# b = float(input())
# c = a if a > b else b
# print(c)

"""Подвиг 2. Вводится целое число. Необходимо переменной msg присвоить строку "кратно 3", 
если введенное число кратно 3, а иначе присвоить строку "не кратно 3". 
Реализовать программу с использованием тернарного оператора. 
Переменную msg отобразить на экране.

Sample Input:

9
Sample Output:

кратно 3"""

# a = int(input())
# msg = "кратно 3" if a % 3 == 0 else "не кратно 3"
# print(msg)
# print(a % 3 )

"""Подвиг 3. Вводится слово. Переменной msg присвоить строку "палиндром", 

если введенное слово является палиндромом (одинаково читается и вперед и назад), 
а иначе присвоить строку "не палиндром". 
Проверку проводить без учета регистра. Программу реализовать с помощью тернарного условного оператора. 
Значение переменной msg отобразить на экране.

Sample Input:

Казак
Sample Output:

палиндром"""

# a = input()
# b = a.lower()
# c = "палиндром" if b == b[::-1] else "не палиндром"
# print(c)

"""Подвиг 4. Вводится целое число 0 или 1. 
Необходимо преобразовать их в строки: 0 - в "False", 1 - в "True". 
Реализовать это с помощью тернарного условного оператора. 
Результат отобразить на экране.

Sample Input:

1
Sample Output:

True"""

# a = int(input())
# b = "False" if a < 1 else "True"
# print(b)

"""Подвиг 5. Вводится текущее время (секунды) в диапазоне [0; 59]. 
Если значение равно 59, то следующее должно быть 0. 
И так по кругу. Необходимо  вычислить следующее значение с проверкой граничного значения 59. 
Реализуйте это с помощью тернарного условного оператора. Результат отобразите на экране.

P.S. Попробуйте также реализовать эту же задачу с использованием только арифметических операций.

Sample Input:

55
Sample Output:

56"""

# мой вариант
# sec = int(input())
# a = []
# b = 0
# while b != 60:
#     if b != 60:
#         a.append(b)
#         b += 1
# next_sec = sec + 1 if sec != 59 else 0
# print(next_sec)
#
# женин
# sec = int(input())
# next_sec = (sec+1) % 60
# print(next_sec)

#
# i = 5
# a = (i%60+1)%60
# print(a)

# a = 59
# b = a + 1 if a <= 58 else 0
# print(b)

"""Подвиг 6. Имеется список базовых нот:

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, 
в одну строчку через пробел. Необходимо отобразить указанные ноты в виде строки через пробел, 
но перед нотами до и фа дополнительно ставить символ диеза '#'. 
Реализовать эту программу с использованием тернарного условного оператора 
(он может использоваться несколько раз).

Sample Input:

1 6 7
Sample Output:

#до ля си"""

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())

d = (((((m[6] if a == 7 else m[5])if a != 5 else m[4])if a != 4 else "#"+m[3])if a != 3 else m[2])if a != 2 else m[1])if a != 1 else "#"+m[0]
e = (((((m[6] if b == 7 else m[5])if b != 5 else m[4])if b != 4 else "#"+m[3])if b != 3 else m[2])if b != 2 else m[1])if b != 1 else "#"+m[0]
f = (((((m[6] if c == 7 else m[5])if c != 5 else m[4])if c != 4 else "#"+m[3])if c != 3 else m[2])if c != 2 else m[1])if c != 1 else "#"+m[0]
print(d, e, f)