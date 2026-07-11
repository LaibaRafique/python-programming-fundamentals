from numpy import *
r=eval(input("Enter rows:"))
c=eval(input("Enter columns:"))
a=ones((r,c))
x =  arange(2, 11).reshape(r,c)
print(x)