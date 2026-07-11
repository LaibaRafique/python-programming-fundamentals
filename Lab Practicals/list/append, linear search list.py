no=10
l=[]
for i in range(no):
    x=eval(input("enter number::"))
    l.append(x)
print(l)
def linear_search(l,num):
    for i in range(len(l)):
        if num==l[i]:
            return "element",num,"found at index",i
            break
    else:
        return "element not found in list"
print(linear_search(l,num=7))
    
    