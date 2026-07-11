l=[]
ch='y'
while ch=='y' or ch=='Y':
    no=eval(input("enter number::"))
    l.append(no)
    ch=input("press y to continue:")
print(l)