prev_25 = list()

# Checks if any combination of 2 numbers in prev_25 adds up to the next number
def check_valid_sum(num:int):
    for idx, i in enumerate(prev_25):
        for j in prev_25[idx + 1:]:
            if i + j == num:
                return True 
    return False            


with open("input", "r") as f:
    # Gets the first 25 number preamble
    for i in range(25):
        prev_25.append(int(f.readline()))

    # Continues checking the sums until an invalid one is found
    for line in f:
        if check_valid_sum(int(line)):
            prev_25 = prev_25[1:]
            prev_25.append(int(line))
        else:
            print(line)
            exit(0)

