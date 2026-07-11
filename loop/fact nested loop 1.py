value=eval(input("enter no::"))
while value!=0:
    fact=1
    for i in range(1,value+1):
        fact=fact*i
    print(value,"!",fact)
    value=eval(input("enter 0 to quit:"))
        
    