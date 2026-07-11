no=eval(input("enter length of list::"))
l=[]
for i in range(no):
    x=eval(input("enter number::"))
    l.append(x)
t=tuple(l)
print(t)

l1=list(t)
l1.append(9)
t1=tuple(l1)
l2=list(t)
l2.remove(7)
t2=tuple(l2)
l3=list(t)
l3[5]=1
t3=tuple(l3)

print(t1)
print(t2)
print(t3)
print(t[1:])
print(t[-3])
print(t[::2])