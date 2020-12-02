valid = 0

with open("input", "r") as f:
    lines = f.readlines()

for line in lines:
    # Parsing the input line
    components = line.split(" ")
    lower_bound = int(components[0].split("-")[0])
    upper_bound = int(components[0].split("-")[1])
    letter = components[1][0]
    password = components[2]

    # Checking if the policy is followed 
    if (password[lower_bound - 1] == letter) ^ (password[upper_bound - 1] == letter):
        valid += 1

print(valid)
