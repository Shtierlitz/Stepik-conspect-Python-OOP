"""Распространение исключений (propagation exceptions
обрабатывать исключения можно на любом уровне ошибки.
то есть одна ошибка обчны за собой ведет каскад ошибок на разных уровнях,
 на каждом из которых ее можно обрабатывать
"""
# def func2():
#     try:                            # Ошибку можно отлавливать на любом уровне
#         return 1 / 0
#     except:
#         print("func2 error 3")
#
# def func1():
#     try:                            # Ошибку можно отлавливать на любом уровне
#         return func2()
#     except:
#         print('func1 error 2')      # Ранее обработанная ошибка не всплывает дальше
#
# print("Я к вам пишу - чего же более?")
# print("Что я могу еще сказать?")
# print("Теперь, я знаю, в вашей воле")
# try:                                # Ошибку можно отлавливать на любом уровне
#     func1()
# except:
#     print("func1 error")            # Ранее обработанная ошибка не всплывает дальше
# print("Меня презреньем наказать.")
# print("Но вы, к моей несчастной доле")
# print("Хоть каплю жалости храня")
# print("Вы не оставите меня")

# https://www.youtube.com/watch?v=jVHvFxmiLmI&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=31



"""Подвиг 3. Объявите функцию с сигнатурой:

def input_int_numbers(): ...

которая бы считывала строку из введенных целых чисел, записанных через пробел, 
и возвращала кортеж из введенных чисел (в виде целых чисел, а не строк).

Если хотя бы одно значение не является целым числом, то генерировать исключение, командой:

raise TypeError('все числа должны быть целыми')
Вызовите эту функцию в цикле до тех пор, пока пользователь не введет в строке все 
целочисленные значения (то есть, цикл завершается, когда функция отработает штатно, без генерации исключения).

Выведите на экран прочитанные значения, записанные в виде строки через пробел.

Sample Input:

1 abc 3 5
2.4 -5 4 3 2
0 -5 8 11
1 2 3 4
Sample Output:

0 -5 8 11"""


# def input_int_numbers():
#     try:
#         t = tuple(map(int, input().split()))
#     except:
#         raise TypeError('все числа должны быть целыми')
#     else:
#         return t
#
# s = True
# while s:
#     try:
#         f = input_int_numbers()
#     except:
#         pass
#     else:
#         s = False
#         print(*f)

"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/IexoPrHUSaA

Подвиг 4. Объявите класс с именем ValidatorString, объекты которого создаются командой:

vs = ValidatorString(min_length, max_length, chars)
где min_length, max_length - минимально и максимально допустимая длина строки (целые числа, 
формируемые диапазон [min_length; max_length]); chars - строка из набора символов 
(хотя бы один из них должен присутствовать в проверяемой строке). Если chars - пустая строка, 
то проверку на вхождение символов не делать.

В самом классе ValidatorString объявите метод:

def is_valid(self, string): ...

который проверяет строку string на соответствие критериям: string должна быть строкой, 
с длиной в диапазоне [min_length; max_length] и в string присутствует хотя бы один символ из chars. 
Если хотя бы один из этих критериев не выполняется, то генерируется исключение командой:

raise ValueError('недопустимая строка')
Затем, объявите класс с именем LoginForm, объекты которого создаются командой:

lg = LoginForm(login_validator, password_validator)
где login_validator - валидатор для логина (объект класса ValidatorString); password_validator - 
валидатор для пароля (объект класса ValidatorString).

В самом классе LoginForm объявите следующий метод:

def form(self, request): ...

где request - объект запроса (словарь). В словаре request должен быть ключ 'login' со 
значением введенного логина (строки) и ключ 'password' со значением введенного пароля (строка). 
Если хотя бы одного ключа нет, то генерировать исключение командой:

raise TypeError('в запросе отсутствует логин или пароль')
В противном случае (если проверка для request прошла), проверять корректность полученного формой логина 
и пароля с помощью валидаторов, указанных в параметрах login_validator и password_validator, 
при создании объекта формы.

Если логин/пароль введены верно, то в объекте класса LoginForm локальным атрибутам _login и _password 
присвоить соответствующие значения.

Пример использования классов (эти строчки должны быть в программе):

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
Sample Input:

sergey balakirev!
Sample Output:

