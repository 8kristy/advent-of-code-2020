rules = dict()

# Put all lines in a more accessible dictionary
def process_line(line:str):
    colour = " ".join(line.split("contain")[0].split(" ")[:-2])
    contains = line.split("contain")[1].split(",")
    rules[colour] = list()
    for col in contains:
        rules[colour].append(" ".join(col.split(" ")[2:-1]))

with open("input", "r") as f:
    for line in f:
        process_line(line)

# Which colours we need to go over from previous iteration
prev_list = ['shiny gold']
# prev_list is moved here so that we can fill up prev_list with new colours
curr_list = list()
# Only need to add a colour once so check it doesn't already exist
all_colours = list()

total = 0

# Use an iterative approach to see what bags can contain the shiny gold bag,
# and then check what bags can contain those bags and so on
# until we can't find any bags which could contain bags from previous iteration
while prev_list:
    curr_list = prev_list
    prev_list = list()
    
    # Go through all colours and check if any of the 
    # colours we had in the previous iteration are present
    for colour in rules:
        for item in curr_list:
            if item in rules[colour]:
                if (colour not in all_colours):
                    total += 1
                    prev_list.append(colour)
                    all_colours.append(colour)

print(total)                