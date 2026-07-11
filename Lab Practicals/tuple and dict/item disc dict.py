disc=0
a={}
n=eval(input("enter number of items="))
for i in range(n):
    k=eval(input("enter name of items="))
    v=eval(input("enter price of items="))
    a.update({k:v})
print(a)
for k,v in a.items():
    print(k,"---->",v)
print("Total=",sum(a.values()))
t=sum(a.values())
if t>=5000:
    disc=0.2*t
    print("Discount=",disc)
elif t>=100 and t<=4999:
    disc=0.1*t
    print("Discount=",disc)
elif t>=0 and t<=99:
    disc=0
    print("Discount=",disc)
else:
    print("No discount")
print("Total with discount=",t-disc)