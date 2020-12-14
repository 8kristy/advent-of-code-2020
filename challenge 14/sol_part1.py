pattern = ""
and_pattern = ""
memory = dict()

with open("input", "r") as f:
    for line in f:
        if "mask" in line:
            pattern = line[line.find("=") + 2:]
            and_pattern = int(pattern.replace("1", "0").replace("X", "1"), 2)
            pattern = int(pattern.replace("X", "0"), 2)
        # We can replace the bits by first deleting the bits at the positions which
        # aren't X, then replace them with our new values; use an AND operation
        # to delete and and OR operation to replace bits
        if "mem" in line:
            mem_loc = int(line[line.find("[") + 1:line.find("]")])
            num = int(line[line.find("=") + 2:])
            num = num & and_pattern
            num = num | pattern
            memory[mem_loc] = num

sum = 0
for item in memory:
    sum += memory[item]

print(sum)