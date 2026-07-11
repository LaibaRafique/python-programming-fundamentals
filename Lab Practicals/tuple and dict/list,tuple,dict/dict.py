def functions_dict(d):
    print("Sum=",sum(d.values()))
    print("Max",max(d.values()))
    print("Min=",min(d.values()))
    print("Lenght=",len(d.values()))
    user=input("enter key to get the value:")
    print("user typed key value =",d.get(eval(user))) 