no=eval(input("enter length of list::"))
l=[]
for i in range(no):
    x=eval(input("enter number::"))
    l.append(x)
t=tuple(l)
print(t)

l1=list(t)
l1.append(9)
l1.remove(7)
l1[5]=1
t1=tuple(l1)

print(t1)
print(t[1:])
print(t[-3])
print(t[::2])