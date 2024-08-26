from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


# ----------------------------------------------------------------------------------
# left = 0
# right = len(height) - 1
# max = 0
# while left < right:
#     hei = min(height[left], height[right])
#     vol = hei * (right - left)
#     if vol > max:
#         max = vol
#     if height[left] < height[right]:
#         left += 1
#     else:
#         right -= 1
#
# return max

print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
