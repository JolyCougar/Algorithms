from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = dict()
        for x in nums:
            if x in test:
                test[x] += 1
                if test[x] >= 2:
                    return True
            else:
                test[x] = 1
        return False


# ----------------------------------------
# if len(set(nums)) != len(nums):
#     return True
# return False
print(Solution().containsDuplicate(nums=[1, 2, 3, 1]))
