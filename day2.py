def number2_1():
    dataFile = open("data/day2.txt", "r")
    
    line = dataFile.readline()
    line = line.replace("\n", "")
    
    l_ranges = line.split(",")
    
    invalidIds = 0
    totalValue = 0
    
    for entry in l_ranges:
        l_range = entry.split("-")
        ids = range(int(l_range[0]), int(l_range[1]))
        for id in ids:
            s_id = str(id)
            part1 = s_id[:len(s_id)//2]
            part2 = s_id[len(s_id)//2:]
            
            if part1 == part2:
                invalidIds += 1
                totalValue += id
                
    print("Day 2-1: Númber of invalid ids " + str(invalidIds) + " with total value of " + str(totalValue))

def isInvalid(id):
    s_id = str(id)
    
    s_chain = ""
    for i in range(0, len(s_id) // 2):
        s_chain = s_chain + s_id[i]
        s_aux = s_id.replace(s_chain, "")
        if s_aux == "":
            return True
        
    return False
    
    
def number2_2():
    dataFile = open("data/day2.txt", "r")
    
    line = dataFile.readline()
    line = line.replace("\n", "")
    
    l_ranges = line.split(",")
    
    invalidIds = 0
    totalValue = 0
    
    for entry in l_ranges:
        l_range = entry.split("-")
        ids = range(int(l_range[0]), int(l_range[1]))
        for id in ids:
            if isInvalid(id):
                invalidIds += 1
                totalValue += id
        
    print("Day 2-2: Númber of invalid ids " + str(invalidIds) + " with total value of " + str(totalValue))

number2_1()
number2_2()
