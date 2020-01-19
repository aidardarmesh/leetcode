from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # anti-clockwise
        # 1. reverse first
        # 2. transpose
        def rotate_left():
            n = len(matrix)

            # reverse
            for i in range(n):
                for j in range(n//2):
                    matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
            
            # transpose
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # clockwise
        # 1. transpose
        # 2. reverse
        def rotate_right():
            n = len(matrix)

            # transpose
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # reverse
            for i in range(n):
                for j in range(n//2):
                    matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        rotate_right()
