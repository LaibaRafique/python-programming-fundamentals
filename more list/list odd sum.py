no=10
l=[]
sum=0
for i in range(no):
    value=eval(input("Enter values::"))
    l.append(value)
print(l)
for i in range(1,len(l),2):
    sum+=l[i]
print("Sum of odd indexes:",sum)