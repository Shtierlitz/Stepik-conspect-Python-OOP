from datetime import datetime
import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper


start_time = datetime.now()

# тут что-то происходит

print(shop_items)
print(datetime.now() - start_time)

