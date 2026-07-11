def printno(no):
    no=no+100
    print("In function")
    print("no=",no)
    
def main():
    no=23
    print("before calling function")
    print("no=",no)
    printno(no)
    print("no=",no)
main()