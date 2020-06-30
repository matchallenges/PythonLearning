#Unpacking argument lists

print(list(range(3, 6)))

listing_range = [50, 150]

print(list(range(*listing_range))) # the star symbol indicates that you want Python to unpack the values from a list

#dictionaries can be done in a similar fashion with **

def key_soup(**kwargs):
    print (kwargs)

dictionary = dict(name='Lucas', age=16)

key_soup(**dictionary) # the double star symbol unpacks the values from the dictionnary we created