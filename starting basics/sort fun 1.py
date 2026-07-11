def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k>=0 and lst[k]>currentElement:
            lst[k + 1] = lst[k]
            k -= 1 
        lst[k + 1]=currentElement
    print(lst)
def main():
    lst=[]
    no=eval(input("enter no::"))
    for i in range(no):
        no=eval(input("enter values::"))
        lst.append(no)
    print(lst)
    insertionSort(lst)
main()
