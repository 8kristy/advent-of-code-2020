with open("input", "r") as f:
    groups = f.read().split("\n\n")

total = 0
# Counting the questions where someone in the group answered a question 
for group in groups:
    group = group.replace("\n", "")
    total += len("".join(set(group)))    

print(total)    