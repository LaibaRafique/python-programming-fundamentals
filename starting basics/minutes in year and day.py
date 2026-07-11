minutes=int(input("enter minutes="))
years=minutes/525600
days=minutes/1440
remaining_minutes=days%525600
print("years=",years,"days=",remaining_minutes)