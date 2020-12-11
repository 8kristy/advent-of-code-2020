# Goes around the given seat at x,y and counts how many '#'s are around it
def count_adjacent(seats, x:int, y:int):
    count = 0
    for i in range(x -1, x + 2):
        for j in range(y - 1, y + 2):
            if i != x or j != y:
                try:
                    if i >= 0 and j >= 0 and seats[i][j] == "#":
                        count += 1
                except:
                    pass  
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
            elif seats[i][j] == "#" and count_adjacent(seats, i, j) >= 4:
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

