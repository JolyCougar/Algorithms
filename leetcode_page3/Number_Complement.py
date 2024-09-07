class Solution:
    def findComplement(self, num: int) -> int:
        num_b = bin(num)[2:]
        result = ''
        for bit in num_b:
            result += '1' if bit == '0' else '0'
        return int(result, 2)


# ------------------------------------------------
# compliment = 1
# while compliment <= num:
#     compliment = compliment << 1
#
# leftCompliment = compliment - 1
# compliment = (leftCompliment) ^ num
#
# return compliment
print(Solution().findComplement(num=5))
