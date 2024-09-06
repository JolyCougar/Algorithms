class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        z = x ^ y
        while z:
            distance += 1
            z &= z - 1
        return distance


# ------------------------------------------------------
# return bin(x^y).count('1')

print(Solution().hammingDistance(x=1, y=4))
