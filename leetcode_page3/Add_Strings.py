class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length = max(len(num1), len(num2))
        num1 = num1.zfill(length)[::-1]
        num2 = num2.zfill(length)[::-1]
        res, plus = '', 0
        for index, num in enumerate(num1):
            tmp = str(int(num) + int(num2[index]) + plus)
            res += tmp[-1]
            if int(tmp) > 9:
                plus = 1
            else:
                plus = 0
        if plus:
            res += '1'
        return res[::-1]


print(Solution().addStrings(num1="11", num2="123"))
