from typing import *

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        def search_rec(left, up, right, down):
            if left > right or up > down:
                return False
            
            if matrix[up][left] > target or target > matrix[down][right]:
                return False
            
            mid = (left + right) // 2
            row = up
            
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)
        
        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)
