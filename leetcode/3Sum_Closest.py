from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ls = len(nums)
        if ls < 3:
            return []

        nums = sorted(nums)

        resuls = sum(nums[0:3])

        for i in range(ls - 2):
            j = i + 1
            m = ls - 1

            while j < m:
                tem = nums[i] + nums[j] + nums[m]
                v = tem - target

                if abs(v) < abs(resuls - target):
                    resuls = tem

                if v == 0:
                    return target
                elif v > 0:
                    m -= 1
                else:
                    j += 1

        return resuls


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

# -------------------------------------------------------------------------------
# nums.sort()
#
# closest = sum(nums[:3])
# if closest >= target:
#     return closest
#
# closest = sum(nums[-3:])
# if closest <= target:
#     return closest
#
# best_diff = float("inf")
# closest = None
# for i in range(len(nums) - 2):
#     if i > 0 and nums[i] == nums[i - 1]:
#         continue
#
#     cur = sum(nums[i:i + 3])
#     if cur >= target:
#         diff = abs(target - cur)
#         if diff == 0:
#             return target
#         if diff < best_diff:
#             best_diff = abs(target - cur)
#             closest = cur
#         continue
#
#     cur = nums[i] + sum(nums[-2:])
#     if cur < target:
#         diff = abs(target - cur)
#         if diff == 0:
#             return target
#         if diff < best_diff:
#             best_diff = abs(target - cur)
#             closest = cur
#         continue
#
#     for j in range(i + 1, len(nums) - 1):
#         if j > 1 and nums[j] == nums[i - 1]:
#             continue
#         cur = nums[i] + nums[j]
#         cur += min(nums[j + 1:], key=lambda x: abs(target - cur - x))
#         diff = abs(cur - target)
#         if diff == 0:
#             return target
#         if diff < best_diff:
#             best_diff = diff
#             closest = cur
# return closest
