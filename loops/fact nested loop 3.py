sum=1
fact=1
for i in range(1,11):
    for j in range(i,i+1):
        fact=fact*j
        sum+=1/fact
    print(i,"!=",fact)
print(sum)