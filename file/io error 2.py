try:
    filename = input("Enter a filename: ")   
    infile = open(filename, "r")
    print(infile.read())
except IOError:
    print("File " + filename + " does not exist. Try again")
