print("1.list sum,max,min,avg","\n2.list element searching","\n3.list sort","\n4.list reverse","\n5.tuple functions")
print("6.tuple element search","\n7.dictionary functions")
from list import *
ch=eval(input("enter choice:"))
if ch==1:
    no1=eval(input("enter length of list::"))
    l1=[]
    for i in range(no1):
        x=eval(input("enter number::"))
        l1.append(x)
    print(l1)
    l,s,m,n,a,o=functions(l1)
    print("length =",l)
    print("sum is=",s)
    print("max is=",m)
    print("min is=",n)
    print("avg is=",a)
    print("Slicing =",o)
    ch=eval(input("enter choice:"))
if ch==2:
    no2=eval(input("enter length of list::"))
    l2=[]
    for i in range(no2):
        x=eval(input("enter number::"))
        l2.append(x)
    print(l2)
    ele=eval(input("enter element for search::"))
    e,c,l1=linear_search(l2,ele)
    print("Element=",e,"\nCount=",c,"\nList of indexes on which element is found=",l1)
    ch=eval(input("enter choice:"))
if ch==3:
    no3=eval(input("enter length of list::"))
    l3=[]
    for i in range(no3):
        x=eval(input("enter number::"))
        l3.append(x)
    print(l3)
    print("sorted list = ",sort(l3))
    ch=eval(input("enter choice:"))
if ch==4:
    l4=[]
    no4=eval(input("enter length::"))
    for i in range(no4):
        z=eval(input("enter values::"))
        l4.append(z)
    print(l4)
    r=reverse(l4)
    print("reverse list=",r)
    ch=eval(input("enter choice:"))
if ch==5:
    no5=eval(input("enter length of tuple::"))
    l5=[]
    for i in range(no5):
        x=eval(input("enter number::"))
        l5.append(x)
    t=tuple(l5)
    print(t)
    l,s,m,n,a,o=functions(t)
    print("length =",l)
    print("sum is=",s)
    print("max is=",m)
    print("min is=",n)
    print("avg is=",a)
    print("Slicing =",o)
    ch=eval(input("enter choice:"))
if ch==6:
    no6=eval(input("enter length of tuple::"))
    l6=[]
    for i in range(no6):
        x=eval(input("enter number::"))
        l6.append(x)
    t2=tuple(l6)
    print(t2)
    ele=eval(input("enter element for search::"))
    e,c,l1=linear_search(t2,ele)
    print("Element=",e,"\nCount=",c,"\nList of indexes on which element is found=",l1)
    ch=eval(input("enter choice:"))
from dict import *
if ch==7:
    d={}
    n=eval(input("enter length of dict ="))
    for i in range(n):
        k=eval(input("enter keys ="))
        v=eval(input("enter values ="))
        d.update({k:v})
    print(d)
    functions_dict(d)
    print("The end")
   