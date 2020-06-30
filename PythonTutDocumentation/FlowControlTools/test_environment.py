def shinobi(name, *args, **kwargs): # one interesting thing about argument is that *arguments can be used to make a tuple and **arguments can be used to make a dictionary
    print ('You have selected the shinobi', name,)
    print (args) # acess the tuple using slice notation
    print(kwargs) # acess the dictionaries using keys in a string 

shinobi('Naruto', 'wassup sasuke', 'idk wassup naruto', speech='hello', key='2') # all the keyword arguments will go to the kwargs parameter and positional arguments will go to args

#YOU CANNOT HAVE MORE THEN ONE *argument and **argument each

tuple = (1, 2, 3, 4, 5)
print(sum(tuple))