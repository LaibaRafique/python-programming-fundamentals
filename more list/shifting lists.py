lst=[2,3,4,5,6,7]
def shift(lst):
    temp=lst[0]
    for i in range(1, len(lst)):
        lst[i-1]=lst[i]
    lst[len(lst) - 1]=temp
    print(lst)
shift(lst)

