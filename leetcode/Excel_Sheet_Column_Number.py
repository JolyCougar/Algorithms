class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result *= 26
            result += ord(columnTitle[i]) - ord('A') + 1
        return result


print(Solution().titleToNumber(columnTitle='A'))
