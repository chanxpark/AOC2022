def input(): 
    with open("./input.txt") as fin: 
        lines = fin.read().strip().split()

    res = []

    for line in lines: 
        pairs = line.split(',')
        res.append([list(map(int, pair.split('-'))) for pair in pairs])

    return res

def partOne(lines): 
    res = 0 
    
    for n in lines: 
        # check which line is larger 
        if n[0][1] - n[0][0] >= n[1][1] - n[1][0]:
            larger = n[0]
            smaller = n[1]
        else: 
            larger = n[1]
            smaller = n[0]
        
        # check if smaller line is within smaller line 
        if larger[0] <= smaller[0] and larger[1] >= smaller[1]: 
            res += 1 

    print('Part 1:', res)

def partTwo(lines): 
    res = 0 

    for n in lines: 
        # check which line is larger 
        if n[0][1] - n[0][0] >= n[1][1] - n[1][0]:
            larger = n[0]
            smaller = n[1]
        else: 
            larger = n[1]
            smaller = n[0]

        if larger[0] <= smaller[0] and larger[1] >= smaller[0]: 
            res += 1
        elif larger[0] <= smaller[1] and larger[1] >= smaller[1]: 
            res += 1 

    print('Part 2:', res)

if __name__ == "__main__": 
    f = input()
    partOne(f)
    partTwo(f)
