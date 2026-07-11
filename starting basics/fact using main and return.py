def factorial(no1):
    fact=1
    for i in range(1,no1+1):
        fact=fact*i
    return fact
def main():
    no1=eval(input("enter no:"))
    f=factorial(no1)
    print(no1,"!",f)
main()
    