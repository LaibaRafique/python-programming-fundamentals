try:
    x=0
    x=eval(input("Enter a number upto 100:"))
    if x>100:
        raise ValueError("greater than 100")
except ValueError as ve:
    print(x,"is out of allowed range")
    print(ve.args)
except:
    print("In default exception handling block")
else:
    print(x,"is within the allowed range")