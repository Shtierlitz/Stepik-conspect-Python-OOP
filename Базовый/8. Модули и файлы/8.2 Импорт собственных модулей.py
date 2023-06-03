"""Импорт собственных модулей"""

import my_module
import pprint
import importlib
importlib.reload((my_module)) # повторно производит импорт

# pprint.pprint(dir(my_module))
# a = my_module.math.floor(-5.6)
# print(a)

