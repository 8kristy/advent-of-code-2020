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
    seats = dict()

    # Noting which seats are already occupied
    for line in f:
        row = bin_search(line[:7], 'F', 'B', 1, 126)
        col = bin_search(line[7:], 'L', 'R', 0, 7)
        
        if row not in seats.keys():
            seats[row] = list()

        seats[row].append(col)    

    # Looking for our seat
    for row in seats:
        # Must be a row where at least one seat is missing
        if len(seats[row]) < 8:
            seats[row].sort()
            for idx, seat in enumerate(seats[row]):
                # Our seat has ids -1 and +1 around it, so 
                # look for such gap
                if idx > 0 and idx < len(seats[row]) - 1:
                    if seat - 1 != seats[row][idx - 1]:
                        print(row * 8 + seat - 1)  
