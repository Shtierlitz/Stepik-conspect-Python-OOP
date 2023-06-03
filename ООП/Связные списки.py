# односвязный список:

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return f"[{self.data}] → {self.next}"
#
# class LinckedList:
#     def __init__(self):
#         self.head = None
#
#     def __str__(self):
#         return str(self.head)
#
#     # метод для подсчета элементов списка
#     def length(self):
#         count = 0
#         temp = self.head
#         while temp:
#             count += 1
#             temp = temp.next
#         return count
#
#
# # пример вывода просто в очереди
# linked_list = LinckedList()
# temp = Node(1)
# linked_list.head = temp
# for i in range(2, 5):
#     temp.next = Node(i)
#     temp=temp.next
# print(linked_list)
# print(linked_list.length())




lst_in = [
    '1. Первые шаги в ООП',
    '1.1 Как правильно проходить этот курс',
    '1.2 Концепция ООП простыми словами',
    '1.3 Классы и объекты. Атрибуты классов и объектов',
    '1.4 Методы классов. Параметр self',
    '1.5 Инициализатор init и финализатор del',
    '1.6 Магический метод new. Пример паттерна Singleton',
    '1.7 Методы класса (classmethod) и статические методы'
]


# class ListObject:
#     def __init__(self, data):
#         self.next_obj = None
#         self.data = data
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# head_obj = ListObject(lst_in[0])    # сохраняем головной элемент
# obj = head_obj
#
# for i in range(1, len(lst_in)):
#     obj_new = ListObject(lst_in[i]) # создаем новый обьект
#     obj.link(obj_new)               # помещаем его же в хвост
#     obj = obj_new                   # промежуточная переменная ссылается на хвост
#     print(obj.data)


# односвязный список с операторами прибавления элементов списка
class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

class Stack:
    def __init__(self):
        self.top = None
        self.end = None

    def push_back(self, obj):
        self.__adder(obj)

    def get_data(self):
        h = self.top
        lst = []
        while h:
            lst.append(h.data)
            h = h.next

        return lst

    def pop_back(self):
        temp = self.top
        if temp is None:
            return
        while temp and temp.next != self.end:
            temp = temp.next
        if temp:
            temp.next = None
        tail = self.end
        self.end = temp
        if self.end is None:
            self.top = None

        return tail

    def __adder(self, obj):
        if not self.__check_node(obj):
            return
        if self.end:
            self.end.next = obj
        obj.prev = self.end
        self.end = obj
        if self.top is None:
            self.top = obj

    def __check_node(self, node):       # Функция не допускающая рекурсию при добавлении одинаковых обьектов
        if not self.top:                # Спасибо (Дернов Иван)
            return True
        f = self.top
        while f:
            if f == node:
                return False
            f = f.next
        return True

    def __add__(self, other):
        sc = other
        if type(sc) == list:
            for i in sc:
                self.__adder(StackObj(i))
            return self
        if type(sc) == StackObj:
            self.__adder(sc)
        if type(sc) not in (StackObj, Stack):
            s = StackObj(sc)
            self.__adder(s)
        return self

    def __iadd__(self, other):
        self.__adder(other)
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if type(other) == list:
            sc = other
            lst = [StackObj(i) for i in sc]
            for i in lst:
                self.__adder(i)
            return self

    def __rmul__(self, other):
        return self.__mul__(other)

# st = Stack()
# st.push_back(StackObj("Давнные 1"))
# st.push_back(StackObj("Давнные 2"))
#
# st.push_back(StackObj("Давнные 3"))
# st.push_back(StackObj("Давнные 4"))
# obj = StackObj("Давнные 5")
# obj2 = StackObj("Давнные 6")
# l = ["ladl", 'asdasd', '123123']
# l + st
# st = st + obj
# st += obj
#
# print(st.get_data())


