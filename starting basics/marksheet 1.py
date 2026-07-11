sum=0
for i in range(1,6):
    print("Enter marks of subjects",i,"::",end="")
    m=eval(input(""))
    sum=sum+m
    per=(sum/500)*100
print("Sum=",sum,"\nPercentage=",per)
