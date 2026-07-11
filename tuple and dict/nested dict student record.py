def record():
    d={}
    no2=20 #For 20 people no2=20
    for i in range(no2):
        u=eval(input("enter number of person:"))
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