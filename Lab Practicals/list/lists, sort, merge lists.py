import random
no=random.randint(1,10)
l1=[]
for i in range(no):
    x=random.randint(0,100)
    l1.append(x)
print(l1)
for i in range(0,len(l1)):
    for j in range(0,len(l1)-1):
        if l1[j]>l1[j+1]:
            c=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=c
print(l1)
no=random.randint(1,10)
l2=[]
for i in range(no):
    y=random.randint(0,100)
    l2.append(y)
print(l2)
for i in range(0,len(l2)):
    for j in range(0,len(l2)-1):
        if l2[j]>l2[j+1]:
            c=l2[j]
            l2[j]=l2[j+1]
            l2[j+1]=c
print(l2)
def merge(l1,l2):
    for i in l2:
        l1.append(i)
    return l1
print(merge(l1,l2))
