from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < 0:
                        left += 1
                    else:
                        right -= 1
        return res


print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
# ------------------------------------------------------------------------------------
# nums.sort()
#
# if not all(n > 0 for n in nums):
#     count = collections.Counter(nums)
#     res = [[0, 0, 0]] if count[0] >= 3 else []
#     nums = [x for x in sorted(count) if x != 0]
#     if count[0] > 0:
#         for i in nums:
#             if i > 0:
#                 break
#             if -i in count:
#                 res.append([-i, 0, i])
#     for i in nums:
#         if i & 1:
#             continue
#         remain = -i >> 1
#         if count[remain] >= 2:
#             res.append([i, remain, remain])
#     for i, n in enumerate(nums):
#         kk = -(nums[0] + n)
#         if kk < n:
#             break
#         j = bisect.bisect_right(nums, -n << 1) if n < 0 else i + 1
#         k = bisect.bisect_right(nums, kk)
#         for right in nums[j:k]:
#             left = -(n + right)
#             if left in count:
#                 res.append([left, n, right])
#     return res
# else:
#     return []
