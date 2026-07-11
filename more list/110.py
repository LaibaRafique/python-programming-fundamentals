def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i 
    return -1
lst = [1, 4, 4, 2, 5, -3, 6, 2]
print(linearSearch(lst, 4))
print(linearSearch(lst, -4))
print(linearSearch(lst, -3))
