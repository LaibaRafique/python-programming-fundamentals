d={1:"apple",2:"banana",3:"mango"}
l1=list(d.items())
t=4, "cake"
l1[2]=tuple(t)

t1=5, "lll"
l1.insert(3,tuple(t1))
print(l1)