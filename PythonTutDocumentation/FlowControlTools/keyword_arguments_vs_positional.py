def positional(a, b):
    print ("the first arg is", a, "the second arg is", b)

positional(1, 2)
positional(2, 1)

#positional arguments are based on the position that you pass the value to the function a b or b a

def key(c, d):
    first = "c is", c
    second = "d is", d
    return first, second
print(key(c=9, d=10))
print(key(d=10, c=9)) # notice that they don't care what postion the arguments are passed
print(key(d=5, c=9))

#keyword arguments can let you omit a value

def default_values(v, n=0):
    return v, n

print(default_values(v=5))

