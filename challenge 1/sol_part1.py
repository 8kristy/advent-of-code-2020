with open("input", "r") as f:
    nums = [int(x) for x in f.readlines()]

for idx, i in enumerate(nums):
    for j in nums[idx + 1:]:
        if i + j == 2020:
            print(str(i * j)) 

