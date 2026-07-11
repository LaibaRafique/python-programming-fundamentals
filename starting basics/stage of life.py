age=eval(input("Enter age::"))
if age<2:
    print("You're a Baby")
elif (age>=2) and (age<4):
    print("You're a Toddler")
elif (age>=4) and (age<13):
    print("You're a Kid")
elif (age>=13) and (age<20):
    print("You're a Teenager")
elif (age>=20) and (age<65):
    print("You're an Adult")
else:
    print("You're an Elder")