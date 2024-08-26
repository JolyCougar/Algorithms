class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        res = ""
        while num > 0:
            while num >= value[i]:
                num -= value[i]
                res += symbol[i]
            i += 1
        return res


# ----------------------------------------------------------------------------------------
# hmap = {
#     1: 'I',
#     4: 'IV',
#     5: 'V',
#     9: 'IX',
#     10: 'X',
#     40: 'XL',
#     50: 'L',
#     90: 'XC',
#     100: 'C',
#     400: 'CD',
#     500: 'D',
#     900: 'CM',
#     1000: 'M'
# }
#
# res = ""
# for n in list(hmap.keys())[::-1]:
#     while num >= n:
#         res += hmap[n]
#         num -= n
# return res

print(Solution().intToRoman(10))
