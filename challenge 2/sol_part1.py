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
    # Checking instances of a character in the password
    count = password.count(letter)
    # Checking if the policy is followed
    if count >= lower_bound and count <= upper_bound:
        valid += 1

print(valid)
