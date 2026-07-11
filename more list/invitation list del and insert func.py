Guest_list=["laiba","dur","khadija","hamna"]
print("Invitation for birthday dinner!")
for i in Guest_list:
    print("Hello",i,"\b,","You're invited for dinner. ")
print("\nNew invitation for birthday dinner!\n")
del Guest_list[3]
Guest_list.insert(3,"ali")
for i in Guest_list:
    print("Hello",i,"\b,","You're invited for dinner. ")