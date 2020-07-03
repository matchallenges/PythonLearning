car = {'Colour':'red', 'Model':'AshtonMartin','Transmission':'manuel'}

for k, v in car.items():
    print (k, v) # to retrive the key and the value use the items() method

# when looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

for k, v in enumerate(car.items()):
    print (k, v)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

for i, o in zip(list1, list2):
    print (i, o) # to loop over two or more sequences at the same time we can use the zip() function / paired entries

print([r for r in zip(list1, list2)]) # can also create pairs with zip() and list comprehesion

# to loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

for i in reversed(range(5)):
    print(i)

for i in sorted(car):
    print (i)

print(car)