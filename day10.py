import heapq

ON = "#"
OFF = "."

# Dijstra funtion receives visited grid and two points. The last parameter is the 
# start value for the starting point
def dijskstra(machine, start, risk = 0):
    # queue is the list of points to be visited, always taken by risk (the least the best)
    # minRisk is the hash map with the points that has minimum value, they do not need to be visited again
    queue = [] # risk (number of cliks on buttons), lights and button pulsed
    heapq.heappush(queue, (risk, start, []))
    target_indicator = machine[0]
    buttons = machine[1]
    
    min_button_pulsed = -1
    
    visited = [start]
    while queue:
        risk, current_indicator, buttons_pulsed = heapq.heappop(queue)

        for button in buttons:
            # if buttons_pulsed and buttons_pulsed[-1] == button: # A button pulsed twice 
            if button in buttons_pulsed: # A button cannot be pulsed more than one time ¿¿¿???
                continue
            
            aux_indicator = current_indicator.copy()
            for light in button:
                if aux_indicator[light] == OFF: 
                    aux_indicator[light] = ON
                elif aux_indicator[light] == ON:
                    aux_indicator[light] = OFF
                
            if aux_indicator == target_indicator: # End, we have found the combination
                if min_button_pulsed == -1:
                    min_button_pulsed = risk + 1
                else:
                    min_button_pulsed = min([min_button_pulsed, risk + 1])
            else: # Added the new position to queue 
                if aux_indicator not in visited: # Testing the loop
                    if min_button_pulsed != -1 and risk + 1 >= min_button_pulsed:
                        continue
                    
                    aux = buttons_pulsed.copy()
                    aux.append(button)
                    heapq.heappush(queue, (risk + 1, aux_indicator, aux))
                    visited.append(aux_indicator)
            
    return min_button_pulsed

def number10():
    dataFile = open("data/day10.txt", "r")
    
    machines = []
    for line in dataFile:
        line = line.replace("\n", "")
        s_line = line.split(" ")
        
        indicator = list(s_line[0][1:-1])
        
        buttons = []
        for i in range(1, len(s_line)):
            if s_line[i].startswith("{"):
                break
            button = s_line[i][1:-1].split(",")
            buttons.append(list(map(int,button)))
        
        joltages = s_line[-1][1:-1].split(",")
        
        machines.append([indicator, buttons, joltages])
        
    total = 0
    for machine in machines:
        indicator = machine[0]
        
        start = list(OFF * len(indicator))
            
        res = dijskstra(machine, start, 0)
        total += res
        print("Result machine --> " + str(res))
        
    print("Day 10_1: The total button pressed are " + str(total))
    
number10()