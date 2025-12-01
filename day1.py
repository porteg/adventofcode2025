def number1_1():
    dataFile = open("data/day1.txt", "r")
    
    start = 50
    password = 0
    
    for line in dataFile:
        line = line.replace("\n", "")
        
        s_direction = line[0:1]
        i_move = int(line[1:])
        i_move = i_move % 100 
        
        if s_direction == "R":
            start = (start + i_move) % 100
        else:
            start = (start - i_move) 
            if start < 0:
                start = 100 - abs(start)
                
        if start == 0:
            password = password + 1
            
    print("Day 1_1: The password is " + str(password))
    
def number1_2():
    dataFile = open("data/day1.txt", "r")
    
    start = 50
    start_orig = start
    password = 0
    
    for line in dataFile:
        line = line.replace("\n", "")
        
        s_direction = line[0:1]
        i_move = int(line[1:])
        
        i_laps = i_move // 100
        if i_laps > 0:
            password = password + i_laps
        
        
        i_move = i_move % 100 
        
        if s_direction == "R":
            start = (start + i_move) % 100
        else:
            start = (start - i_move) 
            if start < 0:
                start = 100 - abs(start)
                
        if start == 0:
            password = password + 1
        elif s_direction == "R" and ((start_orig + i_move) > 100) and start_orig != 0: 
            password = password + 1
        elif s_direction == "L" and ((start_orig - i_move) < 0) and start_orig != 0:
            password = password + 1
            
        start_orig = start 
            
    print("Day 1_2: The password is " + str(password))
    
number1_1()
number1_2()