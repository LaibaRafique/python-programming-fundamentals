def main():
    f=open("tuple.txt","w")
    lst = []
    no=eval(input("enter length of tuple:"))
    for i in range(no):
        x=eval(input("Enter elements:"))
        lst.append(x)
    t=tuple(lst)
    f.write(str(t))
    f.close()
main()