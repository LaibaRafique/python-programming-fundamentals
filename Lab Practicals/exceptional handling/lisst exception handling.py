try:
    my_list = [3,7, 9, 4, 6]
    print(my_list[6])
except IndexError:
    print("Index out of range.")
except:
    print("In except block")