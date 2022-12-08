from collections import defaultdict

def input(): 
    with open("./input.txt") as fin: 
        lines = fin.read().split('\n')

    return [line.split(' ') for line in lines]

def get_path(path): 
    return '/'.join(path)[1:]

def solution(cmds): 
    path = []
    dirs = defaultdict(int)

    for cmd in cmds: 
        if 'cd' in cmd: 
            path.pop() if cmd[2] == '..' else path.append(cmd[2])

            if get_path(path) not in dirs: 
                dirs[get_path(path)] = 0 

        elif '$' not in cmd: 
            if 'dir' in cmd: 
                continue

            # size to each relevant directory
            p = path.copy()
            while len(p) > 0: 
                _dir = get_path(p)
                size = dirs[_dir]
                dirs[_dir] = size + int(cmd[0])
                p.pop()

    res = 0 
    for n in dirs.values(): 
        res += n if n <= 100_000 else 0

    print('Part 1:', res)
    
    TOTAL_SPACE = 70_000_000
    UPDATE_SPACE = 30_000_000
    SPACE_REQUIRED = abs(TOTAL_SPACE - dirs[''] - UPDATE_SPACE)

    to_delete = ('', dirs[''])
    for key, val in dirs.items(): 
        if val > SPACE_REQUIRED and val < to_delete[1]: 
            to_delete = (key, val)

    print('Part 2:', to_delete[1])
    
if __name__ == "__main__": 
    f = input()
    solution(f)
    
