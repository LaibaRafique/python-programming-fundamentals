def exponent(no,power):
    ans=no**power
    return ans

def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact*=i
    print(no,"!",fact)

no=eval(input("enter number::"))
power=eval(input("enter power::"))
factorial(exponent(no,power))