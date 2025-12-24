def printGrid(rows, cols, grid):
    row = list("#" * cols)
    p_grid = []
    for r in range(0, rows):
        p_grid.append(row.copy())
    
    for r, c in grid:
        p_grid[r][c] = "."
        
    print(" ")
    for r in range(0, len(p_grid)):
        print(" ".join(p_grid[r]))
    print(" ")
    
def canBeInside(shapes, polyminos, grid, grid_sizes):
    
 #   printGrid(int(grid_sizes[0]), int(grid_sizes[1]), grid)

  #  print(polyminos)
    
    if len(polyminos) == 0 and len(grid) >= 0:
        return True
    
    if not enoughSpace(shapes, polyminos, grid):
        return False
    
    (type, poly_index) = polyminos[0]
    rotations = shapes[type]
    for rotation in rotations:
        for cell in grid:
            if cell in grid: # it is a free cell
                res = canBeAdded(rotation, cell, grid, grid_sizes)
                if res != None:
                    aux = [ node for node in grid if node not in res ]
                    if canBeInside(shapes, polyminos[1:], aux, grid_sizes):
                        return True
    
    return False

def canBeAdded(shape, cell, grid, grid_sizes):
    aux = []
    row, col = cell
    rows = int(grid_sizes[0]) - 1
    cols = int(grid_sizes[1]) - 1
    for r, c in shape:
        new_row = row + r
        new_col = col + c
        if new_row > rows or new_col > cols:
            return None
        if (new_row, new_col) not in grid:
            return None
        aux.append((new_row, new_col))
    
    return aux
    
def enoughSpace(shapes, polyminos, grid):
    free = len(grid)
    
    required = 0
    for (type, index) in polyminos:
        required += len(shapes[type][0])
        
    return free >= required
            
def rotate(shape, rotation):
    res = []
    if rotation == 1: # 90 
        for (r, c) in shape:
            row = c
            col = 2 if r == 0 else (r + 2) % 2
            res.append((row, col))
    elif rotation == 2: # 180
        for (r, c) in shape:
            row = 2 if r == 0 else (r + 2) % 2
            col = 2 if c == 0 else (c + 2) % 2
            res.append((row, col))
    else: # 270
        for (r, c) in shape:
            row = 2 if c == 0 else (c + 2) % 2
            col = r
            res.append((row, col))
    
    return res

def number12():
    dataFile = open("data/day12.txt", "r")
    
    i_type = None
    problems = []
    currentShape = []
    shapes = dict()
    for line in dataFile:
        line = line.replace("\n", "")
        
        if line == "":
            if currentShape:
                shape = []
                for i in range(0, len(currentShape)):
                    for j in range(0, len(currentShape[i])):
                        if currentShape[i][j] == "#":
                            shape.append((i, j))
                if i_type in shapes.keys():                        
                    shapes[i_type].append(shape)
                else:
                    shapes[i_type] = [shape]
                    
                currentShape = []
            continue
        
        if ":" in line and not "x" in line:
            i_type = int(line[0])
        elif "x" in line:
            s_line = line.split(": ")
            grid = s_line[0].split("x")
            shape_nums = list(map(int, s_line[1].split(" ")))
            problems.append((grid, shape_nums))
        else:
            currentShape.append(list(line))
    
    # generating the rotations
    for key in shapes.keys():
        original = shapes[key][0]
        for rotation in [1, 2, 3]:
            rotated = rotate(original, rotation)
            if rotated not in shapes[key]:
                rotated.sort()
                shapes[key].append(rotated)
    
    total = 0
    for problem in problems:            
        # generating the polyminos list, (type, index)
        polyminos = [] 
        shape_nums = problem[1]
        for i in range(0, len(shape_nums)):
            for j in range(0, shape_nums[i]):
                polyminos.append((i, j))
                
        # generating the grid list usin the X alg 
        grid_matrix = []
        grid_sizes = problem[0]
        for i in range(0, int(grid_sizes[0])):
            for j in range(0, int(grid_sizes[1])):
                grid_matrix.append((i,j))
                
        # The soluiton will be a backtracking with some inteligence. The backtraking will be done using recurrence
        # because of the number of polyminos to add can be covered without full the stack. All the possible rotations
        # will be covered in the same recurrence level
        
        res = canBeInside(shapes, polyminos, grid_matrix, grid_sizes)
        if res:
            print("Problem ok")
            total += 1
        else:
            print("Problem ko")
            
    print("Day 12_1: Number of regions that can fix --> " + str(total))
    
number12()