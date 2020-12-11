# "Beaming" from some x,y then going in the direction until either
# a seat is found or we get out of bounds of the array
def find_seat(seats, x, y, x_step, y_step):
    while x >= 0 and y >= 0 and x < len(seats) and y < len(seats[0]):
        if seats[x][y] == '#':
            return 1
        elif seats[x][y] == 'L':
            return 0
        else:
            x += x_step
            y += y_step

    return 0         

# Count visible occupied seats
def count_adjacent(seats, x:int, y:int):
    count = 0
    # Up
    count += find_seat(seats, x, y - 1, 0, -1)
    # Up right
    count += find_seat(seats, x + 1, y - 1, 1, -1)
    # Right
    count += find_seat(seats, x + 1, y, 1, 0)
    # Down right
    count += find_seat(seats, x + 1, y + 1, 1, 1)
    # Down
    count += find_seat(seats, x, y + 1, 0, 1)
    # Down left
    count += find_seat(seats, x - 1, y + 1, -1, 1)
    # Left
    count += find_seat(seats, x - 1, y, -1, 0)
    # Up left
    count += find_seat(seats, x - 1, y - 1, -1, -1)
    return count                  

with open("input", "r") as f:
    # Initially, all seats will get occupied
    seats = [x.strip().replace("L", "#") for x in f.readlines()]
   
new_seats = list()
changes = 1
# Looping until we reach equilibrium
while changes > 0:
    changes = 0
    new_seats = list()
    for i in range(len(seats)):
        new_seats.append(list())
        for j in range(len(seats[0])):
            # Changing the empty seats
            if seats[i][j] == "L" and count_adjacent(seats, i, j) == 0:
                new_seats[i].append("#")
                changes += 1
            # Changing the occupied seats
            elif seats[i][j] == "#" and count_adjacent(seats, i, j) >= 5:
                new_seats[i].append("L")
                changes += 1
            else:
                new_seats[i].append(seats[i][j])
    seats = new_seats   

# Counting seats after equilibrium reached
total_occupied = 0
for row in seats:
    total_occupied += row.count("#")

print(total_occupied)    

