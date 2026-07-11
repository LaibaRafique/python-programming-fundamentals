def square(x):
    assert x>=0,"Only positive numbers are allowed"
    return x*x
try:
    print(square(-2))
except AssertionError as msg:
    print(msg)
except:
    print("In default exception handling block")