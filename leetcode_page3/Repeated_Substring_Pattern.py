class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


# ----------------------------------------------------------
# repeat = ''
# n = len(s)
# for i in range(n // 2):
#     repeat += s[i]
#
#     if n % len(repeat) == 0:
#         if repeat * (n // len(repeat)) == s:
#             return True

print(Solution().repeatedSubstringPattern(s="abcabcabcabc"))
