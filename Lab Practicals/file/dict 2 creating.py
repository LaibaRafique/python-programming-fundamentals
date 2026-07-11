f=open("dict2.txt","w")
a={}
n=eval(input("enter length="))
for i in range(n):
    k=eval(input("enter key="))
    v=eval(input("enter values="))
    a.update({k:v})
f.write(str(a))
f.close()
while True:
    f=open("dict2.txt","r")
    data=f.read()
    if data=="":
        break
    print(data,end=" ")
f.close()