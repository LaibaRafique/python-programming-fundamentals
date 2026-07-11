try:
    a=int(input("enter a positive integer:"))
    if a<=0:
        raise ValueError (a,"is not a positive number")
    else:
        print(a,"is a positive number")
except ValueError as ve:
    print(ve)