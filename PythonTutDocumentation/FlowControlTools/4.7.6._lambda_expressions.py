# from documentation below

# Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition.

def reduce(n):
    return lambda x : x - n

number = reduce(2)

print(number(40))

# you can think of lambda functions as nested function definitions

adding = lambda a, b, c : print (a + b + c) # we can make a small function without the syntaxical mess of creating a full function and have it print to the screen

adding(1, 2, 3)