import fileinput
from collections import OrderedDict

# A, X = Rock = 1
# B, Y = Paper = 2
# C, Z = Scissor = 3
# Win / Loss = 0 / 1

def input(): 
    file = "./input.txt"

    res = []

    for f in fileinput.input(file, encoding="utf-8"): 
        res.append(f.strip('\n').split(' '))
    
    return res

def partOne(f): 
    score = 0 

    rules = {
        'X': ['BAC', 1],
        'Y': ['CBA', 2],
        'Z': ['ACB', 3],
    }

    for game in f: 
        opp = game[0]
        me = game[1]
        score += rules[me][1]
        i = rules[me][0].index(opp)
        score += (i * 2) + i

    print('Part 1:', score)

def partTwo(f): 
    score = 0 
    strats = 'XYZ'

    rules = {
        'A': 'ZXY', 
        'B': 'XYZ', 
        'C': 'YZX',
    }
    
    for game in f: 
        opp = game[0]
        strat = game[1]
        i = strats.index(strat)

        # win / loss / draw score 
        score += (i * 2) + i 

        # rock / paper / scissor score 
        score += strats.index(rules[opp][i]) + 1

    print('Part 2:', score)

if __name__ == "__main__": 
    f = input()
    partOne(f)
    partTwo(f)