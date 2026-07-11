import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i==0:
        print("The function is",sys.argv[0])
    else:
        print("Argument:",sys.argv[i]) 