def number5():
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
            l_ranges.append(range(l_line[0], l_line[1] + 1))
        else:
            l_ingredients.append(int(line))
            
    i_fresh = 0
    for ing in l_ingredients:
        for rng in l_ranges:
            if ing in rng:
                i_fresh += 1
                break
                
    print("Day 5_1: The number of fresh ingredients is: " + str(i_fresh))
    
    l_fresh_ranges = []
    for rng in l_ranges:
        i_start = rng[0]
        i_end = rng[-1]
        if not l_fresh_ranges:
            l_fresh_ranges.append(i_start)
            l_fresh_ranges.append(i_end)
        else:
            l_aux = []
            i = 0
            while i < len(l_fresh_ranges):
                current = l_fresh_ranges[i]
                if i % 2 == 0: # even, current is a range start
                    if i_start <= current: # it is before
                        if i_end < current: # it is also before
                            l_aux.extend([i_start, i_end])
                            l_aux.extend(l_fresh_ranges[i:])
                            l_fresh_ranges = l_aux.copy()
                            break # The range is included in the list
                        else: # The end is beyond current
                            l_aux.append(i_start)
                            if i == len(l_fresh_ranges) - 1: # The last
                                l_aux.append(i_end)
                                l_fresh_ranges = l_aux.copy()
                                break # it is not necesary but ... 
                            else:
                                i += 1
                                is_done = False
                                while i < len(l_fresh_ranges):
                                    current = l_fresh_ranges[i]
                                    if i_end < current: # Add it and finish
                                        if i % 2 == 0: #even, the end is i_end
                                            l_aux.append(i_end)
                                            l_aux.extend(l_fresh_ranges[i:])
                                        else: # odd, the end is the current                                        
                                            l_aux.append(current)
                                            l_aux.extend(l_fresh_ranges[i+1:])
                                        is_done = True
                                        break
                                    else: # continue in the list
                                        i += 1
                                if is_done:
                                    l_fresh_ranges = l_aux.copy()
                                    break
                                if i == len(l_fresh_ranges): # the end
                                    l_aux = l_aux.append(i_end)
                                    l_fresh_ranges = l_aux.copy()
                                    break
                                
                    else: # i_start is after current, continue in the list
                        l_aux.append(current)
                
                else: # odd, current is a range end
                    if i_start <= current: # it is before or equal
                        if i_end <= current: # the range is completely included, nothing to do
                            break
                        else: # The end is beyond current
                            if i == len(l_fresh_ranges) - 1: # The last
                                l_aux.append(i_end)
                                l_fresh_ranges = l_aux.copy()
                                break # it is not necesary but ... 
                            else:
                                i += 1
                                is_done = False
                                while i < len(l_fresh_ranges):
                                    current = l_fresh_ranges[i]
                                    if i_end < current: # Add it and finish
                                        if i % 2 == 0: #even, the end is i_end
                                            l_aux.append(i_end)
                                            l_aux.extend(l_fresh_ranges[i:])
                                        else: # odd, the end is the current                                        
                                            l_aux.append(current)
                                            l_aux.extend(l_fresh_ranges[i+1:])
                                        is_done = True
                                        break
                                    else: # continue in the list
                                        i += 1
                                if is_done:
                                    l_fresh_ranges = l_aux.copy()
                                    break
                                if i == len(l_fresh_ranges): # the end
                                    l_aux.append(i_end)
                                    l_fresh_ranges = l_aux.copy()
                                    break
                    else: # i_start is after the current, continue in the list
                        l_aux.append(current)
                        if i == len(l_fresh_ranges) - 1: # The last
                            l_aux.extend([i_start, i_end])
                            l_fresh_ranges = l_aux.copy()
                            break
                    
                i += 1
                if i == len(l_fresh_ranges):
                    l_fresh_ranges = l_aux.copy()
        
    total_fresh = 0
    i = 0
    while i in range(0, len(l_fresh_ranges) - 1):
        total_fresh += l_fresh_ranges[i + 1] - l_fresh_ranges[i] + 1
        i += 2
        
    print("Day 5_2: The number of fresh ingredients is: " + str(total_fresh))
    

number5()
        