flavour = 'chocolat'

print(f"I love {flavour} ice cream")

print(f"this list is cool {[x**5 for x in range(11)]}") # { and } can be used to hold variable or expressions such as list comprehensions

#str.format

print('hello I love {0}'.format(flavour))

# when you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the repr() or str() functions.

print(repr(flavour)) # repr adds string quotations and backslashes

for x in range (11):
    print(f'{x} {x**2} {x**3}')

for x in range(1, 11):
    print('{0} {1} {2}'.format(x, x*x, x*x*x))