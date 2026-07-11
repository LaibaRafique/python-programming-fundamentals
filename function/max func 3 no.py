def max(no1,no2,no3):
    if no1>no2 and no1>no3:
        print("The greatest number is",no1)
    elif no2>no1 and no2>no3:
        print("The greatest number is",no2)
    else:
        print("The greatest number is",no3)
    return
no1=eval(input("enter no1:"))
no2=eval(input("enter no2:"))
no3=eval(input("enter no3:"))
max(no1,no2,no3)