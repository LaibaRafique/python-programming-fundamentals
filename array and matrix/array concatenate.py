from numpy import *
x=array(ones(10),int)
y=array(zeros(10),int)
z=array(ones(10)*5,int)
a=concatenate((x,y,z), axis=None)
print(a)