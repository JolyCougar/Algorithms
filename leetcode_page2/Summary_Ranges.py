from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return ranges

        start, end = nums[0], nums[0]
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]

        return ranges

# ---------------------------------------------------------
# if not nums:
#     return ''
#
# ans = []
#
# i = 0
# while i < len(nums):
#     start = nums[i]
#
#     while i < (len(nums) - 1) and nums[i] + 1 == nums[i + 1]:
#         i += 1
#
#     if start != nums[i]:
#         ans.append(str(start) + '->' + str(nums[i]))
#
#     else:
#         ans.append(str(nums[i]))
#
#     i += 1
#
# return ans
