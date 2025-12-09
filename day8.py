import math

distances = dict()

def mergeCircuits(l_circuits):
    l_aux = []
    l_aux_2 = l_circuits.copy()
    added = False 
    removed = True
    while removed:
        l_aux = []
        removed = False
        for circuit in l_aux_2:
            added = False
            for aux in l_aux:
                if len(aux & circuit) > 0:
                    aux.update(circuit)
                    added = True
                    removed = True
                    break
            if not added:
                l_aux.append(circuit)
        l_aux_2 = l_aux.copy()
        
    return l_aux
            
def quick_sort_length(l_circuits):
    if len(l_circuits) <= 1:
        return l_circuits

    l_pivot = l_circuits[0].copy()
    pivot = len(l_pivot)
    left = []
    for l_aux in l_circuits[1:]:
        if len(l_aux) >= pivot:
            left.append(l_aux.copy())
    right = []
    for l_aux in l_circuits[1:]:
        if len(l_aux) < pivot:
            right.append(l_aux.copy())
    return quick_sort_length(left) + [l_pivot] + quick_sort_length(right)
    
    
# Modified to order list of junction boxes by distance
def quick_sort(l_distances):
    if len(l_distances) <= 1:
        return l_distances
    (box, target) = l_distances[0]
    (box_target, pivot) = target
    left = []
    for (box, (tgt, val)) in l_distances[1:]:
        if val < pivot:
            left.append((box, (tgt, val))) 
    right = []
    for (box, (tgt, val)) in l_distances[1:]:
        if val >= pivot:
            right.append((box, (tgt, val)))
    return quick_sort(left) + [l_distances[0]] + quick_sort(right)
    
def distance(p1, p2):
    aux = math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2) + math.pow(p2[2] - p1[2], 2)
    # return math.sqrt(aux)
    return aux

def number8_1(max):
    dataFile = open("data/day8.txt", "r")
    
    boxes = []
    
    for line in dataFile:
        line = line.replace("\n", "")
        
        s_line = line.split(",")
        boxes.append(tuple(list(map(int, s_line))))

    l_distances = []
    for i in range(0, len(boxes)):
        box_1 = boxes[i]
        for j in range(i + 1, len(boxes)):
            box_2 = boxes[j]
            d = distance(boxes[i], boxes[j])
            l_distances.append((box_1, (box_2, d)))
        
    l_distances = quick_sort(l_distances)

    l_circuits = []
    for (box_1, (box_2, d)) in l_distances:
        if max == 0:
            break
        else:
            max -= 1
        added = False
        for i in range(0, len(l_circuits)):
            circuit = l_circuits[i]
            if box_1 in circuit or box_2 in circuit:
                circuit.update({box_1, box_2})
                added = True
                break
        if not added:
            l_circuits.append({box_1, box_2})
    
    
    l_circuits = mergeCircuits(l_circuits)
    
    l_circuits = quick_sort_length(l_circuits) 
    
    total = len(l_circuits[0]) * len(l_circuits[1]) * len(l_circuits[2])
    
    print("Result day 8_1: " + str(total)) 
    
number8_1(1000)
        
        
    