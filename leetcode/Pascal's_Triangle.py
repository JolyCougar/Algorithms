from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangles = []
        for i in range(numRows):
            triangles.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    triangles[i].append(1)
                else:
                    triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])
        return triangles


# ----------------------------------------
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         result = []
#         if numRows == 0:
#             return result
#
#         result.append([1])
#
#         for i in range(1, numRows):
#             prev_row = result[i - 1]
#             current_row = [1]
#
#             for j in range(1, i):
#                 current_row.append(prev_row[j - 1] + prev_row[j])
#
#             current_row.append(1)
#             result.append(current_row)
#
#         return result
print(Solution().generate(5))
