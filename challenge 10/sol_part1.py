with open("input", "r") as f:
    adapters =  [int(x) for x in f.readlines()]
    adapters.sort()

# Start at 1 as we ignored implied 0 and max + 3
one_diff = 1
three_diff = 1   

for i in range(len(adapters) - 1):
    if adapters[i + 1] - adapters[i] == 1:
        one_diff += 1
    if adapters[i + 1] - adapters[i] == 3:
        three_diff += 1

print(one_diff * three_diff)