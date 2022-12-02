import fileinput

def input(): 
    file = "./input.txt"

    res = []
    line = []

    for f in fileinput.input(file, encoding="utf-8"): 
        val = f.strip('\n')
        
        if val == '': 
            res.append(line)
            line = []
        else: 
            line.append(int(val))
    
    return res

def partOne(f): 
    max = 0 

    for n in f: 
        tmp = sum(n)
        max = tmp if tmp > max else max

    print('Part 1:', max)

def partTwo(f): 
    max = []

    for n in f: 
        tmp = sum(n)
        max.append(tmp)
        
        if len(max) > 3: 
            max.pop(max.index(min(max)))

    print('Part 2:', sum(max))
 
if __name__ == "__main__": 
    f = input()
    partOne(f)
    partTwo(f)