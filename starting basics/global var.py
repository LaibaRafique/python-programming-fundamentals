g=5
def f():
    global g
    g=g*10
    print("Global variable=",g)
def main():
    print("Global variable=",g)
    f()
    print("Global variable=",g)
main()