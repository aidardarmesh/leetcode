from typing import *

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [0 for _ in range(n)]
        hills = [0 for _ in range(2*n-1)]
        dales = [0 for _ in range(2*n-1)]

        def is_not_attacked(row, col):
            return not (cols[col] or hills[row + col] or dales[row - col])
        
        def place_queen(row, col):
            cols[col] = 1
            hills[row + col] = 1
            dales[row - col] = 1
        
        def remove_queen(row, col):
            cols[col] = 0
            hills[row + col] = 0
            dales[row - col] = 0

        def backtrack(row, count):
            for col in range(n):
                if is_not_attacked(row, col):
                    if row == n-1:
                        count += 1
                    else:
                        place_queen(row, col)
                        count = backtrack(row + 1, count)
                        remove_queen(row, col)
            
            return count
        
        return backtrack(0, 0)