
    #East
    if dir == 'East' or dir == 'E':
    
        if 1 in Row1:
            if pos == 0:
                os.system('cls')
                Row1[pos] = 0
                Row1[1] = 1
                update_pos()
                update_screen()
            if pos == 1:
                os.system('cls')
                Row1[pos] = 0
                Row1[2] = 1
                update_pos()
                update_screen()
            if pos == 2:
                os.system('cls')
                print("Move out of bounds!")
                update_pos()
                update_screen()
    
        if 1 in Row2:
            if pos == 0:
                os.system('cls')
                Row2[pos] = 0
                Row2[1] = 1
                update_pos()
                update_screen()
            if pos == 1:
                os.system('cls')
                Row2[pos] = 0
                Row2[2] = 1
                update_pos()
                update_screen()
            if pos == 2:
                os.system('cls')
                print("Move out of bounds!")
                update_pos()
                update_screen()

        if 1 in Row3:
            print(update_pos)
            if pos == 0:
                os.system('cls')
                Row3[pos] = 0
                Row3[1] = 1
                update_pos()
                update_screen()
            if pos == 1:
                os.system('cls')
                Row3[pos] = 0
                Row3[2] = 1
                update_pos()
                update_screen()
            if pos == 2:
                os.system('cls')
                print("Move out of bounds!")
                update_pos()
                update_screen()