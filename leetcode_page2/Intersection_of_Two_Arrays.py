from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        if len(nums1) < len(nums2):
            test = nums1
            test1 = nums2
        else:
            test = nums2
            test1 = nums1
        for x in test:
            if x in test1 and x not in result:
                result.append(x)
        return result


# ---------------------------------------------------
# return list(set(nums1) & set(nums2))

print(Solution().intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(Solution().intersection(nums1=[2, 6, 2, 9, 1], nums2=[7, 1]))
