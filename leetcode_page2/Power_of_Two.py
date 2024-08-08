import decimal


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        current_number = 0
        counter = 0
        while current_number <= n:
            current_number = 2 ** counter
            counter += 1
            if current_number == n:
                return True
        return False


# --------------------------------------
#         if n <= 0:
#             return False
#         while n >= 3:
#             if n % 2:
#                 return False
#             n = n // 2
#         return True

print(Solution().isPowerOfTwo(n=3))
