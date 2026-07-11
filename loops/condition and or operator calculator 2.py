ch=input("Enter choice::")
if ch=="1" or ch=="+" or ch=="a" or ch=="Addition":
    no1,no2=eval(input("Enter no1,no2::"))
    ans=no1+no2
    print(no1,"+",no2,"=",ans)
elif ch=="2" or ch=="-" or ch=="s" or ch=="Subtraction":
    no1,no2=eval(input("Enter no1,no2::"))
    ans=no1-no2
    print(no1,"-",no2,"=",ans)
elif ch=="3" or ch=="*" or ch=="m" or ch=="Multiplication":
    no1,no2=eval(input("Enter no1,no2::"))
    ans=no1*no2
    print(no1,"*",no2,"=",ans)
elif ch=="4" or ch=="/" or ch=="d" or ch=="Division":
    no1,no2=eval(input("Enter no1,no2::"))
    ans=no1/no2
    print(no1,"/",no2,"=",ans)
elif ch=="5" or ch=="//" or ch=="f" or ch=="Floor_Division":
    no1,no2=eval(input("Enter no1,no2::"))
    ans=no1//no2
    print(no1,"//",no2,"=",ans)
elif ch=="6" or ch=="%" or ch=="r" or ch=="Reminder":
    no1,no2=eval(input("Enter no1,no2::"))
    ans=no1%no2
    print(no1,"%",no2,"=",ans)
elif ch=="7" or ch=="**" or ch=="e" or ch=="Exponent":
    no1,no2=eval(input("Enter no1,no2::"))
    ans=no1**no2
    print(no1,"^",no2,"=",ans)

