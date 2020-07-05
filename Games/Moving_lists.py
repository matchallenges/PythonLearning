import os

Row1 = [1, 0, 0]
Row2 = [0, 0, 0]
Row3 = [0, 0, 0]

def update_screen():
    print (Row1)
    print (Row2)
    print (Row3)

def update_pos():
    try:
        position = Row1.index(1)
    except ValueError:
        pass

    try:
        position = Row2.index(1)
    except ValueError:
        pass

    try:
        position = Row3.index(1)
    except ValueError:
        pass
    
    return position

switch = True

print('Current Map:')
update_screen()
update_pos()

while switch == True:
    dir = input('Which direction will you travel? (North South East West) "X" to exit: ')
    
    #Exit mechanic
    if dir == 'X' or dir == 'exit':
        os.system('cls')
        break

    #North
    if dir == 'North' or dir == 'N':
        if 1 in Row1:
            os.system('cls')
            print(f"Index in list: {update_pos()}")
            print("Position in Row1")
            update_screen()
        if 1 in Row2:
            os.system('cls')
            Row1[update_pos()] = 1
            Row2[update_pos()] = 0
            print(f"Index in list: {update_pos()}")
            print("Position in Row1")
            update_screen()
        if 1 in Row3:
            os.system('cls')
            Row2[update_pos()] = 1
            Row3[update_pos()] = 0
            print(f"Index in list: {update_pos()}")
            print("Position in Row2")
            update_screen()
    
    #South
    if dir == 'South' or dir == 'S':
        if 1 in Row3:
            os.system('cls')
            print(f"Index in list: {update_pos()}")
            print("Position in Row3")
            update_screen()
        if 1 in Row2:
            os.system('cls')
            Row3[update_pos()] = 1
            Row2[update_pos()] = 0
            print(f"Index in list: {update_pos()}")
            print("Position in Row3")
            update_screen()
        if 1 in Row1:
            os.system('cls')
            Row2[update_pos()] = 1
            Row1[update_pos()] = 0
            print(f"Index in list: {update_pos()}")
            print("Position in Row2")
            update_screen()

    #East
    if dir == 'East' or dir == 'E':

        if 1 in Row3:
            if update_pos() == 0:
                os.system('cls')
                Row3[update_pos()] = 0
                Row3[1] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 1:
                os.system('cls')
                Row3[update_pos()] = 0
                Row3[2] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 2:
                os.system('cls')
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
        
        if 1 in Row2:
            if update_pos() == 0:
                os.system('cls')
                Row2[update_pos()] = 0
                Row2[1] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 1:
                os.system('cls')
                Row2[update_pos()] = 0
                Row2[2] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 2:
                os.system('cls')
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
        
        if 1 in Row1:
            if update_pos() == 0:
                os.system('cls')
                Row1[update_pos()] = 0
                Row1[1] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 1:
                os.system('cls')
                Row1[update_pos()] = 0
                Row1[2] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 2:
                os.system('cls')
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
    
    #West
    if dir == 'West' or dir == 'W':
        
        if 1 in Row3:
            if update_pos() == 0:
                os.system('cls')
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 1:
                os.system('cls')
                Row3[update_pos()] = 0
                Row3[0] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 2:
                os.system('cls')
                Row3[update_pos()] = 0
                Row3[1] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
        
        if 1 in Row2:
            if update_pos() == 0:
                os.system('cls')
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 1:
                os.system('cls')
                Row2[update_pos()] = 0
                Row2[0] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 2:
                os.system('cls')
                Row2[update_pos()] = 0
                Row2[1] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
        
        if 1 in Row1:
            if update_pos() == 0:
                os.system('cls')
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 1:
                os.system('cls')
                Row1[update_pos()] = 0
                Row1[0] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue
            if update_pos() == 2:
                os.system('cls')
                Row1[update_pos()] = 0
                Row1[1] = 1
                print(f"Index in list: {update_pos()}")
                print("Position in Row1")
                update_screen()
                continue