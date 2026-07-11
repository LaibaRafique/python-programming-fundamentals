students = {"111-34-3434":"John", "132-56-6290":"Peter"} 
students["234-56-9010"] = "Susan" 
print(students)

students["111-34-3434"] = "John Smith" 
print(students["111-34-3434"])

del students["132-56-6290"]
print(students)

print(students.keys())
print(students.values())  
print(students.items())