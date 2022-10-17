import sys
import random

def print_board(board):
    s = int(len(board) ** 0.5)
    for i in range(0,len(board),s):
        print(board[i:i+s])

def possible_moves(board,token): #return a list of all possible squares that can be played into by that token (x or o)
    out = set()
    out2 = list()
    if token == "x": token2 = "o"
    else: token2 = "x"
    qboard = "??????????"
    for i in range(0,64,8):
        qboard += "?" + board[i:i+8] + "?"
    qboard += "??????????"
    directions = [-11, -10, -9, -1, 1, 9, 10, 11]

    tinds = [i for i, element in enumerate(qboard) if element == token]
    for tind in tinds: 
        for d in directions:
            temp1 = tind+d
            temp2 = tind+d
            while(qboard[temp2]!="?"):
                if(qboard[temp1]==token2):
                    temp1+=d
                temp2+=d
            if(qboard[temp1]=="." and temp1!=tind+d): out.add(temp1)
    lboard = list(qboard)
    for i in out:
        lboard[i]="*"
    lboard = "".join([x for x in lboard if x!="?"])
    return [i for i, j in enumerate(lboard) if j == "*"]

def make_move(board, token, index):
    nboard = board[:index] + token + board[index+1:]
    index = index+11+2*(index//8)
    if token == "x": token2 = "o"
    else: token2 = "x"
    qboard = "??????????"
    for i in range(0,64,8):
        qboard += "?" + nboard[i:i+8] + "?"
    qboard += "??????????"
    directions = [-11, -10, -9, -1, 1, 9, 10, 11]

    for d in directions:
        temp1 = index+d
        temp2 = index+d
        tempL = []
        while(qboard[temp2]!="?" and qboard[temp2]!="." and qboard[temp1]!=token):
            if(qboard[temp1]==token2):
                tempL.append(temp1)
                temp1+=d
            temp2+=d
        for i in tempL:
            if qboard[temp2]!="?" and qboard[temp2]!=".":
                qboard=qboard[0:i] + token + qboard[i+1:]
    lboard = "".join([x for x in qboard if x!="?"])
    return lboard

def score_board(board):
    corners = [0,7,56,63]
    score = 0
    x = board.count("x")
    o = board.count("o")
    e = board.count(".")
    raw = x-o
    if e <10: score+=raw
    if e == 0:
        if raw>0: return 1000000 + raw
        else: return -1000000 + raw
    mob = len(possible_moves(board,"x")) - len(possible_moves(board,"o"))
    if e <= 50: mob = mob*3
    elif e<= 55: mob = mob*2
    score+=mob
    for i in corners:
        if board[i] == "x": score += 120
        if board[i] == "o": score -= 120
    return score

def find_next_move(board, player, depth, alpha, beta):
    # Based on whether player is x or o, start an appropriate version of minimax
    # that is depth-limited to "depth".  Return the best available move.
    if player == "x": player2 = "o"
    else: player2 = "x"
    scoreToBoard = dict()
    boardToIndex = dict()
    next_boards = []

    for next_move in possible_moves(board, player):
        temp = make_move(board,player,next_move)
        next_boards.append(temp)
        boardToIndex[temp] = next_move
    if depth == 0:
        return (None, score_board(board)) #return will be (index, score)
    if len(next_boards) == 0:
        return (None, score_board(board))

    for nboard in next_boards:
        score = find_next_move(nboard, player2, depth-1, alpha, beta)[1]
        if player == "x": alpha = max(alpha,score)
        if player == "o": beta = min (beta,score)
        if score not in scoreToBoard.keys():
            scoreToBoard[score] = nboard
        if(alpha>=beta): break

    if player == "x":   #max of board scores and that index
        mscore = max(scoreToBoard.keys())
        return (boardToIndex[scoreToBoard[mscore]],mscore)
    mscore = min(scoreToBoard.keys()) #min of board scores and that index
    return (boardToIndex[scoreToBoard[mscore]],mscore)



# class Strategy():
#    logging = True  # Optional
#    def best_strategy(self, board, player, best_move, still_running):
#        depth = 1
#        for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
#            best_move.value = find_next_move(board, player, depth,-100000,)[0]
#            depth += 1

# board = "...........................ox......xxx.........................."
# player =  "o"
# depth = 1

board = sys.argv[1]
player = sys.argv[2]
depth = 1
for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
   print(find_next_move(board, player, depth,-100000,100000)[0])
   depth += 1

#print(find_next_move(board, player, depth,-100000,100000)[0])
