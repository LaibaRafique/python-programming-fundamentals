from numpy import *
a=array([[1,2,3],[4,5,6]])
print(a)
print(a[0])
print(a[0][1])
print()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    print()
a=zeros((1,2),dtype=int)
print(a)
r=int(input("enter rows="))
c=int(input("enter coulumn="))
a=zeros((r,c))
print(a)