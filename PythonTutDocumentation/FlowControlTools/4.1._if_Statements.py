# this code was created while reading the 4.1. if Statement documentation on the tutorial page

x = 0

if x == 12: #Simple if statement to check if x equals 12
    print (True)

if x % 2 == 0:
    print ('Even')
elif x % 2 != 0: # elif short for else if can replace case switch statements
    print ('Odd')

# else statement is optional

if x < 0: # check to see if x is smaller than 0 else print positive 
    print ('negative')
else:
    print ('positive')

