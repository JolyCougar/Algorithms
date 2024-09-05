from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result, i = 0, 0
        for j in range(len(s)):
            if i == len(g):
                break
            if s[j] >= g[i]:
                result += 1
                i += 1
        return result


# --------------------------------------------------------------------
# g.sort()
# s.sort()
# i = 0
# j = 0
#
# result = 0
# while i < len(g) and j < len(s):
#     if s[j] >= g[i]:
#         result += 1
#         i += 1
#     j += 1
#
# return result

print(Solution().findContentChildren(g=[1, 2, 3], s=[1, 1]))
