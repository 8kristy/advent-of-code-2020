with open("input", "r") as f:
    trees = 0
    curr_x = 0
    line_length = len(f.readline().strip())
    for line in f:
        curr_x = (curr_x + 3) % line_length
        if line[curr_x] == "#":
            trees += 1
    print(trees)        