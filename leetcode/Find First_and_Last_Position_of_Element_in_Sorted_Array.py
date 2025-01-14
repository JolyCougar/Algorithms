from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # leftBias=[True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i

# ------------------------------------------------------------------------
# if len(nums) == 0:
#     return [-1, -1]
#
#     # find upper bound
# low = 0
# high = len(nums) - 1
# pos = [-1, -1]
#
# while low < high:
#     mid = (low + high) // 2
#     if nums[mid] == target and nums[mid + 1] != target:
#         pos[1] = mid
#         break
#     elif nums[mid] == target and nums[mid + 1] == target:
#         low = mid + 1
#     elif nums[mid] < target:
#         low = mid + 1
#     elif nums[mid] > target:
#         high = mid
#
# if pos[1] == -1 and nums[low] == target:
#     pos[1] = low
#
# # find lower bound
# low = 0
# high = len(nums) - 1
#
# while low < high:
#     mid = (low + high) // 2
#     if nums[mid + 1] == target and nums[mid] != target:
#         pos[0] = mid + 1
#         break
#     elif nums[mid + 1] == target and nums[mid] == target:
#         high = mid
#     elif nums[mid + 1] < target:
#         low = mid + 1
#     elif nums[mid + 1] > target:
#         high = mid
#
# if pos[0] == -1 and nums[low] == target:
#     pos[0] = low
#
# return pos
