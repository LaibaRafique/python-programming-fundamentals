def sum(nos):
    sum=0
    for i in range(1,nos+1):
        print("enter marks of subject",i,"=",end=" ")
        m=eval(input(''))
        sum=sum+m
    return sum
def per(sum,nos,mmax):
    total=nos*mmax
    p=(sum/total)*100.0
    return p

def grade(p1):
    if p1>=90 and p1<=100:
        grade="A+"
        return grade
    elif p1>=80 and p1<=89:
        grade="A"
        return grade
    elif p1>=70 and p1<=79:
        grade="B"
        return grade
    elif p1>=60 and p1<=69:
        grade="C"
        return grade
    elif p1>=50 and p1<=59:
        grade="D"
        return grade
    else:
        grade="fail"
        return grade

def main():
    nos=eval(input("enter no of subjects="))
    mmax=eval(input("enter max marks="))
    s=sum(nos)
    
    p1=per(s,nos,mmax)
    print("sum=",s)
    print("percentage=",p1,"%")
    
    g=grade(p1)
    print("Grade=",g)
        
main()

    
    
   
        
        