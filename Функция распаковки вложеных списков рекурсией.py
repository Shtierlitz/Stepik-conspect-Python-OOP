li = [[[]]]
def flatten(l):
    if len(l) == 1:
            if type(l[0]) == list:
                    result = flatten(l[0])
            else:
                    result = l
    elif type(l[0]) == list:
            result = flatten(l[0]) + flatten(l[1:])
    else:
            result = [l[0]] + flatten(l[1:])
    return result

# print(flatten(li))



# версия
def get_line_list(d,a=[]):
    for i in d:
        if type(i) != list:
            a.append(i)
        elif type(i) == list:
            get_line_list(i)
    return a

lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
lst = []
for i in lst_in:
    lst.append(i.split())
print(get_line_list(lst))