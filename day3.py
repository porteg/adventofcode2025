def getBigger(s_num1, s_num2):
    if int(s_num2) > int(s_num1):
        return s_num2
    
    current = s_num1[0]
    aux_1 = aux_2 = ""
    for i in range(1, len(s_num1)):
        aux_1 = s_num1[i:]
        aux_2 = s_num2[i:]
        if int(aux_2) > int(aux_1):
            return current + aux_2
        else:
            current = current + aux_1[0]
    
    return current

def getJoltage2(bat_bank, n_elements):
    current = "0" * n_elements
        
    for i in range(0, len(bat_bank) - n_elements + 1):
        aux = bat_bank[i:i + n_elements]
        current = getBigger(current, aux)
    
    return int(current)

def getJoltage(bat_bank):   
    current = "00"
    for i in range(0, len(bat_bank) - 1):
        aux = bat_bank[i:i+2]
        if int(aux) > int(current):
            current = aux
        else:
            if int(aux[1]) > int(current[1]):
                current = current[0] + aux[1]
    
    return int(current)

def number3():
    dataFile = open("data/day3.txt", "r")
    
    totalOutput_1 = 0
    totalOutput_2 = 0
    for line in dataFile:
        line = line.replace("\n", "")
        
        # totalOutput += getJoltage(line)
        totalOutput_1 += getJoltage2(line, 2)
        totalOutput_2 += getJoltage2(line, 12)
        
    print("Day 3-1: The total joltage is " + str(totalOutput_1))
    print("Day 3-2: The total joltage is " + str(totalOutput_2))
    
number3()