def add(no1,no2):
    ans=no1+no2
    return ans
def main():
    no1=eval(input("enter no1:"))
    no2=eval(input("enter no2:"))
    a=add(no1,no2)
    print(no1,"+",no2,"=",a)
main()

def multiply(no1,no2):
    ans=no1*no2
    return ans
def main():
    no1=eval(input("enter no1:"))
    no2=eval(input("enter no2:"))
    m=multiply(no1,no2)
    print(no1,"*",no2,"=",m)
main()

def divide(no1,no2):
    ans=no1/no2
    return ans
def main():
    no1=eval(input("enter no1:"))
    no2=eval(input("enter no2:"))
    d=divide(no1,no2)
    print(no1,"/",no2,"=",d)
main()
    
def minus(no1,no2):
    ans=no1-no2
    return ans
def main():
    no1=eval(input("enter no1:"))
    no2=eval(input("enter no2:"))
    m=minus(no1,no2)
    print(no1,"-",no2,"=",m)
main()    