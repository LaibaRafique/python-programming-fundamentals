def rev(list):
    l=[]
    for i in range(len(list)-1,-1,-1):
        l.append(list[i])
    return l
def main():
    l=[]
    no=eval(input("enter no::"))
    for i in range(no):
        no=eval(input("enter values::"))
        l.append(no)
    print(l)
    list=rev(l)
    print(list)
main()