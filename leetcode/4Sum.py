from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                total = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > total:
                        right -= 1
                    else:
                        left += 1
        return result


# -------------------------------------------------------------------------------------------------
# ans = []
# nums.sort()
#
# for i in range(len(nums) - 3):
#
#     if i > 0 and nums[i] == nums[i - 1]:
#         continue
#
#     for j in range(i + 1, len(nums) - 2):
#
#         if j > i + 1 and nums[j] == nums[j - 1]:
#             continue
#
#         diff = target - nums[i] - nums[j]
#         l, r = j + 1, len(nums) - 1
#
#         if nums[l] + nums[l + 1] > diff or nums[r] + nums[r - 1] < diff:
#             continue
#
#         while l < r:
#             if nums[l] + nums[r] == diff:
#                 ans.append([nums[i], nums[j], nums[l], nums[r]])
#                 l += 1
#                 while l < r and nums[l] == nums[l - 1]:
#                     l += 1
#                 r -= 1
#                 while l < r and nums[r] == nums[r + 1]:
#                     r -= 1
#             elif nums[l] + nums[r] > diff:
#                 r -= 1
#             else:
#                 l += 1
#
# return ans


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
