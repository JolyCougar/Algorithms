from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


# --------------------------------------------------------------------
# res = []
# n = len(nums)
# num_set = set(nums)
# for i in range(1, n + 1):
#     if i not in num_set:
#         res.append(i)
# return res

print(Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
