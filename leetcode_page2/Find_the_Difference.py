class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        s = list(s)
        for i in s:
            t.remove(i)
        return t[0]


# ---------------------------------------------------------------
# w = []
# for i in t:
#     if s.count(i) != t.count(i):
#         return i
print(Solution().findTheDifference("abcd", "abcd"))
