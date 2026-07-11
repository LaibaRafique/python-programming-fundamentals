odd=0
even=0
o=0
e=0
no=1000
for i in range(0,no+1):
    if i%2==0:
        even+=i
        e=e+1
    else:
        odd+=i
        o=o+1
print("Even numbers",e,"Sum of even numbers=",even)
print("Odd numbers",o,"Sum of odd numbers=",odd)