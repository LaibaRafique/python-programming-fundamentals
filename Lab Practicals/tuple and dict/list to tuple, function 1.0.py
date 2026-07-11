l=[]
n=eval(input("enter length:"))
for i in range(n):
    x=eval(input("enter elements:"))
    l.append(x)
print(l)
t=tuple(l)
def operation(t):
    return sum(t),max(t),min(t),sum(t)/len(t)
def main():
    print(operation(t))
main()