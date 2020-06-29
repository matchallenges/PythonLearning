# this code was created while reading the 4.4. break, continue, else loops documentation on the tutorial pag

for i in range(10):
    for x in range(10):
        if x < 10:
            print ('hello it\'s me')
            break
    else:
        print ('no it\'s not me')

# loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.

x = 10

while x in range(20):
    print ('the value is', (x))
    x += 1
    break # break will stop the loop no matter the circustances unless it's nested

for i in range(1000000):
    print (i)
    break

#so you can do somthing like this

# for i in range(10):
#   for i in list:
#       if i[0] = 'M':
#           print ("Found M")
#           break
#       
#

q = ['Charles', 'Charles', 'Charles', 'Charles', 'Charles', 'Charles', 'Charles', 'Charles', 'Charles', 'Mathieu', 'Terry']

for i in range(10):
    for x in q:
        print (x)
        if x[0] == 'M':
            print ('Found M')
            break # so I can stop the loop when certain requirements are met

# WIP