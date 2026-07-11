import math
v,a=eval(input("enter speed in m/s,acceleration in m/s^2:"))
l=(math.pow(v,2.0))/(2*a)
print("Minimum runway length=",l,"meters")