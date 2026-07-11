value=eval(input("enter no:"))
sum=0
while value!=0:
    sum=sum+value
    value=eval(input("enter 0 to quit:"))
print("Sum=",sum)