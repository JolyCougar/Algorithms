from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        middle = len(nums) // 2
        return nums[middle]


print(Solution().majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
