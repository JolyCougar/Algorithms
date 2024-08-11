class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        for k in [2, 3, 5]:
            while n % k == 0:
                n = n // k

        return n == 1


print(Solution().isUgly(5))
