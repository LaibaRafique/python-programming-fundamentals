def functions(l1):
    l=len(l1)
    s=sum(l1)
    m=max(l1)
    n=min(l1)
    a=s/l
    x=eval(input("enter start value for slicing:"))
    y=eval(input("enter end value for slicing:"))
    s=eval(input("enter step value for slicing:"))
    o=l1[x:y:s]
    return l,s,m,n,a,o

def linear_search(l,ele):
    l1=[]
    count=0
    for i in range(len(l)):
        if ele==l[i]:
            print("Element",ele,"found at index",i)
            l1.append(i)
            count+=1
    return ele,count,l1

def sort(l):
    for i in range(0,len(l)):
        for j in range(0,len(l)-1):
            if l[j]>l[j+1]:
                c=l[j]
                l[j]=l[j+1]
                l[j+1]=c
    return l

def reverse(l):
    l1=[]
    for i in range(len(l)-1,-1,-1):
        l1.append(l[i])
    return l1