from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(), nums2.sort()
        res = []
        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res += nums1[it1],
                it1 += 1
                it2 += 1

        return res


# ---------------------------------------------------
# nums1.sort()
# nums2.sort()
# res = []
# p = q = 0
# while p < len(nums1) and q < len(nums2):
#     if nums1[p] < nums2[q]:
#         p += 1
#     elif nums1[p] > nums2[q]:
#         q += 1
#     else:
#         res.append(nums1[p])
#         p += 1
#         q += 1
# return res
# ---------------------------------------------------
# freq1 = {}
# freq2 = {}
#
# # Count the frequency of elements in nums1
# for num in nums1:
#     freq1[num] = freq1.get(num, 0) + 1
#
# # Check if elements in nums2 are present in nums1 and add them to the result
# result = []
# for num in nums2:
#     if num in freq1 and freq1[num] > 0:
#         result.append(num)
#         freq1[num] -= 1
#
# return result


print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
