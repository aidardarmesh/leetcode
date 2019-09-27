from typing import *

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        top_bottom_maxs = []
        left_right_maxs = []
        total_sum = 0
        min_inf = -999999

        for i in range(0, n):
            top_bottom_max = min_inf
            left_right_max = min_inf

            for j in range(0, n):
                if grid[i][j] > left_right_max:
                    left_right_max = grid[i][j]
                
                if grid[j][i] > top_bottom_max:
                    top_bottom_max = grid[j][i]
            
            left_right_maxs.append(left_right_max)
            top_bottom_maxs.append(top_bottom_max)

        for i in range(0, n):
            for j in range(0, n):
                local_max = min(left_right_maxs[i], top_bottom_maxs[j])
                total_sum += (local_max - grid[i][j])

        return total_sum

s = Solution()

assert s.maxIncreaseKeepingSkyline([
    [3, 0, 8, 4], 
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]) == 35

assert s.maxIncreaseKeepingSkyline([
    [0, 30],
    [49, 13]
]) == 47