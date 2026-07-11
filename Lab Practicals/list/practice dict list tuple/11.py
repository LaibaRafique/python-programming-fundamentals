d={1:"apple",2:"banana",3:"mango"}
l=list(map(list,d.items()))
print(l)
w=7, "koko"
l.insert(3,list(w))
print(l)
del l[1]
print(l)
l[1]=[2, "lolol"]
print(l)
print(l[1][0])
l1=l[0][0],l[1][0],l[2][0]
print(l1)
print(sum(l1))
print(list(l1))