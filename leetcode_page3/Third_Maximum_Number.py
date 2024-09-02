from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        n = list(set(nums))
        if len(n) < 3:
            return max(n)
        else:
            return sorted(n)[-3]


# ---------------------------------------------------
# nums = sorted(set(nums))
# if len(nums) < 3:
#     return max(nums)
# return nums[-3]

print(Solution().thirdMax(nums=[3, 2, 1]))
