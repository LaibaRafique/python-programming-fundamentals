def search(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                return "list 1 and list 2 are same or have atleast 1 member in common."
                break
    else:
        return "list 1 and list 2 are not same."
no=eval(input("enter length of list::"))
l1=[]
for i in range(no):
    x=eval(input("enter number::"))
    l1.append(x)
print(l1)
no=eval(input("enter length of list::"))
l2=[]
for i in range(no):
    y=eval(input("enter number::"))
    l2.append(y)
print(l2)
print(search(l1,l2))