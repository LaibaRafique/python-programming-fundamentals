import random
sum=0
for i in range(1,5+1):
    print("enter marks of subjects",i,"=",end="")
    m=random.randint(1,100)
    print(m)
    sum=sum+m
print("Sum=",sum)
per=sum/500.0*100
print("Percentage=",per)
if (per>=90) and (per<=100):
    print("Grade A+")
elif (per>=80) and (per<=89):
    print("Grade A")
elif (per>=70) and (per<=79):
    print("Grade B")
elif (per>=60) and (per<=69):
    print("Grade C")
elif (per>=50) and (per<=59):
    print("Grade D")
else:
    print("Fail")
    