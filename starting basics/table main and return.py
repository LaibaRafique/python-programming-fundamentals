def table(no):
    for i in range(1,11):
        print(no,"x",i,"=",no*i)
        
def main():
    no=eval(input("enter no:"))
    table(no)
main()