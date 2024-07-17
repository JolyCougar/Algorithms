class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        current = 1
        for i in range(n):
            prev, current = current, prev + current,

        return current

        # if n <= 2:
        #     return n
        # else:
        # prev1 = 1
        # prev2 = 2
        # current = 0
        #
        # for i in range(2, n):
        #     current = prev1 + prev2
        #     print('Current is ', current)
        #     prev1 = prev2
        #     print('prev1 is ', prev1)
        #     prev2 = current
        #     print('prev2 is ', prev2)
        #
        # return current

test = Solution()
print(test.climbStairs(n=6))
# 6 - 13(+5)
# 5 - 8(+3)
# 4 - 5(+2)
# 3 - 3

