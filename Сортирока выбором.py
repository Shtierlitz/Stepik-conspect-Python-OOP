# Сортирока выбором (медленная)

# Ищем индекс наименьшего элемента
def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# сортируем по наименьшему элементу
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


lst = [5, 3, 6, 2, 10]
print(selectionSort(lst))

# Шпаргалка

# Память компьютера напоминает огромный шкаф с ящиками.

# Если вам потребуется сохранить набор элементов, воспользуйтесь массивом или списком.

# В массиве все элементы хранятся в памяти рядом друг с другом.

# В списке элементы распределяются в произвольных местах памяти, при
# этом в одном элементе хранится адрес следующего элемента.

# Массивы обеспечивают быстрое чтение.

# Списки обеспечивают быструю вставку и выполнение.

# Все элементы массива должны быть однотипными (только целые числа,
# только вещественные числа и т. д.).