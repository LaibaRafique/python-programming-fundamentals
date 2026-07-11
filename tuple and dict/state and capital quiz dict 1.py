count1=0
count2=0
d1={"Alabama":"Montgomery","Montana":"Helena","Mississippi":"Jackson"}
for k,v in d1.items():
    print("Question:",k)
    g=input("Enter Capital of State:")
    if v==g:
        print("Your answer is True.")
        count1=count1+1
    else:
        print("Your answer is False.")
        count2=count2+1
print("Correct answer=",count1)
print("Wrong answer=",count2)