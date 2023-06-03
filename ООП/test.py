# Односвязный спискок урок ООП 1.5

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
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(len(lst_in)):
#     new_obj = ListObject(lst_in[i])
#     obj.link(new_obj)
#     obj = new_obj
#     print(obj.data)


# class ObjList:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#         self.__prev = None
#
#     def set_next(self, obj):
#         self.__next = obj
#
#     def set_prev(self, obj):
#         self.__prev = obj
#
#     def get_next(self):
#         return self.__next
#
#     def get_prev(self):
#         return self.__prev
#
#     def set_data(self, data):
#         self.__data = data
#
#     def get_data(self):
#         return self.__data
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if self.tail:
#             self.tail.set_next(obj)
#
#         obj.set_prev(self.tail)
#         self.tail = obj
#         if not self.head:
#             self.head = obj
#
#     def get_data(self):
#         h = self.head
#         l = []
#         while h:
#             l.append(h.get_data())
#             h = h.get_next()
#         return l
#
#     def remove_obj(self):
#         if self.tail is None:
#             return
#         prev = self.tail.get_prev()
#         if prev:
#             prev.set_next(None)
#         self.tail = prev
#         if self.tail is None:
#             self.head = None

# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# lst.remove_obj()
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
# print(res)

class Descriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class ObjList:
    data = Descriptor()
    next = Descriptor()
    prev = Descriptor()

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.next = obj
        obj.prev = self.tail
        self.tail = obj
        if self.head is None:
            self.head = obj

    def get_obj(self):
        h = self.head
        l = []
        while h:
            l.append(h.data)
            h = h.next
        return l

    def __index_getter(self, indx):
        counter = 0
        h = self.head
        while h and counter < indx:
            counter += 1
            h = h.next
        return h

    def remove_obj(self, indx):
        obj = self.__index_getter(indx)
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

    def __len__(self):
        h = self.head
        l = []
        while h:
            l.append(h.data)
            h = h.next
        return len(l)

    def __call__(self, indx, *args, **kwargs):
        return self.__index_getter(indx).data



# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# print(linked_lst.get_obj())
# linked_lst.remove_obj(2)
# print(linked_lst.get_obj())
# linked_lst.add_obj(ObjList("Python ООП"))
# print(linked_lst.get_obj())
# n = len(linked_lst)  # n = 3
# print(n)
# s = linked_lst(1) # s = Balakirev
# print(s)

import moviepy
