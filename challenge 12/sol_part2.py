import math 

with open("input", "r") as f:

    # East
    ship_x = 0
    waypoint_x = 10
    # North
    ship_y = 0
    waypoint_y = 1

    for dir in f:
        # Coordinate rotation
        if "L" in dir or "R" in dir:
            deg = math.radians(int(dir[1:]))
            if "R" in dir:
                deg = -deg
            # Temps needed because we need to use our old values and don't want to overwrite them
            temp_x = round(waypoint_x * math.cos(deg) - waypoint_y * math.sin(deg))
            temp_y = round(waypoint_y * math.cos(deg) + waypoint_x * math.sin(deg)) 

            waypoint_x = temp_x
            waypoint_y = temp_y

        # Move in the direction of the waypoint specified number of times
        if "F" in dir:
            ship_x += int(dir[1:]) * waypoint_x
            ship_y += int(dir[1:]) * waypoint_y

        # Update the waypoint directions
        if "N" in dir:
            waypoint_y += int(dir[1:])    
        if "E" in dir:
            waypoint_x += int(dir[1:])
        if "S" in dir:
            waypoint_y -= int(dir[1:])
        if "W" in dir:
            waypoint_x -= int(dir[1:])

print(abs(ship_x) + abs(ship_y))