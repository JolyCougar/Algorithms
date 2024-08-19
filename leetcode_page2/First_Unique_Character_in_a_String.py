class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets = {}
        for c in s:
            alphabets[c] = alphabets.get(c, 0) + 1

        for i in range(len(s)):
            if alphabets.get(s[i]) == 1:
                return i
        return -1


# ----------------------------------------------------
# chars = set(s)
# u_c = ""
# ind = -1
# for char in chars:
#     first_ind = s.index(char)
#     try:
#         second_ind = s.index(char, first_ind + 1)
#     except Exception:
#         if ind == -1:
#             ind = first_ind
#             u_c = char
#         else:
#             if first_ind < ind:
#                 u_c = char
#                 ind = first_ind
#
#         continue
#
# return ind

print(Solution().firstUniqChar("loveleetcode"))
