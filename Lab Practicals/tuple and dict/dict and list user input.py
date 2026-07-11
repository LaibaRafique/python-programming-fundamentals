a={}
n=eval(input("enter number of people="))
for i in range(n):
    k=eval(input("enter name of person="))
    o=eval(input("enter number of hobbies="))
    b=[]
    for i in range(o):
        v=eval(input("enter hobbies="))
        b.append(v)
    a.update({k:b})
print(a)
for k,v in a.items():
    print("\n",k,"=",end=" ")
    for i in v:
        print(i,end=",")