import random
no1=random.randint(1,10)
no2=random.randint(1,10)
ch=random.randint(1,7)
print(ch)
if ch==1:
    ans=no1+no2
    print(no1,"+",no2,"=",ans)
elif ch==2:
    ans=no1-no2
    print(no1,"-",no2,"=",ans)
elif ch==3:
    ans=no1*no2
    print(no1,"*",no2,"=",ans)
elif ch==4:
    ans=no1/no2
    print(no1,"/",no2,"=",ans)
elif ch==5:
    ans=no1//no2
    print(no1,"//",no2,"=",ans)
elif ch==6:
    ans=no1%no2
    print(no1,"%",no2,"=",ans)
elif ch==7:
    ans=no1**no2
    print(no1,"^",no2,"=",ans)
else:
    print("Invalid choice")
    