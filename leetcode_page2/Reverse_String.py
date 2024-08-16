from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count = 0
        count_max = len(s) - 1
        temp = str()
        while count < count_max:
            temp = s[count_max]
            s[count_max] = s[count]
            s[count] = temp
            count += 1
            count_max -= 1


# ----------------------------------------
# s[:]=s[::-1]

print(Solution().reverseString(s=["h", "e", "l", "l", "o"]))
