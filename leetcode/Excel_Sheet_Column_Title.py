class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        curr = ''
        n = columnNumber
        while n > 26:
            if n % 26:
                curr = chr((n % 26) + 64) + curr
                n = n // 26
            else:
                curr = 'Z' + curr
                n = (n // 26) - 1
        curr = chr(n + 64) + curr
        return curr


print(Solution().convertToTitle(columnNumber=28))
