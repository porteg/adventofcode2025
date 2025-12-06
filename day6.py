SUM = "+"
MULTI = "*"

def operate(matrix, col):
    operand = matrix[-1][col]
    total = None
    for row in range(0, len(matrix) - 1):
        if operand == SUM:
            if not total:
                total = 0
            total += matrix[row][col]
        else:
            if not total:
                total = 1
            total *= matrix[row][col]
            
    return total
    
def number6_1():
    dataFile = open("./data/day6.txt", "r")
    math_grid = []
    
    for line in dataFile:
        line = line.replace("\n", "")
        line = " ".join(line.split())
        s_line = line.split()
        
        if SUM in s_line or MULTI in s_line:
            math_grid.append(s_line)
        else:
            math_grid.append(list(map(int, s_line)))
            
    grand_total = 0
    for i in range(0, len(math_grid[0])):
        grand_total += operate(math_grid, i)
        
    print("Day 6 part 1: The grand total is " + str(grand_total))
        
number6_1()
            