# this code was created while reading the 4.7.1 default argument values documentation on the tutorial page

#we can create default values for our specific functions

tries = 6 # notice how these variables do not effect the tries parameter default value 

def OnePeice(keyword='Monkey.D.Luffy', tries=4, reward_message='You got 5 cookies!'): # the values are evaluated at the point of defining scope / when defining the function
    for i in range(tries):
        print ("Who will become the king of the pirates? ")
        user_input = input()
        if user_input == keyword:
            print (reward_message)
            break
        else:
            tries -= 1
            if tries > 1:
                print ('You have', tries, 'tries left!')
            elif tries == 1:
                print ('You have', tries, 'try left!')
            elif tries == 0:
                print ('You failed!')

tries = 5 # notice how these variables do not effect the tries parameter default value     

OnePeice()

# Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

