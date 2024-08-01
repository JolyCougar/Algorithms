class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

# ------------------------------------------------------------------------------------
#         if n == 0:
#             return 0
#         output = 0
#         cnt = 31
#         while n != 0:
#             num = n % 2
#             output = output + num * pow(2, cnt)
#             n = int (n / 2)
#             cnt = cnt - 1
#
#         return output
