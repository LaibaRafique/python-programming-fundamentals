def add(no1,no2):
    ans=no1+no2
    return ans

def mul(no1,no2):
    ans=no1*no2
    print(no1,"*",no2,"=",ans)

no1=eval(input("enter no1::"))
no2=eval(input("enter no2::"))
mul(add(no1,no2),add(no1,no2))