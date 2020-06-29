def add(n1, n2):
    """adds two integers together to make a sum"""
    print (n1 + n2)

add(1, 2) # now we call the function by creating func() and passing our parameters

# the first statement of our function body can optionally be a s tring literal to define what our function does

def substract(n1, n2):
    """subtracts two given integers"""
    return n1 - n2 # return the value but don't print it and have that outisde the function

s = substract(7, 3)

print(s)

