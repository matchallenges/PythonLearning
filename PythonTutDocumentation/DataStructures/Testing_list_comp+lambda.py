adding = lambda *args : sum(args)

add_powers= [adding(x**2, x**3) for x in range(10)] # THERE WE GOOOOOO this line of code took me hours!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! this use to print 25 times

#add_all_nums = [x**2 + x**3 for x in range(10)] # how did I not realise you just have to use x not two different variables

print(add_powers)

# this means we can couple functions with a variable amount of elements inside of a list comprehension

# we can also make the function unpack lists for example

func = lambda *args : comp2.extend(*args)

comp1 = [1, 2, 3, 4, 5]
comp2 = []

mega_add = [func(comp1) for x in range(1)]

print(comp2)