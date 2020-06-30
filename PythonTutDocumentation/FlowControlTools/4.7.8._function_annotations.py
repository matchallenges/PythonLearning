def func(a: int, b: int) -> int: # we can annotate that the variables should be integers and the result of the function should also be an integer with -> int
    return(a + b)

print(func(5, 5)) # however the annotations are ignored by the python interpreter

# __annotations__ is stored as a dictionnary so we can retrieve what they are supposed to be in our function

print(f"{func.__annotations__['a']}, {func.__annotations__['b']}, {func.__annotations__['return']}")