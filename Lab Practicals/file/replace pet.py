import sys
import fileinput
 
x = input("Enter text to be replaced:")
y = input("Enter replacement text:")
 
for l in fileinput.input(files = "pet.txt"):
    l = l.replace(x, y)
    sys.stdout.write(l)

f = open("pet.txt", "r+")
l = f.readlines()
for i in l:
    if x in i:
        Replacement = i.replace(x, y)
        l = Replacement
f.truncate(0)
f.writelines(l)
f.close()