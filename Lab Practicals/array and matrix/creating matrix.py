from numpy import *
r=int(input("enter rows="))
c=int(input("enter coulumn="))
a=zeros((r,c))
#print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        x=int(input("enter elements of matrix:"))
        a[i][j]=x
print(a)