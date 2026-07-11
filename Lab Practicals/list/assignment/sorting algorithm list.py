no=eval(input("enter length of list::"))
l=[]
for i in range(no):
    x=eval(input("enter number::"))
    l.append(x)
print(l)
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[j]>l[j+1]:
            c=l[j]
            l[j]=l[j+1]
            l[j+1]=c
print("sorted list = ",l)