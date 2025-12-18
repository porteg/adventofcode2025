def quick_sort_segments(l_segments):
    if len(l_segments) <= 1:
        return l_segments

    l_pivot = l_segments[0]
    pivot = l_pivot[0] # the value
    left = []
    for l_aux in l_segments[1:]:
        if l_aux[0] <= pivot:
            (a, b, c) = l_aux
            left.append((a, b, c))
    right = []
    for l_aux in l_segments[1:]:
        if l_aux[0] > pivot:
            (a, b, c) = l_aux
            right.append((a, b, c))
    return quick_sort_segments(left) + [l_pivot] + quick_sort_segments(right)

# Receive a list of vertical segments to be sure how many are crossed until arrive to x,y.
def insideVerticalSegment(l_segments, p_x, p_y):
    UP = 1
    DOWN = 2
    OTHER = -1

    i = 0
    inside = False
    lastInLine = OTHER
    previous = inside
    
    while i < len(l_segments):
        (x, y1, y2) = l_segments[i]
        if p_x >= x: # beyond
            if p_y > y1 and p_y < y2: # beyond so crossed 
                lastInLine = OTHER
                if x == p_x: # point in the border
                    previous = not inside
                    inside = True                    
                else:
                    previous = inside
                    inside = not inside
            elif p_y == y1: # UP or 1
                if lastInLine == OTHER: # There is not an horizontal segment open, its a F
                    lastInLine = UP
                    previous = inside
                    inside = True
                elif lastInLine == UP: # F - 7
                    if x == p_x: # point x, y in the border
                        inside = True
                        break
                    else:
                        inside = previous # IN - IN, OUT - OUT        
                        lastInLine = OTHER                        
                else: # lastInLine == DOWN, L - 7
                    if x == p_x: # point x, y in the border
                        inside = True
                        break
                    else:
                        inside = not previous # IN - OUT, OUT - IN
                        lastInLine = OTHER
            elif p_y == y2: # DOWN or 2
                if lastInLine == OTHER: # There is not an horizontal segment open 
                    lastInLine = DOWN
                    previous = inside
                    inside = True
                elif lastInLine == UP: # F - J
                    if x == p_x: # point x, y in the border
                        inside = True
                        break 
                    else:
                        if previous:
                            inside = False # IN - OUT
                        else:
                            inside = True # OUT - IN
                        lastInLine = OTHER
                else: # lastInLine = DOWN, L - J
                    if x == p_x: # point x, y in the border
                        inside = True
                        break
                    else:
                        inside = previous # IN - IN , OUT - OUT 
                        lastInLine = OTHER
        
        i += 1
        
    return inside

# Look if the segment defined by p1 and p2 cross any vertical segment
# If cross anything, it is outside at least do it
def segmentCrossVertical(p1, p2, v_segments):
    (p1_x, p1_y) = p1
    (p2_x, p2_y) = p2
    
    # Order the x values
    l_x = min([p1_x, p2_x])
    u_x = max([p1_x, p2_x])
    
    # A segment is a value and a range, the value is x, the range y
    # The p1-p2 cross a vertical if l_x < x < u_x and y is inside the range
    
    n_c = 0
    for seg in v_segments:
        (x, y1, y2) = seg
        if p1_y > y1 and p1_y < y2: #inside
            if l_x < x < u_x:
                return True
            
    return False
        
# Look if the segment defined by p1 and p2 cross any horizontal segment
def segmentCrossHorizontal(p1, p2, h_segments):  
    (p1_x, p1_y) = p1
    (p2_x, p2_y) = p2
    
    # Order the y values
    l_y = min([p1_y, p2_y])
    u_y = max([p1_y, p2_y])
    
    # A segment is a value and a range, the value is y, the range x
    # The p1 - p2 cross an horizntal p1_y < y < p2_y and x inside the range
    for seg in h_segments:
        (y, x1, x2) = seg 
        if p1_x > x1 and p1_x < x2:
            if l_y < y < u_y:
                return True
    
    return False                                   

def area(p1, p2):
    b = abs(p1[0] - p2[0]) + 1
    a = abs(p1[1] - p2[1]) + 1
    
    return b * a
    
def number9_1():
    dataFile = open("data/day9.txt", "r")
    
    redTiles = []
    for line in dataFile:
        line = line.replace("\n", "")
        redTiles.append(list(map(int,line.split(","))))
        
    current = 0
    for i in range(0, len(redTiles)):
        for j in range(i + 1, len(redTiles)):
            aux = area(redTiles[i], redTiles[j])
            if aux > current:
                current = aux
    
    print("Day 9 part 1: The biggest rectangule is " + str(current))
        
def number9_2():
    dataFile = open("data/day9.txt", "r")
    
    v_segments = []
    h_segments = []
    redTiles = []
    
    # Reading vertix
    redTiles = []
    for line in dataFile:
        line = line.replace("\n", "")
        redTiles.append(list(map(int,line.split(","))))
        
    # Generating poligon sides
    for i in range(0, len(redTiles)):    
        (x1, y1) = redTiles[i]
        if i == len(redTiles) - 1:
            (x2, y2) = redTiles[0]
        else:
            (x2, y2) = redTiles[i + 1]
        
        if x1 == x2: # Same vertical, range in y
            up = y1 if y1 < y2 else y2
            down = y1 if y1 > y2 else y2 
            v_segments.append((x1, up, down))
        else: # y1 == y2 same horizontal 
            up = x1 if x1 < x2 else x2
            down = x1 if x1 > x2 else x2
            h_segments.append((y1, up, down))
        
    v_segments = quick_sort_segments(v_segments)
    h_segments = quick_sort_segments(h_segments)
    
    current = 0
    current_v1 = current_v2 = None
    
    for i in range(0, len(redTiles)):
        (x1, y1) = p1 = redTiles[i]
        for j in range(i + 1, len(redTiles)):
            # Test if all the area is formed by green tiles
            (x2, y2) = p2 = redTiles[j]
            
            aux = area(p1, p2)
            # Same vertical line, both are vertix, so test if the line is inside not crossing any horizontal 
            if x1 == x2: 
                if not segmentCrossHorizontal(p1, p2, h_segments):         
                    current = aux if aux > current else current
            # Same horizontal line, both are vertix, so test if the line is inside not crossing any vertical
            elif y1 == y2: # same valur for y, vertical                
                if not segmentCrossVertical(p1, p2, v_segments):
                    current = aux if aux > current else current
            # p2 in cuadrant 1, 2, 3 or 4
            elif (x1 > x2 and y1 > y2) or (x1 < x2 and y1 > y2) or (x1 < x2 and y1 < y2) or (x1 > x2 and y1 < y2):
                if aux > current: # test if the new area should be better
                    if (insideVerticalSegment(v_segments, x1, y2) and
                        insideVerticalSegment(v_segments, x2, y1)):
                        if (not segmentCrossVertical(p2, (x1, y2), v_segments) and
                            not segmentCrossVertical((x2, y1), p1, v_segments) and
                            not segmentCrossHorizontal(p2, (x2, y1), h_segments) and
                            not segmentCrossHorizontal((x1, y2), p1, h_segments)
                        ):
                            current = aux
                            current_v1 = p1
                            current_v2 = p2
            
    print("Day 9 part 2: The biggest rectangule is " + str(current) + " v: " + str(current_v1) + ", " + str(current_v2))
    
number9_1()
number9_2()