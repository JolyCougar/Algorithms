class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = set()
        ans = i = 0
        for j, c in enumerate(s):
            while c in test:
                test.remove(s[i])
                i += 1
            test.add(c)
            ans = max(ans, j - i + 1)
        return ans


# ----------------------------------------------------------
# n = len(s)
# if n == 0:
#     return 0
# idx = {s[0]: 0}
# ret = 1
# curr_start = 0
# curr_len = 1
# for i in range(1, n):
#     if (j := idx.get(s[i], -1)) >= curr_start:
#         ret = max(ret, curr_len)
#         curr_start = j + 1
#         curr_len = i - j
#     else:
#         curr_len += 1
#     idx[s[i]] = i
# ret = max(ret, curr_len)
# return ret

print(Solution().lengthOfLongestSubstring("pwwkew"))
