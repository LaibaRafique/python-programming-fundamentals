def record():
    d={}
    no2=5 #For 20 people no2=20
    for i in range(no2):
        u=eval(input("enter number of person:"))
        d1={}
        no1=7
        for i in range(no1):
            k=eval(input("enter keys::"))
            v=eval(input("enter values::"))
            d1.update({k:v})
        d.update({u:d1})
    return d
def main():
    print(record())
main()