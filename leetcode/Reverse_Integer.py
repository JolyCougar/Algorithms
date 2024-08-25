class Solution:
    def reverse(self, x: int) -> int:
        result = str()
        current = str(x)
        test = list(current)
        while test:
            current = test.pop()
            if current.isdigit():
                result += current
            else:
                result = current + result
        result = int(result)
        if result > ((2 ** 31) - 1) or result < (-2 ** 31):
            return 0
        return result


# ---------------------------------------------------------------
# x = str(x)
# x = x[::-1]
# x.lstrip('0')
# if (x[-1] == '-'):
#     x = x[:len(x) - 1]
#     x = '-' + x
# x = int(x)
# if (x < -(2 ** 31) or x > (2 ** 31 - 1)):
#     return 0
# return x
print(Solution().reverse(x=1534236469))
