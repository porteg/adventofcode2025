import heapq

START = "svr"
END = "out"
DAC = "dac"
FFT = "fft"
SPECIAL_MACHINES = set(["dac", "fft"])

machine_paths = dict()

def getAllPaths(machines, start, target, current_path):
    if start in machine_paths.keys():
        return machine_paths[start]

    paths_completed = paths_with_dac = paths_with_fft = paths_with_out = 0

    outputs = machines[start]
    for output in outputs:
        if output in machine_paths.keys():
            aux = machine_paths[output]
            paths_completed += aux[0]
            paths_with_dac += aux[1]
            paths_with_fft += aux[2]
            paths_with_out += aux[3]
        else:
            if output == target:
                paths_with_out += 1
            else:
                str_current_path = ",".join(current_path)
                str_current_machine_output = start + "," + output
                if str_current_path.find(str_current_machine_output) != -1: # a loop
                    continue

                aux = current_path.copy()
                aux.append(output)
                res = getAllPaths(machines, output, target, aux)
                paths_completed += res[0]
                paths_with_dac += res[1]
                paths_with_fft += res[2]
                paths_with_out += res[3]                

    if start == DAC:
        paths_with_dac = paths_with_out
        if paths_with_fft > 0:
            paths_completed += paths_with_fft        

    elif start == FFT:
        paths_with_fft = paths_with_out
        if paths_with_dac > 0:
            paths_completed += paths_with_dac

    machine_paths[start] = (paths_completed, paths_with_dac, paths_with_fft, paths_with_out)

    return machine_paths[start]

def number11_2():
    dataFile = open("data/day11.txt", "r")

    machines = dict()

    for line in dataFile:
        line = line.replace("\n", "")
        s_line = line.split(": ")
        outputs = s_line[1].split(" ")
        machines[s_line[0]] = outputs

    res = getAllPaths(machines, START, END, [START])

    print("Day 11 part 2: Number of paths " + str(res[0]))

number11_2()