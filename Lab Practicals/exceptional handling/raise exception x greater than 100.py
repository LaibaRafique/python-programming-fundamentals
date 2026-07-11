try:
    x=int(input("Enter a number upto 100:"))
    if x>100:
        raise ValueError("greater than 100")
except ValueError as ve:
    print(x,"is out of allowed range")
    print(ve)
else:
    print(x,"is within the allowed range")