d={1:"apple",2:"banana",3:"mango"}
l=list(map(list,d.items()))
print(l)

d1={1:"apple",2:"banana",3:"mango"}
l1=list(map(tuple,d1.items()))
print(l1)
del l[2]
print(l)
l1[1]=2, "lolol"
print(l1)
print(l1[1][0])
l2=l1[0][0],l1[1][0],l1[2][0]
print(l2)
print(sum(l2))
print(list(l2))