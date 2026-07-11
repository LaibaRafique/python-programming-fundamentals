def GCD(no1,no2):
    if no2==0:
        return no1
    else:
        return GCD(no2,no1%no2)
no1=eval(input("enter no1:"))
no2=eval(input("enter no2:"))
print("GCD=",GCD(no1,no2))     