"""Исключение FileNotFoundError и менеджер контекста (with) для файлов"""

# try:
#     file = open("my_file.txt", encoding="utf=8")
#     try:
#         s = file.readlines()
#         int(s)
#         print(s)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print("Невозможно открыть файл")
# except:
#     print("Ошибка при работе с файлом")

# try:
#     with open("my_file.txt", encoding="utf=8") as file:
#         s = file.readlines()
#         print(s)
# except FileNotFoundError:
#     print("Невозможно открыть файл")
# except:
#     print("Ошибка при работе с файлом")
# finally:
#     print(file.closed)


"""Подвиг 2. Имеется фрагмент программы (см. листинг ниже). 
При его выполнении возникает ошибка FileNotFoundError. 
Запишите конструкцию try / except, чтобы отображалось сообщение 
"File Not Found", если файл не удается открыть."""

# try:
#     f = open("abc.txt")
#     r = f.read(1)
#     f.close()
# except FileNotFoundError:
#     print("File Not Found")

