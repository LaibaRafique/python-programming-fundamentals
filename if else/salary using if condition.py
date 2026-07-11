years=eval(input("Enter Years of service="))
qualification=input("Enter Qualification=")
degree1="Masters"
degree2="Bachelors"
if (years>=10) and (qualification==degree1):
    print("Salary=150,000")
elif (years>=10) and (qualification==degree2):
    print("Salary=100,000")
elif (years<10) and (qualification==degree1):
    print("Salary=100,000")
elif (years<10) and (qualification==degree2):
    print("Salary=70,000")

