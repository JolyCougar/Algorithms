from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        while True:
            if result in nums:
                result += 1
            else:
                return result


print(Solution().missingNumber([3, 0, 1]))

# -----------------------------------------------------------------
#         n=len(nums)
#         expected_sum = n*(n+1)//2
#         actual_sum=sum(nums)
#         return expected_sum - actual_sum
