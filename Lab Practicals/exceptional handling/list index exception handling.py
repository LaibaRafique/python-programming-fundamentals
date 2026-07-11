a=[1,2,3]
try:
    print("First element = %d" % (a[0]))
    print("Second element = %d" % (a[1]))
    print("Third element = %d" % (a[2]))
    print("Sixth element = %d" % (a[5]))
except:
    print("An error occured")
else:
    print("In else block")
finally:
    print("In finally block")
print("Program terminates")