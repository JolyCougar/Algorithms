class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        res = {}
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = t[i]
            elif res[s[i]] != t[i]:
                return False
        return True


# --------------------------------------------
#         s_map = {}
#         for i in range(len(s)):
#             if s[i] not in s_map:
#                 if t[i] not in s_map.values():
#                     s_map[s[i]] = t[i]
#                 else:
#                     return False
#             elif s_map[s[i]] != t[i]:
#                 return False
#         return True

print(Solution().isIsomorphic(s='egg', t='add'))
