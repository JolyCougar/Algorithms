class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[i] = nums[x]
                i += 1
        return i


test = Solution()
print(test.removeElement([0,1,2,2,3,0,4,2], val = 2))
