class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        i = 1
        for x in range(len(nums)):
            if k == len(nums) or i == len(nums):
                return k
            if nums[i] != nums[x]:
                nums[k] = nums[i]
                k += 1
                i += 1
            elif nums[i] == nums[x]:
                i += 1


# 2 option (80ms) 1 opinion - 67ms
# ----------------------------------------------------------
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         k = 1
#         for x in range(1, len(nums)):
#             if nums[x] != nums[x-1]:
#                 nums[k] = nums[x]
#                 k += 1
#         return k


test = Solution()
print(test.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
