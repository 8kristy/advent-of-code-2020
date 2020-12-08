with open("input", "r") as f:
    operations = f.readlines()

executed_ops = list() 
curr_op = 0
acc = 0

# Looping until we notice that the operation is already in our list,
# meaning that that's the point where we detect a loop
while curr_op not in executed_ops:  
    executed_ops.append(curr_op)    
    argument = int(operations[curr_op].split(" ")[1])
    
    if "jmp" in operations[curr_op]:
        curr_op += argument
    elif "acc" in operations[curr_op]:
        acc += argument
        curr_op += 1
    else:
        curr_op += 1    

print(acc)            