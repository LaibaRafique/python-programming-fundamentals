sub1=eval(input("Enter marks of subject 1="))
sub2=eval(input("Enter marks of subject 2="))
sub3=eval(input("Enter marks of subject 3="))
sub4=eval(input("Enter marks of subject 4="))
sub5=eval(input("Enter marks of subject 5="))
total_marks=sub1+sub2+sub3+sub4+sub5
percentage=(total_marks/500.0)*100
print("Percentage=",percentage)
if (percentage>=90) and (percentage<=100):
    print("Grade A+")
elif (percentage>=80) and (percentage<=89):
    print("Grade A")
elif (percentage>=70) and (percentage<=79):
    print("Grade B")
elif (percentage>=60) and (percentage<=69):
    print("Grade C")
elif (percentage>=50) and (percentage<=59):
    print("Grade D")
else:
    print("Fail")