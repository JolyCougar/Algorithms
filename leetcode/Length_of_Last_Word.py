class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        z = s.split(' ')
        i = len(z) - 1
        while z:
            if z[i].isalpha():
                return len(z[i])
            i -= 1


test = Solution()
print(test.lengthOfLastWord(s="   fly me   to   the moon  "))
