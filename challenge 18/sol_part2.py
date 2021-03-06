
# Evaluates all instances of sym in the expression
def add(expr, sym):
    while sym in expr:
        idx = expr.index(sym)
        
        if sym == "+":
            expr = expr[:idx - 1] + [int(expr[idx - 1]) + int(expr[idx + 1])] + expr[idx + 2:]
        if sym == "*":
            expr = expr[:idx - 1] + [int(expr[idx - 1]) * int(expr[idx + 1])] + expr[idx + 2:]

    return expr

# Gets a result of some expression
def calculate_expression(expr:str):

    # For easier processing later
    expr = expr.replace("((", "( (")
    expr = expr.strip()

    # Calculating all subexpressions first recursively and putting them back
    # into the string after we have the result
    while "(" in expr:
        left_idx = expr.rfind("(") 
        right_idx = left_idx + expr[left_idx:].find(")", 1)

        # Required for an edge case where ( is at index 0 so that it doesn't wrap around
        if left_idx == 0:
            expr = expr[:left_idx] + " " + str(calculate_expression(expr[left_idx + 1:right_idx])) + " " + expr[right_idx + 1:]
        else:
            expr = expr[:left_idx - 1] + " " + str(calculate_expression(expr[left_idx + 1:right_idx])) + " " + expr[right_idx + 1:]

    # Tidying up to calculate properly later
    expr = expr.split(" ")
    while "" in expr:
        expr.remove("")
    
    expr = add(expr, "+")
    expr = add(expr, "*")
            
    return expr[0]

with open("input", "r") as f:
    sum = 0
    for line in f:
        sum += calculate_expression(line.strip())

print(sum)