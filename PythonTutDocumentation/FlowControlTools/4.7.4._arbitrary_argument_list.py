# Using a varibale number of arguments can be used like this 

def add_all(*args): # one or more normal arguments may occur before the variable parameter
    return sum(args)

print(add_all(1, 2, 3, 4, 5)) # will add an indefinet amount or arguments

