from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        test = dict()
        for x in nums:
            if x not in test:
                test[x] = 1
            else:
                test.pop(x)
        for y in test:
            if test[y] == 1:
                return y


# ------------------------------------
# test = dict()
#         for x in nums:
#             if x not in test:
#                 test[x] = 1
#             else:
#                 test.pop(x)
#         return test.popitem()[0]


print(Solution().singleNumber(nums=[4, 1, 2, 1, 2]))
