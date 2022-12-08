def input(): 
    with open("./input.txt") as fin: 
        lines = fin.read()

    return list(lines)

def solution(signal, length): 
    marker = []

    for i, v in enumerate(signal): 
        # check if letter already in marker 
        # if in marker, remove all items until initial instance
        if v in marker: 
            marker = marker[marker.index(v)+1:]

        # add new signal 
        marker.append(v)

        # if marker is required length, return index of newest signal
        if len(marker) >= length: 
            return i+1
        
if __name__ == "__main__": 
    f = input()
    print("Part 1:", solution(f, 4))
    print("Part 2:", solution(f, 14))
