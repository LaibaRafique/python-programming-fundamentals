cities={}
no2=3 
for i in range(1,no2+1):
    u=input("Enter City:")
    print("City:",u)
    info={}
    no1=["Country","Population","Fact"]
    for i in no1:
        print(i)
        v=eval(input("enter:"))
        info.update({i:v})
    cities.update({u:info})
print(cities)
for k,v in cities.items():
    print(k)
    for i in v:
        print(i,"=",v[i])