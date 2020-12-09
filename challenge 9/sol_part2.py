# Using the input with everything up to the number found in part 1 (excluded)
with open("input_shortened", "r") as f:
    numbers = [int(x) for x in f.readlines()]
    num = 18272118

    # Checking all possible ranges
    for start_idx in range(len(numbers)):
        for end_idx in range(start_idx + 2, len(numbers) + 1):
            # Checking if all numbers in some range add up to our number
            if sum(numbers[start_idx:end_idx]) == num:
                # Printing the sum of min and max in the range
                print(min(numbers[start_idx:end_idx]) + max(numbers[start_idx:end_idx]))