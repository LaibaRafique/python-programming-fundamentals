def linear_search(l,ele1,ele2):
    for i in range(len(l)):
        if ele1==l[i]:
            x="Element",ele1,"found at index",i
            break
    else:
        x="Element 1 not found"
    for j in range(len(l)):
        if ele2==l[j]:
            y="Element",ele2,"found at index",j
            break
    else:
        y="Element 2 not found"
    return x,y
no=eval(input("enter length of list::"))
l=[]
for i in range(no):
    x=eval(input("enter number::"))
    l.append(x)
t=tuple(l)
print(t)
ele1=eval(input("enter element for search::"))
ele2=eval(input("enter element for search::"))
print(linear_search(t,ele1,ele2))