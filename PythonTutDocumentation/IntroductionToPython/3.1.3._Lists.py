# this code was created while reading the 3.1.3. Lists documentation on the tutorial page

# python knows a variety of compound data types, used to group variables together

# one of the most versatile is a list

squares = [1, 4, 9, 16, 25]
print (squares)
print (4 * squares) # you can also concatenate lists into one big lists
print (squares + [64, 1000])

# unlike strings whihc are immutable, lists are mutable which means you can change it's contents
squares[0] = 4000
print (squares)

# you can also add elements to the end of a list, by using the append() method

squares.append(500) # append 500 to the end of the list
print (squares)
squares.append(squares[:4]) # you can also append lists to other lists and they will be saved as an individual element (nested list)
print (squares)

# you can also append, change and delete slices of a list

squares[:4] = ['M', 'M', 'M', 'M'] # replace the integers in the list with strings
print (squares)
squares[:4] = []
print (squares) # delete specific elements
squares[:] = [] # we can also clear the list with blank slice

# the function len() also applies to lists

print (len(squares))
