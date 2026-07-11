name=input("Enter name=")
roll_no=eval(input("Enter Roll no.="))
sub1=eval(input("Enter marks of subject 1 ="))
sub2=eval(input("Enter marks of subject 2="))
sub3=eval(input("Enter marks of subject 3="))
total_marks=sub1+sub2+sub3
per=(total_marks/300.0)*100
print("\t\t\tReport Card")
print("Name=",name)
print("Roll no.=",roll_no)
print("Percentage=",per,"%")
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
