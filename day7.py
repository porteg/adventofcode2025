SPACE = "."
SPLITTER = "^"
START = "S"

def number7_1():
    dataFile = open("data/day7.txt", "r")
    
    manifold = []
    index = 0
    row = 0
    col = 0
    for line in dataFile:
        line = line.replace("\n", "")
        s_line = list(line)
        if START in s_line: 
            row = index
            col = s_line.index(START)
        index += 1
        manifold.append(list(line))
    
    l_tach = [(row, col)]
    i_splits = 0
    for i in range(0, len(manifold)):
        l_aux = []
        for (r, c) in l_tach:
            if r < len(manifold) - 1: 
                if manifold[r + 1][c] == SPACE:
                    if (r + 1, c) not in l_aux:
                        l_aux.append((r + 1, c))
                else:
                    i_splits += 1
                    if (r + 1, c - 1) not in l_aux:
                        l_aux.append((r + 1, c - 1))
                    if (r + 1, c + 1) not in l_aux:
                        l_aux.append((r + 1, c + 1))
        l_tach = l_aux.copy()
        
    print("Day 7.1, the number of splits are " + str(i_splits))
    
number7_1()
        
    