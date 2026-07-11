def type_int(i):
    if i % 2==0:
        return 'even'
    else:
        return 'odd'
i=eval(input("enter no:"))
z=type_int(i)
print(z)