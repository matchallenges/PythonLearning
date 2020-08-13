
#try:
    #x = int(input('Enter a integer: '))
#except ValueError:
    #print("Oops that's not an integer")

# the last except caluse can omit execption names to be used as a wildcard
#print('second loop')

#try:
    #x = str(input('Enter a str: '))
#except ValueError:
    #print("Oops that's not a str")
#else:
    #print("Finished with no exceptions")


try:
    x = int(input('Enter a integer: '))
except ValueError:
    raise ValueError("That was not what I was looking for")