# month, day = map(int, input().split())
#
# big = [1, 3, 5, 7, 8, 10, 12]
# smal = [4, 6, 9, 11]
# d_l, d_r, m_l, m_r = 0, 0, 0, 0
# if month == 2:
#     m_l = month
#     m_r = month
#
#     if day == 28:
#         d_l = day - 1
#         d_r = 1
#         m_r = m_r + 1
#     elif day == 1:
#         d_l = 31
#         d_r = day + 1
#         m_l = month - 1
#         if month == 3:
#             d_l = 28
#     elif day > 28:
#         d_l = day
#         d_r = 1
#         m_r = m_r + 1
#     else:
#         d_l = day - 1
#         d_r = day + 1
# elif month == 8 and day == 1:
#     d_l = 31
#     d_r = day + 1
#     m_l = month - 1
#     m_r = month
# elif month in big:
#     m_l = month
#     m_r = month
#     if day == 31:
#         d_r = 1
#         d_l = day - 1
#         m_r = m_r + 1
#
#     elif day == 1:
#         d_l = 30
#         d_r = day + 1
#         m_l = month - 1
#         if month == 3:
#             d_l = 28
#     elif month == 8 and day == 31:
#         d_l = 30
#         d_r = day + 1
#         m_l = month - 1
#         m_r = month
#     else:
#         d_l = day - 1
#         d_r = day + 1
# elif month in smal:
#     m_l = month
#     m_r = month
#     if day == 30:
#         d_l = day - 1
#         d_r = 1
#         m_r = m_r + 1
#     elif day == 1:
#         d_l = 31
#         d_r = day + 1
#         m_l = m_l - 1
#     else:
#         d_l = day - 1
#         d_r = day + 1
#
# if month in big and day > 31:
#     raise ValueError("Вводить надо только даты месяцев")
# elif day < 1:
#     raise ValueError("Вводить надо только даты месяцев")
# elif month in smal and day > 30:
#     raise ValueError("Вводить надо только даты месяцев")
# elif month == 2 and day > 28:
#     raise ValueError("Этот год не высокосный")
# elif month == 12 and day == 31:
#     raise ValueError("По условиям задачи этот день не используется")
# elif month == 1 and day == 1:
#     raise ValueError("По условиям задачи этот день не используется")
#
# if month == 2:
#     if day == 1:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day < 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
#     elif day == 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day == 10:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day >= 28:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day > 10 and day < 28:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month <= 8:
#     if day == 1:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day < 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
#     elif day == 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day == 10:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     elif month in big and day == 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     elif month in big and day == 31:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif month in smal and day >= 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month == 9:
#     if day == 1:
#         print(f"0{m_l}.{d_l} 0{m_r}.0{d_r}")
#     elif day < 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
#     elif day == 9:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day == 10:
#         print(f"0{m_l}.0{d_l} 0{m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"0{m_l}.{d_l} 0{m_r}.{d_r}")
#     elif day >= 30:
#         print(f"0{m_l}.{d_l} {m_r}.0{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month == 10:
#     if day == 1:
#         print(f"0{m_l}.{d_l} {m_r}.0{d_r}")
#     elif day < 9:
#         print(f"{m_l}.0{d_l} {m_r}.0{d_r}")
#     elif day == 9:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day == 10:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 31:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     else:
#         print(f"0{m_l}.0{d_l} 0{m_r}.0{d_r}")
# elif month > 10:
#     if day == 1:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     elif day < 9:
#         print(f"{m_l}.0{d_l} {m_r}.0{d_r}")
#     elif day == 9:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day == 10:
#         print(f"{m_l}.0{d_l} {m_r}.{d_r}")
#     elif day > 10 and day < 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 30:
#         print(f"{m_l}.{d_l} {m_r}.{d_r}")
#     elif month in big and day == 31:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     elif month in smal and day >= 30:
#         print(f"{m_l}.{d_l} {m_r}.0{d_r}")
#     else:
#         print(f"{m_l}.0{d_l} {m_r}.0{d_r}")
#
#
# # else:
# #     print(f"{m_l:02}.{d_l:02} {m_r:02}.{d_r:02}")
#
# # near_date(8, 1)
# # near_date(8, 2)
# # near_date(8, 3)
# # near_date(8, 4)
# # near_date(8, 5)
# # near_date(8, 6)
# # near_date(8, 7)
# # near_date(8, 8)
# # near_date(8, 9)
# # near_date(8, 10)
# # near_date(8, 11)
# # near_date(8, 12)
# # near_date(8, 13)
# # near_date(8, 14)
# # near_date(8, 15)
# # near_date(8, 16)
# # near_date(8, 17)
# # near_date(8, 18)
# # near_date(8, 19)
# # near_date(8, 20)
# # near_date(8, 21)
# # near_date(8, 22)
# # near_date(8, 23)
# # near_date(8, 24)
# # near_date(8, 25)
# # near_date(8, 26)
# # near_date(8, 27)
# # near_date(8, 28)
# # near_date(8, 29)
# # near_date(8, 30)
# # near_date(8, 31)
#










st = "6.00000"
num = float(st)
print("{:.4f}".format(num))



