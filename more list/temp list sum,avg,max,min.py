nod=7
l=[]
sum=0

for i in range(nod):
    temp=eval(input("Enter a new number::"))
    l.append(temp)
    sum+=temp
print(l)
avg=sum/nod
print("Average:",avg)
print("Highest temperature:",max(l))
print("Lowest temperature:",min(l))