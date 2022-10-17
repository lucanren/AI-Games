#python3 TTTNegamaxGreen.py "........."
#python3 TTTNegamaxGreen.py "......XOX"
#python3 TTTNegamaxGreen.py "O.....OXX"

import sys

def printBoard(s):
    print("Current board: ")
    for i in range(0,len(s),3):
        print(s[i:i+3])

def check(s): 
    temp = [s[x:x+3] for x in range(0,len(s),3)]
    if(compLetter == "X" ):
        for r in temp: #check rows
            if r.count("X")==3:
                return 1
            if r.count("O")==3:
                return -1
        for c in range(3): #check col
            temp2 = [x[c] for x in temp]
            if temp2.count("X")==3:
                return 1
            if temp2.count("O")==3:
                return -1
        temp3 = [[temp[0][0],temp[1][1],temp[2][2]],[temp[0][2],temp[1][1],temp[2][0]]]
        for t in temp3:
            if t.count("X")==3:
                return 1
            if t.count("O")==3:
                return -1
        if "." not in s: #tie
            return 0
    else:
        for r in temp: #check rows
            if r.count("X")==3:
                return -1
            if r.count("O")==3:
                return 1
        for c in range(3): #check col
            temp2 = [x[c] for x in temp]
            if temp2.count("X")==3:
                return -1
            if temp2.count("O")==3:
                return 1
        temp3 = [[temp[0][0],temp[1][1],temp[2][2]],[temp[0][2],temp[1][1],temp[2][0]]]
        for t in temp3:
            if t.count("X")==3:
                return -1
            if t.count("O")==3:
                return 1
        if "." not in s: #tie
            return 0
    return None
    # moves = [] #game not over
    # for i in range(len(s)):
    #     if(s[i]=="."):
    #         moves.append(s[:i]+ "X" + s[i+1:])
    #         moves.append(s[:i]+ "O" + s[i+1:])
    # return moves 
def check2(s,cp): 
    temp = [s[x:x+3] for x in range(0,len(s),3)]
    if(cp == "X" ):
        for r in temp: #check rows
            if r.count("X")==3:
                return 1
            if r.count("O")==3:
                return -1
        for c in range(3): #check col
            temp2 = [x[c] for x in temp]
            if temp2.count("X")==3:
                return 1
            if temp2.count("O")==3:
                return -1
        temp3 = [[temp[0][0],temp[1][1],temp[2][2]],[temp[0][2],temp[1][1],temp[2][0]]]
        for t in temp3:
            if t.count("X")==3:
                return 1
            if t.count("O")==3:
                return -1
        if "." not in s: #tie
            return 0
    else:
        for r in temp: #check rows
            if r.count("X")==3:
                return -1
            if r.count("O")==3:
                return 1
        for c in range(3): #check col
            temp2 = [x[c] for x in temp]
            if temp2.count("X")==3:
                return -1
            if temp2.count("O")==3:
                return 1
        temp3 = [[temp[0][0],temp[1][1],temp[2][2]],[temp[0][2],temp[1][1],temp[2][0]]]
        for t in temp3:
            if t.count("X")==3:
                return -1
            if t.count("O")==3:
                return 1
        if "." not in s: #tie
            return 0
    return None
    # moves = [] #game not over
    # for i in range(len(s)):
    #     if(s[i]=="."):
    #         moves.append(s[:i]+ "X" + s[i+1:])
    #         moves.append(s[:i]+ "O" + s[i+1:])
    # return moves 

def openSpaces(s):
    lst=[]
    for i in range(len(s)):
        if(s[i]=="."):
            lst.append(i)
    return lst

def get_next(s,cp):
    moves = [] #game not over
    for i in range(len(s)):
        if(s[i]=="."):
            moves.append(s[:i]+ cp + s[i+1:])
    return moves

# NEGA MAX STEP FUNCTION (returns value)
def negamax_step(s,cp):
    score = check2(s,cp)    #check2 takes in the player about to play next, and finds the status of the board for that player (cp = current player)
    if score is not None:
        return score
    results = list()
    if cp==compLetter:  # if the current player is the computer's letter (predetermined), then
        for next_board in get_next(s,compLetter):   # we'll find all the possible next moves the computer can make
            results.append(-1*negamax_step(next_board,userLetter))  # and then call the function again for that next move board, but change the current player to the user's letter since moves alternate. 
    elif cp==userLetter:
        for next_board in get_next(s,userLetter):
            results.append(-1*negamax_step(next_board,compLetter))
    return max(results)

# NEGAMAX MOVE FUNCTION (returns the baord with best move)
def negamax_move(s):
    d = {1:"win",0:"tie",-1:"loss"}
    moves = []
    for i in openSpaces(s):
        temp = s[:i]+ compLetter + s[i+1:]
        p = -1*negamax_step(temp,userLetter)
        print("Moving at " + str(i) + " results in a " + d[p])
        moves.append((p,i,temp))
    ind = moves.index(max(moves))
    print()
    print("I chose space " + str(moves[ind][1]))
    print()
    s = moves[ind][2]
    printBoard(s)
    return s

def play(s): 
    global compLetter
    global userLetter
    s = sys.argv[1]
    if s.count(".")==9:
        compLetter = input("Should I be X or O? ")
        print()
        printBoard(s)
        if(compLetter == "O"):
            userLetter = "X"
            print()
            print("You can move to any of these spaces: " + str(openSpaces(s)))
            userMove = int(input("Your choice? "))
            s = s[:userMove]+ userLetter + s[userMove+1:]
            print()
        else:
            userLetter="O"
    else:
        xs = s.count("X")
        os = s.count("O")
        if xs > os:
            compLetter="O"
            userLetter="X"
        else: 
            compLetter="X"
            userLetter="O"
        printBoard(s)
        print()
    
    while check(s) is None  : # ai always plays first here; if board empty, user already has played once
        s = negamax_move(s)
        print()

        if check(s) is not None:
            break
        
        print("You can move to any of these spaces: " + str(openSpaces(s)))
        userMove = int(input("Your choice? "))
        s = s[:userMove]+ userLetter + s[userMove+1:]
        print()
        printBoard(s)
        print()

    over = check(s)
    if over == 1:
        print("I win!")
    elif over == -1:
         print("You win!")
    else:
        print("Tie!")

print()
play(sys.argv[1])


