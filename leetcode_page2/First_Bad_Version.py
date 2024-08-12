# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) / 2
            if Solution.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# -------------------------------------------------------
# l = 1
# r = n
#
# while r > l:
#     m = (l + r) // 2
#
#     if isBadVersion(m):
#         r = m
#     else:
#         l = m + 1
#
# return l
