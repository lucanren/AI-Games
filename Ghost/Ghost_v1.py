import sys
import time
dictionary = sys.argv[1]
minLen = int(sys.argv[2])
game = ""
if(len(sys.argv) == 4):
    game = sys.argv[3].lower()
with open(dictionary) as f:
    words = set()
    for line in f:
        temp = line.strip().lower()
        if(temp.isalpha() and len(temp) >= minLen and temp[:len(game)] == game):
            words.add(temp)
    
def nextLetters(sequence, allWords):
    w = allWords.copy()
    wordSet = set()
    removeSet = set()
    for x in w:
        if(x[:len(sequence)] == sequence):
            wordSet.add(x[len(sequence)])
        else:
            removeSet.add(x)
    for x in removeSet:
        w.remove(x)
    return wordSet, w


def minStep(sequence, wordSet, alpha, beta, player):
    if(sequence in words):
        if(player == 0):
            return (-1, None)
        else:
            return (1, None)
    letterDic = {}
    nextL = nextLetters(sequence, wordSet)
    for x in nextL[0]:
        temp = sequence + x
        if(player == 1):
            a = maxStep(temp, nextL[1], alpha, beta)[0]
            beta = min(a, beta)
        else:
            a = minStep(temp, nextL[1], alpha, beta, 1)[0]
            alpha = max(a, alpha)
        if(a not in letterDic):
            letterDic[a] = {x}
        else:
            letterDic[a].add(x)
        if(alpha > beta):
            break
    m = min(letterDic)
    return (m, letterDic[m])
        
def maxStep(sequence, wordSet, alpha, beta):
    if(sequence in words):
        return (1, None)
    letterDic = {}
    nextL = nextLetters(sequence, wordSet)
    for x in nextL[0]:
        temp = sequence + x
        a = minStep(temp, nextL[1], alpha, beta, 0)[0]
        alpha = max(a, alpha)
        if(a not in letterDic):
            letterDic[a] = {x}
        else:
            letterDic[a].add(x)
        if(alpha > beta):
            break
    m = max(letterDic)
    return (m, letterDic[m])

a = maxStep(game, words, -10, 10)
if(a[0] == 1):
    print("Next player can guarantee victory by playing any of these letters: " + str(a[1]))
else:
    print("Next player will lose!")