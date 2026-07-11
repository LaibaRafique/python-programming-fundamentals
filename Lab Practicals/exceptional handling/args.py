def add(no1,no2):
    try:
        if (no1 < 0 or no2 < 0) or (no1 < 0 and no2 < 0):
            raise TypeError("not possible")
    except TypeError as te:
        print(te.args)
    except:
        print("In except block (add)")
    else:
        print(no1,"+",no2,"=",no1+no2)
no1=eval(input("Enter number 1:"))
no2=eval(input("Enter number 2:"))
add(no1,no2)