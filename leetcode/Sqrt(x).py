class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        if x <= 1:
            return x
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1


# ----------------------------------------------
# if x < 2:
#     return x
# for i in range(0, x // 2 + 1):
#     if i * i <= x < (i + 1) ** 2:
#         return i
# -------------------------------------
# if x < 2:
#     return x
#
# left, right = 1, x // 2
# while left <= right:
#     mid = left + (right - left) // 2
#     if mid * mid == x:
#         return mid
#     elif mid * mid < x:
#         left = mid + 1
#     else:
#         right = mid - 1
#
# return right

test = Solution()
print(test.mySqrt(x=8))
