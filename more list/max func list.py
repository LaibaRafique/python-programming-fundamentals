def max(l):
    m=l[0]
    for i in range(len(l)):
        if l[i]>m:
            m=l[i]
    print("Maximum value=",m)     
def main():
    l=[]
    no=eval(input("enter no::"))
    for i in range(no):
        no=eval(input("enter values::"))
        l.append(no)
    print(l)
    max(l)
main()