def main():
    f=open("list.txt","w")
    lst = []
    no=eval(input("enter length of list:"))
    for i in range(no):
        x=eval(input("Enter elements:"))
        lst.append(x)
    f.write(str(lst))
    f.close()
main()