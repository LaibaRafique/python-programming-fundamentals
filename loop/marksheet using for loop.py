tsub=eval(input("Enter total number of subjects:"))
max=eval(input("Enter max marks of subjects:"))
total=tsub*max
sum=0
for i in range(1,tsub+1):
    print("Enter marks of subjects",i,"::",end="")
    marks=eval(input(""))
    sum=sum+marks
print("Sum=",sum)
per=(sum/total)*100.0
print("Percentage=",per,"%")
