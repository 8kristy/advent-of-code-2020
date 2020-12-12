with open("input", "r") as f:
    # 0 = North, 1 =  East, 2 = South, 3 = West
    facing = 1
    # East
    x = 0
    # South
    y = 0
    for dir in f:
        # Changing the direction
        if "L" in dir:
            facing = (facing - int(dir[1:]) / 90) % 4
        if "R" in dir:
            facing = (facing + int(dir[1:]) / 90) % 4    

        # Moving forward in the direction we're facing
        if "F" in dir:
            if facing == 0:
                y += int(dir[1:]) 
            if facing == 1:
                x += int(dir[1:])
            if facing == 2:
                y -= int(dir[1:])
            if facing == 3:
                x -= int(dir[1:])

        # Moving in the direction given
        if "N" in dir:
            y += int(dir[1:])    
        if "E" in dir:
            x += int(dir[1:])
        if "S" in dir:
            y -= int(dir[1:])
        if "W" in dir:
            x -= int(dir[1:])

print(abs(x) + abs(y))