a={}
n=eval(input("enter length="))
for i in range(n):
    k=eval(input("enter key="))
    v=eval(input("enter values="))
    a.update({k:v})
print(a)
for k,v in a.items():
    print(k,"---->",v)
print("Sum=",sum(a.values()))