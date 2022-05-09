def superlist(list_1, list_2):
    k = 0
    list_3 = []
    while k < len(list_1):  # Main condition - lists must have same number of elements
        list_3.append(list_1[k])
        list_3.append(list_2[k])
        k += 1
        continue
    return (list_3)


print(superlist([1, 2, 3], [11, 22, 33]))
