import heapq

START = "you"
END = "out"

def dijskstra(machines, start, target, risk = 0):
    queue = []
    heapq.heappush(queue, (risk, start, [start]))
        
    paths = []        
    while queue:
        risk, machine, current_path = heapq.heappop(queue)
        outputs = machines[machine]
        
        for output in outputs:
            
            if output == target: 
                current_path.append(target)
                paths.append(current_path)
                continue

            current_str = ",".join(current_path)
            aux_str = machine + "," + output 
            
            if current_str.find(aux_str) != -1:                 
                continue
                       
            aux = current_path.copy()
            aux.append(output)
            heapq.heappush(queue, (risk + 1, output, aux))
            
    return paths

def number11_1():
    dataFile = open("data/day11.txt", "r")

    machines = dict()
    for line in dataFile:
        line = line.replace("\n", "")
        s_line = line.split(": ")
        machines[s_line[0]] = s_line[1].split(" ")
    
    res = dijskstra(machines, START, END, 0)

    print("Day 11 part 1: Number of paths " + str(len(res)))

number11_1()