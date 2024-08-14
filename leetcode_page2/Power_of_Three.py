class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n >= 3:
            if n % 3:
                return False
            n = n // 3
        if n == 1:
            return True


# ------------------------------------
# return n > 0 and 3**19 % n == 0

# ------------------------------------
# if n == 1:
#     return 1
# elif (((n % 3) != 0) or (n < 1)):
#     return 0
# else:
#     return self.isPowerOfThree(n / 3)

# ------------------------------------
# if (n > 1):
#     while (n % 3 == 0): n //= 3
# return n == 1

print(Solution().isPowerOfThree(n=27))
