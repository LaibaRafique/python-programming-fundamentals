def max(num1,num2):
    if num1>num2:
        result=num1
    else:
        result=num2
    return result
def main():
    num1=eval(input("enter num1:"))
    num2=eval(input("enter num2:"))
    z=max(num1,num2)
    print("The maximum number from",num1,"and",num2,"is",z,".")
main()

def min(num1,num2):
    if num1<num2:
        result=num1
    else:
        result=num2
    return result
def main():
    num1=eval(input("enter num1:"))
    num2=eval(input("enter num2:"))
    z=min(num1,num2)
    print("The minimum number from",num1,"and",num2,"is",z,".")
main()