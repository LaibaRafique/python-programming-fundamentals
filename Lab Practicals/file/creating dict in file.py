def main():
    f=open("dict.txt","w")
    a={}
    n=eval(input("enter length="))
    for i in range(n):
        k=eval(input("enter key="))
        v=eval(input("enter values="))
        a.update({k:v})
    f.write(str(a))
    f.close()
main()