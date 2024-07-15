class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if target <= nums[0]:
            return 0
        while True:
            mid = (high + low) // 2
            if nums[mid] >= target > nums[mid - 1]:
                return mid
            elif mid == (len(nums) - 1):
                return len(nums)
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                return mid


# -------------------------------------------------------------------
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums) - 1
#         mid = (high + low) // 2
#         if target < nums[0]:
#             return 0
#         while mid < len(nums):
#             if nums[mid] > target > nums[mid - 1]:
#                 return mid
#             elif nums[mid] > target:
#                 mid -= 1
#             elif nums[mid] < target:
#                 mid += 1
#             elif nums[mid] == target:
#                 return mid
#
#         return len(nums)

test = Solution()
print(test.searchInsert(nums=[1, 3], target=3))
