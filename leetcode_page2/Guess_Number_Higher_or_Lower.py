class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == -1:
                right = mid - 1
            elif res == 1:
                left = mid + 1
            else:
                return mid



