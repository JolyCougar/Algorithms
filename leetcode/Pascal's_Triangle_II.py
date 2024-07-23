from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = list()
        if rowIndex == 0:
            return [1]
        for i in range(rowIndex + 1):
            result.append([])
            for x in range(i + 1):
                if x == 0 or x == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][x - 1] + result[i - 1][x])

        return result[rowIndex]


print(Solution().getRow(5))
