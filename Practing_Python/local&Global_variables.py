print("Local and Global variables")
n = 42 
def func():
    global n 
    print(f"within function: n is {n}") 
    n = 3 
    print(f"within function: change n to {n}")

    func()
    print(f"Outside function: Value of n is {n}") 
    return n 