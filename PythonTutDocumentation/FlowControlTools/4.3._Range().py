# this code was created while reading the 4.3. range() documentation on the tutorial page

for i in range(10):
    print (i)

# the given end point is never printed as part of the sequence

a = ['wow', 'so cool', 'hi']

for i in range(len(a)):
    print(i, a[i])

# to iterate over the indices of a sequence, you can combine range() and len()

for i in enumerate(a): # enumerate also provides a similar function
    print (i)
