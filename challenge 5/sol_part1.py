import math

# Picks lower half of current subdomain if the next letter read
# is min_letter, upper half if the next letter read is max_letter
def bin_search(string, min_letter, max_letter, min, max):
    for letter in string:
        if letter == min_letter:
            max = math.floor((min + max) / 2)
        if letter == max_letter:
            min = math.ceil((min + max) / 2)

    return max

with open("input", "r") as f:
    max_id = 0
    # Going through all seats and looking for max id
    for line in f:
        row = bin_search(line[:7], 'F', 'B', 0, 127)
        col = bin_search(line[7:], 'L', 'R', 0, 7)

        if (max_id < row * 8 + col):
            max_id = row * 8 + col

    print(max_id)            
