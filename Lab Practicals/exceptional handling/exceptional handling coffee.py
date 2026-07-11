coffee={1:"Espresso",2:"Cappuccino",3:"Macchiato",4:"Latte",5:"Regular Coffee"}
try:
    n=eval(input("Which coffee you would like to have, please enter your desired number:"))
    for i in coffee:
        if n==i:
            print(coffee[i])
            break
    if n!=i:
        raise ValueError("Invalid number or character has been entered.")
except ValueError as ve:
    print(ve)
finally:
    print("Thank You for ordering!")