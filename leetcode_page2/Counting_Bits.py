from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append((i & 1) + res[i >> 1])
        return res


# --------------------------------------
# ans = [0] * (n + 1)
#
# offset = 1
# for i in range(1, n + 1):
#     if offset * 2 == i:
#         offset = i
#     ans[i] = 1 + ans[i - offset]
# return ans

print(Solution().countBits(5))
