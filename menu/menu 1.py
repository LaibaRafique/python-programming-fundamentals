print("----Menu----")
print("1.Calculator \n2.Area of circle \n3.Factorial \n4.Table")
ch=input("Enter choice::")
print(ch)
if ch=='1':
    ch='y'
    while ch=='y':
        no1=eval(input("Enter no1::"))
        no2=eval(input("Enter no2::"))
        ch=input("Enter choice::")
        if ch=="1" or ch=="+" or ch=="a" or ch=="Addition":
            ans=no1+no2
            print(no1,"+",no2,"=",ans)
        elif ch=="2" or ch=="-" or ch=="s" or ch=="Subtraction":
            ans=no1-no2
            print(no1,"-",no2,"=",ans)
        elif ch=="3" or ch=="*" or ch=="m" or ch=="Multiplication":
            ans=no1*no2
            print(no1,"*",no2,"=",ans)
        elif ch=="4" or ch=="/" or ch=="d" or ch=="Division":
            ans=no1/no2
            print(no1,"/",no2,"=",ans)
        elif ch=="5" or ch=="//" or ch=="f" or ch=="Floor_Division":
            ans=no1//no2
            print(no1,"//",no2,"=",ans)
        elif ch=="6" or ch=="%" or ch=="r" or ch=="Reminder":
            ans=no1%no2
            print(no1,"%",no2,"=",ans)
        elif ch=="7" or ch=="**" or ch=="e" or ch=="Exponent":
            ans=no1**no2
            print(no1,"^",no2,"=",ans)
        else:
            print("Invalid operator")
        ch=input("Press y to continue:")
elif ch=='2':
    radius=eval(input("Enter radius::"))
    PI=3.1416
    while radius!=0:
        area=PI*radius**2
        print("radius=",radius,"\tArea of circle=",area)
        radius=eval(input("Enter radius::"))
elif ch=='3':
    value=eval(input("enter no::"))
    while value!=0:
        fact=1
        for i in range(1,value+1):
            fact=fact*i
        print(value,"!",fact)
        value=eval(input("enter 0 to quit:"))
elif ch=='4':
    ch='yes'
    while ch!='no':
        no=eval(input("enter a no:"))
        for i in range(1,11):
            print(no,"*",i,"=",no*i)
        ch=input("Press any letter to continue:")
else:
    print("Invalid choice")