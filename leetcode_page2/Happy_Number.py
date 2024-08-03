class Solution:
    def isHappy(self, n: int) -> bool:
        current = n
        last_current = int()
        result = int()
        inter = int()
        remainder = int()
        while True:
            if current == 1:
                return True
            else:
                inter = current // 10
                remainder = current % 10
                if inter < 10:
                    current = inter ** 2 + remainder ** 2 + result
                    result = 0
                    if current == last_current:
                        return False
                else:
                    last_current = current
                    result += remainder ** 2
                    current = inter


# --------------------------------------------------------
# store = []
# cur = n
# store.append(cur)
# while cur != 1:
#     tmp = cur
#     res = 0
#     while tmp:
#         res += (tmp % 10) * (tmp % 10)
#         tmp //= 10
#     if res in store:
#         return False
#     cur = res
#     store.append(cur)
#
# return True


print(Solution().isHappy(n=1221))
