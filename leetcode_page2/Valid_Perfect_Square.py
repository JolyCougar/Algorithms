class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (int(num ** 0.5) ** 2) == num


# ---------------------------------------------
# if num == 1:
#     return True
# l, r = 1, (num // 2) + 1
# while l <= r:
#     mid = (r + l) // 2
#     if mid * mid == num:
#         return True
#     elif mid * mid < num:
#         l = mid + 1
#     else:
#         r = mid - 1
# return False
print(Solution().isPerfectSquare(13))
