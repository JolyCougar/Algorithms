class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits


test = Solution()
print(test.plusOne(digits=[8, 9, 9, 9]))
print(test.plusOne(digits=[9, 8, 9]))
