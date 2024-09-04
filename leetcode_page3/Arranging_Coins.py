class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = start + (end - start) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                start = mid + 1
            else:
                end = mid - 1

        return end


# ------------------------------------------------
# return int((math.sqrt(1 + 8 * n) - 1) / 2)

print(Solution().arrangeCoins(n=5))
