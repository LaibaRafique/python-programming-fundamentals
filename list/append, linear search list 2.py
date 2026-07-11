def linear_search(l,ele):
    for i in range(len(l)):
        if ele==l[i]:
            return "Element",ele,"found at index",i
            break
    else:
        return "Not found"
no=eval(input("enter length of list::"))
l=[]
for i in range(no):
    x=eval(input("enter number::"))
    l.append(x)
print(l)
ele=eval(input("enter element for search::"))
print(linear_search(l,ele))