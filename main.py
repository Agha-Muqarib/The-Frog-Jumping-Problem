

def play_game(starting_position, move_sequence):
    greenFrog = []
    brownFrog = []
    Empty = 0
    totalmoves = 0
    counter = 0
    flag = 0

    for i in range(0, len(starting_position)):
        if starting_position[i] == '1':
            counter += 1
            greenFrog.append(counter)
        if starting_position[i] == '2':
            counter += 1
            brownFrog.append(counter)
        if starting_position[i] == '0':
            counter += 1
            Empty = counter

    startGreenFrog = list.copy(greenFrog)
    startBrownFrog = list.copy(brownFrog)
    startEmpty = Empty

    for i in range(0, len(move_sequence)):
        if move_sequence[i] == '1':
            totalmoves += 1
            print("")
            if Empty - 1 in greenFrog:
                greenFrog.remove(Empty - 1)
                greenFrog.append(Empty)
                Empty = Empty - 1
            elif Empty - 2 in greenFrog and Empty - 1 in brownFrog:
                greenFrog.remove(Empty - 2)
                greenFrog.append(Empty)
                Empty = Empty - 2
            else:
                print("")
                print("ERROR: at move ", totalmoves)
                flag = 1
                break
        if move_sequence[i] == '2':
            totalmoves += 1
            print("")
            if Empty + 1 in brownFrog:
                brownFrog.remove(Empty + 1)
                brownFrog.append(Empty)
                Empty = Empty + 1
            elif Empty + 2 in brownFrog and Empty + 1 in greenFrog:
                brownFrog.remove(Empty + 2)
                brownFrog.append(Empty)
                Empty = Empty + 2
            else:
                print("")
                print("ERROR: at move ", totalmoves)
                flag = 1
                break

        if move_sequence[i] == '1' or move_sequence[i] == '2':
            for j in range(0, counter + 1):
                if j in greenFrog:
                    print("1 ", end=" ")
                elif j in brownFrog:
                    print("2 ", end=" ")
                elif j == Empty:
                    print("0 ", end=" ")
                else:
                    print("", end=" ")
            print("")

    print("")

    startGreenFrog.sort()
    startBrownFrog.sort()
    greenFrog.sort()
    brownFrog.sort()

    if flag == 0:
        if startGreenFrog == brownFrog and startBrownFrog == greenFrog and startEmpty == Empty:
            print("Total States = ", totalmoves)
        else:
            print("Current State Number = ", totalmoves)

# Driver Code

starting_position = '1110222'
move_sequence = '1 2 2 1 1 1 2 2 2 1 1 1 2 2 1'


# starting_position = '111102222'
# move_sequence = '1 2 2 1 1 1 2 2 2 2 1 1 1 1  2 2 2 2 1 1 1 2 2 1'

print("Initially," "\n")
print(" 1  1  1  0  2  2  2 " "\n")
print("Start ...!")

play_game(starting_position, move_sequence)
