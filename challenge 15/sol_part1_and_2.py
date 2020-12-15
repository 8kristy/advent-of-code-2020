with open("input", "r") as f:
    numbers = [int(x) for x in f.readline().split(",")]

def get_nth_number_spoken(target_turn:int):
    spoken = dict()
    lastSpoken = 0
    turn = 1

    # Initialise the spoken array
    for num in numbers:
        spoken[num] = turn
        turn += 1

    # To account for the last number being spoken
    lastSpoken = 0
    turn += 1

    while turn <= target_turn:
        # Keeping the number to update later 
        curr = lastSpoken
        # Last number was new
        if lastSpoken not in spoken:
            lastSpoken = 0
        # Speak the difference between last round and last time
        # the number was spoken
        else:
            lastSpoken = turn - 1 - spoken[lastSpoken]
        # Need to update it here as it otherwise messes things up
        spoken[curr] = turn - 1
        turn += 1
    return lastSpoken

print("Part 1:", get_nth_number_spoken(2020))
# This runs a bit slower but it finishes at a reasonable time still
print("Part 2:", get_nth_number_spoken(30000000))