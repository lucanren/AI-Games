#python3 GhostRed.py words_all.txt 4
#python3 GhostRed.py words_all.txt 4 AB

#python3 GhostRed.py wordlist.txt 4

import sys

#letters = "qwertyuiopasdfghjklzxcvbnm"
minLen = int(sys.argv[2])
if len(sys.argv) > 3:
    firstLet = sys.argv[3].upper()
else: firstLet = ""
with open(sys.argv[1]) as f:
    dic = {line.strip().upper() for line in f if line.strip().isalpha() and len(line.strip())>=minLen and line.strip().upper()[0:len(firstLet)]==firstLet}
#maxLen = max([len(s) for s in dic])

# def still_valid(word):
#     for x in dic:
#         if word in x:
#             return True
#     return False

def get_next(game, words): #edits the dictionary to make the next search faster + returns plausible next letters
    copyWords = {w for w in words} 
    toDelete = set()
    out = set()
    for w in copyWords:
        if w[0:len(game)] == game: out.add(w[len(game)])
        else: toDelete.add(w)
    for w in toDelete: copyWords.remove(w)
    return (copyWords,out)

def max_step(game,words,alpha,beta):
    if game in dic: return (1,None)
    lDic = {}
    nextLs = get_next(game,words)
    for l in nextLs[1]:
        nextG = game + l
        temp2 = min_step_1(nextG,nextLs[0],alpha,beta)[0]
        if temp2 not in lDic: lDic[temp2] = {l}
        else: lDic[temp2].add(l)
        if (max(temp2,alpha)>beta): break
    return (max(lDic),lDic[max(lDic)])

def min_step_1(game,words,alpha,beta):
    if game in dic: return (-1,None)
    lDic = {}
    nextLs = get_next(game,words)
    for l in nextLs[1]:
        nextG = game + l
        temp2 = min_step_2(nextG,nextLs[0],alpha,beta)[0]
        if temp2 not in lDic: lDic[temp2] = {l}
        else: lDic[temp2].add(l)
        if (alpha>min(temp2,beta)): break
    return (min(lDic),lDic[min(lDic)])

def min_step_2(game,words,alpha,beta):
    if game in dic: return (1,None)
    lDic = {}
    nextLs = get_next(game,words)
    for l in nextLs[1]:
        nextG = game + l
        temp2 = max_step(nextG,nextLs[0],alpha,beta)[0]
        if temp2 not in lDic: lDic[temp2] = {l}
        else: lDic[temp2].add(l)
        if (alpha>min(temp2,beta)): break
    return (min(lDic),lDic[min(lDic)])

run = max_step(firstLet,dic,-1000,1000)
if run[0] > 0:
    print("Next player can guarantee victory by playing any of these letters: " + str(run[1]))
else: 
    print("Next player will lose!")

# winWords = []
# def negamax(word,cp,alpha,beta):
#     results = list()
#     print(winWords)
#     if word in dic:
#         if cp == "x": 
#             winWords.append(word)
#             return 1
#         return -1
#     if cp == "x":
#         for next_word in get_next(word):
#             score = negamax(next_word,"x",alpha,beta)
#             alpha = max(alpha,score)
#             results.append(score)
#             if alpha>=beta:break
#         if len(results) == 0:
#             return 0
#         return max(results)
#     elif cp == "o":
#         for next_word in get_next(word):
#             score = negamax(next_word,"x",alpha,beta)
#             beta = min(beta,score)
#             results.append(score)
#             if alpha>=beta:break
#         if len(results) == 0:
#             return 0
#         return min(results)



