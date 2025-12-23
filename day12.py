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
    
  #  input("Press Enter to continue...")
    
    
def getLocations(shape, cell, grid):
    (row, col) = cell
    
    # The shape can be in for places (4 cuadrants) using the cell as pivot
    # Cuadrant 1 (cell is the bottom-right corner)
    # Cuadrant 2 (cell is the bottom-left corner)
    # Cuadrant 3 (cell is the top-right corner)
    # Cuadrant 4 (cell is the top-left corner)
    
    # Only try quadrants that have not been tested by other cells before
    row1 = row - (len(shape) - 1)
    col1 = col - (len(shape[0]) - 1)
    row2 = row - (len(shape) - 1)
    col2 = col
    row3 = row - (len(shape) - 1)
    col3 = col + (len(shape[0]) - 1)
    row4 = row 
    col4 = col - (len(shape[0]) - 1)
    
    c1 = []
    c2 = []
    c3 = [] 
    c4 = []
    
    if row1 >= 0 and col1 >= 0 and (row1, col1) in grid:
        c1 = None
    if row2 >= 0 and col2 >= 0 and (row2, col2) in grid:
        c1 = None
        c2 = None
    if row3 >= 0 and col3 >= 0 and (row3, col3) in grid:
        c2 = None
    if row4 >= 0 and col4 >= 0 and (row4, col4) in grid:
        c1 = None
        c4 = None
    
    for i in range(0, len(shape)):
        for j in range(0, len(shape[i])):
            if c1 == c2 == c3 == c4 == None:
                return []
            
            if shape[i][j] == "#":
                # 1
                if c1 != None:
                    pos = row - (len(shape) - 1 - i), col - (len(shape[i]) - 1 - j)
                    if pos in grid and c1 != None:
                        c1.append(pos)
                    else:
                        c1 = None
                # 2
                if c2 != None:
                    pos = row - (len(shape) - i - 1), col + j
                    if pos in grid and c2 != None:
                        c2.append(pos)
                    else: 
                        c2 = None
                # 3
                if c3 != None:
                    pos = row + i, col + j
                    if pos in grid and c3 != None:
                        c3.append(pos)
                    else:
                        c3 = None
                # 4
                if c4 != None:
                    pos = row + i, col - (len(shape[i]) - j - 1)
                    if pos in grid and c4 != None:
                        c4.append(pos)
                    else: 
                        c4 = None
    res = []
    if c1:
        res.append(c1)
    if c2:
        res.append(c2)
    if c3:
        res.append(c3)
    if c4:
        res.append(c4)
        
    return res
    
def canBeInside(shapes, polyminos, grid, grid_sizes):
    
    printGrid(int(grid_sizes[0]), int(grid_sizes[1]), grid)
    
    if len(polyminos) == 0 and len(grid) >= 0:
        return True
    
    if not enoughSpace(shapes, polyminos, grid):
        return False
    
    (type, poly_index) = polyminos[0]
    rotations = shapes[type][1]
    for rotation in rotations:
        for cell in grid:
            locations = getLocations(rotation, cell, grid)
            for location in locations:
                if location:
                    aux = grid.copy()
                    for node in location: 
                        aux.pop(aux.index(node))
                    if canBeInside(shapes, polyminos[1:], aux, grid_sizes):
                        return True
    
    return False
    
def enoughSpace(shapes, polyminos, grid):
    free = len(grid)
    
    required = 0
    for (type, index) in polyminos:
        required += shapes[type][0]
        
    return free >= required
    
def getShapeSize(shape):
    size = 0
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            size += (1 if shape[i][j] == "#" else 0)
    
    return size
            
def rotate(shape, rotation):
    if rotation == 1: # 90 
        res = [
            [shape[2][0],shape[1][0],shape[0][0]],
            [shape[2][1],shape[1][1],shape[0][1]],
            [shape[2][2],shape[1][2],shape[0][2]], 
        ]
    elif rotation == 2: # 180
        res = [
            [shape[2][2],shape[2][1],shape[2][0]],
            [shape[1][2],shape[1][1],shape[1][0]],
            [shape[0][2],shape[0][1],shape[0][0]], 
        ]
    else: # 270
        res = [
            [shape[0][2],shape[1][2],shape[2][2]],
            [shape[0][1],shape[1][1],shape[2][1]],
            [shape[0][0],shape[1][0],shape[2][0]], 
        ]
    
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
                size = getShapeSize(currentShape)
                if i_type in shapes.keys():
                    shapes[i_type][1].append(currentShape)
                else:
                    shapes[i_type] = [size, [currentShape]]
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
        original = shapes[key][1][0]
        for rotation in [1, 2, 3]:
            rotated = rotate(original, rotation)
            if rotated not in shapes[key][1]:
                shapes[key][1].append(rotated)
    
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