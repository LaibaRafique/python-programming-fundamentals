name=input("Enter name:")
roll_no=eval(input("Roll no.:"))
Islamiat=eval(input("enter marks of Islamiat:"))
percentage1=(Islamiat/100)*100
Physics=eval(input("enter marks of Physics:"))
percentage2=(Physics/100)*100
English=eval(input("enter marks of English:"))
percentage3=(English/100)*100
Maths=eval(input("enter marks of Maths:"))
percentage4=(Maths/100)*100
Computer=eval(input("enter marks of Computer:"))
percentage5=(Computer/100)*100
Pak_studies=eval(input("enter marks of Pak_studies:"))
percentage6=(Pak_studies/100)*100
Urdu=eval(input("enter marks of Urdu:"))
percentage7=(Urdu/100)*100
Chemistry=eval(input("enter marks of Chemistry:"))
percentage8=(Chemistry/100)*100
Biology=eval(input("enter marks of Biology:"))
percentage9=(Biology/100)*100
Zoology=eval(input("enter marks of Zoology:"))
percentage10=(Zoology/100)*100
total_marks=Islamiat+Physics+English+Maths+Computer+Pak_studies+Urdu+Chemistry+Biology+Zoology
percentage=(total_marks/1000.0)*100
print("\t\t\tReport card")
print("Name:",name)
print("Roll No.:",roll_no)
print("Islamiat=",Islamiat,"and Percentage of Islamiat=",percentage1)
print("Physics=",Physics,"and Percentage of Physics=",percentage2)
print("English=",English,"and Percentage of English=",percentage3)
print("Maths=",Maths,"and Percentage of Maths=",percentage4)
print("Computer=",Computer,"and Percentage of Computer=",percentage5)
print("Pak_studies=",Pak_studies,"and Percentage of Pak_studies=",percentage6)
print("Urdu=",Urdu,"and Percentage of Urdu=",percentage7)
print("Chemistry=",Chemistry,"and Percentage of Chemistry=",percentage8)
print("Biology=",Biology,"and Percentage of Biology=",percentage9)
print("Zoology=",Zoology,"and Percentage of Zoology=",percentage10)
print("-----Total marks-----=",total_marks)
print("-----Percentage-------=",percentage)

