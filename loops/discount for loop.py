sum=0
disc=0
for i in range(1,6):
    print("Enter price of item",i,"::",end="")
    price=eval(input(""))
    sum=sum+price
print("Total price before discount=",sum)
if sum>1000:
    disc=0.15*sum
elif sum>=500 and sum<=1000:
    disc=0.10*sum
else:
    disc=0
print("Discount=",disc)
d=sum-disc
print("Total price after discount=",d)