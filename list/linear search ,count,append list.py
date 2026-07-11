def linear_search(l,ele):
    l1=[]
    count=0
    for i in range(len(l)):
        if ele==l[i]:
            print("Element",ele,"found at index",i)
            l1.append(i)
            count+=1
    return ele,count,l1
no=eval(input("enter length of list::"))
l=[]
for i in range(no):
    x=eval(input("enter number::"))
    l.append(x)
print(l)
ele=eval(input("enter element for search::"))
e,c,l1=linear_search(l,ele)
print("Element=",e,"\nCount=",c,"\nList of indexes on which element is found=",l1)