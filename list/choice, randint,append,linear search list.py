ch='y'
while ch=='y':
    ch1=eval(input("enter choice::"))
    if ch1==1:
        import random
        no=random.randint(1,10)
        l=[]
        for i in range(no):
            x=random.randint(0,100)
            l.append(x)
        print(l)
    elif ch1==2:
        no=eval(input("enter length of list::"))
        l=[]
        for i in range(no):
            x=eval(input("enter number::"))
            l.append(x)
        print(l)
    def linear_search(l,ele):
        for i in range(len(l)):
            if ele==l[i]:
                return "Element",ele,"found at index",i
                break
        else:
            return "Not found"
    ele=eval(input("enter element for search::"))
    print(linear_search(l,ele))
    ch=input("press y to continue::")