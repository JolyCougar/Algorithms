def twoSum(nums: list, target: int):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]
    return "Error"


print(twoSum(nums=[3, 2, 4], target=6))
