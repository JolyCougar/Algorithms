class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        count = 0
        for c in t:
            if c == s[count]:
                count += 1
            if count == len(s):
                break
        return count == len(s)


print(Solution().isSubsequence("abc", "bcd"))
