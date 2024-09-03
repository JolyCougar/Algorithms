class Solution:
    def countSegments(self, s: str) -> int:
        result = s.split(' ')
        count = 0
        for x in result:
            if x != '':
                count += 1
        return count


# -------------------------------------------------------
# return len(s.split())

print(Solution().countSegments(s="Of all the gin joints in all the towns in all the world,    "))
