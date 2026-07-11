s = input("Enter numbers separated by spaces from one line: ")
items = s.split() 
lst = [eval(x) for x in items]
print(lst)