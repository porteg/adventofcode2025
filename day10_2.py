from pulp import *

def number10_2():
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
        
        joltages = list(map(int, s_line[-1][1:-1].split(",")))
        
        machines.append([indicator, buttons, joltages])
        
    total = 0
    for machine in machines:
        buttons = machine[1]
        joltages = machine[2]

        # Variables, xi is the number of time that button i is pressed (x0, x1, etc.)
        variables = []
        max_value = max(joltages)
        for i in range(0, len(buttons)):
            aux = LpVariable("x" + str(i), 0, None, LpInteger)
            variables.append(aux)
        
        prob = LpProblem("problem", LpMinimize)
        prob += lpSum(variables), "objetivo_min_suma"
        
        # Restrictions
        # Each joltage must be equal to the sum of the pulsations
        for i in range(0, len(joltages)):
            aux = []
            for j in range(0, len(buttons)):
                if i in buttons[j]:
                    aux.append(variables[j])
            prob += lpSum(aux) >= joltages[i]
        
        for i in range(0, len(joltages)):
            aux = []
            for j in range(0, len(buttons)):
                if i in buttons[j]:
                    aux.append(variables[j])
            prob += lpSum(aux) <= joltages[i]
        
        status = prob.solve(GLPK(msg=0))
        LpStatus[status]

        total_machine = 0
        for v in prob.variables():
            total_machine += int(v.varValue)

        total += total_machine

    print("Day 10 part 2: Number of pulsations " + str(total))
            
    
    
number10_2()
    