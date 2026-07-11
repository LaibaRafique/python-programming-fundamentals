w=eval(input("enter weight in pounds:"))
h=eval(input("enter height in inches:"))
weight=w*0.45359237
height=h*0.0254
BMI=weight/(height**2)
print("BMI=",BMI)