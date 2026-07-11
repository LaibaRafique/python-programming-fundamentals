start_val=900
end_val=1000
for num in range(start_val,end_val+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")