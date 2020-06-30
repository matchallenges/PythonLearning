# this code was created while reading the 4.7.3 special parameters documentation on the tutorial page

# from documentatio below

# By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

#postional only arguments can be created by placing them before a forward slash

#def function_pos(args, args1, /, kwargs=0):
    #print (args, args1)
    
#function_pos('first positional argument', args1=20) # the function will not work because we tried to pass a keyword argument when the function aparameter is positional only

# keyword only arguments and both

def function_soup(arg1, arg2, /, marg1, *, kwarg1, kwarg2):
    print (arg1, arg2, marg1, kwarg1, kwarg2)

function_soup(1, 2, marg1='can be either keyword or postional argument', kwarg1='first keyword argument', kwarg2='second keyword argument')

# pos only follows by /
# keyword only preceeded by *
# in the middle can be both

