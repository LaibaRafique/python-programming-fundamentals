ch=0
def calculator():
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

def factorial(no1):
        fact=1
        for i in range(1,no1+1):
            fact=fact*i
        return fact

def table(no):
        for i in range(1,11):
            print(no,"x",i,"=",no*i)

def main():
    print("----Menu----")
    print("1.Calculator \n2.Factorial \n3.Table")
    ch=input("Enter choice::")
    print(ch)
    if ch=='1':
        ch='y'
        while ch=='y':
            calculator()
            ch=input("Press y to continue or n to exit:")
            if ch=='n':
                print("----Menu----")
                print("1.Calculator \n2.Factorial \n3.Table")
                ch=input("Enter choice::")
                print(ch)
    if ch=='2':
        no1=eval(input("enter no:"))
        while no1!=0:
            factorial(no1)
            f=factorial(no1)
            print(no1,"!",f)
            no1=eval(input("enter number or press 0 to quit:"))
            if no1==0:
                print("----Menu----")
                print("1.Calculator \n2.Factorial \n3.Table")
                ch=input("Enter choice::")
                print(ch)
        
    if ch=='3':
        no=eval(input("enter no:"))
        ch='yes'
        while ch!='no':
            table(no)
            ch=input("enter number or press no to exit:")
                
main()
