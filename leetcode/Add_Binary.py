class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first = int(a, 2)
        second = int(b, 2)

        first = bin(first + second)
        return first[2:]



test = Solution()
print(test.addBinary(a='1', b='1'))
