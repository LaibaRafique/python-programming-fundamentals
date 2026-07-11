txt=input("Enter string:")
print(txt)
t=txt.lower()
vc=0
wc=0
dc=0
for i in range(len(t)):
    if t[i]=='a'or t[i]=='e'or t[i]=='i'or t[i]=='o'or t[i]=='u':
        vc=vc+1
    elif t[i]==" ":
        wc=wc+1
    elif ord(t[i])>=49 and ord(t[i])<=57:
        dc=dc+1
print("Characters=",len(t))
print("Vowels=",vc)
print("Words=",wc+1)
print("Digits=",dc)