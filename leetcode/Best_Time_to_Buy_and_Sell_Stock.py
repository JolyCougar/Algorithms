from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit(prices=[2, 4, 1]))
print(Solution().maxProfit(prices=[2, 2, 5]))
