balance = int(input("enter your balance1:"))
while True:
    if balance <=9000:
        continue
    balance = balance+999.99
    print("Balance is", balance)
    break