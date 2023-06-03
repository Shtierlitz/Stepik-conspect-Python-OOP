k = int(input())
if (1 <= k <= 365):
    if k % 7 == 1:
        print("понедельник")
    elif k % 7 == 2:
        print("вторник")
    elif k % 7 == 3:
        print("среда")
    elif k % 7 == 4:
        print("четверг")
    elif k % 7 == 5:
        print("пятница")
    elif k % 7 == 6:
        print("суббота")
    elif k % 7 == 7:
        print("воскресенье")
