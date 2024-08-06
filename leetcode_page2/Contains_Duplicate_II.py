from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                if i - lookup[num] <= k:
                    return True
                lookup[num] = i
        return False


# print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
# print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
print(Solution().containsNearbyDuplicate(nums =[0,1,2,3,4,0,0,7,8,9,10,11,12,0], k=1))
