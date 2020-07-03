# There is a way to remove an item from a list given its index instead of its value: the del statement.

list = [1, 5, 7, 3, 4, 5]
del list[0]
print (list)

# del also does not return a value like pop()

del list[1:2] # del also works with slice notation

print(list)