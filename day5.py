def number5_1():
    dataFile = open("data/day5.txt", "r")
    
    l_ranges = []
    l_ingredients = []
    b_read_ranges = True
    
    for line in dataFile:
        line = line.replace("\n", "")
        
        if line == "":
            b_read_ranges = False
            continue
            
        if b_read_ranges:
            l_line = list(map(int, line.split("-")))
            l_ranges.append(range(l_line[0], l_line[1]))
        else:
            l_ingredients.append(int(line))
            
    i_fresh = 0
    for ing in l_ingredients:
        for rng in l_ranges:
            if ing in rng:
                i_fresh += 1
                break
                
    print("Day 5_1: The bumber of fresh ingredients is: " + str(i_fresh))

number5_1()
        