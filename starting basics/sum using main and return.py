def sum(i1,i2):
    ans=0
    for i in range (i1,i2+1):
        ans=ans+i
    return ans
def main():
    print("sum of 1-10=",sum(1,10))
    print("sum of 1-10=",sum(11,20))
    print("sum of 1-10=",sum(21,30))
main()