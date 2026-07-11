ch='y'
while ch=='y':
    no=eval(input("enter a no:"))
    for i in range(1,11):
        print(no,"*",i,"=",no*i)
    ch=input("Press y to continue")