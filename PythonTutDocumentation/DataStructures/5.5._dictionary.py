# It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

#Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

car1 = {'model':'Ford', 'colour':'blue'}
print(car1['model'])

car2 = dict(model='Chevy', colour='red')
print(car2['model'])

car3 = dict([('model', 'lamborghini'), ('colour', 'black')])
print(car3['colour'])