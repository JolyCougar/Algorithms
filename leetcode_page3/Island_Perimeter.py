from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island = 0
        neighbor = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    island = island + 1
                    if x < len(grid[y]) - 1 and grid[y][x + 1] == 1:
                        neighbor = neighbor + 1
                    if y < len(grid) - 1 and grid[y + 1][x] == 1:
                        neighbor = neighbor + 1
        return island * 4 - 2 * neighbor


# -----------------------------------------------------------------------
# rows = len(grid)
# cols = len(grid[0])
#
# perimeter = 0
# for row in range(rows):
#     for col in range(cols):
#         if grid[row][col] == 1:
#             perimeter += 4
#             if row > 0 and grid[row - 1][col] == 1:
#                 perimeter -= 2
#             if col > 0 and grid[row][col - 1] == 1:
#                 perimeter -= 2
#
# return perimeter

print(Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
