d={}
n=eval(input("enter length:"))
for i in range(n):
    k=eval(input("enter keys:"))
    v=eval(input("enter values:"))
    d.update({k:v})
print(d)
def operation(d):
    s=sum(d.values())
    m=max(d.values())
    n=min(d.values())
    a=s/len(d.values())
    return s,m,n,a
def main():
    s,m,n,a=operation(d)
    print("sum is=",s)
    print("max is=",m)
    print("min is=",n)
    print("avg is=",a)
main()