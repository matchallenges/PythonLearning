# from documentation below:
# we saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequence data types
# since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple.

# tuples can be made without brackets, just elements seperated by commas

tuple1 = 'Luffy', "Zoro", "Sanji" # this will create a tuple with three strings

print(tuple1)

# tuples can be nested aswell

nested_tup = ((3, 4, 5), (2, 3, 4), (2, 3, 6))
print(nested_tup)

# we can also unpack tuples

print(*nested_tup)

# tuples are immutable i.e. they cannot be changed

# however they can contain mutable objects

list_tuple = [1], [2], [3]

print(list_tuple)

tuple2 = () #blank tuple

single = 'one', #creates a tuple with one element

print (single)

