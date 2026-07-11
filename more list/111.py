l=[i for i in range(100)]
print(l)
print()

l=[]
for i in range(100):
    if i%7==0:
        l.append(i)
print(l)

l=[i for i in range(100) if i%7==0]
print(l)