sergey"""

# class ValidatorString:
#     def __init__(self, min_length, max_length, chars):
#         self.__min_length, self.__max_length, self.__chars = min_length, max_length, chars
#
#     def is_valid(self, string):
#         if self.__chars == "":
#             return string
#         if type(string) != str or not self.__min_length <= len(string) <= self.__max_length:
#             raise ValueError('недопустимая строка')
#         count = 0
#         for i in string:
#             if i in self.__chars:
#                 count += 1
#         if not count:
#             raise ValueError('недопустимая строка')
#         return string
#
# class LoginForm:
#     def __init__(self, login_validator, password_validator):
#         self.login_validator, self.password_validator = login_validator, password_validator
#         self._login = None
#         self._password = None
#
#     def form(self, request: dict):
#         if "login" not in request or "password" not in request:
#             raise TypeError('в запросе отсутствует логин или пароль')
#         self._login = self.login_validator.is_valid(request["login"])
#         self._password = self.password_validator.is_valid(request["password"])
#
#
#
#
# login_v = ValidatorString(4, 50, "")
# password_v = ValidatorString(10, 50, "!$#@%&?")
# lg = LoginForm(login_v, password_v)
# login, password = input().split()
# try:
#     lg.form({'login': login, 'password': password})
# except (TypeError, ValueError) as e:
#     print(e)
# else:
#     print(lg._login)


"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/AVh6hs06oCU

Подвиг 5. Вы начинаете разрабатывать свой сервис по тестированию. 
Для этого вам поручается разработать базовый класс Test для всех видов тестов, объекты которого создаются командой:

test = Test(descr)
где descr - формулировка теста (строка). Если длина строки descr меньше 10 или больше 10 000 символов, 
то генерировать исключение командой:

raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
В самом классе Test должен быть объявлен абстрактный метод:

def run(self): ...

который должен быть переопределен в дочернем классе. 
Если это не так, то должно генерироваться исключение командой:

raise NotImplementedError
Далее, объявите дочерний класс с именем TestAnsDigit для тестирования правильного введенного 
числового ответа на вопрос теста. Объекты класса TestAnsDigit должны создаваться командой:

test_d = TestAnsDigit(descr, ans_digit, max_error_digit)
где ans_digit - верный числовой ответ на тест; max_error_digit - максимальная погрешность в указании 
числового ответа (необходимо для проверки корректности вещественных чисел, по умолчанию принимает значение 0.01).

Если аргумент ans_digit или max_error_digit не число (также проверить, что max_error_digit больше или равно нулю),
 то генерировать исключение командой:

raise ValueError('недопустимые значения аргументов теста')
В классе TestAnsDigit переопределите метод:

def run(self): ...

который должен читать строку из входного потока (ответ пользователя) командой:

ans = float(input()) # именно такой командой, ее прописывайте в методе run()
и возвращать булево значение True, если введенный числовой ответ ans принадлежит диапазону
 [ans_digit-max_error_digit; ans_digit+max_error_digit]. Иначе возвращается булево значение False.

Теперь нужно воспользоваться классом TestAnsDigit. Для этого в программе вначале читается сам тест с помощью команд:

descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
Далее, вам необходимо создать объект класса TestAnsDigit с аргументами descr, ans, 
а аргумент max_error_digit должен принимать значение по умолчанию 0.01.

Запустите тест командой run() и выведите на экран результат его работы (значение True или False). 
Если в процессе создания объекта класса TestAnsDigit или в процессе работы метода run() 
возникли исключения, то они должны быть обработаны и на экран выведено сообщение, содержащееся в исключении.

Sample Input:

Какое значение получим, при выполнении команды int(5.7)? | 5
6
Sample Output:

False"""



# class Test():
#     def __init__(self, descr: str):
#         if not 10 <= len(descr) <= 10000:
#             raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
#         self.descr = descr
#
#     def run(self):
#         raise NotImplementedError
#
# class TestAnsDigit(Test):
#     def __init__(self, descr, ans_digit, max_error_digit=0.01):
#         super().__init__(descr)
#         if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
#             raise ValueError('недопустимые значения аргументов теста')
#         self.ans_digit, self.max_error_digit = ans_digit, max_error_digit
#
#     def run(self):
#         ans = float(input())
#         if self.ans_digit <= ans <= self.ans_digit + self.max_error_digit:
#             return True
#         return False
#
#
# descr, ans = map(str.strip, input().split('|'))
# ans = float(ans)
#
# try:
#     an = TestAnsDigit(descr, ans)
#     print(an.run())
# except Exception as e:
#     print(e)


"""Подвиг 7. В программе выполняется считывание числовых данных из входного потока, командой:

digits = list(map(float, input().split()))
Эти данные следует представить в виде объекта класса TupleLimit. Сам класс должен наследоваться от класса tuple, 
а его объекты создаваться командой:

tl = TupleLimit(lst, max_length)
где lst - коллекция (список или кортеж) из данных; max_length - максимально допустимая длина коллекции TupleLimit.
 Если длина lst превышает значение max_length, то должно генерироваться исключение командой:

raise ValueError('число элементов коллекции превышает заданный предел')
В самом классе TupleLimit переопределить магические методы __str__() и __repr__() 
для отображения объекта класса TupleLimit в виде строки из набора данных lst, записанных через пробел. Например:

"1.0 2.5 -5.0 11.2"

Создайте в программе объект класса TupleLimit для прочитанных данных digits и параметром max_length = 5. 
Выведите на экран объект в случае его успешного создания. Иначе, выведите сообщение обработанного исключения.

Sample Input:

1 2 3 4 5
Sample Output:

1.0 2.0 3.0 4.0 5.0"""

# digits = list(map(float, input().split()))
digits = [1.0, 2.0, 3.0, 4.0, 5.0]

class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        return super(TupleLimit, cls).__new__(cls)

    def __init__(self, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst, self.max_length = lst, max_length


    def __str__(self):
        return ' '.join(str(i) for i in self.lst)

    def __repr__(self):
        return ' '.join(str(i) for i in self.lst)

try:
    tp = TupleLimit(digits, 5)
    print(tp)
except Exception as e:
    print(e)