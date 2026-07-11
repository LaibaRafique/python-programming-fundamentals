no=eval(input("Enter table no:"))
star=eval(input("Enter starting no:"))
end=eval(input("Enter ending no:"))
k=eval(input("Enter step size:"))
i=star
while i<=end:
    print(no,"x",i,"=",no*i)
    i=i+k