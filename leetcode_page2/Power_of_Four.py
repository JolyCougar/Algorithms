class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n >= 4:
            if n % 4:
                return False
            n = n // 4
        if n == 1:
            return True


print(Solution().isPowerOfFour(n=5))
