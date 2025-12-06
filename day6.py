import math

SUM = "+"
MULTI = "*"     

def operateSpecial(matrix):
    grandTotal = 0
    
    col = len(matrix[0]) - 1
    l_numbers = []
    while col >= 0:
        number = ""
        for row in range(0, len(matrix)):
            value = matrix[row][col]
            if row == len(matrix) - 1: # The last
                if not value == SUM and not value == MULTI:
                    if not number.replace(" ", "") == "":
                        l_numbers.append(number)
                else:
                    if len(l_numbers) > 0:
                        l_numbers.append(number)
                        l_numbers = list(map(int, l_numbers))
                        if value == SUM:
                            grandTotal += sum(l_numbers)
                        else: 
                            grandTotal += math.prod(l_numbers)     
                        l_numbers = []
                col = col - 1
                break               
            else:
                number = number + value
    
    return grandTotal

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
    
def number6_2():
    dataFile = open("./data/day6.txt", "r")
    math_grid = []
    
    for line in dataFile:
        line = line.replace("\n", "")
        s_line = list(line)
        
        math_grid.append(s_line)
    
    grand_total = 0
    grand_total = operateSpecial(math_grid)
        
    print("Day 6 part 2: The grand total is " + str(grand_total))
        
number6_1()
number6_2()
            