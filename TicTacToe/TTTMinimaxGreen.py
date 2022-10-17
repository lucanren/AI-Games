#python3 TTTMinimaxGreen.py "........."
#python3 TTTMinimaxGreen.py "......XOX"
#python3 TTTMinimaxGreen.py "O.....OXX"

import sys

def printBoard(s):
    print("Current board: ")
    for i in range(0,len(s),3):
        print(s[i:i+3])

def check(s): #x=1, O=-1, tie=0
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

def get_cp(s):
    xs = s.count("X")
    os = s.count("O")
    if xs > os:
        cp="O"
    else: 
        cp="X"
    return cp

def max_step(s):
    score = check(s)
    if score is not None:
        return score
    results = list()
    for next_board in get_next(s,compLetter):
        results.append(min_step(next_board))
    return max(results)

def min_step(s):
    score = check(s)
    if score is not None:
        return score
    results = list()
    for next_board in get_next(s,userLetter):
        results.append(max_step(next_board))
    return min(results)
    
def max_move(s):
    d = {1:"win",0:"tie",-1:"loss"}
    moves = []
    for i in openSpaces(s):
        temp = s[:i]+ compLetter + s[i+1:]
        p = min_step(temp)
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
        s = max_move(s)
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


