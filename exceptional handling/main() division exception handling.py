def main():
    try:
        no1,no2=eval(input("Enter numbers seperated by a comma::"))
        result=no1/no2
        print("Result is=",result)
    except ZeroDivisionError:
        print("Division by zero")
    except SyntaxError:
        print("A comma may be missing in the input")
    except:
        print("Something is wrong in the input")
    else:
        print("No exceptions")
    finally:
        print("The finally clause is executed")
main()