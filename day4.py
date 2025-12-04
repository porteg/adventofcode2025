def isAccessible(grid, row, col):
    n_rolls = 0
    for i in [row - 1, row, row + 1]:
        if i >= 0 and i < len(grid):
            for j in [col - 1, col, col + 1]:
                if j >= 0 and j < len(grid[i]):
                    if not (i == row and j == col):
                        n_rolls += (1 if grid[i][j] == ROLL else 0)
                        if n_rolls == 4: 
                            return False
    
    return n_rolls < 4
    
ROLL = "@"
EMPTY = "."
    
def number4_1():
    dataFile = open("data/day4.txt", "r")
    
    grid = []
    for line in dataFile:
        line = line.replace("\n", "")
        grid.append(line)
        
    rolls = 0
    for i in range(0, len(grid)):
        for j in range (0, len(grid[i])):
            if grid[i][j] == ROLL:
                if isAccessible(grid, i, j):
                    rolls += 1
                
    print("Day 4-1. The number of rolls accessible are " + str(rolls))

number4_1()
        