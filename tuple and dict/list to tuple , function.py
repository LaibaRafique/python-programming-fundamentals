l=[]
n=eval(input("enter length:"))
for i in range(n):
    x=eval(input("enter elements:"))
    l.append(x)
print(l)
t=tuple(l)
def operation(t):
    s=sum(t)
    m=max(t)
    n=min(t)
    a=s/len(t)
    return s,m,n,a
def main():
    print(operation(t))
main()