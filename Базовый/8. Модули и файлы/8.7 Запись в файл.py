"""Запись данных в файл в текстовом и бинарном режимах"""
import pickle
# try:
#     with open("my_file.txt", "a+") as file: # w = на запись (удаляет прежднее содержимое) # a = добавить, а+ и читать и добавлять
#         file.seek(0)
#         file.writelines(["yo\n", "asshole\n"])  # записывает сразу несколько строк
#         s = file.readlines()
#         print(s)
#         file.write("Hello4\n")
#
# except:
#     print("Ошибка при работе с файлом")

#Бинарный режим
# books = [
#     ("Евгений Онегин", "Пушкин А.С.", 200),
#     ("Муму", "Тургенев И.С.", 250),
#     ("Мастер и Маргарита", "Булгаков М.А.", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# ]
# # file = open("out.bin", "wb")  # wb = запись в файл бинарным режимом
# # pickle.dump(books, file)
# # file.close()
#
# file = open("out.bin", "rb")    # rb = чтение в бинарном режиме
# bs = pickle.load(file)
# print(bs)

book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
book2 = ["Муму", "Тургенев И.С.", 250]
book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
book4 = ["Мертвые души", "Гоголь Н.В.", 190]

try:
    with open("out.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
        # pickle.dump(book1, file)
        # pickle.dump(book2, file)
        # pickle.dump(book3, file)
        # pickle.dump(book4, file)
except:
    print("Ошибка при работе с файлом")

print(b1, b2, b3, b4, sep="\n")
