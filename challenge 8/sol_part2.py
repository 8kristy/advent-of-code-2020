with open("input", "r") as f:
    operations = f.readlines()

def replaceOp(op:str):
    if "jmp" in op:
        return op.replace("jmp", "nop")
    elif "nop" in op:
        return op.replace("nop", "jmp")

# Looping until we notice that the operation is already in our list
# (loop) or until it goes beyond it (terminates).
# Besides telling if it terminates, it returns the last value in the accumulator
def checkIfTerminates(operations):
    executed_ops = list()
    curr_op = 0
    acc = 0 
    while curr_op not in executed_ops:
        executed_ops.append(curr_op)    
        argument = int(operations[curr_op].split(" ")[1])

        # Rrgular program execution
        if "jmp" in operations[curr_op]:
            curr_op += argument
        elif "acc" in operations[curr_op]:
            acc += argument
            curr_op += 1
        else:
            curr_op += 1

        # Terminating condition of going beyond the list
        if curr_op > len(operations) - 1:
            return True, acc

    # Found curr_op in list
    return False, acc       

# Replacing jmp with nop or nop with jmp one by one and checking if
# that program terminates
for idx, op in enumerate(operations):
    if "jmp" in op or "nop" in op:
        operations[idx] = replaceOp(op)
        
        terminates, acc_value = checkIfTerminates(operations)

        if terminates:
            print(acc_value)
            break 

        # Putting the value back
        operations[idx] = replaceOp(operations[idx])    


