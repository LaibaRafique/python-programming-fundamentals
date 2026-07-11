import sys 
 
List_random = ['a', 0, 2] 
 
for enter in List_random:
    try:
        print("The entry is", enter)
        r = 1/int(enter)
        break
    except: 
        print("Oops!", sys.exc_info()[0], "occurred.") 
        print("Next entry.") 
        print() 
print("The reciprocal of", enter, "is", r) 