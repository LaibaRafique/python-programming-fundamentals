l1=['a','b','c']
l2=[1,2,3,4]
l3=l1+l2
print(l3)
l1=['a','b','c']
l2=[1,2,3,4]
for x in l2:
    l1.append(x)
print(l1)
l1=['a','b','c']
l2=[1,2,3,4]
l1.extend(l2)
print(l1)