from numpy import *
r=int(input("Enter rows:"))
c=int(input("Enter columns:"))
a=ones((r,c))

n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        x=int(input("Enter elements of matrix::"))
        a[i][j]=x
print(a)