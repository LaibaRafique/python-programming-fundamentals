def add(no1,no2):
    ans=no1+no2
    return ans
def add(no3,no4):
    ans=no3+no4
    return ans
def mul(no1,no2):
    ans=no1*no2
    print(no1,"*",no2,"=",ans)
no1=eval(input("enter no1::"))
no2=eval(input("enter no2::"))
no3=eval(input("enter no3::"))
no4=eval(input("enter no4::"))
mul(add(no1,no2),add(no3,no4))