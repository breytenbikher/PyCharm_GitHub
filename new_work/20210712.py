list_1 = [2, 2, 2, 3, 7, 5, 5]
list_2 = [2, 2, 3, 5, 5, 19]
for i in list_1[:]:
    if i in list_2:
        list_2.remove(i)
        list_1.remove(i)
print(list_1, '\n', list_2)
