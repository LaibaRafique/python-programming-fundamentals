def Interest(cost, month, rate):
    try:
        if rate > 100:
            raise ValueError("Enter a number upto 100")
    except ValueError as ve:
        print(rate,"is greater than 100")
        print(ve)
    except:
        print("In default exception handling block")
    else:
        interest1 = (cost * month * rate) / 100
        print('The Interest is', interest1)
        return interest1 
print('Case 1')
Interest(650, 2, 6) 
print('Case 2')
Interest(880, 2, 900)