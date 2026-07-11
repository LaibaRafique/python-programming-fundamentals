sum1=0
sum2=0
for i in range(0,1000+1):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
print("Sum of even numbers=",sum1)
print("Sum of odd numbers=",sum2)