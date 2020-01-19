from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[n-1-j] = matrix[n-1-j], matrix[i][j]
