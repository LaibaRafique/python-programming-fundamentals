try:
    a=5
    b=0
    print(a/b)
except TypeError as a:
    print("Unsuportted operation")
    print(a.args)
except ZeroDivisionError as zs:
    print("Division by zero not allowed")
    print(zs.args)
except:
    print("In default exception handling block")
print("Out of try except blocks")