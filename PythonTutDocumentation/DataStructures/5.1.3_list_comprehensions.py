# list comprehensions porvide a concises way to create lists

squares = []
for x in range(10):
     squares.append(x**2)
print (squares) # this is how we create a list normally with squares

# or we can do a list comprehesion

squares = [x**2 for x in range(20)] # the x is the operation you want to do

# and then you can add flow control statements pertaining to that operation

#print (squares)

multiply = [x*2 for x in squares] # in list comprehensions you can you use for and if clauses

#print (multiply)

# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

triplets = [[x*2, y*4, z*6] for x in range(10) for y in range(10) for z in range(10) if x**3 == y]

#print (triplets) # prints triplets ten times each and searches for when x cubed is equal to y

#print([x*2 for x in squares]) # the comprehesion can automatically create a new list without being assigned to a variable 

# this list doubles the squares in the first list

print([x for x in squares if x < 0]) # will filter positive of negative numbers

# apply a function to all the elements



