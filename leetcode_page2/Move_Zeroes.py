from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            current = 0
            nextnumb = 1
            while nextnumb != len(nums):
                if nums[current] == 0:
                    if nums[nextnumb] != 0:
                        nums[current] = nums[nextnumb]
                        nums[nextnumb] = 0
                    else:
                        nextnumb += 1
                else:
                    current += 1
                    nextnumb += 1


# ------------------------------------------
# left = 0
# for right in range(len(nums)):
#     if nums[right] != 0:
#         nums[right], nums[left] = nums[left], nums[right]
#         left+=1
# return nums


print(Solution().moveZeroes(nums=[4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))
print(Solution().moveZeroes(nums=[0, 1, 0, 3, 12]))
