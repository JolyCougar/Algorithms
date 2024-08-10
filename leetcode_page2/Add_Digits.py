class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        return self.addDigits(num // 10 + num % 10)


print(Solution().addDigits(38))
