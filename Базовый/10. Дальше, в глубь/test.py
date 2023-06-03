

# еще вариант однонаправленного

# class LinkedList:
#     head = None
#
#     class Node:
#         element = None
#         next_node = None
#
#         def __init__(self, element, next_node = None):
#             self.element = element
#             self. next_node = next_node
#
#     def append(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             return element
#
#         node = self.head
#         while node.next_node:
#             node = node.next_node
#
#         node.next_node = self.Node(element)
#
#     def insert(self, element, index):
#         i = 0
#         node = self.head
#         prev = self.head
#         while i <= index:
#             prev = node
#             node = node.next_node
#             i += 1
#
#         prev.next_node = self.Node(element, next_node=node)
#         return element
#
#     def out(self):
#         node = self.head
#         while node.next_node:
#             print(node.element)
#             node = node.next_node
#         print(node.element)
#
# link_list = LinkedList()
# link_list.append(1)
# link_list.append(2)
# link_list.append(3)
# link_list.insert(10, 1)
# link_list.append(5)
# link_list.out()
import sys



class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj



    def pop(self):
        h = self.top
        if h is None:
            return
        while h and h.next != self.last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None

        return last


    def get_data(self):
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
print(res)

# assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"
