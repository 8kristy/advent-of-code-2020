pattern = ""
memory = dict()

def get_mem_combs(mem_loc, pattern):
    mem_loc = bin(mem_loc)[2:]
    # Padding the address
    mem_loc = '0' * (36 - len(mem_loc)) + mem_loc
    new_mem_loc = ""
    # Replacing values with the rules defined 
    for idx, num in enumerate(pattern):
        if num == "X" or num == "1":
            new_mem_loc += num
        else:
            new_mem_loc += mem_loc[idx]
    
    # Getting all the combinations using an iterative binary counter type of thing
    combs = [new_mem_loc.replace("X", "1", 1), new_mem_loc.replace("X", "0", 1)]
    for comb in combs:
        # Check for X so that it doesn't just add empty strings and get stuck in a loop
        if "X" in comb:
            combs.append(comb.replace("X", "1", 1))
            combs.append(comb.replace("X", "0", 1))

    # Filter out any leftover strings with Xs
    return [int(x, 2) for x in combs if "X" not in x]


with open("input", "r") as f:
    for line in f:
        if "mask" in line:
            pattern = line[line.find("=") + 2:].strip()
            x_count = pattern.count("X")   
        if "mem" in line:
            mem_loc = int(line[line.find("[") + 1:line.find("]")])
            num = int(line[line.find("=") + 2:])
            for comb in get_mem_combs(mem_loc, pattern):
                memory[comb] = num

sum = 0
for item in memory:
    sum += memory[item]

print(sum)