list = []

list.append('X') # append list
list.extend([1, 2, 4]) # extend list with another iterable
list.append([1, 2, 3]) # notice how this creates a nested list if I try to add it to the list
list.insert(0, 'inserted at first position') # first intger is the index of the list and then the contents

print (list)

list.remove(1) # remove an element that matches the element passed
list.pop(0) # removes an element at a certain position 
# list.clear removes all from the list

print (list)

print(list.index('X')) # returns the position of a certain element in the list with optional start and end parameters like slice notation
print(list.count(2)) # returns the number of times the specified element appears in the list
# print(list.sort()) sorting lists will have to be coded in the future as it is a very expansive topic
print (list.reverse())
print (list.copy())

