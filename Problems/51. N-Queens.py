from typing import *

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0] * n
        hills = [0] * (2*n-1)
        dales = [0] * (2*n-1)
        matrix = ['.' * n for _ in range(n)]
        ans = []
        
        def is_valid(row, col):
            return not (cols[col] or hills[row + col] or dales[row - col])
        
        def place(row, col):
            matrix[row] = matrix[row][:col] + 'Q' + matrix[row][col+1:]
            cols[col] = 1
            hills[row + col] = 1
            dales[row - col] = 1
        
        def remove(row, col):
            matrix[row] = matrix[row][:col] + '.' + matrix[row][col+1:]
            cols[col] = 0
            hills[row + col] = 0
            dales[row - col] = 0
        
        def shallow_copy(matrix):
            return [row[:] for row in matrix]
        
        def backtrack(row):
            for col in range(n):
                if is_valid(row, col):
                    if row == n-1:
                        place(row, col)
                        ans.append(shallow_copy(matrix))
                        remove(row, col)
                    else:
                        place(row, col)
                        backtrack(row+1)
                        remove(row, col)
        
        backtrack(0)
        
        return ans
