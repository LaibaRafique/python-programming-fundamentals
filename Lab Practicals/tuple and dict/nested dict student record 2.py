def record():
    d={}
    no2=20 #For 20 people no2=20
    for i in range(1,no2+1):
        u=i
        print("Person:",u)
        d1={}
        no1=["Name","Roll no","Pfund","Itc","Linear algebra","Islamiat","English"]
        for i in no1:
            print(i)
            v=eval(input("enter values::"))
            d1.update({i:v})
        d.update({u:d1})
    return d
def main():
    print(record())
main()