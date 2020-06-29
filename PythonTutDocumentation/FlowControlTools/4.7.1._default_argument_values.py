# this code was created while reading the 4.7.1 default argument values documentation on the tutorial page

#we can create default values for our specific functions

def OnePeice(keyword='Monkey.D.Luffy', tries=4, reward_message='You got 5 cookies!'): # the values are evaluated at the point of defining scope / when defining the function
    for i in range(tries):
        print ("Who will become the king of the pirates? ")
        user_input = input()
        if user_input == keyword:
            print (reward_message)
            break
        else:
            tries -= 1
            print ('You have', tries, 'tries left!')

OnePeice()