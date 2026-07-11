try:
    print("In try block")
    print(1/0)
    print("After exception block")
except:
    print("In except block")
else:
    print("In else block")
finally:
    print("In finally block")