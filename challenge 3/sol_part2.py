# Counts the number of trees enountered for a particular slope
def trees(f, down, right):
    trees = 0
    curr_x = 0
    line_length = len(f.readline().strip())

    # Skipping to get onto the next line determined by down
    f.seek(0)
    for i in range(down):
        f.readline()

    for line in f:
        curr_x = (curr_x + right) % line_length
        if line[curr_x] == "#":
            trees += 1
        # Skipping lines if down > 1
        for i in range(down - 1):
            f.readline()   
    return trees

with open("input", "r") as f:
    trees_product = 1
    for slope in [1,3,5,7]:
        trees_product *= trees(f, 1, slope)
        f.seek(0)
        
    trees_product *= trees(f, 2, 1)
    print(trees_product)