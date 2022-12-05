import fileinput
import string

priority = string.ascii_lowercase + string.ascii_uppercase

def input(): 
    file = "./input.txt"

    res = []

    for f in fileinput.input(file, encoding="utf-8"): 
        res.append(f.strip('\n'))
        
    return res

def partOne(f): 
    res = 0 

    # check each line 
    for line in f:
        mid = int(len(line)//2) 

        # check if letter in first word 
        # also in second word 
        for item in line[:mid]: 
            if item in line[mid:]: 
                res += priority.index(item) + 1
                break

    print('Part 1:', res)

def partTwo(f): 
    res = 0 

    # create groupings of 3 
    # increment by 3
    for i in range(0, len(f), 3): 
    
        lines = f[i:(i+3)]

        # check if each character in first line 
        # are also in both other lines
        for n in lines[0]: 
            if n in lines[1] and n in lines[2]: 
                res += priority.index(n) + 1
                break

    print('Part 2:', res)

if __name__ == "__main__": 
    f = input()
    partOne(f)
    partTwo(f)
