def print_crates(cmap): 
    for row in cmap: 
        print(row)

def input(): 
    with open("./input.txt") as fin: 
        lines = fin.read().strip().split('\n\n')

    res = []
    # step up crates
    crates = lines[0].split('\n')
    cmap = [ [] for _ in range(9) ] # crate map

    for r in range(0, len(crates)-1):
        row = crates[r] 
        for c, crate in enumerate(range(1, len(row), 4)): 
            if row[crate] != ' ': 
                cmap[c].insert(0, (row[crate]))

    # set up instructions
    instructions = lines[1].split('\n')
    # list of (num, from, to)
    instruct_list = []
    for instruction in instructions: 
        t = instruction.split(' ')
        instruct_list.append((int(t[1]), int(t[3]), int(t[5])))

    return cmap, instruct_list

def solution(crates, instructions, reverse=True): 
    # instruction written as (num, from, to)
    for instruction in instructions: 
        _num = instruction[0]
        _from = instruction[1] - 1 
        _to = instruction[2] - 1
        move = crates[_from][-_num:]
        crates[_from] = crates[_from][:-_num]
        
        if reverse: 
            move.reverse()

        crates[_to] = crates[_to] + move

    print_crates(crates)
    res = ''
    for row in crates: 
        res += row[-1]

    print(res)

if __name__ == "__main__": 
    crates, instructions = input()
    solution(crates, instructions, reverse=True)

    crates, instructions = input()
    solution(crates, instructions, reverse=False)
