class Solution:
    def hammingWeight(self, n: int) -> int:
        numb = bin(n)[2:]
        count = 0
        for i in str(numb):
            if int(i) > 0:
                count += 1
        return count


print(Solution().hammingWeight(11))
