# Бинарный Посиск числа. (Не работает со строками
lst = [i for i in range(1, 101)]

def binary_search(lst, item):
    low = 0                       # Минимальная разделительная переменная
    high = len(lst) - 1           # Максмимальная
    while low <= high :
        mid = (low + high)
        guess = lst[int(mid)]
        if guess == item:
            return mid
        if guess > item:        # Если названное число было слишком мало,
            high = mid - 1      # то переменная low обновляется соответственно
    else:
        low = mid + 1
    return None


print(binary_search(lst, 33))