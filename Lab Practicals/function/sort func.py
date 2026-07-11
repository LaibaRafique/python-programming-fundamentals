def sort(number1, number2,number3):
    if number1 < number2:
        if number2<number3:
            return number1,number2,number3
        else:
            if number1<number3:
                return number1,number3,number2
            else:
                return number3,number1,number2
    else:
        if number3<number2:
            return number3,number2,number1
        else:
            if number3<number1:
                return number2,number3,number1
            else:
                return number2,number1,number3
n1=eval(input("enter 1st number:"))
n2=eval(input("enter 2nd number:"))
n3=eval(input("enter 3rd number:"))
print(sort(n1,n2,n3))

