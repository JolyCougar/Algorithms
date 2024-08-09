class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = dict()
        dict_2 = dict()
        for x in s:
            if x in dict_1:
                dict_1[x] += 1
            else:
                dict_1[x] = 1
        for y in t:
            if y in dict_2:
                dict_2[y] += 1
            else:
                dict_2[y] = 1
        return dict_1 == dict_2


print(Solution().isAnagram(s="anagram", t="nagaram"))

# ------------------------------------------------------------------
#         if len(s) != len(t):
#             return False
#         s_st = set(s)
#
#         for i in s_st:
#             if s.count(i) != t.count(i):
#                 return False
#         return True
