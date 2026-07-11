odd=0
even=0
o=0
e=0
i=0
no=1000
while i<=no:
    if i%2==0:
        even+=i
        i+=1
        e=e+1
    else:
        odd+=i
        i+=1
        o=o+1
print("Even numbers",e,"Sum of even numbers=",even)
print("Odd numbers",o,"Sum of odd numbers=",odd)