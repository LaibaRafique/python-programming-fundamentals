no=eval(input("Enter number for factorial="))
fact=1
for i in range(1,no+1):
    fact*=i
print(no,"!=",fact)