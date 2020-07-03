# python also includes a data type for sets. A set is an unordered collection with no duplicate elements.\

crew = {'Marco', 'Trafalgar', 'Nami', 'Nami'}
print(crew) # show that duplicate has been removed

print('Marco' in crew) # returns boolean if the element is in the set

a = set('hello')
b = set('woah')

print(a) # print unique letters in a

print(a - b) # letters in a but not in b

print(a | b) # letters in a or b or both

print(a & b) # letters in a and b

print(a ^ b) # letters in a or b but not both

# it's interesting that you can do some pseudo randomization with sets because each times you run it, it changes

# set comprehensions are also supported

s = {x for x in 'GomuGomuNoMi' if x in 'Gcd'}
print(s)