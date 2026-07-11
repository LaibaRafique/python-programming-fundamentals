s=0
l=[]
def printsquare():
    for i in range(0,7+1):
        s=i**2
        l.append(s)
printsquare()
print(l)
sum=0
for i in range(len(l)):
    sum+=l[i]
print("Sum of list:",sum)
    
