def factorial(no=5):
    fact=1
    for i in range(1,no+1):
        fact*=i
    print(no,"!",fact)

no=eval(input("enter number::"))
factorial(no)