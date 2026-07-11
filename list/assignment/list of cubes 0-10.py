l=[]
no=10
for i in range(no+1):
    y=i*i*i # y=i**3
    l.append(y)
print(l)
for j in range(len(l)):
    print(j,"=",l[j])
