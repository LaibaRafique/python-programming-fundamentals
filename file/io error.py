while True:
    try:
        filename = input("Enter a filename: ").strip()    
        infile = open(filename, "r")
        print(infile.read())
        break
    except IOError:
        print("File " + filename + " does not exist. Try again")
