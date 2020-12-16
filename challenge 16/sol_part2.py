valid_numbers = dict()
valid_tickets = list()
nearby_possible = dict()
my_ticket = ""

with open("input", "r") as f:

    checking_nearby = False
    checking_my_ticket = False

    # Tracking position in the nearby_possible list
    pos_idx = 0

    for line in f:
        # Checking the rule lines
        if ":" in line and line.split(":")[1] != "\n":
            rule = line.split(":")[1]
            rule_name = line.split(":")[0]

            # Determining the intervals
            valid_interval1 = rule.split("or")[0].strip()
            valid_interval2 = rule.split("or")[1].strip()

            # Adding valid numbers from the interval
            for i in range(int(valid_interval1.split("-")[0]), int(valid_interval1.split("-")[1]) + 1):
                if rule_name not in valid_numbers:
                    valid_numbers[rule_name] = list()
                valid_numbers[rule_name].append(i)

            for i in range(int(valid_interval2.split("-")[0]), int(valid_interval2.split("-")[1]) + 1):
                if rule_name not in valid_numbers:
                    valid_numbers[rule_name] = list()
                valid_numbers[rule_name].append(i)

        # Intersects the possible values to check what the position on the ticket could mean
        # (same number must be valid for all words in all tickets)
        if checking_nearby:
            for idx, num in enumerate([int(x) for x in line.split(",")]):
                # Getting all possibilities for a position in a ticket
                possibility = list()
                for key in valid_numbers:
                    if num in valid_numbers[key]:
                        possibility.append(key)
                # Updating what the ticket could mean
                if possibility:
                    nearby_possible[idx] = set(nearby_possible[idx]) & set(possibility)
                        
        # Flag to tell that the next entries are nearby tickets
        if "nearby" in line:
            checking_nearby = True
            
            # Putting all keywords into the list of possibilities to start with
            for pos in range(len(valid_numbers)):
                nearby_possible[pos] = list()
                for key in valid_numbers:
                    nearby_possible[pos].append(key)

        # Copying the "your ticket" field
        if checking_my_ticket:
            my_ticket = line
            checking_my_ticket = False

        # Flag to notify the next value is your ticket
        if "your" in line:
            checking_my_ticket = True

    longer_found = True

    # Going over the list of possibilities multiple times and deleting
    # already reserved values until all positions have only one value possible
    while(longer_found):
        used_keywords = list()

        # Adding the keywords to a list where we are certain that position is that
        # keyword (only one possibility)
        for pos in nearby_possible:
            if len(nearby_possible[pos]) == 1:
                longer_found = False
                used_keywords.append(min(nearby_possible[pos]))
            
        # Deleting the found keywords from the rest of the records
        for pos in nearby_possible:
            if len(nearby_possible[pos]) > 1:
                longer_found = True
                for word in used_keywords:
                    if word in nearby_possible[pos]:
                        nearby_possible[pos].remove(word)

    product = 1
    my_ticket = [int(x) for x in my_ticket.strip().split(",")]
    
    # Looking for all fields starting with departure and multiplying
    # the values from my ticket together
    for pos in nearby_possible:
        if min(nearby_possible[pos]).startswith("departure"):
            product *= my_ticket[pos]

    print(product)
