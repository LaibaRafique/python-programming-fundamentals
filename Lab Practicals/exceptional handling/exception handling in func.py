def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
try:
    AbyB(2.0,3.0)
    AbyB(0,0)
    AbyB("a","b")
except:
    print("In main exception block")