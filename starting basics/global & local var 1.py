g=5
def f():
    l=10
    print("Global variable=",g)
    print("Local variable=",l)
def main():
    f()
    print("Global variable=",g)
main()