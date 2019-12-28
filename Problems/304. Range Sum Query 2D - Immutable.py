from typing import *

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        
        self.m = matrix
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] += matrix[i][j-1]
        
        print(self.m)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        col1 -= 1
        ans = 0
        
        for row in range(row1, row2+1):
            ans += self.m[row][col2] - (self.m[row][col1] if col1 >= 0 else 0)
        
        return ans
