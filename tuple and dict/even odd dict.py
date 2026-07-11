dict={"odd":[1,3,5,7,9],"even":[2,4,6,8,10]}
for k,v in dict.items():
    print("\n",k,"=",end=" ")
    for i in v:
        print(i,end=" ")