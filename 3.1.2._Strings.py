# this code was created while reading the 3.1.2. Strings documentation on the tutorial page

print ('eggs') # single quote string
print ("sandwhich") # double quote string

print ('yesn\'t') # use a backslash to escpae a single quote (have python not be confused printing the string)
print ("yesn't") # alternatively you can use double quotes and the single quote will be seen as apart of the string
print ('"Wow," he said.')
print ("\"Wow,\" he said.") # escape double quotes

print ("First line\nSecond line") # \n creates a newline

# if you would like the backslash to be printed or not interpreted as a special character use a raw string

print (r"First line\nSecond line") # notice the 'r' before the string

# multiple lines

print("""

hey

wow

so cool             boop

""")

# concatening strings (glued together) with the + operator and repeated with the * operator

print (4 * "um" + "ha")

# you can concatenate two strings by putting them beside each other
print ('p''i')

text = ('wow this is such a long string'
        ', and it continues'
)

print (text)

# however you cannot concatenate a variable and a string literal