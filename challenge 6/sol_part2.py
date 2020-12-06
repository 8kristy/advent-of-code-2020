with open("input", "r") as f:
    groups = f.read().split("\n\n")

total = 0

# Counting the questions where everyone in the group answered the question 
for group in groups:
    individual_answers = group.split("\n")
    common_answers = set(individual_answers[0])

    # Continuously intersect to eliminate answers which didn't appear in someone else's list
    for answer in individual_answers[0:]:
        common_answers = common_answers.intersection(set(answer))   

    total += len(common_answers)
print(total)   