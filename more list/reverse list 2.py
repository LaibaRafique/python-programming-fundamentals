def reverse(lst):
    result = []
    for element in lst:
        result.insert(0, element)
    return result
lst=[1, 2, 3, 4, 5, 6]
lst2=reverse(lst)
print(lst2)