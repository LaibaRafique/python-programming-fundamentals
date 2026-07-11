def add(no1,no2):
    try:
        if (no1 < 0 or no2 < 0) or (no1 < 0 and no2 < 0):
            raise ValueError
    except ValueError:
        print("Value Error in add function")
    except:
        print("In except block (add)")
    else:
        print(no1,"+",no2,"=",no1+no2)
        
def sub(no1,no2):
    try:
        if (no1 < 0 or no2 < 0) or (no2 > no1):
            raise ValueError
    except ValueError:
        print("Value Error in sub function")
    except:
        print("In except block (sub)")
    else:
        print(no1,"-",no2,"=",no1-no2)
        
def mul(no1,no2):
    try:
        if (no1 < 0 or no2 < 0) or (no1 < 0 and no2 < 0):
            raise ValueError
    except ValueError:
        print("Value Error in mul function")
    except:
        print("In except block (mul)")
    else:
        print(no1,"x",no2,"=",no1*no2)
        
def div(no1,no2):
    try:
        if (no1 < 0 or no2 < 0):
            raise ValueError
    except ValueError:
        print("Value Error in div function")
    except:
        print("In except block (div)")
    else:
        print(no1,"/",no2,"=",no1/no2)
print("1-Addition \n2-Subtraction \n3-Multiplication \n4-Division")
ch='y'
while ch=='y':
    no1=eval(input("Enter number 1:"))
    no2=eval(input("Enter number 2:"))
    ch1=eval(input("Enter operation:"))
    if ch1==1 or ch=="Addition" or ch=="+":
        add(no1,no2)
    elif ch1==2 or ch=="Subtraction" or ch=="-":
        sub(no1,no2)
    elif ch1==3 or ch=="Multiplication" or ch=="*":
        mul(no1,no2)
    elif ch1==4 or ch=="Division" or ch=="/":
        div(no1,no2)
    ch=input("Enter choice:")
