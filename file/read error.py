filename = input("Enter a filename: ")  
infile = open(filename, "r")
print(infile.read())
infile.close()