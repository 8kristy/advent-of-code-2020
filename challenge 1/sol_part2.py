with open("input", "r") as f:
    num_lst =  [int(x) for x in f.readlines()]
    # Put all of the entries into a hashmap
    nums = dict(zip(num_lst, "0" * len(num_lst)))
        
for idx, i in enumerate(num_lst):
    for j in num_lst[idx + 1:]:
        # Faster than traversing the array 3 times
        if 2020 - (i + j) in nums.keys():
            print(i * j * (2020 - i - j))
