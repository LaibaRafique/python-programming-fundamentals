x = input("enter text to be replaced:")
y = input("enter text that will replace:")
f = open("pet.txt", "r+")
l = f.readlines()
c = 0
for i in l:
    if x in i:
        Replacement = i.replace(x, y)
        l = Replacement
    c += 1
f.truncate(0)
f.writelines(l)
f.close()
print("Text successfully replaced")