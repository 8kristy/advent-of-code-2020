valid_numbers = list()

with open("input", "r") as f:
    checking_nearby = False
    sum = 0
    for line in f:
        # Checking the rule lines
        if ":" in line and line.split(":")[1] != "\n":
            rule = line.split(":")[1]

            # Determining the intervals
            valid_interval1 = rule.split("or")[0].strip()
            valid_interval2 = rule.split("or")[1].strip()

            # Adding valid numbers from the interval
            for i in range(int(valid_interval1.split("-")[0]), int(valid_interval1.split("-")[1]) + 1):
                if i not in valid_numbers:
                    valid_numbers.append(i)
            for i in range(int(valid_interval2.split("-")[0]), int(valid_interval2.split("-")[1]) + 1):
                if i not in valid_numbers:
                    valid_numbers.append(i)

        # Going through all nearby tickets and checking if they contain any invalid values
        if checking_nearby:
            for num in [int(x) for x in line.split(",")]:
                if num not in valid_numbers:
                    sum += num

        # Flag to tell that the next entries are nearby tickets
        if "nearby" in line:
            checking_nearby = True
        
    print(sum)
