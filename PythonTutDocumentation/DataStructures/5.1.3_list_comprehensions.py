# list comprehensions porvide a concises way to create lists

squares = []
for x in range(10):
     squares.append(x**2)
print (squares) # this is how we create a list normally with squares

# or we can do a list comprehesion

squares = [x**2 for x in range(20)] # the x is the operation you want to do

# and then you can add flow control statements pertaining to that operation

print (squares)

multiply = [x*2 ] # in list comprehensions you can you use for and if clauses

print (multiply)
