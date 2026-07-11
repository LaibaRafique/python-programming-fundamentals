l=[45,-2,7.8,0,9]
max=l[0]
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
print("Maximum value=",max)

min=l[0]
for i in range(len(l)):
    if l[i]<min:
        min=l[i]
print("Minimum value=",min)