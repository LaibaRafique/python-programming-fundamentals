message=input("enter message::")
v=0
for i in message.lower():
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        v+=1
print("vowels=",v)