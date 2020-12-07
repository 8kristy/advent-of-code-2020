rules = dict()

# Put all lines in a more accessible dictionary
def process_line(line:str):
    colour = " ".join(line.split("contain")[0].split(" ")[:-2])
    contains = line.split("contain")[1].split(",")
    rules[colour] = list()
    for col in contains:
        if (not "no other" in col):
            rules[colour].append(" ".join(col.split(" ")[1:-1]))

# Recursive function which calculates how many other bags need to be in current bag
# by checking how many bags are contained within the bags in out current bag and so on
def bags_at_colour(colour:str):
    # Only contains our bag and nothing inside it
    if not rules[colour]:
        return 1

    total = 0
    # Add how many bags are contained in the bag of our colour
    for col in rules[colour]:
        total += int(col.split(" ")[0]) * bags_at_colour(" ".join(col.split(" ")[1:]))
    # Bags contained inside + bag itself
    return total + 1          

with open("input", "r") as f:
    for line in f:
        process_line(line)

# All bags inside shiny gold bag (except shiny gold bag itself)
print(bags_at_colour("shiny gold") - 1)
   