sum=0
fact=1
for i in range(1,8):
    for j in range(i,i+1):
        fact=fact*j
        sum+=j/fact
    print(i,"!=",fact)
print(sum)