""""Задача 3.8.7 на gettitem и setitem"""


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None
        self.__indx = None

    @property
    def indx(self):
        return self.__indx

    @indx.setter
    def indx(self, indx):
        self.__indx = indx

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

class Stack:
    def __init__(self):
        self.top = None
        self.__end = None

    def push(self, obj):
        self.__adder(obj)
        h = self.top
        count = 0
        while h:
            if h.indx is None:
                h.indx = count
            count += 1
            h = h.next

    def get(self):
        h = self.top
        lst = []
        while h:
            lst.append(h.data)
            h = h.next
        return lst

    def pop(self):
        temp = self.top
        if temp is None:
            return
        while temp and temp.next != self.__end:
            temp = temp.next
        if temp:
            temp.next = None
        end = self.__end
        self.__end = temp
        if self.__end is None:
            self.top = None

        return end

    def __adder(self, obj):
        """Доп метод который добавляет в конец списка"""
        if not self.__check_node(obj):
            return
        if self.__end:
            self.__end.next = obj
        obj.prev = self.__end
        self.__end = obj
        if self.top is None:
            self.top = obj


    def __check_node(self, node):
        """ Функция не допускающая рекурсию при добавлении одинаковых обьектов,
            Спасибо (Дернов Иван)"""
        if not self.top:                #
            return True
        f = self.top
        while f:
            if f == node:
                return False
            f = f.next
        return True

    def __getitem__(self, item):
        """Все так же как в get"""
        h = self.top
        lst = []
        while h:
            lst.append(h)
            h = h.next
        if not (-len(lst) <= item < len(lst)) or type(item) != int:
            raise IndexError('неверный индекс')
        return lst[item]

    def __get_obj_key(self, key):
        """Ищет нужный индекс в имеющемся списке"""
        h = self.top
        while h:
            if h.indx == key:
                return h
            h = h.next
            if h is None:
                raise IndexError('неверный индекс')

    def __setitem__(self, key, value: StackObj):
        """Просто меняем у обьекта по индексу его значение на значение value.data"""
        obj = self.__get_obj_key(key)
        obj.data = value.data



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError

"""Задача 3.9.8 на __iter__"""

# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#             instance.__dict__[self.name] = value
#
# class StackObj:
#
#     data = Descriptor()
#     next = Descriptor()
#     prev = Descriptor()
#     indx = Descriptor()
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#         self.indx = None
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.tail = None
#
#     def get(self):
#         h = self.top
#         lst = []
#         while h:
#             lst.append(h.data)
#             h = h.next
#         return lst
#
#     def __adder(self, obj):
#         if not self.__check_node(obj):
#             return
#         if self.tail:
#             self.tail.next = obj
#         obj.prev = self.tail
#         self.tail = obj
#         if self.top is None:
#             self.top = obj
#
#     def __check_node(self, node):       # Функция не допускающая рекурсию при добавлении одинаковых обьектов
#         if not self.top:                # Спасибо (Дернов Иван)
#             return True
#         f = self.top
#         while f:
#             if f == node:
#                 return False
#             f = f.next
#         return True
#
#     def push_back(self, obj):
#         self.__adder(obj)
#         self.__indx_recounter()
#
#     def push_front(self, obj):
#         if self.top:
#             obj.next = self.top
#             self.top = obj
#             self.__indx_recounter()
#         if self.top is None:
#             self.__adder(obj)
#             self.__indx_recounter()
#
#     def __indx_recounter(self):
#         """Доп метод для перерасчета индексов"""
#         h = self.top
#         count = 0
#         while h:
#             if h.indx is None:
#                 h.indx = count
#             count += 1
#             h = h.next
#
#     def __getitem__(self, item):
#         """Все так же как в get"""
#         h = self.top
#         lst = []
#         while h:
#             lst.append(h)
#             h = h.next
#         if not (-len(lst) <= item < len(lst)) or type(item) != int:
#             raise IndexError('неверный индекс')
#         return lst[item].data
#
#     def __get_obj_key(self, key):
#         """Ищет нужный индекс в имеющемся списке"""
#         h = self.top
#         while h:
#             if h.indx == key:
#                 return h
#             h = h.next
#             if h is None:
#                 raise IndexError('неверный индекс')
#
#     def __setitem__(self, key, value):
#         """Просто меняем у обьекта по индексу его значение на значение value или value.data"""
#         obj = self.__get_obj_key(key)
#         if type(value) == StackObj:
#             obj.data = value.data
#         else:
#             obj.data = value
#
#     def __len__(self):
#         lst = self.get()
#         return len(lst)
#
#     def __iter__(self):
#         h = self.top
#         lst = []
#         while h:
#             lst.append(h)
#             h = h.next
#         for i in lst:
#             yield i

    def add_obj(self, obj):
        """чтобы бобавить обьект в конец:
            1. проверить есть ли в хвосте что-то. Если есть, то нексту хвоста присвоить новый обьект
            2. в любом случае новому обьекту в prev нужно вставить хвост
            3. в любом случае надо назначить хвосту новый обьект
            4. если головы нету, то назначить ее обьектом"""

        if self.tail:                # если в хвосте что-то есть
            self.tail.set_next(obj)  # то тогда связываем хвост с новым обьектом
        obj.set_prev(self.tail)      # а у обьекта привязываем зад к хвосту
        self.tail = obj              # далее хвост меняется на новый обьект
        if not self.head:            # а голову проверяем. Если ее нет:
            self.head = obj          # то новый обьект кладем в голову


    def remove_obj(self):
        """Чтобы удалить последний обьект:
        1. сперва проверить хвост и если там ничего нет, то ничего не делать
        2. во временную переменную достать зад последнего обьекта (хвоста)
        3. Проверить есть ли там обьект, а то у первого там ничего нету, и если есть установить у его обьекта в нексте None
        4. Текущией обьект хвоста назначить тем что во временной
        5. А если в хвосте ничего нет, то и голову тоже удалить"""
        if self.tail is None:         # Если хвоста нет, то ничего не делаем
            return
        prev = self.tail.get_prev()   # временно помещаем обьект зада хвоста (Предыдущий обьект)
        if prev:                      # и если там не None
            prev.set_next(None)       # делаем у его нехта тоже None (у предыдущего обьекта стираем связь со следущим)
        self.tail = prev              # хвост делаем обрезанным обьектом (тогда пропадает следущий, он же последний)
        if self.tail is None:         # если это самый первый обьект и в хвосте ничего нет
            self.head = None           #то тогда убираем и голову (удаляя вообще все)



    def get_data(self):
        s = []                          # создаем пустой список
        h = self.head                   # назначаем переменную, начинаем с головы
        while h:                        # пока там не пустот
            s.append(h.get_data())      # берем данные из переменной и добавляем в список
            h = h.get_next()            # меняем переменную на некст этого обьекта и дальше все будут идти только нексты
        print(s)

    def __get_obj_indx(self, indx):
        """приватный метод в который передается иднекс
        1. делаем временную переменную и помещаем в нее голову
        2. создаем переменную счетчик с 0
        3. пока голова и счетчик меньше переданного индекса:
        4. переменная головы каждый раз становится переменной.next
        5 счетчик += 1
        6 вернуть временную переменную голову"""
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj_index(self, indx):
        """Тут понадобится дополнительный скрытый метод. Назовем его ind_taker
        1. создаем временную переменную (obj) и помещаем в нее выполненый ind_taker и передаем в него индекс
        2. если obj None
        3. ничего не делаем
        4. создаем 2 переменные и помещаем в них obj.prev и obj.next
        5. если в переменной prev что-то есть:
         6. переменной.next присваеваем переменную obj.next
        7. Тоже самое только наоборот в переменной obj.next
        8. проверяем если голова равна наш obj:
        9. тогда голова становится временной obj.next
        10. Если хвост равено obj:
        11 делаем хвос временной obj.prev
        12 все. Возвращать ничего не надо"""

        obj = self.__get_obj_indx(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p



# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# # lst.remove_obj()
# lst.remove_obj_index(1)
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']


"""чтобы бобавить обьект в конец двусвязного списка:
            1. проверить есть ли в хвосте что-то. Если есть, то нексту хвоста присвоить новый обьект
            2. в любом случае новому обьекту в prev нужно вставить хвост
            3. в любом случае надо назначить хвосту новый обьект
            4. если головы нету, то назначить ее обьектом"""

# если в хвосте что-то есть
# то тогда связываем хвост с новым обьектом
# а у обьекта привязываем зад к хвосту
# далее хвост меняется на новый обьект
# а голову проверяем. Если ее нет:
# то новый обьект кладем в голову


""" удалить последний обьект в односвязном списке"""
# 1. создаем временную для головы
# 2. если в ней ничего нету возвращаем пустоту
# 3. пока есть временная (голова) и в ней есть некст и они не равны хвосту
# 4. временная каждый раз становится временной.некст (это для того чтобы дойти до последнего обьекта)
# 5. (когда дошли до конца) если во временной что-то есть:
# 6. Временной.некст делаем None (вот тут собственно и рубим связь с концом)
# 7. создаем еще одну временную для хвоста
# 8. а сам хвост (не временную хвоста) засовываем в нею временную головы
# 9. если в хвосте нет ничег:
# 10. голову тоже делаем None
# 11. возвращаем временную хвоста


"""Чтобы удалить последний обьект в дувсвязном :
        1. сперва проверить хвост и если там ничего нет, то ничего не делать
        2. во временную переменную достать зад последнего обьекта (хвоста)
        3. Проверить есть ли там обьект, а то у первого там ничего нету, и если есть установить у его обьекта в нексте None
        4. Текущией хвост назначить обьектом кторым является временная
        5. А если в хвосте ничего нет, то и голову тоже удалить"""
# Если хвоста нет, то ничего не делаем
# временно помещаем обьект зада хвоста (Предыдущий обьект)
# и если там не None
# делаем у его нехта тоже None (у предыдущего обьекта стираем связь со следущим)
# хвост делаем обрезанным обьектом (тогда пропадает следущий, он же последний)
# если это самый первый обьект и в хвосте ничего нет
# то тогда убираем и голову (удаляя вообще все)

"""Чтобы вывести данные из списка"""
# создаем пустой список
# назначаем переменную, начинаем с головы
# пока там не пустот
# берем данные из переменной и добавляем в список
# меняем переменную на некст этого обьекта и дальше все будут идти только нексты

"""чтобы удалять по индексу"""

"""Тут понадобится дополнительный скрытый метод. Назовем его ind_taker"""
# 1. создаем временную переменную (obj) и помещаем в нее выполненый ind_taker и передаем в него индекс
# 2. если obj None
# 3. ничего не делаем
# 4. создаем 2 переменные и помещаем в них obj.prev и obj.next
# 5. если в переменной prev что-то есть:
#  6. переменной.next присваеваем переменную obj.next
# 7. если есть в переменной next что-то есть:
# 7.1 переменной.prev присваеваем p
# 8. проверяем если голова равна наш obj:
# 9. тогда голова становится временной obj.next
# 10. Если хвост равено obj:
# 11 делаем хвос временной obj.prev
# 12 все. Возвращать ничего не надо

"""скрытый метод для удалятора"""
"""приватный метод в который передается иднекс"""
# 1. делаем временную переменную и помещаем в нее голову
# 2. создаем переменную счетчик с 0
# 3. пока в голове что-то есть и счетчик меньше переданного индекса:
# 4. переменная головы каждый раз становится переменной.next
# 5 счетчик += 1
# 6 вернуть временную переменную голову